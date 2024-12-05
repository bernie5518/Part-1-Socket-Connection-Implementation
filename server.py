import socket
from datetime import datetime

def log_with_timestamp(message):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")

def start_server():
    """
    Starts a server that can send and receive messages and disconnect gracefully.
    """
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    try:
        # Step 1: Create the server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log_with_timestamp("Server socket created.")

        # Step 2: Bind the server socket
        server_socket.bind((host, port))
        log_with_timestamp(f"Server socket bound to {host}:{port}")

        # Step 3: Listen for incoming connections
        server_socket.listen(5)
        log_with_timestamp("Server is listening for incoming connections.")

        while True:
            log_with_timestamp("Waiting for a connection...")
            conn, addr = server_socket.accept()  # Accept a new connection
            log_with_timestamp(f"Connection established with {addr}")

            try:
                while True:
                    # Step 4: Server sends a message to the client
                    server_message = input("Enter a message to send to the client (type 'exit' to disconnect): ")
                    if server_message.lower() == 'exit':
                        log_with_timestamp("Server is closing the connection.")
                        conn.sendall("exit".encode())  # Notify the client
                        break
                    conn.sendall(server_message.encode())  # Send the message
                    log_with_timestamp("Message sent to the client.")

                    # Step 5: Receive a message from the client
                    client_message = conn.recv(1024).decode()  # Receive and decode data
                    if client_message.lower() == 'exit':
                        log_with_timestamp("Client requested to disconnect.")
                        break
                    log_with_timestamp(f"Received from client: {client_message}")
            except Exception as e:
                log_with_timestamp(f"Error during communication: {e}")
            finally:
                # Step 6: Close the connection
                conn.close()
                log_with_timestamp(f"Connection with {addr} closed.")
    except socket.error as e:
        log_with_timestamp(f"Socket error: {e}")
    except Exception as e:
        log_with_timestamp(f"Server error: {e}")
    finally:
        server_socket.close()
        log_with_timestamp("Server socket closed.")

if __name__ == "__main__":
    start_server()
