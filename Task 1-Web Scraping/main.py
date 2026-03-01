import sys
import time
import random
import pandas as pd
from seleniumbase import Driver

if 'distutils' not in sys.modules:
    try:
        import setuptools.dist
        sys.modules['distutils'] = setuptools.dist
    except ImportError:
        pass

def scrape_zameen_wide(pages=10):
    print(f"🚀 Launching Widened Scraper ({pages} pages)...")
    driver = Driver(uc=True, headless=False)
    all_properties = []

    try:
        for p in range(1, pages + 1):
            url = f"https://www.zameen.com/Houses_Property/Lahore-1-{p}.html"
            print(f"🔗 Page {p}: Navigating...")
            driver.get(url)
            
            time.sleep(random.uniform(8, 12)) 
            
            # Slow scroll to trigger lazy-loading houses
            for _ in range(4):
                driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(1.5)

            listings = driver.find_elements("css selector", "li[role='article']")
            
            for house in listings:
                text = house.text
                if "PKR" in text:
                    lines = [l.strip() for l in text.split('\n') if l.strip()]
                    try:
                        price_line = next(l for l in lines if "PKR" in l)
                        # The Title is usually the first line, or a number if misaligned
                        title = lines[0]
                        
                        # Grab location (usually has a comma)
                        loc = "Lahore"
                        for l in lines:
                            if "," in l and "PKR" not in l:
                                loc = l
                                break
                        
                        all_properties.append({
                            "Title": title,
                            "Price": price_line,
                            "Location": loc
                        })
                    except:
                        continue
            
            print(f"✅ Page {p} complete. Total so far: {len(all_properties)}")

    finally:
        driver.quit()
    return all_properties

if __name__ == "__main__":
    data = scrape_zameen_wide(10) # Change to 15 for even more data
    if data:
        df = pd.DataFrame(data).drop_duplicates()
        df.to_csv("CodeAlpha_Task1_Zameen_Final.csv", index=False)
        print(f"\n🏆 SUCCESS! Saved {len(df)} rows to CodeAlpha_Task1_Zameen_Final.csv")