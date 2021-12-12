from ficsit import smb
from ficsit import nmb


def amb(itemc, amount):
    search = smb.calc(itemc, amount)
    research(search)


def research(search):
    if search[len(search)-1] == 1:
        for i in range(0, len(search[0])):
            itemc = nmb.calc(search[0][i])
            amb(itemc, search[2][i])
    else:
        print("------------------------")


def tenessine(item, amount):
    itemc = nmb.calc(item)
    search = smb.calc(itemc, amount)
    research(search)


tenessine("ReinforcedIronPlate", 100)
