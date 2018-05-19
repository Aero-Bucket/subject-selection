subject=input("Input a number here: ")

try:
    print(int(subject))
except ValueError:
    print("Input is not a number")
    # execute the block when the input value is wrong
except:
    print("Unknown error occured")
    # execute the block when other errors occured
finally:
    print("end")
    # execute this block no matter errors occured or not
