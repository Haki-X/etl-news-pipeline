# transformation.py

import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    """Menganalisis dan mengkategorikan sentimen dari sebuah teks."""
    # Membuat objek TextBlob
    analysis = TextBlob(str(text))
    # Menentukan sentimen berdasarkan polaritas
    if analysis.sentiment.polarity > 0:
        return 'Positif'
    elif analysis.sentiment.polarity < 0:
        return 'Negatif'
    else:
        return 'Netral'

def clean_and_transform_data(df):
    """
    Membersihkan dan mentransformasi data mentah.
    Mengembalikan DataFrame yang siap untuk dimuat.
    """
    print("Memulai proses transformasi data...")
    
    # 1. Menangani data hilang dan duplikat
    df.dropna(subset=['title', 'content'], inplace=True)
    df.drop_duplicates(subset=['title'], inplace=True, keep='first')
    
    # 2. Konversi tipe data tanggal
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    
    # 3. Membongkar kolom 'source'
    df['source_name'] = df['source'].apply(lambda x: eval(str(x))['name'])
    
    # 4. Analisis Sentimen (Fitur Baru)
    df['sentiment'] = df['title'].apply(get_sentiment)
    
    # 5. Memilih dan menata ulang kolom
    df_cleaned = df[['publishedAt', 'source_name', 'author', 'title', 'sentiment', 'description', 'url', 'content']]
    
    print("Transformasi data selesai.")
    return df_cleaned