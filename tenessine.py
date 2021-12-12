from ficsit import smb
from ficsit import nmb


def amb(itemc, amount):
    search = smb.calc(itemc, amount)
    research(search)


def research(search):
    if search[3] == 1:
        itemc = nmb.calc(search[0])
        amb(itemc, search[2])
    else:
        print("done")


def tenessine(item, amount):
    itemc = nmb.calc(item)
    search = smb.calc(itemc, amount)
    research(search)


tenessine("Screw", 100)
