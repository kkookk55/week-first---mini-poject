from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient("mongodb+srv://test:test@cluster0.15fhovx.mongodb.net/test", tlsCAFile=ca)
db = client.dbsparta_plus_week4

@app.route('/')
def home():
    return render_template('mainpage.html')


@app.route("/posts", methods=["GET"])
def posts_get():
    posts_list = list(db.mbti.find({},{'_id':False}))
    return jsonify({'post':posts_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)