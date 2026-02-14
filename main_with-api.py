import socket
import threading
import json
from services.health_system import HealthSystem
from services.admin_service import AdminService
from services.symptom_service import SymptomEngine
from utils.load_data_with_db import DataLoadWithDB
from database.init_db import init_db

HOST = "127.0.0.1"
PORT = 8080

data = DataLoadWithDB()
init_db(data)
admin = AdminService(data)
system = HealthSystem(data)
symptomEngine = SymptomEngine(data)

def parse_request(request):
    try:
        headers_part, body = request.split("\r\n\r\n", 1)
        lines = headers_part.split("\r\n")
        method, path, _ = lines[0].split()
        headers = {}
        for line in lines[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key] = value
        return method, path, headers, body

    except Exception as e:
        print("Parse error", e)  
        return None, None, {}, None      

def http_response(status_code, data):
    reason = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        404: "Not Found"
    }.get(status_code, "OK")
    print(data)
    body = json.dumps(data)
    headers = [
        f"HTTP/1.1 {status_code} {reason}",
        "Content-Type: application/json",
        f"Content-Length: {len(body)}",
        "Connection: close",
        "",
        body
    ]
    return "\r\n".join(headers)

def process_request(request):
    
    method, path, headers, body = parse_request(request)

    if path == "/doctors" and method == "GET":
        doctors = system.all_doctors()
        return http_response(200, {"data": doctors})
      

def handle_client(conn, addr):
    request = conn.recv(1024).decode('utf-8')
    response = process_request(request)
    if response:
        conn.sendall(response.encode('utf-8'))
    conn.close()    

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"server is runing on http://{HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()


