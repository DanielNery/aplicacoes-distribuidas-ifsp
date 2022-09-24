import socket

HOST = "127.0.0.1"
PORT = 50000
MAX_BYTES_PACKAGE = 1024

valor_produto = str(input("\nInforme o valor do produto: "))

# ipv4 tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(valor_produto.encode())
novo_valor = s.recv(MAX_BYTES_PACKAGE)
print(f"Produto: {novo_valor.decode()}")


