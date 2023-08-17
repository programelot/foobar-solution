'''
Escape Pods
===========

You've blown up the LAMBCHOP doomsday device and relieved the bunnies of their work duries -- and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time. 

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function solution(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

Then in each time step, the following might happen:
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final solution remains the same.)

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
Solution.solution({0, 1}, {4, 5}, {{0, 0, 4, 6, 0, 0}, {0, 0, 5, 2, 0, 0}, {0, 0, 0, 0, 4, 4}, {0, 0, 0, 0, 6, 6}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    16

Input:
Solution.solution({0}, {3}, {{0, 7, 0, 0}, {0, 0, 6, 0}, {0, 0, 0, 8}, {9, 0, 0, 0}})
Output:
    6

-- Python cases --
Input:
solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
Output:
    6

Input:
solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    16
'''

def findPath(src, dst, exclude, forward, backward):
    #return (p, v, t)
    #       path p that from s to t that doesn't go through exclude
    #       With capacity v
    #       and edge type t
    if src == dst:
        return ([dst], float('inf'), [])
    n = len(forward)
    for i in range(n):
        if forward[src][i] != 0 and (not i in exclude):
            p,v,t = findPath(i, dst, exclude + [src], forward, backward)
            if p != None:
                return ([src] + p, min(v, forward[src][i]), ['forward' ] + t)
        if backward[src][i] != 0 and (not i in exclude):
            p,v,t = findPath(i, dst, exclude + [src], forward, backward)
            if p != None:
                return ([src] + p, min(v, backward[src][i]), ['backward' ]+ t)
    return (None, 0, [])

def solution(entrances, exits, path):
    n = len(path)
    forward = [[0] + [(float('inf') if i in entrances else 0) for i in range(n)] + [0]] \
        + [([0] + [path[i][j] for j in range(n)] + [(float('inf') if i in exits else 0)]) for i in range(n)] \
        + [[0] * (n + 2)]
    backward = [[0 for x in range(n + 2)] for y in range(n + 2)]
    n += 2 #adjust number to argumented graph
    while True:
        p,v, t = findPath(0, n - 1, [], forward, backward)
        if p == None:# no path found
            break
        for i in range(len(p) - 1):
            if t[i] == 'forward':
                forward[p[i]][p[i + 1]] -= v
                backward[p[i + 1]][p[i]] += v
            else: #if t[i] == 'backward':
                backward[p[i]][p[i + 1]] -= v
                forward[p[i + 1]] [p[i]]+= v
    return sum(backward[n - 1])

'''
Submitting solution...
Oh no! You escaped Commander Lambda's exploding space station -- but so did the Commander, and Lambda is definitely not happy with you. Lambda is chasing you in a heavily-armed starfighter, while you and the bunny workers are stuck in these lumbering escape pods. It'll take all your wits and cleverness to escape such a hare-y situation, so you'd better hop to it!
Submission: SUCCESSFUL. Completed in: 43 mins, 18 secs.
'''


