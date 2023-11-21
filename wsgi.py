from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
# from app import app

app = Flask(__name__)

cxn_str = 'mongodb+srv://franklinchang08:123456788@felix08.jreclb8.mongodb.net/'
client = MongoClient(cxn_str)
db = client.db_restaurant

@app.route('/')
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)