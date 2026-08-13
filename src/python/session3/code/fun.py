def main():
    print ("calc app")
    print ("--------------------------")
    print ("choose number of process:")
    print ("1- sum")
    print ("2- sub")
    print ("3- multiply")
    print ("4- divison")
    print ("--------------------------")
    process = int(input("enter number of process:"))
    num_1 = float(input("enter first number"))
    num_2 = float(input("enter second number"))

    if process == 1:
        print(f"sum of two numbers {sumnum(num_1,num_2)}")
    elif process == 2:
        print(f"sub of two numbers {subnum(num_1,num_2)}")
    elif process == 3:
        print(f"multiply of two numbers {multiplynum(num_1,num_2)}")
    elif process == 4:
        print(f"divison of two numbers {divisonnum(num_1,num_2)}")
    else:
        print("invalid process")


def sumnum(x: float,y:float):
    '''sum function
        args:
            Parm_1 = user must input the first sum
            type_parm1 = float
            Parm_2 = user must input the first sum
            type_parm2 = float
        return: returns sum of 2 numbers
        type_of_return = float
    '''
    return x+y

def subnum(x: float,y:float):
    '''sub function
        args:
            Parm_1 = user must input the first sum
            type_parm1 = float
            Parm_2 = user must input the first sum
            type_parm2 = float
        return: returns sub of 2 numbers
        type_of_return = float
    '''
    return x-y

def multiplynum(x: float,y:float):
    '''multiply function
        args:
            Parm_1 = user must input the first sum
            type_parm1 = float
            Parm_2 = user must input the first sum
            type_parm2 = float
        return: returns multiply of 2 numbers
        type_of_return = float
    '''
    return x*y

def divisonnum(x: float,y:float):
    '''divison function
        args:
            Parm_1 = user must input the first sum
            type_parm1 = float
            Parm_2 = user must input the first sum
            type_parm2 = float
        return: returns divison of 2 numbers
        type_of_return = float
    '''
    return x/y

