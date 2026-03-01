# Task 1: Web Scraping
This task focuses on automated data extraction from Zameen.pk.

## ⚙️ Technical Implementation
- **Tool:** `SeleniumBase` (Undetected Chrome Mode)
- **Target:** 10+ pages of Lahore residential listings.
- **Data Points:** Title, Price, and Location.

## 🛡️ Challenges Overcome
Zameen.pk uses advanced bot detection. I implemented **stealth headers** and **randomized sleep intervals** to ensure the scraper mimics human behavior and successfully bypassed Cloudflare/Captcha blocks.

## 📄 Files
- `main.py`: The scraping engine.
- `CodeAlpha_Task1_Zameen_Final.csv`: The raw, uncleaned dataset.