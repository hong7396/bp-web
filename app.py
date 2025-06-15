# -*- coding: utf-8 -*-


from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_ngrok_url():
    try:
        res = requests.get("http://127.0.0.1:4040/api/tunnels")
        data = res.json()
        for tunnel in data['tunnels']:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
        return "Could not find HTTPS address"
    except Exception as e:
        return f"Failed to fetch ngrok URL: {e}"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    print("✅ Flask server is running")
    print("🌐 Public access URL:", get_ngrok_url())
    app.run(host="0.0.0.0", port=5000)
