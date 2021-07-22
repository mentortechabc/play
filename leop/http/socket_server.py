import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7000

print("listening on {0}:{1}".format(SERVER_HOST, SERVER_PORT))

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse address on Ctrl+C
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)


def is_file_accessible(path_to_file: str, mode='r') -> bool:
    """
    Проверка, является ли файл или папка из `path`
    доступным для работы в предоставленном `mode` формате.
    """
    try:
        f = open(path_to_file, mode)
        f.close()
        return True
    except IOError:
        return False


def handle_error(client: socket, message: str):
    client.sendall('HTTP/1.0 {0}\n\n'.format(message).encode())
    client.close()


while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()

    # Parse HTTP headers
    top_line = request.splitlines()[0]
    top_line_split = top_line.split(" ")
    method = top_line_split[0]
    filename = top_line_split[1]

    if filename == '/':
        filename = '/index.html'

    path = 'htdocs' + filename

    if not is_file_accessible(path):
        handle_error(client_connection, '404 Not Found')
        continue

    if method != 'GET':
        handle_error(client_connection, '405 Method Not Allowed')
        continue

    fin = open(path)
    content = fin.read()
    fin.close()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

server_socket.close()
