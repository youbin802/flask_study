from flask import Flask
app = Flask(__name__)

def index():
    return 'index'

def main():
    return 'main'

app.add_url_rule('/','index',index)
app.add_url_rule('/main','main',main)

app.run(host='localhost', port=5002)
