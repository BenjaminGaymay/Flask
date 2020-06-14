from mouse import *
from secret import *

from time import sleep

SIDES_COORD = {'gauche': [100, 540],
               'droite': [1820, 540],
               'haut': [960, 30],
               'bas': [960, 920]}


def changeDMap(secret, side_list):

    if secret != getSecret("Dofus"):
        return

    for side in side_list.split():
        if side in SIDES_COORD.keys():
            x = SIDES_COORD[side][0]
            y = SIDES_COORD[side][1]
            mouseClick(x, y)
            sleep(5)
