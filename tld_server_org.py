import socket

port = 58
ip_addr = "3.2.6.7"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sock.bind((ip_addr, port))
print ("Tld server of org listening...")

while 1:
    data, addr = sock.recvfrom(512)
    #data = "lol.com"

    domain_name, tld_type = data.split('.')
    with open("tld names") as myfile:
        lines = myfile.readlines()
        print lines

        for line in lines:
            if domain_name in line:
                print "cool"
                print line
                name, ip = line.split(' ')
                print name
                print ip
                sock.sendto()
            else:
                print ("Not available: " + data)
                exit()
    #sock.sendto(data, ip_addr)
    #sock.sendto(domain_name, addr)

    #Send back to root
    #Look for Auth Name server
    #data = "google.com A"
    #print type(data)
    #print data

    #domain, dns_type = data.split('.')
    #print domain
    #print dns_type

    #with open("tld_cache.txt") as myfile:
    #    line = myfile.readlines()
    #    print type(line)