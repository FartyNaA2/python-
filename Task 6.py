from fastapi import FastAPI
import threading
import time
import requests
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")


if __name__ == "__main__":
    # Запускаємо сервер у фоновому потоці
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Даємо серверу 1 секунду, щоб запуститися
    time.sleep(1)

    # Клієнтський запит
    try:
        response = requests.get("http://127.0.0.1:8000/")
        print("Відповідь від сервера:", response.json())
    except Exception as e:
        print("Помилка під час запиту:", e)
