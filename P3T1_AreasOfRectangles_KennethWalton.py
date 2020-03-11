#Kenneth Walton
#CTI 110-0902
#This program gets the area of two rectangles and determines which has
#the greater area

# Get the length and width of the first rectangle
length1 = int(input('Enter the length of rectangleOne: '))
width1 = int(input('Enter the width of rectangleOne: '))

#Get the length and width of the second rectangle
length2 = int(input('Enter the length of rectangleTwo: '))
width2 = int(input('Enter the width of rectangleTwo: '))

#calculate the area of the rectangles
area1 = length1 * width1
area2 = length2 * width2

#Determine which rectangle has greater area
if area1 > area2:
    print ('The first rectangle has a greater area')
else:
    if area2 > area1:
        print ('The second rectangle has a greater area')
    else:
        print ('The rectangles have the same area')
