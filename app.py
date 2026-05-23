from flask import Flask, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_request_count', 'Total request count')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return render_template('index.html')

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)