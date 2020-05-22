import random as r

def SaM(m, binEList, n):
    binEList.reverse()
    s = len(binEList)
    mList = [0 for i in range(s)]
    mList[0] = (m ** (int(binEList[s - 1]))) % n
    #print(mList[0])

    for i in range(1, s):
        mList[i] = ((mList[i-1] ** 2) * (m ** int(binEList[s - 1 - i]))) % n
        #print(mList[i-1], binEList[s - 1 - i])
        #print(mList[i])

    return mList[s-1]

p = 431
q = 509
n = p * q
e = 7
piN = (p-1) * (q-1)
d = 124823

pub = (e, n)
pri = d

print(pub, pri)

m = r.randint(1, n-1)    #랜덤한 평문
print(m)

strE = str(bin(e)).strip('0b')
listE = []
for i in strE:
    listE.append(i)

strD = str(bin(d)).strip('0b')
listD = []
for i in strD:
    listD.append(i)

#print(listE)
#암호화
c = SaM(m, listE, n)
print('The result of encryption is %s' %c)

#복호화
mPrime = SaM(c, listD, n)
print('The result of decryption is %s' %mPrime)

print('M: %s M\': %s' %(m, mPrime))

#커밋어케함??
