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
    else:
        return "Error"

    return itemc
