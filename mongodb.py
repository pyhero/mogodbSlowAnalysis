from flask import Flask

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('mongodb_slowlog.html')

if __name__ == '__main__':
    app.run(port=5001)
