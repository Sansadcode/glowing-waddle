from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def forms():
    return render_template('forms.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
