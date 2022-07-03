#create program that adds two number using recursion,majorly used in Scheme language\
#accept looping
def summing(number):  #create function and pass in paramter
    # start=0
    # start+=number
    # print(number)
    # # i=0
    if number==0:   #need edge case to validate 
        return 0
    else:
        return number+ summing(number-1)      #need a base case ,where you need to return sum of the numbers 
        # start+=number                       #uses return ,no printing 
        # print(start)
    

        # start.append(number)
        # print(number)
c=summing(7)                             #create a variable  that'll hold the function.

print(c)
