from flask import Flask
app = Flask(__name__)

@app.get("/")
def root():
    return "users service v1.0\n"

@app.get("/healthz")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
