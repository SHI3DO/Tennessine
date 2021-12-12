from ficsit import smb
from ficsit import nmb
from ficsit import lmb


def amb(itemc, amount):
    search = smb.calc(itemc, amount)
    research(search)


def research(search):
    if search[len(search) - 1] == 1:
        for i in range(0, len(search[0])):
            itemc = nmb.calc(search[0][i])
            amb(itemc, search[2][i])
    else:
        pass


def tenessine(item, amount):
    lmb.reset()
    itemc = nmb.calc(item)
    search = smb.calc(itemc, amount)
    research(search)
    logk = lmb.get()
    for i in range(0, len(logk)):
        # print(logk[i])
        return 0


tenessine("ReinforcedIronPlate", 400)
