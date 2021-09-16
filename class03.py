import json
from flask import Flask , request
app = Flask(__name__)

# GET 방식 
# URL http://127.0.0.1:5003/board?question=anw 
@app.route("/board")
def board_list():
    return f"question 변수의 값은 {request.args.get('question')}"

@app.route("/boards",methods=["POST"])
def board_list2():
    post_result = json.loads(request.get_data())
    
    return f"question 변수의 값은 {post_result}"

@app.route("/dobule",methods=["POST","GET"])
def dobule():
    if request.method == "GET":
        return "GET 요청 내용은{}".format(request.args.get('question'))
    if request.method == "POST":
        return "POST 요청 내용은{}".format(json.loads(request.get_data()))

        
app.run(host="localhost",port=5003)

#f-string : formatting
#-> 백슬래시(\) 사용 불가