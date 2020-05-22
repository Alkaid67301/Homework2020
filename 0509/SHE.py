import random

p = 509
q = 431
n = p * q

#C = ap + 2r + m (r<10) mod n

#m = 0 or 1 //

def Encrypt(m):
    r = random.randint(1, 9)
    a = random.randint(1, 9)

    c = ((a * p) + (2 * r) + m) % n

    return c

def Decrypt(c):
    mPrime = (c % p) % 2

    return mPrime

m1 = 1
m2 = 1
m3 = 1

c1 = Encrypt(m1)
c2 = Encrypt(m2)
c3 = Encrypt(m3)

print('m1 = %s, m2 = %s, m3 = %s,  m1 * m2 * m3 = %s' %(m1, m2, m3, m1 * m2 * m3))
print('Encryption result is m1\' = %s, m2\' = %s, m3\' = %s, m1\' * m2\' * m3\' = %s' %(c1, c2, c3, c1 * c2 * c3))
print('Decryption result is m1\' = %s, m2\' = %s, m3\' = %s, m1\' * m2\' * m3\' = %s' %(Decrypt(c1), Decrypt(c2), Decrypt(c3), Decrypt(c1 * c2 * c3)))
