
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
uri = os.getenv("MONGO_URI")

try:
	client = MongoClient(uri)
	print("Koneksi berhasil!")
	print(client.list_database_names())
except Exception as e:
	print("Koneksi gagal:", e)