import socket

port = 65000
ip_addr = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((ip_addr, port))
print "Listening..."

while 1:
    data, addr = sock.recvfrom(512)
    #data = "google.com A"
    #print type(data)
    #print data

    domain, dns_type = data.split(' ')
    print domain
    print dns_type

    with open("mappingFirstChild.txt") as myfile:
        line = myfile.readlines()
        print type(line)

    for x in line:
        temp = x.split(' ')
        if temp[0]=='ns.'+domain:
            print("found in cache...")
            sock.sendto(x,(ip_addr))