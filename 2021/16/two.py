import math

example = '04005AC33890 '
# C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
# 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
# 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
# CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
# D8005AC2A8F0 produces 1, because 5 is less than 15.
# F600BC2D8F produces 0, because 5 is not greater than 15.
# 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
# 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.


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

def calculate(vals, type_id):
    # print(f'calculate {type_id}', vals)
    if type_id == 0:
        return sum(vals)
    elif type_id == 1:
        return math.prod(vals)
    elif type_id == 2:
        return min(vals)
    elif type_id == 3:
        return max(vals)
    elif type_id == 5:
        if len(vals) != 2:
            raise Exception('Greater than check requires 2 packets')
        return vals[0] > vals[1]
    elif type_id == 6:
        if len(vals) != 2:
            raise Exception('Less than check requires 2 packets')
        return vals[0] < vals[1]
    elif type_id == 7:
        if len(vals) != 2:
            raise Exception('Equal check requires 2 packets')
        return vals[0] == vals[1]

    raise Exception('Unknown packet type')


def parse_packet(data):

    version = int(data[:3], 2)
    type_id = int(data[3:6], 2)
    vsum(version)

    if type_id == 4:
        #print('LITERAL       version/type_id', (version, type_id))
        return parse_literal(data)
    else:
        length_type_id = data[6] 
        vals = []
        if length_type_id == '0':
            #print('OPERATOR(len) version/type_id', (version, type_id))
            # next 15 bits are a number that represents the total length in
            # bits of the sub-packets contained by this packet.
            pos = 22
            total_len = 22 + int(data[7:22], 2)
            while pos < total_len:
                packet_end, val = parse_packet(data[pos:total_len])
                pos = pos + packet_end
                vals.append(val)

            return pos, calculate(vals, type_id)

        else:
            #print('OPERATOR(cnt) version/type_id', (version, type_id))
            # next 11 bits are a number that represents the number of
            # sub-packets immediately contained by this packet.
            pos = 18
            sub_packets = int(data[7:18], 2)
            for i in range(sub_packets): # something if off here
                packet_end, val = (parse_packet(data[pos:]))
                pos = pos + packet_end
                vals.append(val)
            return pos, calculate(vals, type_id) 

def convertHex(raw):
    return bin(int('1'+raw, 16))[3:] # hack to preseve leading zero

print(parse_packet(convertHex(lines[0])))
print(version_sum)

