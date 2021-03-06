#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021
# this calculates the area and perimiter of a circle witht a radius of 15


import math


def main():
    # this function calculates area and perimiter

    print(
        "This program calculates the area and perimiter of a circle with the radius 15mm:"
    )
    print("")
    print("Area is {} mm².".format(math.pi * 15 ** 2))
    print("perimiter is {} mm.".format(math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
