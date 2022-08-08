import random

category = [78, 79, 140, 141, 202, 203, 260, 261, 310, 311, 350, 351]
display_page = [30, 31, 38, 39, 50, 51, 56, 57, 68, 69, 
    90, 91, 108, 109, 118, 119, 122, 123, 154, 155, 
    176, 177, 182, 183, 188, 189, 214, 215, 226, 227, 
    238, 239, 272, 273, 278, 279, 288, 289, 314, 315]
virgin = [13, 33, 43, 53, 59, 93, 125, 187, 208, 217, 229, 291, 313, 317, 335, 352, 353, 355, 356]

def main():
    roll = random.randint(12, 349)
    while roll in virgin or roll in category:
        roll = random.randint(12, 349)
    if roll in display_page and (roll%2==0):
        roll = roll + 2
    elif roll in display_page and (roll%2==1):
        roll = roll + 1
    print(roll)


main()