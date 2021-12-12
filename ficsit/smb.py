import ficsit.items.Components.Cable as cable
import ficsit.items.Components.Concrete as concrete
import ficsit.items.Components.CopperIngot as copperingot
import ficsit.items.Components.IronIngot as ironingot
import ficsit.items.Components.IronPlate as ironplate
import ficsit.items.Components.IronRod as ironrod
import ficsit.items.Components.ReinforcedIronPlate as reinforcedironplate
import ficsit.items.Components.Screw as screw
import ficsit.items.Components.Wire as wire

from ficsit import nmb
from ficsit import lmb


def calc(itemc, amount):
    search = 0
    if itemc == 1:
        search = cable.prod(amount)
    elif itemc == 2:
        search = concrete.prod(amount)
    elif itemc == 3:
        search = copperingot.prod(amount)
    elif itemc == 4:
        search = ironingot.prod(amount)
    elif itemc == 5:
        search = ironplate.prod(amount)
    elif itemc == 6:
        search = ironrod.prod(amount)
    elif itemc == 7:
        search = reinforcedironplate.prod(amount)
    elif itemc == 8:
        search = screw.prod(amount)
    elif itemc == 9:
        search = wire.prod(amount)

    print(f"{search[0]} | {search[2]} + {search[1]} | {search[3]} -> {nmb.uncalc(itemc)}")
    lmb.log(search)
    return search
