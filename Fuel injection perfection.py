'''
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

-- Java cases --
Input:
Solution.solution('4')
Output:
    2

Input:
Solution.solution('15')
Output:
    5
'''

def solution(n):
    n = int(n)
    b = list(bin(n)[2:]) #binary representation
    # divide by 2 => remove one digit by cost 1
    # add 1 => check flip cost(may can get advantage)
    # subtract 1 => remove one digit by cost 2
    count = 0
    while b != ['1']:
        if b[-1] == '0':
            b = b[:-1]
            count += 1
        else:
            if len(b) >= 3 and b[-2] == '1':
                for i in range(len(b)):
                    ti = len(b) - 1 - i
                    if b[ti] == '0':
                        b[ti] = '1'
                        break
                    else:
                        b[ti] = '0'
                        if ti == 0:
                            b.insert(0, '1')
                count += 1
            else:
                b = b[:-1]
                count += 2
    return count

def answer(n):
    n = int(n)
    
    counter = 0
    while n > 3:
        if n & 1:
            if n & 2:
                n = (n + 1) >> 2
                counter += 3
            else:
                n = (n - 1) >> 1
                counter += 2
        else:
            n = n >> 1
            counter += 1
    
    if n == 3:
        n = n - 1
        counter += 1

    if n == 2:
        n = n - 1
        counter += 1

    return counter
  
'''
Submitting solution...
Submission: SUCCESSFUL. Completed in: 1 hr, 41 mins, 0 secs.
'''
