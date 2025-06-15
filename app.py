# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
# import subprocess   # ← ngrok 자동 실행 시 사용

app = Flask(__name__)

def get_ngrok_url() -> str | None:
    """현재 실행 중인 ngrok(4040 API)에서 https 터널 주소를 가져온다."""
    try:
        res = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=2)
        tunnels = res.json().get("tunnels", [])
        for t in tunnels:
            if t.get("proto") == "https":
                return t["public_url"]
    except Exception as e:
        print("⚠️  ngrok URL fetch error:", e)
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/heat")
def page_heat():
    return render_template("heat.html")

@app.route("/optics")
def page_optics():
    return render_template("optics.html")

@app.route("/imaging")
def page_imaging():
    return render_template("imaging.html")

if __name__ == "__main__":
    # subprocess.Popen(["ngrok", "http", "5000"])  # ← 원하면 주석 해제
    public = get_ngrok_url()
    print("✅ Flask server is running")
    if public:
        print("🌐 Public access URL:", public)
    else:
        print("🌐 ngrok not detected (run `ngrok http 5000` separately)")
    app.run(host="0.0.0.0", port=5000)

    app.run(host="0.0.0.0", port=5000)
