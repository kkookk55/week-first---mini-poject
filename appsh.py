from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.xig8tvq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/writing')
def homes():
    return render_template('writing.html')

@app.route('/writing', methods=['POST'])
def web_mbti_post():
    title_receive = request.form['title_give']
    mbti_receive = request.form['mbti_give']
    contents_receive = request.form['contents_give']
# doc = 저장
    doc = {
        'title':title_receive,
        'mbti':mbti_receive,
        'contents':contents_receive
    }
    db.mbti.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/index", methods=["GET"])
def contents_get():
    contents_list = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'content':contents_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
