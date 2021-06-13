# Q38. You are given an integer array cost where cost[i] 
# is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
#   Examples:
#   Input: cost = [10,15,20]
#   Output: 15
#   Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
#   Input: cost = [1,100,1,1,1,100,1,1,100,1]
#   Output: 6
#   Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].


def pay(cost):
    if len(cost) == 1:
        return cost[0]
 
    m = cost[0]
    n = cost[1]

    for i in range(2, len(cost)):
        temp = n
        n = cost[i] + min(m, n)
        m = temp
    return min(m, n)

cost = [1,100,1,1,1,100,1,1,100,1]
print(pay(cost))