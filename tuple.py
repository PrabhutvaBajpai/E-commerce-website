# alist = [11,22,44] 
# atuple = tuple(alist) 
# print(atuple) 

# astr = "rgij" ; 
# atuple = tuple(astr) 
# print(atuple) 

# a = [1,'e', 'e' , 2 , 1] ; 
# b = set(a) 
# c = list(b)  
# print(b) 
# print(c)

# emptyset = set() ; # To create an empty set .

# list = [3,2,4] 
# s ={1 ,2, 3, 1, 3, 2 , 5} ; # set
# s.update(list)  
# print(s) 

# # Add strings into the existing set . 
# s.add("cat") 
# s.add("cat") 
# print(s) 

# # To discard preexisting element in the set 
# s.discard("cat") ; 
# print(s) 

# s.discard("bat") #There will be no error

# s.remove(1) 
# # s.remove(7) There will be error because 7 is not present . 
# print(s) ; 

# Operations in set 
# set1 = {1,4,2,5,6} ; 
# set2 = {3,2,1,5,3,1} ; 
# print(set2-set1) 
# print(set1^set2) 
# print((set1-set2)|(set2-set1)) 
# print(set1 | set2)
# print(set1 & set2) 

# is subset 

# set1 = {1,2,4,5,6,} ; 
# set2 = {1,2} ; 

# if (set2.issubset(set1)) :
#      print("Yes") 

# if(set1.issuperset(set2)) :
#      print("superset") 

# print(set1.symmetric_difference(set2)) ; 
# print(set2.symmetric_difference(set1)) ; 

#frozenset - It is immutable set . 

# list1 = [1,2,3,2,1,4,3] ; 
# f = frozenset(list1) ; 
# print(f) ; 

# set is unordered 
# set1 = {'1' , '2' , '3' , '4'}
# print(set1) 

# list1 = [{"name":"amit" , "roll" : 123} , {"name":"sonu" , "roll" : 345} , {"name":"shamit" , "roll" : 999}] 

# def add(n , r) : 
#     dict = {"name":n , "roll" : r} 
#     list1.append(dict) 

# def search(r) : 
#     for i in range(0,len(list1)) :
#         if(list1[i]["roll"] == r) :
#             print("Element found") 
#             return 
        
#     print("Element not found") 

# def edit (r,rol,n) : 
#     for i in range(0,len(list1)) :
#         if(list1[i]["roll"] == r) :
#             list1[i]['name'] = n 
#             list1[i]['roll'] = rol 
#             print("Edited Successfully") 
#             return 
        
#     print("Element not found") 

# def delete(r) :
#     for i in range(0,len(list1)) :
#         if(list1[i]["roll"] == r) :
#             list1.pop(i) 
#             print("Deleted Successfully") 
#             return 
        
#     print("Element not found") 
# res = 1 
# while(res != 0) : 
#     res = int(input("Which operation do you want to perform : Add = 1 , Search = 2 , edit = 3 , delete = 4 , exit = 0 : ")) 
#     if(res == 1) : 
#         n = input("Enter name : ") 
#         r = int(input("Enter roll : ")) 
#         add(n , r) 

#     if(res == 2) : 
#         r = int(input("Enter roll : ")) 
#         search(r) 

#     if(res == 3) : 
#         r = int(input("Enter roll : ")) 
#         rol = int(input("Enter new roll : ")) 
#         n = input("Enter new name : ") 
#         edit(r,rol,n) 
    
#     if(res == 4) : 
#         r = int(input("Enter roll : "))
#         delete(r) 

# print(list1) 


# dict = {} ; 
# s = "aabcabbhngjdhgmakhg" 

# for i in s : 
#     dict[i] += 1 

# for i in dict : 
#     str += i ; 

# print(str) 

