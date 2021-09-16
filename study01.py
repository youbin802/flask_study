from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/main', methods=['GET'])
def main():
    color = {'2021-02-01':'youbin', '2021-02-04':'JYP'}
    return render_template('main.html', value=color)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404

if __name__ == '__main__':
    app.run(debug=True)

