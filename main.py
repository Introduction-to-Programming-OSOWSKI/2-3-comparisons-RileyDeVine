#WRITE YOUR CODE IN THIS FILE

#define greater than function
def greaterThan(x,y):  
    if x>y:
     return True

    else: 
        return False

#define less than function
def lessThan(x,y): 
    if x<y:
     return True

    else: 
        return False

#define equal to function
def equalTo(x,y):  
    if x == y:
     return True

    else: 
        return False

#define greater than or equal to function
def greaterOrEqual(x,y):  
    if x >= y:
     return True

    else: 
        return False

#define less than or equal to function
def lessOrEqual(x,y):  
    if x <= y:
        return True

    else: 
        return False


#run functions

print(greaterOrEqual(10, 5))

print(lessThan(5, 10))

print(equalTo(5, 5))

print(greaterOrEqual(6, 5))

print(lessOrEqual(4, 5))