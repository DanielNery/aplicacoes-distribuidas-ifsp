import socket

def calcular_gorjeta(total_despesa):
    return str(total_despesa * 0.1).encode("UTF-8")

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
    total_despesa = conn.recv(MAX_BYTES_PACKAGE) # Recebendo mensagem do cliente
    if not total_despesa:
        print("Fechando Conexão...")
        conn.close()
        break
    
    gorjeta = calcular_gorjeta(float(total_despesa))
    conn.sendall(gorjeta) # Enviando resposta ao cliente
