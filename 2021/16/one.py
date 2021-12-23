literal_value= 'D2FE28'
operator = '38006F45291200'
operator_2 = 'EE00D40C823060'

example_a = '8A004A801A8002F478'
example_b = '620080001611562C8802118E34'
example_c = 'C0015000016115A2E0802F182340'
example_d = 'A0016C880162017C3686B18A3D4780'

input = open('input.txt', 'r')
lines = [ v.rstrip() for v in input.readlines()  ]

version_sum = 0
def vsum(v):
    global version_sum
    version_sum = version_sum + v

def parse_literal(data):
    version = int(data[:3], 2)
    type_id = int(data[3:6], 2)

    bits = ''
    for pos in range(6, len(data), 5):
        bits = bits + data[pos+1: pos+5]

        if data[pos] == '0':
            return pos + 5, int(bits, 2)

    raise Exception(f'Invalid literal {data}')

def parse_packet(data):

    version = int(data[:3], 2)
    type_id = int(data[3:6], 2)
    vsum(version)

    if type_id == 4:
        #print('LITERAL       version/type_id', (version, type_id))
        return parse_literal(data)
    else:
        length_type_id = data[6] 
        if length_type_id == '0':
            #print('OPERATOR(len) version/type_id', (version, type_id))
            # next 15 bits are a number that represents the total length in
            # bits of the sub-packets contained by this packet.
            pos = 22
            total_len = 22 + int(data[7:22], 2)
            while pos < total_len:
                packet_end, val = parse_packet(data[pos:total_len])
                pos = pos + packet_end

            return pos, None

        else:
            #print('OPERATOR(cnt) version/type_id', (version, type_id))
            # next 11 bits are a number that represents the number of
            # sub-packets immediately contained by this packet.
            pos = 18
            sub_packets = int(data[7:18], 2)
            for i in range(sub_packets): # something if off here
                packet_end, value = (parse_packet(data[pos:]))
                pos = pos + packet_end
            return pos, None

def convertHex(raw):
    return bin(int('1'+raw, 16))[3:] # hack to preseve leading zero

print(parse_packet(convertHex(lines[0])))
print(version_sum)

