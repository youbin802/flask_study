from flask import Flask
app = Flask(__name__)

#일반적인 라우팅 방식
@app.route('/board')
def board():
    return "그냥 보드"


# 단순하게 입력값 받아서 그 주소로 라우팅
# url 매개변수 받음
@app.route('/board/<article_idx>')
def board_view(article_idx):
    return article_idx


@app.route('/boards',defaults={'page':'index'})

@app.route('/boards/<page>')
def boards(page):
    return page+"페이지입니다."

app.run(host="localhost",port=5001)