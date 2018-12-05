import socket

port = 57
ip_addr = "127.0.0.1"

auth_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sock.bind((ip_addr, port))
print "Auth server listening..."

while 1:
    data, addr = auth_sock.recvfrom(512)
    data = "bob.com"

    with open("mappingSolution.txt") as myfile:
        for line in myfile:
            print type(line)

            if data in line:
                # Send back to TLD
                print line
                auth_sock.sendto(line, addr)
                print "Sent!"

    # data = "google.com A"
    # print type(data)
    # print data

    # domain, dns_type = data.split('.')
    # print domain
    # print dns_type

    #domain_name, tld_type = data.split(' ')
        # Look for Auth Name server
        #sock.sendto(domain_name, ip_addr)