#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      achoubey
#
# Created:     18/09/2017
# Copyright:   (c) achoubey 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def main():
    nums1 = [x for x in range(10)]
##    print(nums1)
    random.shuffle(nums1)
    nums2 = [y for y in range(10)]
##    print(nums2)
    random.shuffle(nums2)

    print nums1
    print nums2
    print nums1[0]

    for i in range(0, len(nums1)):
        print nums1[i]+9, "\t","-","\t", nums2[i]+0
##    print "\n"
##    for i in nums2:
##        print i,
##    print random.shuffle(nums2)

if __name__ == '__main__':
    main()


