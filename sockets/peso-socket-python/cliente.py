import socket
import json

HOST = "127.0.0.1"
PORT = 50000
MAX_BYTES_PACKAGE = 1024

peso_atual = str(input("\nInforme o peso atual: "))
peso_desejado = str(input("\nInforme o peso desejado: "))

pesos = {
    "peso_atual": peso_atual,
    "peso_desejado": peso_desejado
}

dados = json.dumps(pesos)

# ipv4 tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(dados.encode())
percentual = s.recv(MAX_BYTES_PACKAGE)
print(f"Percentual: {percentual.decode()}")


