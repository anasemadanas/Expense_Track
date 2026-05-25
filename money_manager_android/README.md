# Money Manager Android

Native Android companion app for the Expense Track project. It stores data locally on
the device using SQLite and does not require a server connection.

## Included Features

- Device-local account creation and sign-in
- Dashboard with monthly income, spending, balance, and budget progress
- Income and expense transaction entry and history
- Monthly budget setup
- Savings goals with contribution updates

## Build

Android Studio can open this directory directly. From PowerShell, with Android Studio
installed:

```powershell
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'
$env:ANDROID_HOME = "$env:LOCALAPPDATA\Android\Sdk"
.\gradlew.bat assembleDebug
```

The resulting installable debug APK is generated at:

```text
app\build\outputs\apk\debug\app-debug.apk
```

The Android database is intentionally separate from the desktop PySide database, so
the mobile app starts with its own accounts and finance records.
