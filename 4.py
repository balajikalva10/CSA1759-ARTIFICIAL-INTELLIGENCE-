from itertools import permutations

letters = 'SENDMORY'
for x in permutations(range(10),len(letters)):
    mapping = dict(zip(letters,x))

    if mapping['S'] == 0 or mapping['M'] == 0:
        continue

    send = 1000*mapping['S'] + 100*mapping['E'] + 10*mapping['N'] + mapping['D']
    more = 1000*mapping['M'] + 100*mapping['O'] + 10*mapping['R'] + mapping['E']
    money = 10000*mapping['M'] + 1000*mapping['O'] + 100*mapping['N'] + 10*mapping['E'] + mapping['Y']

    if send + more == money:
        print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
        print(f"Mappings: {mapping}")
        break
    
