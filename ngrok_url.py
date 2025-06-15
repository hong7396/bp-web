# ngrok_url.py
import requests
import time

def get_ngrok_url():
    time.sleep(2)  # ngrok이 완전히 뜰 때까지 잠시 대기
    try:
        r = requests.get("http://127.0.0.1:4040/api/tunnels")
        data = r.json()
        public_url = data['tunnels'][0]['public_url']
        return public_url
    except Exception as e:
        return f"ngrok 주소 가져오기 실패: {e}"
