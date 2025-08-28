from pymongo import MongoClient
import os

uri = os.getenv("MONGO_URI")  # or paste it directly here for testing
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=False)
print(client.list_database_names())
