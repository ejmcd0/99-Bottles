BOTTLES = 100
NEW_BOTTLES = 99


while BOTTLES >= 1:
    if BOTTLES == 1:
        NEW_BOTTLES = 0
        print(f"{BOTTLES} bottle of beer on the wall, {BOTTLES} bottle of beer. Take one down, pass it around"
            f" {NEW_BOTTLES} bottles of beer on the wall.")
        BOTTLES = NEW_BOTTLES
    elif BOTTLES == 2 and NEW_BOTTLES == 1:
        print(f"{BOTTLES} bottles of beer on the wall, {BOTTLES} bottles of beer. Take one down, pass it around"
            f" {NEW_BOTTLES} bottle of beer on the wall.")
        NEW_BOTTLES = BOTTLES - 1
        BOTTLES = NEW_BOTTLES
    elif BOTTLES > 2 and NEW_BOTTLES > 1:
        print(f"{BOTTLES} bottles of beer on the wall, {BOTTLES} bottles of beer. Take one down, pass it around"
              f" {NEW_BOTTLES} bottles of beer on the wall.")
        BOTTLES = NEW_BOTTLES
        NEW_BOTTLES = BOTTLES - 1


