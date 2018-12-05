import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 65000
MESSAGE = raw_input("Enter your message: ")

# print "UDP target IP:", UDP_IP
# print "UDP target port:", UDP_PORT
# print "message:", MESSAGE

print "Sending!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data, server = sock.recvfrom(512)
print(data)
print "Sent!"