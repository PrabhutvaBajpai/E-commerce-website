# def binary(n) : 
#     if(n==1) : 
#         print(n%2,end=' ')
#         return 
#     binary(n//2) 
#     print(n%2,end=' ')

# binary(int(input("Enter decimal number : "))) 


# def sum(a,b) : 
#     if(b==0) :
#         print(a)
#         return 

#     sum(a+1,b-1) 

# sum(int(input("Enter a : ")),int(input("Enter b : ")))


# def fib(n) :
#     if(n <= 1) :  
#         print(n)
#         return n

#     a = fib(n-2) + fib(n-1)
#     return a 

# fib(int(input("Enter term of fibonacii : ")))


# Higher order function 

# To add numbers 
def add_two_nums(x,y) : 
    return x+y 

def add_three_nums(x,y,z) : 
    return x+y+z 

def get_appropriate_function(num_len) : #normal function which returns functions depend 
    if num_len == 3 : 
        return add_three_nums 
    
    else : 
        return add_two_nums 

# if __name__ == "__main__" :
args = [1,2,3] 
num_len = len(args) 
res_function = get_appropriate_function(num_len) 
print(res_function) # address of the function
print(res_function(*args)) 
args = [1,2]
num_len = len(args)
res_function = get_appropriate_function(num_len)
print(res_function) # address of the function 
print(res_function(*args))


# To sum

# def summation(nums) : # normal function 
#     return sum(nums)

# def main(f,args) : #function as an argument 
#     result = f(args) 
#     print(result)
#     print("in side function " + str(f))

# if __name__ == "__main__" : 
#     main(summation , [1,2,3,4])

# print(summation)