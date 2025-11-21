import socket

#Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

def send_and_receive(prompt=True):
    message = client.recv(1024).decode()
    if prompt:
        response = input(message + " ") #Shows the message as a prompt
        client.send(response.encode())
    else:
        print(message) #Prints message without responding

#Get Action (login or signup)
send_and_receive() #Do you want to login or signup?

#Receives and responds based on the server prompts
while True:
    try:
        message = client.recv(1024).decode()

        #final success or fail message - print and break
        if "Login Successful" in message or "Login Failed" in message or "Signup Successful" in message or "Signup Failed" in message:
            print(message)
            break
        response= input(message + " ")
        client.send(response.encode())
    except KeyboardInterrupt:
        print("\nClient closed")
        break
