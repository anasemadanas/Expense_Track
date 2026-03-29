<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

</head>
<body>

<h1>💰 Money Manager App</h1>

<p> A modern and scalable financial management tool to track your spending and improve your budgeting.</p>

<h2 id="table-of-contents">📑 Table of Contents</h2>
<nav>
  <ul>
    <li><a href="#introduction">🧾 Introduction</a></li>
    <li><a href="#features">✨ Features</a></li>
    <li><a href="#installation">⚙️ Installation</a></li>
    <li><a href="#how-to-contribute">🙌 How to Contribute</a></li>
    <li><a href="#license">📝 License</a></li>
  </ul>
</nav>

<h2 id="introduction">🧾 Introduction</h2>
<p> Money Manager is built in Python using a clean 3-Tier Architecture and SOLID principles.
It provides an easy and efficient way to track expenses, log income, plan budgets, and monitor financial health through charts and reports. </p>

<h2 id="features">✨ Features</h2>
<ul>
    <li>Track expenses & income</li>
    <li>Categorize transactions</li>
    <li>Monthly budget planning</li>
    <li>Dashboard with charts</li>
    <li>Notes & goals system</li>
    <li>Clean architecture suitable for future scaling</li>
    <li>SQLite database with Repository Pattern</li>
</ul>

<h2>🧱 Architecture</h2>
<ul>
    <li><strong>Presentation Layer:</strong> Handles GUI (PyQt5 or pySlide6)</li>
    <li><strong>Business Logic Layer:</strong> Implements financial rules and validation</li>
    <li><strong>Data Layer:</strong> Handles SQLite storage using repositories and interfaces</li>
</ul>

<h2 id="installation">⚙️ Installation</h2>
<pre>
git clone https://github.com/anasemadanas/Expense_Track.git
cd Expense_Track
pip install -r requirements.txt
</pre>

<h2>▶️ Run the App</h2>
<pre>
python money_manager/main.py
</pre>

<h2>🔮 Future Enhancements</h2>
<ul>
    <li>Android version (Kivy or Flutter)</li>
    <li>Web version (FastAPI backend)</li>
    <li>Cloud sync</li>
    <li>PDF Reports</li>
    <li>AI income/spending predictions</li>
</ul>

## 📝 License
MIT License — see the [License](https://github.com/anasemadanas/Expense_Track/blob/main/LICENSE)

<p><a href="#table-of-contents">↩️ Back to Table of Contents</a></p>

</body>
</html>
