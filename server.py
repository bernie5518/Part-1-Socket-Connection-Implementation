import socket

def start_server():
    """
    Starts a server that can send and receive messages and disconnect gracefully.
    """
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    try:
        # Step 1: Create the server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server socket created.")

        # Step 2: Bind the server socket
        server_socket.bind((host, port))
        print(f"Server socket bound to {host}:{port}")

        # Step 3: Listen for incoming connections
        server_socket.listen(5)
        print("Server is listening for incoming connections.")

        while True:
            print("Waiting for a connection...")
            conn, addr = server_socket.accept()  # Accept a new connection
            print(f"Connection established with {addr}")

            try:
                while True:
                    # Step 4: Server sends a message to the client
                    server_message = input("Enter a message to send to the client (type 'exit' to disconnect): ")
                    if server_message.lower() == 'exit':
                        print("Server is closing the connection.")
                        conn.sendall("exit".encode())  # Notify the client
                        break
                    conn.sendall(server_message.encode())  # Send the message
                    print("Message sent to the client.")

                    # Step 5: Receive a message from the client
                    client_message = conn.recv(1024).decode()  # Receive and decode data
                    if client_message.lower() == 'exit':
                        print("Client requested to disconnect.")
                        break
                    print(f"Received from client: {client_message}")
            except Exception as e:
                print(f"Error during communication: {e}")
            finally:
                # Step 6: Close the connection
                conn.close()
                print(f"Connection with {addr} closed.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    start_server()
