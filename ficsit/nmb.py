def calc(item):
    if item == "Cable":
        itemc = 1
    elif item == "Concrete":
        itemc = 2
    elif item == "CopperIngot":
        itemc = 3
    elif item == "IronIngot":
        itemc = 4
    elif item == "IronPlate":
        itemc = 5
    elif item == "IronRod":
        itemc = 6
    elif item == "ReinforcedIronPlate":
        itemc = 7
    elif item == "Screw":
        itemc = 8
    elif item == "Wire":
        itemc = 9
    elif item == "Constructor":
        itemc = 700
    elif item == "Smelter":
        itemc = 701
    elif item == "Assembler":
        itemc = 702
    else:
        return "Error"

    return itemc


def uncalc(itemc):
    if itemc == 1:
        item = "Cable"
    elif itemc == 2:
        item = "Concrete"
    elif itemc == 3:
        item = "CopperIngot"
    elif itemc == 4:
        item = "IronIngot"
    elif itemc == 5:
        item = "IronPlate"
    elif itemc == 6:
        item = "IronRod"
    elif itemc == 7:
        item = "ReinforcedIronPlate"
    elif itemc == 8:
        item = "Screw"
    elif itemc == 9:
        item = "Wire"
    elif itemc == 700:
        item = "Constructor"
    else:
        return "Error"

    return item
