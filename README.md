# 🥚 Smart Protein Tracker

**A Full-Stack Nutrition Dashboard with Real-Time Market Inflation Analysis.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0-green?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite)

---

## 💡 The Problem
Most fitness trackers are static—they track what you eat but ignore what it costs. In an economy where food prices fluctuate daily, maintaining a high-protein diet requires financial optimization, not just calorie counting.

## 🚀 The Solution
I built a **Market-Aware Nutrition Engine** that:
1.  **Tracks** daily protein intake and expenses.
2.  **Scrapes** real-time market prices for commodities (Eggs & Chicken) to benchmark user spending against national averages.
3.  **Adapts** to network failures using a fault-tolerant architecture.

---

## 🛠️ Key Features
* **🐍 Python Scraping Engine:** Uses `BeautifulSoup` and `Requests` to fetch live commodity prices from Google Search results.
* **🛡️ Fault Tolerance & Graceful Degradation:** The system automatically detects if the scraper is blocked (Anti-Bot defenses) and seamlessly switches to an **"Offline Simulation Mode"** (visualized by an Orange status badge in the UI) to prevent application downtime.
* **📊 SQL Data Aggregation:** Uses SQL windowing and grouping logic to generate a rolling **10-
