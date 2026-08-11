from flask import Flask, render_template

# create client
app = Flask(__name__)


@app.route('/')
# home => render index.html
def home():
    return render_template('index.html')




# run main fnx
if __name__ == '__main__':
    app.run(debug=True, port=5002)