def change_to_hex(num):
    final = ''
    for i in range(len(num)):
        final = final + hex_change[num[i]]
    return final

hex_change = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
s = '123123123333333333333'
print(s.find('33333'))

print(change_to_hex('A'))