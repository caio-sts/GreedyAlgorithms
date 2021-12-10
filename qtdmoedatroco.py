import numpy as np

def qntdMoedas(troco, moedas):
    qntds = np.zeros(len(moedas))
    moedas.reverse()
    ind = 0

    troco = troco.split(" ")
    if troco[1] == "reais":
        troco = int(troco[0])*100
    else:
        troco = int(troco[0])

    while troco > 0:
        if troco >= moedas[ind]:
            troco -= moedas[ind]
            qntds[ind] += 1
            if troco < moedas[-1] and troco != 0:
                troco = moedas[-1]

        else:
            ind += 1

    msg = ""
    for i in range(len(moedas)):
        msg += "{} moedas de {} centavos\n".format(qntds[i], moedas[i])

    return msg


troco = "14 reais"

moedasdispon = [5, 10, 25, 50, 100]

print(qntdMoedas(troco, moedasdispon))
