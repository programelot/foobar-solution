'''
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random IDs based on a Completely Foolproof Scheme. 

Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(0)
Output:
    23571

Input:
Solution.solution(3)
Output:
    71113

-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113
'''

def solution(n):
    prime = [2]
    length = 1
    v = 3
    while True:
        isPrime = True
        sqrtV = v ** 0.5
        for p in prime:
            if v % p == 0:
                isPrime = False
                break
            if p > sqrtV:
                break
        if isPrime:
            prime.append(v)
            length += len(str(v))
            if length >= n + 5:
                v = str(prime[-1])
                if length - (n+5) == 0:
                    ret = v
                else:
                    ret = v[:-(length - (n+5))]
                idx = -2
                while len(ret) < 5:
                    v = str(prime[idx])
                    ret = v + ret
                    idx -=1
                return ret[-5:]
        v += 2
        
