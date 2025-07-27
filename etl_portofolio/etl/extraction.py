# extraction.py

import os
import requests
import pandas as pd

def extract_news_data(api_key, domains, search_query='Indonesia'):
    
    print(f"Memulai ekstraksi dari domain: {domains}...")
    
    URL = 'https://newsapi.org/v2/everything'
    
    # Konfigurasi parameter hanya untuk satu halaman
    query_params = {
        'q': search_query,
        'domains': domains,
        'language': 'id',
        'sortBy': 'publishedAt', # Urutkan berdasarkan yang terbaru
        'apiKey': api_key,
        'pageSize': 100  # Minta jumlah artikel maksimal
    }
    
    try:
        response = requests.get(URL, params=query_params)
        
        if response.status_code != 200:
            print(f"Gagal mengambil data. Status: {response.status_code} - Pesan: {response.json().get('message', '')}")
            return None
            
        data = response.json()
        articles = data.get('articles', [])
        
        if not articles:
            print("Tidak ada artikel yang ditemukan dari domain tersebut.")
            return None
        
        df_raw = pd.DataFrame(articles)
        # Hapus duplikat jika ada
        df_raw.drop_duplicates(subset=['title'], inplace=True, keep='first')
        
        print(f"Ekstraksi selesai. Total {len(df_raw)} artikel unik berhasil didapatkan.")
        return df_raw

    except Exception as e:
        print(f"Terjadi error pada saat ekstraksi: {e}")
        return None