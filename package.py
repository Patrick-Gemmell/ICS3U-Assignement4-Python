
#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This program calculates the wight and size of a package

import constants

def main():
    # this function compares the weight and volume
   
   # Inputs
    weight_as_string = input("Input the weight: (kg) ")
    length_as_string = input("Input the length: (cm)")
    height_as_string = input("Input the height: (cm)")
    width_as_string = input("Input the width: (cm)")
    
    # Processes and Outputs
    try:
        integer_as_number = int(weight_as_string)
        integer_as_length = int(length_as_string)
        integer_as_height = int(height_as_string)
        integer_as_width = int(width_as_string)
        
        volume = integer_as_height*integer_as_length*integer_as_width
        
        print("")
        if (integer_as_number <= constants.WEIGHT and volume <= constants.SIZE):
            print("Your package can be processed ")
        else:
           if (integer_as_number > constants.WEIGHT and volume > constants.SIZE):
                print(" Your package cannot be processed because, the weight \
 needs to be under 27 and yours is {0} and the size needs to be under \
 10,000cm^3 and  yours is {1}cm^3".format(integer_as_number, volume))
           elif (integer_as_number > constants.WEIGHT):
               print("Your package cannot be processed as the maximum weight \
 is 27 kg, and yours is {0}".format(integer_as_number))
           elif (volume > constants.SIZE): 
               print("Your package cannot be processed as the maximum volume \
 is 10,000cm^3, but yours is {0}".format(volume)) 
    except Exception:
        print("This is not a number")
    finally:
        print("Thank you for using our services")
        
        
if __name__ == "__main__":
    main()