"""Shuffle
In JavaScript, the Array object has numerous useful methods. It does not, however, 
contain a method that will randomize the order of an arrays elements. Lets create shuffle(arr), 
to efficiently shuffle a given arrays values. Work in-place, naturally. Do you need to return anything from your function?"""

import random

def shuffle(arr):
    for i in range(len(arr)):
        rand_index = random.randint(0, len(arr)-1)
        temp = arr[i]
        arr[i] = arr[rand_index]
        arr[rand_index] = temp
    return arr

print(shuffle(['a','b','c','d','e']))
print(shuffle([1,2,3,4,5,6,7]))
print(shuffle(["woa", False, 3, 6, 2.5]))

"""Skyline Heights
Lovely Burbank has a breathtaking view of the Los Angeles skyline. 
Lets say you are given an array with heights of consecutive buildings, starting closest to you and extending away. 
Array [-1,7,3] would represent three buildings: first is actually out of view below street level, 
behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). 
You are situated at street level. Return array containing heights of buildings you can see, in order. 
Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift()"""

def skyline(input):
    buildingsWeSee = []
    tallestBuilding = 0
    for i in range(0, len(input), 1):
        if input[i] > 0 and input[i] > tallestBuilding:
            buildingsWeSee.append(input[i])
            tallestBuilding = input[i]
    return buildingsWeSee

print(skyline([-1,1,1,7,3]))
print(skyline([0,4]))
print(skyline([0,56,900,7,9,1000]))


"""Zip It
Create a standalone function that accepts two arrays and combines their values sequentially into a new array. 
Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100]."""

def zipIt(arr1, arr2):
    newArray = []
    longerArray = arr1 if len(arr1) > len(arr2) else arr2
    for i in range(len(longerArray)):
        if i <= (len(arr1))-1:
            newArray.append(arr1[i])
        if i <= (len(arr2))-1:
            newArray.append(arr2[i])
    return newArray



print(zipIt([4,15,100],[10,20,30,40]))
print(zipIt([5,9,25,78,90], [0,200,900,8,56,1]))

"""Credit Card Validation (Bonus)
The Luhn formula is sometimes used to validate credit card numbers. 
Create the function isCreditCardValid(digitArr) that accepts an array of digits on the card (13-19 depending on the card), 
and returns a boolean whether the card digits satisfy the Luhn formula, as follows:

Set aside the last digit; do not include it in these calculations (until step 5);
Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
If any results are larger than 9, subtract 9 from them;
Add all numbers (not just our odds) together;
Now add the last digit back in  the sum should be a multiple of 10.
For example, when given digit array [5,2,2,8,2], after step 1) it becomes [5,2,2,8], then after step 2) it is [5,4,2,16]. 
Post-3) we have [5,4,2,7], then following 4) it becomes 18. After step 5) our value is 20, so ultimately we return true. 
If the final digit were any non-multiple-of-10, we would instead return false."""

def isCreditCardValid(digitArr):
    lastDigit = digitArr[len(digitArr)-1]
    digitArr.pop()
    sum = 0
    for i in range(len(digitArr)-1, -1,-2):
        digitArr[i] = digitArr[i]*2
        if digitArr[i] > 9:
            digitArr[i] = digitArr[i]-9
    digitArr.append(lastDigit)
    for j in range(len(digitArr)):
        sum += digitArr[j]
    return sum % 10 == 0
    
    
print(isCreditCardValid([5,2,2,8,2]))
print(isCreditCardValid([5,2,2,8,3]))








