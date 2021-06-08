import socket,cv2, pickle,struct


#socket creation

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = ('192.168.29.76',port)
print("Socket Created Successfully")
# Binding the socket with ip and port no 9999 . choose any  port no which you want

server_socket.bind(socket_address)
print("Socket Bind Successfully")

server_socket.listen(5)
print("Listening At:",socket_address)

print("Socket Accepted")

while True:
    client_socket,addr = server_socket.accept()
    print('connected from',addr)
    if client_socket:
        video = cv2.VideoCapture(0) # 0 for internel cam 1 for external cam

        while(video.isOpened()):
            img,frame = video.read()
            temp = pickle.dumps(frame)
            message = struct.pack("Q",len(temp))+temp
            client_socket.sendall(message)

            cv2.imshow('Transmitting Video',frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                client_socket.close()

print("THANK YOU ALL")