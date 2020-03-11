#CTI-110-0902
#P3HW1 - Color Mixer
#Kenneth Walton
#9 March 2020
#
#Get the primary colors
color1 = input("Enter primary color 1: " )
color2 = input("Enter primary color 2: " )

if ( color1 == "red" and color2 == "blue" ) or \
   ( color1 == "blue" and color2 == "red" ):
    print("The secondary color is purple" )
elif ( color1 == "red" and color2 == "yellow" ) or \
     (color1 == "yellow" and color2 == "red" ):
    print("The secondary color is orange" )
elif (color1 == "blue" and color2 == "yellow" ) or \
     (color1 == "yellow" and color2 == "blue" ):
    print("The secondary color is green" )
else:
    print( "Error: one or both of your colors is not a primary color. Try again." )


    
