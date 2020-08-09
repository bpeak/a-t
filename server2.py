from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "444"

app.run(host='0.0.0.0', port=80)

