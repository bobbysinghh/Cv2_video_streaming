import socket,cv2, pickle,struct


#socket creation

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.29.76'  # paste your server ip address here
port = 9999
print("Socket Created Successfully")

# Binding the socket with ip and port no 9999 . choose any  port no which you want

client_socket.connect((host_ip,port)) # a tuple
data = b""
payload_size = struct.calcsize("Q")
print("Socket Accepted")

while True:
    while len(data)< payload_size:
        packet = client_socket.recv(4*1024) # 4 bytes
        if not packet : break
        data+=packet
    packed_msg_size= data[:payload_size]
    data= data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4*1024) # 4 bytes
        frame_data= data[:msg_size]
        data = data[msg_size:]
        frame= pickle.loads(frame_data)
        cv2.imshow("Receiving Video", frame)
        key= cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            client_socket.close()

print("THANK YOU ALL")