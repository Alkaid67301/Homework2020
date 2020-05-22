import random as r

registerx = []
registery = []
registerz = []

def xRegisterLFSR(register):
    output = register[-1]
    newbit = register[13] ^ register[16] ^ register[17] ^ register[18]
    for i in range(18, 0, -1):
        register[i] = register[i-1]
    register[0] = newbit
    #print(newbit, output)
    return output

def yRegisterLFSR(register):
    output = register[-1]
    newbit = register[20] ^ register[21]
    for i in range(21, 0, -1):
        register[i] = register[i-1]
    register[0] = newbit
    #print(newbit, output)
    return output

def zRegisterLFSR(register):
    output = register[-1]
    newbit = register[7] ^ register[20] ^ register[21] ^ register[22]
    for i in range(22, 0, -1):
        register[i] = register[i-1]
    register[0] = newbit
    #print(newbit, output)
    return output

def selectOutput(xregi, yregi, zregi):
    x = xregi[8]
    y = yregi[10]
    z = zregi[10]
    if x == y:
        return 'z'
    else:
        if x == z:
            return 'y'
        else:
            return 'x'

for i in range (19):
    a = r.randint(0, 1)
    registerx.append(a)

for i in range (22):
    a = r.randint(0, 1)
    registery.append(a)

for i in range (23):
    a = r.randint(0, 1)
    registerz.append(a)

print('Register X: %s \nRegister Y: %s \nRegister Z:%s' %(registerx, registery, registerz))

resultBit = ''

for i in range(3):
    xBit = xRegisterLFSR(registerx)
    yBit = yRegisterLFSR(registery)
    zBit = zRegisterLFSR(registerz)

    print('Output Bit of X: %s Y: %s Z: %s' %(xBit, yBit, zBit))
    print('Register X: %s \nRegister Y: %s \nRegister Z:%s' %(registerx, registery, registerz))

    exceptLine = selectOutput(registerx, registery, registerz)

    print('exceptLine: %s' %exceptLine)

    appendBit = 0
    if exceptLine == 'x':
        appendBit = yBit ^ zBit
    elif exceptLine == 'y':
        appendBit = xBit ^ zBit
    else:
        appendBit = xBit ^ yBit

    resultBit += str(appendBit)

print(resultBit)
