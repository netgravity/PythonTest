import pcapy
from struct import *
import binascii

devs = pcapy.findalldevs()
print(devs)


cap = pcapy.open_live('\\Device\\NPF_{6D0AC5EA-31A9-4820-B472-3A80D8164AD1}', 65536, 1, 0)


def ipv4(addr):
    return '.'.join(map(str, addr))


def ConvertHexToIP(hexdata):
    a = [hexdata[i:i + 2] for i in range(0, len(hexdata), 2)]
    b = map(str, a)
    # print b

    def hexi(n):
        d = int(n, 16)
        return str(d)
    c = map(hexi, b)
    return ('.'.join(map(str, c)))


def EthernetMap(eth_addr):
    eth_addr1 = [eth_addr[i:i + 2] for i in range(0, len(eth_addr), 2)]
    return '.'.join(map(str, eth_addr1))


while 1:
    (header, payload) = cap.next()
    l2hdr = payload[:14]
    # print (ord(l2hdr[5]))
    l2data = unpack("!6s6sH", l2hdr)
    # print l2data
    dstmac = binascii.hexlify(l2data[0])
    srcmac = binascii.hexlify(l2data[1])
    eth_Protocol = hex(l2data[2])

    # dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[0]), ord(
    #     l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
    # srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[6]), ord(
    #     l2hdr[7]), ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
    print ('====================++++  Ethernet Header Info  ++++======================')
    # print("Source MAC: ", srcmac, " Destination MAC: ", dstmac, "eth_Protocol: ", eth_Protocol)
    print ("Source_MAC: {}, Dest_Mac: {}, Eth_Protocol: {}").format(
        EthernetMap(srcmac), EthernetMap(dstmac), eth_Protocol)


# get IP header, which is 20 bytes long
# then unpack it into what it is
    ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
    timetolive = ipheader[5]
    protocol = ipheader[6]
    # Src_IP = ipv4(ipheader[8])
    Src_IP_hex = binascii.hexlify(ipheader[8])
    # print (Src_IP_hex)
    Src_IP = ConvertHexToIP(Src_IP_hex)
    DST_IP_Hex = binascii.hexlify(ipheader[9])
    DST_IP = ConvertHexToIP(DST_IP_Hex)
    # DST_IP = ipheader[9]
    # DST_IP_Hex = (ipheader[9])
    # DST_IP = ipv4(DST_IP_Hex)
    print ('====================++++  IP Header Info  ++++======================')
    print("Protocol ", str(protocol), " Time To Live: ", str(timetolive),
          'Source_IP: ', Src_IP,  'Dest_IP: ', DST_IP)
    print ('\n')
    # print (len(ipheader))
