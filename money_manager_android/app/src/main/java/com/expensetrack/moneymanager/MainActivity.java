package com.expensetrack.moneymanager;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.ScrollView;
import android.widget.Space;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class MainActivity extends Activity {
    private static final String PREFS = "money_manager_session";
    private static final String DASHBOARD = "Dashboard";
    private static final String TRANSACTIONS = "Transactions";
    private static final String BUDGET = "Budget";
    private static final String GOALS = "Goals";

    private final int primary = Color.rgb(19, 93, 102);
    private final int primaryDark = Color.rgb(12, 65, 72);
    private final int canvas = Color.rgb(245, 247, 247);
    private final int panel = Color.WHITE;
    private final int muted = Color.rgb(88, 104, 110);
    private final int positive = Color.rgb(16, 134, 83);
    private final int negative = Color.rgb(196, 51, 53);

    private MoneyDatabase database;
    private SharedPreferences preferences;
    private long userId;
    private String username;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        database = new MoneyDatabase(this);
        preferences = getSharedPreferences(PREFS, Context.MODE_PRIVATE);
        userId = preferences.getLong("user_id", -1);
        username = preferences.getString("username", "");
        if (userId > 0) {
            showPage(DASHBOARD);
        } else {
            showAuthentication();
        }
    }

    private void showAuthentication() {
        LinearLayout page = vertical(24);
        page.setBackgroundColor(canvas);
        page.setGravity(Gravity.CENTER_HORIZONTAL);

        ScrollView scrollView = new ScrollView(this);
        LinearLayout.LayoutParams fill = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT);
        scrollView.setLayoutParams(fill);
        scrollView.addView(page);

        addSpace(page, 54);
        ImageView logo = new ImageView(this);
        logo.setImageResource(R.drawable.ic_wallet);
        page.addView(logo, new LinearLayout.LayoutParams(dp(82), dp(82)));
        page.addView(title("Money Manager", 30));
        page.addView(text("Track expenses and grow your savings.", muted, 16));
        addSpace(page, 28);

        LinearLayout card = card();
        card.addView(title("Welcome", 22));
        card.addView(text("Sign in or create an offline account on this device.", muted, 14));
        addSpace(card, 12);
        EditText usernameInput = input("Username", InputType.TYPE_CLASS_TEXT);
        EditText passwordInput = input(
                "Password",
                InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_PASSWORD);
        card.addView(usernameInput);
        card.addView(passwordInput);
        Button signIn = button("Sign in", primary);
        Button create = outlineButton("Create account");
        card.addView(signIn);
        card.addView(create);
        page.addView(card, widthMargin());

        signIn.setOnClickListener(view -> authenticate(
                usernameInput.getText().toString(),
                passwordInput.getText().toString(),
                false));
        create.setOnClickListener(view -> authenticate(
                usernameInput.getText().toString(),
                passwordInput.getText().toString(),
                true));

        setContentView(scrollView);
    }

    private void authenticate(String requestedUsername, String password, boolean create) {
        String trimmed = requestedUsername.trim();
        if (trimmed.length() < 3 || password.length() < 4) {
            toast("Username must be 3+ characters and password 4+ characters.");
            return;
        }
        long id = create
                ? database.createAccount(trimmed, password)
                : database.authenticate(trimmed, password);
        if (id < 0) {
            toast(create ? "That username already exists." : "Incorrect username or password.");
            return;
        }
        userId = id;
        username = trimmed;
        preferences.edit().putLong("user_id", id).putString("username", trimmed).apply();
        showPage(DASHBOARD);
    }

    private void showPage(String activePage) {
        LinearLayout root = vertical(0);
        root.setBackgroundColor(canvas);
        root.addView(toolbar());
        root.addView(navigation(activePage));

        ScrollView scroll = new ScrollView(this);
        LinearLayout body = vertical(18);
        body.setPadding(dp(18), dp(18), dp(18), dp(34));
        scroll.addView(body);
        root.addView(scroll, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, 0, 1));

        if (TRANSACTIONS.equals(activePage)) {
            renderTransactions(body);
        } else if (BUDGET.equals(activePage)) {
            renderBudget(body);
        } else if (GOALS.equals(activePage)) {
            renderGoals(body);
        } else {
            renderDashboard(body);
        }
        setContentView(root);
    }

    private View toolbar() {
        LinearLayout bar = new LinearLayout(this);
        bar.setOrientation(LinearLayout.HORIZONTAL);
        bar.setGravity(Gravity.CENTER_VERTICAL);
        bar.setPadding(dp(18), dp(12), dp(12), dp(12));
        bar.setBackgroundColor(primaryDark);

        LinearLayout labels = vertical(0);
        TextView heading = text("Money Manager", Color.WHITE, 21);
        heading.setTypeface(Typeface.DEFAULT_BOLD);
        labels.addView(heading);
        labels.addView(text("Hello, " + username, Color.rgb(202, 223, 225), 13));
        bar.addView(labels, new LinearLayout.LayoutParams(0, ViewGroup.LayoutParams.WRAP_CONTENT, 1));

        Button logout = compactButton("Log out", Color.TRANSPARENT);
        logout.setTextColor(Color.WHITE);
        logout.setOnClickListener(view -> {
            preferences.edit().clear().apply();
            userId = -1;
            username = "";
            showAuthentication();
        });
        bar.addView(logout);
        return bar;
    }

    private View navigation(String activePage) {
        HorizontalScrollView scroller = new HorizontalScrollView(this);
        scroller.setHorizontalScrollBarEnabled(false);
        scroller.setBackgroundColor(Color.WHITE);
        LinearLayout navigation = new LinearLayout(this);
        navigation.setOrientation(LinearLayout.HORIZONTAL);
        navigation.setPadding(dp(10), dp(8), dp(10), dp(8));
        String[] pages = {DASHBOARD, TRANSACTIONS, BUDGET, GOALS};
        for (String page : pages) {
            Button item = compactButton(page, page.equals(activePage) ? primary : Color.TRANSPARENT);
            item.setTextColor(page.equals(activePage) ? Color.WHITE : primary);
            item.setOnClickListener(view -> showPage(page));
            navigation.addView(item);
        }
        scroller.addView(navigation);
        return scroller;
    }

    private void renderDashboard(LinearLayout body) {
        String period = currentPeriod();
        MoneyDatabase.Summary summary = database.getSummary(userId, period);
        body.addView(title("Overview", 27));
        body.addView(text(periodLabel() + " snapshot", muted, 15));
        addSpace(body, 14);

        body.addView(metric("Balance", money(summary.balance()), summary.balance() >= 0 ? positive : negative));
        body.addView(metric("Income", money(summary.income), positive));
        body.addView(metric("Spent", money(summary.spent), negative));

        LinearLayout budgetCard = card();
        budgetCard.addView(title("Monthly budget", 19));
        if (summary.budget <= 0) {
            budgetCard.addView(text("No budget has been set for this month.", muted, 14));
        } else {
            int progress = (int) Math.min(100, Math.round(summary.spent / summary.budget * 100));
            budgetCard.addView(text(
                    money(summary.spent) + " of " + money(summary.budget) + " spent",
                    muted,
                    14));
            ProgressBar bar = progress(progress);
            budgetCard.addView(bar);
            budgetCard.addView(text(progress + "% used", progress >= 100 ? negative : primary, 13));
        }
        body.addView(budgetCard);

        LinearLayout recent = card();
        recent.addView(title("Recent activity", 19));
        List<MoneyDatabase.TransactionItem> items = database.getTransactions(userId);
        if (items.isEmpty()) {
            recent.addView(text("Add your first income or expense from Transactions.", muted, 14));
        } else {
            int limit = Math.min(4, items.size());
            for (int index = 0; index < limit; index++) {
                recent.addView(transactionRow(items.get(index)));
            }
        }
        body.addView(recent);
    }

    private void renderTransactions(LinearLayout body) {
        body.addView(title("Transactions", 27));
        body.addView(text("Record income and expenses in one place.", muted, 15));
        addSpace(body, 14);

        LinearLayout entry = card();
        entry.addView(title("New transaction", 19));
        Spinner type = new Spinner(this);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(
                this, android.R.layout.simple_spinner_dropdown_item, new String[]{"Expense", "Income"});
        type.setAdapter(adapter);
        EditText amount = input("Amount", InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
        EditText category = input("Category (for example, Groceries)", InputType.TYPE_CLASS_TEXT);
        EditText note = input("Note (optional)", InputType.TYPE_CLASS_TEXT);
        entry.addView(type);
        entry.addView(amount);
        entry.addView(category);
        entry.addView(note);
        Button add = button("Add transaction", primary);
        entry.addView(add);
        body.addView(entry);

        add.setOnClickListener(view -> {
            Double value = positiveAmount(amount.getText().toString());
            if (value == null || category.getText().toString().trim().isEmpty()) {
                toast("Enter a positive amount and a category.");
                return;
            }
            double signedValue = type.getSelectedItemPosition() == 0 ? -value : value;
            database.addTransaction(
                    userId, signedValue, category.getText().toString(), note.getText().toString(), today());
            toast("Transaction added.");
            showPage(TRANSACTIONS);
        });

        List<MoneyDatabase.TransactionItem> items = database.getTransactions(userId);
        LinearLayout list = card();
        list.addView(title("History", 19));
        if (items.isEmpty()) {
            list.addView(text("No transactions yet.", muted, 14));
        } else {
            for (MoneyDatabase.TransactionItem item : items) {
                list.addView(transactionRow(item));
            }
        }
        body.addView(list);
    }

    private void renderBudget(LinearLayout body) {
        String period = currentPeriod();
        double existingBudget = database.getBudget(userId, period);
        MoneyDatabase.Summary summary = database.getSummary(userId, period);

        body.addView(title("Budget", 27));
        body.addView(text("Plan your spending for " + periodLabel() + ".", muted, 15));
        addSpace(body, 14);

        LinearLayout setup = card();
        setup.addView(title("Monthly limit", 19));
        EditText amount = input("Budget amount", InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
        if (existingBudget > 0) {
            amount.setText(decimal(existingBudget));
        }
        setup.addView(amount);
        Button save = button(existingBudget > 0 ? "Update budget" : "Save budget", primary);
        setup.addView(save);
        body.addView(setup);

        save.setOnClickListener(view -> {
            Double value = positiveAmount(amount.getText().toString());
            if (value == null) {
                toast("Enter a positive budget amount.");
                return;
            }
            database.saveBudget(userId, period, value);
            toast("Budget saved.");
            showPage(BUDGET);
        });

        if (existingBudget > 0) {
            LinearLayout status = card();
            status.addView(title("Progress", 19));
            int used = (int) Math.min(100, Math.round(summary.spent / existingBudget * 100));
            double remaining = existingBudget - summary.spent;
            status.addView(text("Spent: " + money(summary.spent), negative, 16));
            status.addView(text(
                    remaining >= 0 ? "Remaining: " + money(remaining) : "Over by: " + money(-remaining),
                    remaining >= 0 ? positive : negative,
                    16));
            status.addView(progress(used));
            body.addView(status);
        }
    }

    private void renderGoals(LinearLayout body) {
        body.addView(title("Savings goals", 27));
        body.addView(text("Turn plans into visible progress.", muted, 15));
        addSpace(body, 14);

        LinearLayout form = card();
        form.addView(title("New goal", 19));
        EditText name = input("Goal name", InputType.TYPE_CLASS_TEXT);
        EditText target = input("Target amount", InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
        EditText saved = input("Already saved (optional)", InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
        form.addView(name);
        form.addView(target);
        form.addView(saved);
        Button add = button("Create goal", primary);
        form.addView(add);
        body.addView(form);

        add.setOnClickListener(view -> {
            Double targetValue = positiveAmount(target.getText().toString());
            Double savedValue = optionalAmount(saved.getText().toString());
            if (name.getText().toString().trim().isEmpty() || targetValue == null || savedValue == null) {
                toast("Enter a goal name and valid amounts.");
                return;
            }
            database.addGoal(userId, name.getText().toString(), targetValue, savedValue);
            toast("Goal created.");
            showPage(GOALS);
        });

        LinearLayout goals = card();
        goals.addView(title("Your goals", 19));
        List<MoneyDatabase.GoalItem> items = database.getGoals(userId);
        if (items.isEmpty()) {
            goals.addView(text("No goals have been created yet.", muted, 14));
        } else {
            for (MoneyDatabase.GoalItem item : items) {
                goals.addView(goalRow(item));
            }
        }
        body.addView(goals);
    }

    private View transactionRow(MoneyDatabase.TransactionItem item) {
        LinearLayout row = vertical(0);
        row.setPadding(0, dp(10), 0, dp(10));
        TextView label = text(item.category + "   " + money(item.amount), item.amount >= 0 ? positive : negative, 16);
        label.setTypeface(Typeface.DEFAULT_BOLD);
        row.addView(label);
        String detail = item.date;
        if (!item.note.isEmpty()) {
            detail += "  |  " + item.note;
        }
        row.addView(text(detail, muted, 13));
        return row;
    }

    private View goalRow(MoneyDatabase.GoalItem item) {
        LinearLayout row = vertical(0);
        row.setPadding(0, dp(10), 0, dp(10));
        TextView name = text(item.name, primaryDark, 17);
        name.setTypeface(Typeface.DEFAULT_BOLD);
        row.addView(name);
        row.addView(text(money(item.saved) + " saved of " + money(item.target), muted, 14));
        row.addView(progress(item.progress()));
        LinearLayout actions = new LinearLayout(this);
        actions.setGravity(Gravity.CENTER_VERTICAL);
        actions.addView(text(item.progress() + "% complete", item.progress() >= 100 ? positive : primary, 13),
                new LinearLayout.LayoutParams(0, ViewGroup.LayoutParams.WRAP_CONTENT, 1));
        Button contribute = compactButton("+ Add saving", primary);
        contribute.setTextColor(Color.WHITE);
        contribute.setOnClickListener(view -> openContribution(item));
        actions.addView(contribute);
        row.addView(actions);
        return row;
    }

    private void openContribution(MoneyDatabase.GoalItem item) {
        EditText amount = input("Amount saved", InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_DECIMAL);
        amount.setPadding(dp(20), dp(12), dp(20), dp(12));
        new AlertDialog.Builder(this)
                .setTitle("Add saving to " + item.name)
                .setView(amount)
                .setPositiveButton("Save", (dialog, which) -> {
                    Double value = positiveAmount(amount.getText().toString());
                    if (value == null) {
                        toast("Enter a positive amount.");
                    } else {
                        database.addGoalSaving(userId, item.id, value);
                        showPage(GOALS);
                    }
                })
                .setNegativeButton("Cancel", null)
                .show();
    }

    private LinearLayout metric(String label, String value, int valueColor) {
        LinearLayout card = card();
        card.addView(text(label, muted, 14));
        TextView number = text(value, valueColor, 28);
        number.setTypeface(Typeface.DEFAULT_BOLD);
        card.addView(number);
        return card;
    }

    private LinearLayout card() {
        LinearLayout card = vertical(10);
        card.setPadding(dp(17), dp(16), dp(17), dp(16));
        card.setBackground(rounded(panel, 15));
        card.setElevation(dp(2));
        card.setLayoutParams(widthMargin());
        return card;
    }

    private LinearLayout vertical(int gap) {
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        if (gap > 0) {
            layout.setShowDividers(LinearLayout.SHOW_DIVIDER_MIDDLE);
            Space divider = new Space(this);
            divider.setMinimumHeight(dp(gap));
            layout.setDividerDrawable(rounded(Color.TRANSPARENT, 0));
            layout.setDividerPadding(0);
        }
        return layout;
    }

    private LinearLayout.LayoutParams widthMargin() {
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        params.setMargins(0, 0, 0, dp(12));
        return params;
    }

    private EditText input(String hint, int inputType) {
        EditText field = new EditText(this);
        field.setHint(hint);
        field.setTextSize(15);
        field.setInputType(inputType);
        field.setSingleLine(true);
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, dp(54));
        params.setMargins(0, dp(4), 0, dp(5));
        field.setLayoutParams(params);
        return field;
    }

    private Button button(String value, int color) {
        Button button = new Button(this);
        button.setText(value);
        button.setTextColor(Color.WHITE);
        button.setTextSize(15);
        button.setAllCaps(false);
        button.setTypeface(Typeface.DEFAULT_BOLD);
        button.setBackground(rounded(color, 12));
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, dp(52));
        params.setMargins(0, dp(9), 0, 0);
        button.setLayoutParams(params);
        return button;
    }

    private Button outlineButton(String value) {
        Button button = button(value, Color.rgb(224, 233, 234));
        button.setTextColor(primary);
        return button;
    }

    private Button compactButton(String value, int color) {
        Button button = new Button(this);
        button.setText(value);
        button.setAllCaps(false);
        button.setTextSize(13);
        button.setBackground(rounded(color, 18));
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT, dp(42));
        params.setMargins(dp(3), 0, dp(3), 0);
        button.setLayoutParams(params);
        return button;
    }

    private ProgressBar progress(int value) {
        ProgressBar progress = new ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal);
        progress.setMax(100);
        progress.setProgress(value);
        progress.setProgressTintList(android.content.res.ColorStateList.valueOf(value >= 100 ? negative : primary));
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, dp(13));
        params.setMargins(0, dp(10), 0, dp(8));
        progress.setLayoutParams(params);
        return progress;
    }

    private TextView title(String value, int size) {
        TextView title = text(value, primaryDark, size);
        title.setTypeface(Typeface.DEFAULT_BOLD);
        return title;
    }

    private TextView text(String value, int color, int size) {
        TextView text = new TextView(this);
        text.setText(value);
        text.setTextColor(color);
        text.setTextSize(size);
        return text;
    }

    private GradientDrawable rounded(int color, int radius) {
        GradientDrawable shape = new GradientDrawable();
        shape.setColor(color);
        shape.setCornerRadius(dp(radius));
        return shape;
    }

    private void addSpace(LinearLayout layout, int height) {
        Space space = new Space(this);
        layout.addView(space, new LinearLayout.LayoutParams(1, dp(height)));
    }

    private int dp(int value) {
        return (int) (value * getResources().getDisplayMetrics().density + 0.5f);
    }

    private String currentPeriod() {
        return new SimpleDateFormat("yyyy-MM", Locale.US).format(new Date());
    }

    private String periodLabel() {
        return new SimpleDateFormat("MMMM yyyy", Locale.getDefault()).format(new Date());
    }

    private String today() {
        return new SimpleDateFormat("yyyy-MM-dd", Locale.US).format(new Date());
    }

    private String money(double value) {
        return String.format(Locale.US, "$%,.2f", value);
    }

    private String decimal(double value) {
        return String.format(Locale.US, "%.2f", value);
    }

    private Double positiveAmount(String raw) {
        Double value = optionalAmount(raw);
        return value != null && value > 0 ? value : null;
    }

    private Double optionalAmount(String raw) {
        if (raw.trim().isEmpty()) {
            return 0.0;
        }
        try {
            double value = Double.parseDouble(raw.trim());
            return value >= 0 ? value : null;
        } catch (NumberFormatException exception) {
            return null;
        }
    }

    private void toast(String value) {
        Toast.makeText(this, value, Toast.LENGTH_SHORT).show();
    }
}
