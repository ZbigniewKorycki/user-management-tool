from client_logic import Client

import socket

client = Client('192.168.0.163', 61033, 1024)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client.host, client.port))

run_client = True
while run_client:
    command = input('Command: ').encode("utf8")
    if command.decode("utf8") == 'login':
        client_socket.send(command)
        username = input('Input username: ').encode("utf8")
        password = input('Input password: ').encode("utf8")
        client_socket.send(username)
        client_socket.send(password)
        if client_socket.recv(client.buffer).decode("utf8") == '"Correct_login_and_password"':
            print(client_socket.recv(client.buffer).decode("utf8"))
            available_commands_list = client_socket.recv(client.buffer).decode("utf8")
            print(available_commands_list)
            while True:
                command = input('Command: ').encode("utf8")
                if command.decode("utf8") == 'stop' and command.decode("utf8") in available_commands_list:
                    client_socket.send(command)
                    client_socket.close()
                    run_client = False
                    break
                elif command.decode("utf8") == 'send' and command.decode("utf8") in available_commands_list:
                    client_socket.send(command)
                    recipient = input('Message recipient: ').encode("utf8")
                    client_socket.send(recipient)
                    message = input('Message: ').encode("utf8")
                    client_socket.send(message)
                    print(client_socket.recv(client.buffer).decode("utf8"))

                elif command.decode("utf8") == 'send-to-all' and command.decode("utf8") in available_commands_list:
                    client_socket.send(command)
                    message = input('Message to all users: ').encode("utf8")
                    client_socket.send(message)
                    print(client_socket.recv(client.buffer).decode("utf8"))

                elif command.decode("utf8") == 'add-user' and command.decode("utf8") in available_commands_list:
                    client_socket.send(command)
                    username = input('Input username: ').encode("utf8")
                    client_socket.send(username)
                    print(client_socket.recv(client.buffer).decode("utf8"))

                elif command.decode("utf8") == 'logout' and command.decode("utf8") in available_commands_list:
                    client_socket.send(command)
                    print(client_socket.recv(client.buffer).decode("utf8"))
                    break

                else:
                    client_socket.send(command)
                    print(client_socket.recv(client.buffer).decode("utf8"))

        else:
            print(client_socket.recv(client.buffer).decode("utf8"))

    elif command.decode("utf8") == 'add-admin':
        client_socket.send(command)
        admin_name = input('Input admin name: ').encode("utf8")
        client_socket.send(admin_name)
        print(client_socket.recv(client.buffer).decode("utf8"))

    else:
        client_socket.send(command)
        print(client_socket.recv(client.buffer).decode("utf8"))
