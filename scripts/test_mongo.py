from pymongo import MongoClient

uri = "mongodb+srv://hawpiw:hawpiw123@cluster0.jexqv2h.mongodb.net/?appName=Cluster0"
try:
	client = MongoClient(uri)
	print("Koneksi berhasil!")
	print(client.list_database_names())
except Exception as e:
	print("Koneksi gagal:", e)