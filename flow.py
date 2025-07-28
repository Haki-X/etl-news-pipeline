# flow.py

import os
from dotenv import load_dotenv
from prefect import task, flow
from datetime import timedelta

# Impor fungsi-fungsi yang sudah Anda buat
from extraction import extract_news_data
from transformation import clean_and_transform_data
from loading import load_to_bigquery

# --- KONFIGURASI PUSAT ---
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")
RELIABLE_DOMAINS = "kompas.com,detik.com,liputan6.com,tempo.co,cnnindonesia.com,cnbcindonesia.com"
SEARCH_QUERY = "Indonesia"
PROJECT_ID = 'indonesia-news-466813' # Ganti dengan ID proyek Anda
DESTINATION_TABLE = 'news_analysis.daily_indonesian_news'

# --- DEFINISI TASK ---
# Tandai setiap fungsi sebagai sebuah 'task' Prefect
@task(retries=3, retry_delay_seconds=10)
def extract_task(api_key, domains, search_query):
    print("Menjalankan task ekstraksi...")
    return extract_news_data(api_key, domains, search_query)

@task
def transform_task(df_raw):
    print("Menjalankan task transformasi...")
    return clean_and_transform_data(df_raw)

@task
def load_task(df_cleaned, project_id, destination_table):
    print("Menjalankan task pemuatan...")
    load_to_bigquery(df_cleaned, project_id, destination_table)

# --- DEFINISI FLOW ---
# Gabungkan semua task menjadi satu 'flow' utama
@flow(name="ETL Pipeline Berita Harian")
def etl_news_pipeline_flow():
    """
    Flow utama yang menjalankan pipeline ETL berita dari awal hingga akhir.
    """
    df_raw = extract_task(API_KEY, RELIABLE_DOMAINS, SEARCH_QUERY)
    
    if df_raw is not None:
        df_cleaned = transform_task(df_raw)
        
        if not df_cleaned.empty:
            load_task(df_cleaned, PROJECT_ID, DESTINATION_TABLE)

# Menjalankan flow secara manual untuk pengujian
if __name__ == "__main__":
    etl_news_pipeline_flow()