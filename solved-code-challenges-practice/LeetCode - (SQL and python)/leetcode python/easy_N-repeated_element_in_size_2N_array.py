#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

#Challenge, return the number in list that's repeated

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        #attempt 1
        #locate number that is repeated
        #list comprehension
        #check if the number is repeated (==)
        #create a new list and if a number is repeated, return it
        #return number that's repeated

        #attempt 2
        #counts
        #for number that shows up add 1 to it
        #whichever one is more than 1, return it
        #create some kind of enumerate

        #attempt 3
        #Planned on going on the enumerate route but found that this was much easier.
        #alternatively I also could've used collections.counter(A)
        numberslist = []
        for number in A:
            if number not in numberslist:
                numberslist.append(number)
            else:
                return number
