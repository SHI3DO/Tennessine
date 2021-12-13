import ficsit.items.Components.Cable as cable
import ficsit.items.Components.Concrete as concrete
import ficsit.items.Components.CopperIngot as copperingot
import ficsit.items.Components.IronIngot as ironingot
import ficsit.items.Components.IronPlate as ironplate
import ficsit.items.Components.IronRod as ironrod
import ficsit.items.Components.ReinforcedIronPlate as reinforcedironplate
import ficsit.items.Components.Screw as screw
import ficsit.items.Components.Wire as wire
import ficsit.items.Components.CopperSheet as coppersheet
import ficsit.items.Components.ModularFrame as modularframe
import ficsit.items.Components.Rotor as rotor
import ficsit.items.Components.SmartPlating as smartplating
import ficsit.items.Components.SteelBeam as steelbeam
import ficsit.items.Components.SteelIngot as steelingot

import ficsit.buildings.Manufaturers.Constructor as constructor
import ficsit.buildings.Smelters.Smelter as smelter
import ficsit.buildings.Manufaturers.Assembler as assembler
import ficsit.buildings.Smelters.Foundry as foundry

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
    elif itemc == 10:
        search = coppersheet.prod(amount)
    elif itemc == 11:
        search = modularframe.prod(amount)
    elif itemc == 12:
        search = rotor.prod(amount)
    elif itemc == 13:
        search = smartplating.prod(amount)
    elif itemc == 14:
        search = steelbeam.prod(amount)
    elif itemc == 15:
        search = steelingot.prod(amount)

    # print(f"{search[0]} | {search[2]} + {search[1]} | {search[3]} -> {nmb.uncalc(itemc)}")
    building = search[1]
    building = nmb.calc(building)

    elec = 0
    if building == 700:
        elec = constructor.prod(search[3][0])
    elif building == 701:
        elec = smelter.prod(search[3][0])
    elif building == 702:
        elec = assembler.prod(search[3][0])
    elif building == 703:
        elec = foundry.prod(search[3][0])

    search.append(elec)
    lmb.log(search)
    return search
