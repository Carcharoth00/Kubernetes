from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/health')
def health():
	return {"status": "ok"}

@app.route('/hello')
def hello():
	return {"mensaje": "Hola desde el backend - v2"}

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
