#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program will calculate the Area and Perimeter of a r=15mm circle

import math


def main():
    print ("If a circle has a radius of 15mm:")
    print ("")
    print ("Area is {}mm^2".format(math.pi*15**2))
    print ("Perimeter is {}mm".format(2*math.pi*15))

if __name__ == "__main__":
    main()