import socket
import threading

IP = '0.0.0.0'
PORT = 9998

#In this function we pass in the IP and Port for the server to listen to and set the max connections to 5 and put it into a
#continous While loop. Once we get a hit we put the connection details into the address varaiable and pass the connection to
#the client_handler function so we can snag another connection.
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')
    
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
 main()