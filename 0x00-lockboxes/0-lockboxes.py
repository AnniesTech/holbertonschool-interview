#!/usr/bin/python3
""" Method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """ Function that determine if all the boxes can be opened. """
    newlist = [0]
    for i in newlist:
        for box in boxes[i]:
            if box < len(boxes) and box not in newlist:
                newlist.append(box)
    if len(newlist) == len(boxes):
        return True
    return False
