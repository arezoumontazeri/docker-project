from flask import Flask
import os
import psycopg2
app = Flask(__name__)
@app.route('/')
def hello():
 conn = psycopg2.connect(
 dbname=os.getenv('DB_NAME'),
 user=os.getenv('DB_USER'),
 password=os.getenv('DB_PASSWORD'),
 host='db',
 port='5432'
 )
 conn.close()
 return "Hello, World!"
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
