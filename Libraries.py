# math module 
# import math

# print(math.pow(2,3)) 

# print(math.factorial(5)) 

# print(math.sqrt(25)) 

# print(math.ceil(3.9876)) 

# print(math.floor(3.7679))

# print(round(5.1))

# import random

# print(random.randint(0,5)) 

# print(random.random())

# print(int(random.random()*100)) 

# print(random.choice(['red' , 'black' , 'green'])) 

# l = [1,2,3,4,5,6] 

# random.shuffle(l) 

# print(l)


# variable length arguement function 

# def fun(*a) :
#     print(type(a)) 
#     if(len(a) == 0) : 
#         print("Zero") 

#     elif len(a) == 1 : 
#         print("one")

#     elif len(a) == 2 : 
#         print("Two") 
    
#     else :
#         print("i am else")

# fun()
# fun(18)
# fun(1,2,3)
# fun(2,1,4) 

#keyword variable length arguements 

# def fun(**a) : 
#     print(a)

# fun(name = "amit")
# fun(name = "tony" , age = "40")
# fun(name = "Prabhu" , age = "39" , networth = "$ 800M")

# def function(a) :
#     print(math.factorial(a)) 

# def function(beg,end) : 
    # i = 0
    # a = 0 
    # b = 1 
    # while(a<end) :
    #     if(i >= beg) :
    #         print(a) 
    #     c = a+b 
    #     a = b
    #     b = c
    #     i = i+1 

    # print(a)  
import math

def function(*arrg) : 
    if(len(arrg) == 1) : 
        print(math.factorial(arrg[0]))

    elif(len(arrg) == 2) : 
        i = 1
        a = 0 
        b = 1 
        while(i<arrg[1]) :
            if(i >= arrg[0]) :
                print(a) 
            c = a+b 
            a = b
            b = c
            i = i+1 

        print(a)

    else :
        if(arrg[2] != "prime") : 
            print("Third arguement is not correct") 
            return 
        for i in range(arrg[0] , arrg[1]+1) : 
            flag = 0
            for j in range(2,int(math.sqrt(i))+1) : 
                if(i%j == 0) : 
                    flag = 1 
                    break 
            if(flag==0) :
                print(i) 

            


function(5) 
function(1,10) 
function(1,7,"prim")
        