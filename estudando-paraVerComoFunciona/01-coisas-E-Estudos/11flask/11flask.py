from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'oi mundo '

if __name__=='__main__':
    app.run()