


#This program displays the following picture using nested loops
##
# #
#  #
#   #
#    #
#     #
#April 8th 2020
#CTI-110 P4HW3-Nested Loops
#Kenneth Walton
#

for row in range (6):
    print("#", end="", sep="" )
    for col in range(row):
        print(" ", end="", sep="")
    print("#", sep="")

#Pseudocode
#for row in range(6)
    #for col in range(6)
    #print: #
