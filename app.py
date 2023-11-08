from flask import Flask, render_template

app = Flask(__name__)


# Define routes and their corresponding functions
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
