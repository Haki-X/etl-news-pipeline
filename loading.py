# loading.py (Versi Diperbaiki)

import os
from google.cloud import bigquery
from google.oauth2 import service_account

def load_to_bigquery(df, project_id, destination_table):
    """
    Memuat DataFrame ke tabel di Google BigQuery dengan kredensial eksplisit.
    """
    print(f"Memulai proses memuat data ke BigQuery...")
    
    # Ambil path ke file kredensial dari environment variable
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    
    # Cek jika path kredensial ada
    if not credentials_path:
        print("❌ Error: Path GOOGLE_APPLICATION_CREDENTIALS tidak ditemukan di file .env")
        return

    try:
        # Buat objek kredensial secara eksplisit dari file JSON
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        
        # Inisialisasi client dengan kredensial dan project_id
        client = bigquery.Client(credentials=credentials, project=project_id)
        
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND",
            autodetect=True,
        )
        
        job = client.load_table_from_dataframe(
            df, destination_table, job_config=job_config
        )
        job.result()
        
        table = client.get_table(destination_table)
        print(f"✅ Proses Selesai. Tabel '{table.table_id}' sekarang memiliki {table.num_rows} baris.")

    except Exception as e:
        print(f"❌ Terjadi error saat memuat ke BigQuery: {e}")