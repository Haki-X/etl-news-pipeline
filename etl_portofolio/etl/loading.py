# loading.py

from google.cloud import bigquery

def load_to_bigquery(df, project_id, destination_table):
    """
    Memuat DataFrame ke tabel di Google BigQuery.
    """
    print(f"Memulai proses memuat data ke BigQuery...")
    
    
    client = bigquery.Client(project=project_id)
    
    # Konfigurasi job untuk mode 'append'
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
        autodetect=True,
    )
    
    # Unggah data
    job = client.load_table_from_dataframe(
        df, destination_table, job_config=job_config
    )
    job.result()  # Menunggu proses selesai
    
    # Verifikasi
    table = client.get_table(destination_table)
    print(f"Proses Selesai. Tabel '{table.table_id}' sekarang memiliki {table.num_rows} baris.")