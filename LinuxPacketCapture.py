import socket
import struct
import binascii


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
#s.bind(('192.168.1.24', 0))
#s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
# conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))


def main():
    while True:
        # print s.recvfrom(65565)
        raw_data, addr = s.recvfrom(65565)
        dest_mac, src_mac, eth_prot = eth_header(raw_data)
        print ('Destination Mac: {}, Source Mac: {}, Protocol: {}'. format(
            dest_mac, src_mac, eth_prot))


def eth_header(data):
    storeobj = data[:14]
    storeobj = struct.unpack('!6s6sH', storeobj)
    # dest_mac = binascii.hexlify(storeobj[0])
    dest_mac = eth_addr(storeobj[0])
    src_mac = binascii.hexlify(storeobj[1])
    eth_protocol = socket.ntohs(storeobj[2])
    #eth_protocol = storeobj[2]
    return dest_mac, src_mac, eth_protocol
# Get string of 6 characters as ethernet address into dash seperated hex string


def eth_addr(a):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(
        a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b


main()
