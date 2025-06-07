import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,address = server.accept() # wait for client
    print("Client connected from", address)
    try:
        message_id = (0).to_bytes(4, byteorder="big", signed=True)
        corr_id = (7).to_bytes(4, byteorder="big", signed=True)
        connection.sendall(message_id + corr_id)
    except Exception as e:
        print("exc occured: ", str(e))


if __name__ == "__main__":
    main()
