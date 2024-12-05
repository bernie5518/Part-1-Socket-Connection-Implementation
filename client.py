import socket

def start_client():
    """
    Starts a client that can send and receive messages and disconnect gracefully.
    """
    host = '127.0.0.1'  # Server's IP address
    port = 65432        # Server's port

    try:
        # Step 1: Create the client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Client socket created.")

        # Step 2: Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            try:
                # Step 3: Receive a message from the server
                server_message = client_socket.recv(1024).decode()  # Receive and decode data
                if server_message.lower() == 'exit':
                    print("Server requested to disconnect.")
                    break
                print(f"Received from server: {server_message}")

                # Step 4: Send a message to the server
                client_message = input("Enter a message to send to the server (type 'exit' to disconnect): ")
                if client_message.lower() == 'exit':
                    print("Client is closing the connection.")
                    client_socket.sendall(client_message.encode())
                    break
                client_socket.sendall(client_message.encode())
            except Exception as e:
                print(f"Error during communication: {e}")
                break
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        # Step 5: Close the client socket
        client_socket.close()
        print("Client socket closed.")

if __name__ == "__main__":
    start_client()
