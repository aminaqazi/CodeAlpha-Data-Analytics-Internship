import pandas as pd

def clean_and_group_data(file_path):
    df = pd.read_csv(file_path)
    clean_data = []
    
    for _, row in df.iterrows():
        raw_val = str(row['Title'])
        
        # 1. Re-align Price and Title
        if raw_val.replace('.', '', 1).isdigit() or "HOT" in raw_val:
            actual_title = "Residential Property"
            price_text = f"PKR {raw_val} Crore" if raw_val.isdigit() else "Consult Agent"
            
            # 2. GROUPING LOGIC: Combine all DHA Phases
            original_location = row['Location'].strip().replace('"', '')
            if "DHA" in original_location.upper():
                grouped_location = "DHA, Lahore"
            else:
                # Keep other major areas clean (e.g., just "Bahria Orchard")
                grouped_location = original_location.split(',')[0].strip()

            clean_data.append({
                "Property_Type": actual_title,
                "Price_Text": price_text,
                "Location": grouped_location, # This is the new grouped column
                "Price_Numeric": float(raw_val) * 10000000 if raw_val.isdigit() else 0
            })

    final_df = pd.DataFrame(clean_data)
    final_df.to_csv("CodeAlpha_Task2_Cleaned.csv", index=False)
    print("✅ DATA GROUPED: All DHA Phases merged into 'DHA, Lahore'")
    print(final_df['Location'].value_counts().head(5))

if __name__ == "__main__":
    # This tells Python to go up one level and into the Task 1 folder
    raw_data_path = r"C:\Users\amina_98geew2\OneDrive\Documents\CodeAlpha Internship\Task 1-Web Scraping\Zameen.pk\Task 1-Web Scraping\CodeAlpha_Task1_Zameen_Final.csv"
    clean_and_group_data(raw_data_path)