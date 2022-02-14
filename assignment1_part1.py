
 Week 1 Assignment - Part 1

#This function returns the number of elements in the numbers list that are divisible by "divide".

#creating a function called listDivide that takes in 2 parameters: numbers & divide (where divide is set to 2)
def listDivide(numbers=[], divide=2):
    divisibilityCount=0
    for i in numbers:
        remainder = i % divide
        if remainder == 0:
            divisibilityCount=divisibilityCount+1
    return divisibilityCount

#creating a custom exception class called "ListDivideException" to be raised when errors occur in the program
class ListDivideException(Exception):
    pass

#Creating a another function called "testListDivide"  to performs various tests cases on "listDivide" function
#the test cases are provided

def testListDivide():
    test1 = listDivide([1, 2, 3, 4, 5])
    if test1 != 2:
        raise ListDivideException("Test 1 Error")
    test2 = listDivide([2,4,6,8,10])
    if test2 != 5:
        raise ListDivideException("Test 2 Error")
    test3 = listDivide([30, 54, 63, 98, 100], divide=10)
    if test3 !=2:
        raise ListDivideException("Test 3 Error")
    test4 = listDivide([])
    if test4 != 0:
        raise ListDivideException ("Test 4 Error")
    test5 = listDivide([1,2,3,4,5], 1)
    if test5 != 5:
        raise ListDivideException ("Test 5 Error")

testListDivide()