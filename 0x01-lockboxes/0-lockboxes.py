#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    total_boxes = len(boxes)
    unlocked_boxes = {0}
    new_keys = {0}

    while new_keys:
        current_keys = new_keys
        new_keys = set()

        for key in current_keys:
            for box in boxes[key]:
                if 0 <= box < total_boxes and box not in unlocked_boxes:
                    unlocked_boxes.add(box)
                    new_keys.add(box)

    return len(unlocked_boxes) == total_boxes
