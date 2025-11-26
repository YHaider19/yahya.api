from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "🔥 Yahya API — Production Ready!"}

@app.route("/about")
def about():
    return {
        "name": "Yahya",
        "project": "Backend API with AWS",
        "version": "1.0",
        "status": "OK"
    }

@app.route("/hello/<name>")
def hello(name):
    return {"message": f"Hello {name}! Welcome to Yahya's API 🚀"}

@app.route("/health")
def health():
    return {"status": "healthy", "service": "flask"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
