#code for linear_search complexity O(n)
def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
#added a few lines
#added few other lines
list1 = [1 ,3, 5, 4, 7, 9] 
//initialising an array
=======
#creating the input data for verifing the code
list1 = [1 ,3, 5, 4, 7, 9]  

key = 7  
//initialising an key
  
n = len(list1)  
res = linear_Search(list1, n, key)  
#checking the base case
if(res == -1):  
    print("Element not found")  
    //for cases in which no ans is posible
else:  
    print("Element found at index: ", res)  
