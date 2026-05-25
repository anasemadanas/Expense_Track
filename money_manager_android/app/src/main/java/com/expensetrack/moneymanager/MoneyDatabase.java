package com.expensetrack.moneymanager;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteConstraintException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;

public class MoneyDatabase extends SQLiteOpenHelper {
    private static final String DB_NAME = "money_manager_mobile.db";
    private static final int DB_VERSION = 1;

    public MoneyDatabase(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE users (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "username TEXT NOT NULL UNIQUE COLLATE NOCASE," +
                "password_hash TEXT NOT NULL)");
        db.execSQL("CREATE TABLE transactions (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE," +
                "amount REAL NOT NULL," +
                "category TEXT NOT NULL," +
                "note TEXT NOT NULL DEFAULT ''," +
                "occurred_at TEXT NOT NULL)");
        db.execSQL("CREATE TABLE budgets (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE," +
                "period TEXT NOT NULL," +
                "total_amount REAL NOT NULL," +
                "UNIQUE(user_id, period))");
        db.execSQL("CREATE TABLE goals (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE," +
                "name TEXT NOT NULL," +
                "target_amount REAL NOT NULL," +
                "saved_amount REAL NOT NULL DEFAULT 0)");
        db.execSQL("CREATE INDEX idx_tx_period ON transactions(user_id, occurred_at)");
    }

    @Override
    public void onConfigure(SQLiteDatabase db) {
        super.onConfigure(db);
        db.setForeignKeyConstraintsEnabled(true);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // The first mobile release has no schema migrations yet.
    }

    public long createAccount(String username, String password) {
        ContentValues values = new ContentValues();
        values.put("username", username.trim());
        values.put("password_hash", hashPassword(password));
        try {
            return getWritableDatabase().insertOrThrow("users", null, values);
        } catch (SQLiteConstraintException exception) {
            return -1;
        }
    }

    public long authenticate(String username, String password) {
        try (Cursor cursor = getReadableDatabase().query(
                "users",
                new String[]{"id"},
                "username = ? COLLATE NOCASE AND password_hash = ?",
                new String[]{username.trim(), hashPassword(password)},
                null,
                null,
                null)) {
            return cursor.moveToFirst() ? cursor.getLong(0) : -1;
        }
    }

    public void addTransaction(long userId, double amount, String category, String note, String date) {
        ContentValues values = new ContentValues();
        values.put("user_id", userId);
        values.put("amount", amount);
        values.put("category", category.trim());
        values.put("note", note.trim());
        values.put("occurred_at", date);
        getWritableDatabase().insertOrThrow("transactions", null, values);
    }

    public List<TransactionItem> getTransactions(long userId) {
        List<TransactionItem> results = new ArrayList<>();
        try (Cursor cursor = getReadableDatabase().query(
                "transactions",
                new String[]{"id", "amount", "category", "note", "occurred_at"},
                "user_id = ?",
                new String[]{String.valueOf(userId)},
                null,
                null,
                "occurred_at DESC, id DESC",
                "100")) {
            while (cursor.moveToNext()) {
                results.add(new TransactionItem(
                        cursor.getLong(0),
                        cursor.getDouble(1),
                        cursor.getString(2),
                        cursor.getString(3),
                        cursor.getString(4)));
            }
        }
        return results;
    }

    public Summary getSummary(long userId, String period) {
        double income = 0;
        double spent = 0;
        int count = 0;
        try (Cursor cursor = getReadableDatabase().rawQuery(
                "SELECT " +
                        "COALESCE(SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END), 0)," +
                        "COALESCE(SUM(CASE WHEN amount < 0 THEN ABS(amount) ELSE 0 END), 0)," +
                        "COUNT(*) FROM transactions " +
                        "WHERE user_id = ? AND substr(occurred_at, 1, 7) = ?",
                new String[]{String.valueOf(userId), period})) {
            if (cursor.moveToFirst()) {
                income = cursor.getDouble(0);
                spent = cursor.getDouble(1);
                count = cursor.getInt(2);
            }
        }
        return new Summary(income, spent, getBudget(userId, period), count);
    }

    public void saveBudget(long userId, String period, double totalAmount) {
        ContentValues values = new ContentValues();
        values.put("user_id", userId);
        values.put("period", period);
        values.put("total_amount", totalAmount);
        getWritableDatabase().insertWithOnConflict(
                "budgets", null, values, SQLiteDatabase.CONFLICT_REPLACE);
    }

    public double getBudget(long userId, String period) {
        try (Cursor cursor = getReadableDatabase().query(
                "budgets",
                new String[]{"total_amount"},
                "user_id = ? AND period = ?",
                new String[]{String.valueOf(userId), period},
                null,
                null,
                null)) {
            return cursor.moveToFirst() ? cursor.getDouble(0) : 0;
        }
    }

    public void addGoal(long userId, String name, double targetAmount, double savedAmount) {
        ContentValues values = new ContentValues();
        values.put("user_id", userId);
        values.put("name", name.trim());
        values.put("target_amount", targetAmount);
        values.put("saved_amount", savedAmount);
        getWritableDatabase().insertOrThrow("goals", null, values);
    }

    public void addGoalSaving(long userId, long goalId, double amount) {
        getWritableDatabase().execSQL(
                "UPDATE goals SET saved_amount = saved_amount + ? WHERE id = ? AND user_id = ?",
                new Object[]{amount, goalId, userId});
    }

    public List<GoalItem> getGoals(long userId) {
        List<GoalItem> results = new ArrayList<>();
        try (Cursor cursor = getReadableDatabase().query(
                "goals",
                new String[]{"id", "name", "target_amount", "saved_amount"},
                "user_id = ?",
                new String[]{String.valueOf(userId)},
                null,
                null,
                "id DESC")) {
            while (cursor.moveToNext()) {
                results.add(new GoalItem(
                        cursor.getLong(0),
                        cursor.getString(1),
                        cursor.getDouble(2),
                        cursor.getDouble(3)));
            }
        }
        return results;
    }

    private String hashPassword(String password) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] bytes = digest.digest(password.getBytes(StandardCharsets.UTF_8));
            StringBuilder result = new StringBuilder();
            for (byte value : bytes) {
                result.append(String.format("%02x", value));
            }
            return result.toString();
        } catch (NoSuchAlgorithmException exception) {
            throw new IllegalStateException("SHA-256 is unavailable", exception);
        }
    }

    public static class Summary {
        public final double income;
        public final double spent;
        public final double budget;
        public final int transactionCount;

        Summary(double income, double spent, double budget, int transactionCount) {
            this.income = income;
            this.spent = spent;
            this.budget = budget;
            this.transactionCount = transactionCount;
        }

        public double balance() {
            return income - spent;
        }
    }

    public static class TransactionItem {
        public final long id;
        public final double amount;
        public final String category;
        public final String note;
        public final String date;

        TransactionItem(long id, double amount, String category, String note, String date) {
            this.id = id;
            this.amount = amount;
            this.category = category;
            this.note = note;
            this.date = date;
        }
    }

    public static class GoalItem {
        public final long id;
        public final String name;
        public final double target;
        public final double saved;

        GoalItem(long id, String name, double target, double saved) {
            this.id = id;
            this.name = name;
            this.target = target;
            this.saved = saved;
        }

        public int progress() {
            if (target <= 0) {
                return 0;
            }
            return Math.min(100, (int) Math.round((saved / target) * 100));
        }
    }
}
