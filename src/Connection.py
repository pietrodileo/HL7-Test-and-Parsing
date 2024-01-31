import socket

def send_hl7_message(hl7_message, host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(hl7_message.encode("utf-8"))
            data = s.recv(1024)
            return data.decode("utf-8")

    except ConnectionError as ce:
        print(f"Error connecting to the server: {str(ce)}")
        return None

    except Exception as e:
        print(f"Error during the communication with the server: {str(e)}")
        return None
