import pandas as pd
import textwrap


key1 = "crypto graphics"
key2 = "network security"

message = "Be at the third pillar from the left outside the lyceum theater tonight at seven If you are distrustful bring two friends"

def encrypt(k,message,enc=True):
    pro = {}
    k = k.replace(" ","")
    for letter in k:
        if len(list(pro.keys())) < 10:
            if letter not in list(pro.keys()):
                pro[letter] = []

    message = message.replace(" ","").lower()

    counter = 0
    max_size = 0
    for letter in message:
        key = list(pro.keys())[counter]
        pro[key].append(letter)

        counter+=1
        if counter == len(list(pro.keys())):
            counter = 0

        if len(pro[key]) > max_size:
            max_size = len(pro[key])


    for key,value in pro.items():
        if len(value) < max_size:
            pro[key].append("X")


    df = pd.DataFrame.from_dict(pro)
    print(df)
    if enc:
        pro = {k:pro[k] for k in sorted(pro)}
    for key,value in pro.items():
        pro[key] = "".join(pro[key])


    word = ''.join(map(str, pro.values()))
    print(word)
    return word

def decrypt(key,message):
    k = key.replace(" ","")
    column_size = len(message)/10
    pro = {}
    message = message[::-1]
    for letter in k:
        if len(list(pro.keys())) < 10:
            if letter not in list(pro.keys()):
                pro[letter] = []
    
    counter = 0
    word_size = 0
    sorted_keys = list(sorted(pro.keys(),reverse=True))
    for letter in message:
        key = sorted_keys[counter]
        pro[key].insert(0,letter)
        word_size += 1

        if word_size == column_size:
            counter+=1
            word_size = 0

    df = pd.DataFrame.from_dict(pro)
    print(df)

    values = list(zip(*pro.values()))
    for i,item in enumerate(values):
        values[i] = ''.join(map(str, item))
    word = ''.join(map(str, values))
    print(word)
    return word

print("First Round of encrypt")
m = encrypt(key1,message)
print()

print("Second Round of encrypt")
m2 = encrypt(key2,m)

print("First Round of decryption")
m3 = decrypt(key2,m2)
print()

print("Second Round of decryption")
m4 = decrypt(key1,m3)
print()



