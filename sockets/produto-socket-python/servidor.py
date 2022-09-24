import socket

def calcular_novo_valor(valor_produto):
    return str( valor_produto * 1.25 ).encode()

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
    valor_produto = conn.recv(MAX_BYTES_PACKAGE) # Recebendo mensagem do cliente
    if not valor_produto:
        print("Fechando Conexão...")
        conn.close()
        break
    
    novo_valor = calcular_novo_valor(float(valor_produto))
    conn.sendall(novo_valor) # Enviando resposta ao cliente
