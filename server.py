import socket
import threading
import os
import mimetypes
import logging
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080
WWW_DIR = 'www'
LOG_FILE = 'server.log'

def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def handle_client(conn, addr):
    try:
        request = conn.recv(2048).decode('utf-8')
        method, path, _ = request.split(' ', 2)
    except Exception:
        conn.close()
        return

    logging.info(f"Richiesta da {addr}: {method} {path}")

    if method != 'GET':
        response = 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'
        conn.sendall(response.encode())
        logging.warning(f"Metodo non supportato: {method}")
        conn.close()
        return

    if path == '/':
        path = '/index.html'
    file_path = os.path.join(WWW_DIR, path.lstrip('/'))

    if os.path.isfile(file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type = mime_type or 'application/octet-stream'
        with open(file_path, 'rb') as f:
            content = f.read()
        header = (
            'HTTP/1.1 200 OK\r\n'
            f'Content-Type: {mime_type}; charset=UTF-8\r\n'
            f'Content-Length: {len(content)}\r\n'
            'Connection: close\r\n'
            '\r\n'
        )
        conn.sendall(header.encode('utf-8') + content)
        logging.info(f"200 OK: {path} ({mime_type})")
    else:
        body = b'<h1>404 Not Found</h1><p>Risorsa non disponibile.</p>'
        header = (
            'HTTP/1.1 404 Not Found\r\n'
            'Content-Type: text/html; charset=UTF-8\r\n'
            f'Content-Length: {len(body)}\r\n'
            'Connection: close\r\n'
            '\r\n'
        )
        conn.sendall(header.encode('utf-8') + body)
        logging.warning(f"404 Not Found: {path}")

    conn.close()

def run_server():
    setup_logging()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f'Server in ascolto su http://{HOST}:{PORT}')
        logging.info(f"Server avviato su {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == '__main__':
    run_server()