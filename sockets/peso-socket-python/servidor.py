import socket
import json

def calcular_percentual(dados):
    peso_atual = dados.get("peso_atual")
    peso_desejado = dados.get("peso_desejado")
    return str( float(peso_desejado) * 100  / float(peso_atual) ).encode()

HOST = "127.0.0.1"
PORT = 50000
MAX_BYTES_PACKAGE = 1024

# IPV4 e TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen() # Modo de escuta
print("Aguardando conexão do cliente.")
conn, endereco = s.accept() # Aceitando conexão do cliente
print(f"Conectado em {endereco}")
while True:
    dados = conn.recv(MAX_BYTES_PACKAGE) # Recebendo mensagem do cliente
    if not dados:
        print("Fechando Conexão...")
        conn.close()
        break
    
    percentual = calcular_percentual(json.loads(dados))
    conn.sendall(percentual) # Enviando resposta ao cliente
