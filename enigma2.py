import time

plaintext = input('Enter a message using only abcdef: ')
ciphertext = ''

plugboard = {'a':'c', 'b':'d', 'c':'a', 'd':'b', 'e':'f', 'f':'e'}
reflector = {'a':'f', 'b':'e', 'c':'d', 'd':'c', 'e':'b', 'f':'a'}

wheel0 = {1:{'a':'e', 'b':'d', 'c':'f', 'd':'a', 'e':'b', 'f':'c'}, 
          2:{'a':'c', 'b':'e', 'c':'d', 'd':'f', 'e':'a', 'f':'b'},
          3:{'a':'b', 'b':'c', 'c':'e', 'd':'d', 'e':'f', 'f':'a'},
          4:{'a':'a', 'b':'b', 'c':'c', 'd':'e', 'e':'d', 'f':'f'},
          5:{'a':'f', 'b':'a', 'c':'b', 'd':'c', 'e':'e', 'f':'d'},
          6:{'a':'d', 'b':'f', 'c':'a', 'd':'b', 'e':'c', 'f':'e'}}

wheel1 = {1:{'a':'d', 'b':'a', 'c':'c', 'd':'b', 'e':'f', 'f':'e'},
          2:{'a':'e', 'b':'d', 'c':'a', 'd':'c', 'e':'b', 'f':'f'},
          3:{'a':'f', 'b':'e', 'c':'d', 'd':'a', 'e':'c', 'f':'b'},
          4:{'a':'b', 'b':'f', 'c':'e', 'd':'d', 'e':'a', 'f':'c'},
          5:{'a':'c', 'b':'b', 'c':'f', 'd':'e', 'e':'d', 'f':'a'},
          6:{'a':'a', 'b':'c', 'c':'b', 'd':'f', 'e':'e', 'f':'d'}}

wheel2 = {1:{'a':'d', 'b':'f', 'c':'e', 'd':'a', 'e':'c', 'f':'b'},
          2:{'a':'b', 'b':'d', 'c':'f', 'd':'e', 'e':'a', 'f':'c'},
          3:{'a':'c', 'b':'b', 'c':'d', 'd':'f', 'e':'e', 'f':'a'},
          4:{'a':'a', 'b':'c', 'c':'b', 'd':'d', 'e':'f', 'f':'e'},
          5:{'a':'e', 'b':'a', 'c':'c', 'd':'b', 'e':'d', 'f':'f'},
          6:{'a':'f', 'b':'e', 'c':'a', 'd':'c', 'e':'b', 'f':'d'}}


ori = 1
ori1 = 21
ori2 = 1
for i in plaintext:

    ori += 1
    if ori > 6:
        ori = 1
        ori1 += 1
    if ori1 > 6:
        ori1 = 1
        ori2 += 1
    if ori2 > 6:
        ori2 = 1
    print(ori, ori1, ori2)

    c = plugboard[i]
    c = wheel1[ori1][c]
    c = wheel0[ori][c]
    c = wheel2[ori2][c]
    c = reflector[c]
    c = list(wheel2[ori2].keys())[list(wheel2[ori2].values()).index(c)]
    c = list(wheel0[ori].keys())[list(wheel0[ori].values()).index(c)]
    c = list(wheel1[ori1].keys())[list(wheel1[ori1].values()).index(c)]
    c = list(plugboard.keys())[list(plugboard.values()).index(c)]

    ciphertext += c
    print(i, '->', c)
    time.sleep(1/len(plaintext))

print('ciphertext:', ciphertext)
