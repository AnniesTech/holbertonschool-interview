#!/usr/bin/python3
def canUnlockAll(boxes):
    newlist = [0]
    for i in newlist:
        for box in boxes[i]:
            if box < len(boxes) and box not in newlist:
                newlist.append(box)
    if len(newlist) == len(boxes):
        return True
    return False
