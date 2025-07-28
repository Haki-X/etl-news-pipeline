# Proyek Pipeline Data ETL: Analisis Berita Indonesia

Proyek ini mendemonstrasikan pembangunan pipeline data ETL (Extract, Transform, Load) *end-to-end* yang sepenuhnya otomatis. Pipeline ini mengambil berita utama dari berbagai sumber media di Indonesia, membersihkannya, melakukan analisis sentimen, menyimpannya di Google BigQuery, dan menyajikannya dalam sebuah dasbor interaktif yang diperbarui setiap hari.

---

##  Fitur Utama
- **Ekstraksi Data Harian**: Mengambil artikel berita terbaru dari **NewsAPI** secara otomatis.
- **Transformasi & Pengayaan Data**: Membersihkan data mentah dan memperkayanya dengan analisis sentimen (Positif, Negatif, Netral) menggunakan **TextBlob**.
- **Penyimpanan di Cloud Data Warehouse**: Menyimpan data yang sudah bersih dan terstruktur di **Google BigQuery**.
- **Dasbor Interaktif**: Memvisualisasikan data dan wawasan dalam dasbor **Looker Studio** yang dinamis, menampilkan tren berita, sumber paling aktif, dan analisis sentimen.
- **Automasi & Orkestrasi**: Seluruh alur kerja diotomatiskan dan dijadwalkeun untuk berjalan setiap hari menggunakan **Prefect**.
- **Version Control**: Kode dan konfigurasi deployment dikelola menggunakan **Git** dan **GitHub**.

---

##  Arsitektur Sistem
Pipeline ini mengikuti alur kerja yang jelas dan modular:

**NewsAPI** → **Python Script (ETL)** → **Google BigQuery** → **Looker Studio**

<p align="center">
  <em>(Prefect bertindak sebagai orkestrator yang menjalankan skrip Python setiap hari)</em>
</p>

---

##  Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python 3
- **Library Utama**: Pandas, Requests, TextBlob, python-dotenv, google-cloud-bigquery
- **Orkestrasi**: Prefect
- **Data Warehouse**: Google BigQuery
- **Visualisasi**: Looker Studio
- **Version Control**: Git & GitHub

---

##  Cara Menjalankan Proyek Secara Lokal

### 1. Prasyarat
- Python 3.8+
- Akun Google Cloud dengan BigQuery API diaktifkan
- Kunci API dari [NewsAPI](https://newsapi.org/)
- Akun gratis [Prefect Cloud](https://app.prefect.cloud/)

### 2. Instalasi
1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/Haki-X/etl-news-pipeline.git](https://github.com/Haki-X/etl-news-pipeline.git)
    cd etl-news-pipeline
    ```
2.  **Buat dan aktifkan lingkungan virtual:**
    ```bash
    # Membuat venv
    python -m venv venv

    # Mengaktifkan di Windows
    .\venv\Scripts\activate
    ```
3.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Konfigurasi
1.  Buat file bernama `.env` di direktori utama proyek.
2.  Isi file `.env` dengan format berikut, ganti dengan nilai Anda sendiri:
    ```env
    NEWS_API_KEY="kunci_api_newsapi_anda"
    GOOGLE_APPLICATION_CREDENTIALS="path/ke/file_kredensial_gcp.json"
    ```

### 4. Menjalankan Pipeline
- **Untuk menjalankan secara manual (pengujian):**
  ```bash
  python flow.py