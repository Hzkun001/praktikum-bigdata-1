# Praktikum Big Data - Praktikum 1

Proyek ini merupakan bagian dari praktikum Big Data yang menggunakan Apache PySpark untuk pemrosesan data terdistribusi.

## 📋 Deskripsi

Repositori ini berisi implementasi dasar pemrosesan data menggunakan PySpark, mencakup operasi-operasi fundamental seperti pembentukan DataFrame, agregasi data, dan manipulasi data terdistribusi.

## 🚀 Fitur

- ✅ Pembuatan Spark Session
- ✅ Pemrosesan data dengan PySpark DataFrame
- ✅ Agregasi data (groupBy dan sum)
- ✅ Struktur proyek yang terorganisir untuk big data pipeline

## 📁 Struktur Proyek

```
praktikum1/
│
├── README.md           # Dokumentasi proyek
├── requirements.txt    # Dependencies Python
│
├── scripts/           # Script Python untuk job PySpark
│   └── simple_job.py  # Job sederhana untuk agregasi data
│
├── notebooks/         # Jupyter notebooks untuk analisis
├── data/             # Dataset (raw dan processed)
├── reports/          # Hasil analisis dan laporan
└── cloud_storage/    # Integrasi dengan cloud storage
```

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Apache Spark 4.1.1** - Framework untuk pemrosesan big data
- **PySpark** - API Python untuk Apache Spark
- **Py4J 0.10.9.9** - Library untuk integrasi Python dengan JVM

## 📦 Instalasi

### Prerequisites

Pastikan Anda telah menginstall:
- Python 3.8 atau lebih baru
- Java JDK 8 atau 11 (diperlukan untuk menjalankan Spark)

### Langkah Instalasi

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/Hzkun001/praktikum-bigdata-1.git
   cd praktikum1
   ```

2. **Buat virtual environment (opsional tapi disarankan):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Untuk macOS/Linux
   # atau
   .venv\Scripts\activate     # Untuk Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Cara Menjalankan

### Menjalankan Simple Job

```bash
python scripts/simple_job.py
```

Script ini akan:
1. Membuat Spark session
2. Membuat DataFrame dari data contoh
3. Melakukan agregasi data berdasarkan kategori
4. Menampilkan hasil agregasi

### Output yang Diharapkan

```
+--------+----------+
|category|sum(value)|
+--------+----------+
|       B|        20|
|       A|        40|
+--------+----------+
```

## 📊 Contoh Penggunaan

### Simple Job - Agregasi Data

File `simple_job.py` mendemonstrasikan operasi dasar PySpark:

```python
from pyspark.sql import SparkSession

# Membuat Spark session
spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

# Data contoh
data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

# Buat dataframe
df = spark.createDataFrame(data, columns)

# Agregasi data
df.groupBy("category").sum("value").show()

spark.stop()
```

## 🔧 Konfigurasi

### Spark Configuration

Anda dapat mengkustomisasi konfigurasi Spark dengan menambahkan parameter pada SparkSession:

```python
spark = SparkSession.builder \
    .appName("SimpleJob") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
```

## 📝 TODO

- [ ] Menambahkan notebook analisis data
- [ ] Implementasi pembacaan data dari file eksternal
- [ ] Integrasi dengan cloud storage
- [ ] Menambahkan unit tests
- [ ] Implementasi data pipeline yang lebih kompleks

## 🤝 Kontribusi

Proyek ini merupakan bagian dari tugas praktikum. Untuk kontribusi:

1. Fork repositori ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 👨‍💻 Author

**Akhmad Hafidz Ardianto**

- GitHub: [@Hzkun001](https://github.com/Hzkun001)

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan praktikum Big Data.

## 📚 Referensi

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [PySpark Getting Started](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)

---

⭐ Jangan lupa berikan star jika repositori ini membantu!
