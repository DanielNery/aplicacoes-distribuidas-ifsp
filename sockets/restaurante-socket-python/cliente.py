import socket

HOST = "127.0.0.1"
PORT = 50000
MAX_BYTES_PACKAGE = 1024

# Lendo total de despesas
total_despesas = str(input("\nInforme o total de despesas: "))

# ipv4 tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(total_despesas.encode())
gorjeta = s.recv(MAX_BYTES_PACKAGE)
print(f"Gorjeta: {gorjeta.decode()}")


