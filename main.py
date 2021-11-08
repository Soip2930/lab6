def rot(num):
    num = str(num)
    num = num.replace('6', '9', 1)
    return int(num)

(listenToBigBabyTape) = input()
print(rot(listenToBigBabyTape))