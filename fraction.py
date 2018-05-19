input_fraction=input("Input fraction here> ")
split_fraction=input_fraction.split("/")

if len(split_fraction) != 2:
        print("Invalid fraction")
else:
    for i in range(2):
        split_fraction[i]=int(split_fraction[i])


def strip_dot_zero(input_num):
    # workaround for the stupid division
    if str(input_num).endswith(".0") == True:
        return int(input_num)
    else:
        return input_num


def possible_reduce(input_list):
    
    # skipped 1, because a number will remain the same when divided by 1
    # using either the numerator or the denominator for the upper limit will work
    can_reduce="Impossible"

    for i in range(2, input_list[0] + 1):
        
        numerator=input_list[0] / i
        denominator=input_list[1] / i

        numerator=strip_dot_zero(numerator)
        denominator=strip_dot_zero(denominator)

        if (type(numerator) == int) and (type(denominator) == int):
            can_reduce="Possible"
            break
        else:
            continue
    
    return can_reduce


def return_reduce(input_list):

    result_numerator=None
    result_denominator=None
    restart=True

    while restart == True and possible_reduce(input_list) == "Possible":

        for i in range(2, input_list[0] + 1):
            
            if result_denominator == None:
                numerator=strip_dot_zero(input_list[0])
                denominator=strip_dot_zero(input_list[1])
            else:
                numerator=strip_dot_zero(result_numerator / i)
                denominator=strip_dot_zero(result_denominator / i)
            
            if (type(numerator) == int) and (type(denominator) == int):
                result_numerator=numerator
                result_denominator=denominator
                break # go to the start of the loop, reducing the fraction again
            else:
                continue
       
        if possible_reduce([result_denominator,result_numerator]) == "Impossible":
            restart=False
     
    if result_denominator == 1:
        return f"{result_numerator}"
    elif result_denominator == None:
        pass
    else:
        return f"{result_numerator}/{result_denominator}"


print(possible_reduce(split_fraction))
print(return_reduce(split_fraction))
