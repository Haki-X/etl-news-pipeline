# main.py

import os
from dotenv import load_dotenv
from etl.extraction import extract_news_data
from etl.transformation import clean_and_transform_data
from etl.loading import load_to_bigquery

load_dotenv()

# --- KONFIGURASI PUSAT ---
API_KEY = os.getenv("NEWS_API_KEY")

# Tentukan domain yang terpercaya
RELIABLE_DOMAINS = "kompas.com,detik.com,liputan6.com,tempo.co,cnnindonesia.com,cnbcindonesia.com"

SEARCH_QUERY = "Indonesia"

PROJECT_ID = 'indonesia-news-466813' 
DESTINATION_TABLE = 'news_analysis.daily_indonesian_news'

def main_etl_pipeline():
    """
    Menjalankan alur kerja ETL lengkap.
    """
    # 1. Ekstraksi (Panggilan fungsi disesuaikan)
    df_raw = extract_news_data(api_key=API_KEY, domains=RELIABLE_DOMAINS, search_query=SEARCH_QUERY)
    
    if df_raw is not None:
        # 2. Transformasi
        df_cleaned = clean_and_transform_data(df_raw)
        
        # 3. Load
        if not df_cleaned.empty:
            load_to_bigquery(df_cleaned, PROJECT_ID, DESTINATION_TABLE)
        else:
            print("Tidak ada data untuk dimuat setelah proses transformasi.")

if __name__ == "__main__":
    main_etl_pipeline()