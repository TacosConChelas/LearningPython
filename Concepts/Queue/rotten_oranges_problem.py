"""
    Exercise 4 — Rotten Oranges Problem (BFS Traversal)
Description:
You have a grid where:
    0 = empty cell
    1 = fresh orange
    2 = rotten orange
Each minute, a rotten orange turns all adjacent (up/down/left/right) fresh oranges rotten.
Return the minimum time for all oranges to rot — or -1 if impossible.
Example:
Input:
    [[2,1,1],
    [1,1,0],
    [0,1,1]]
Output: 4
Hint:        Use a queue for BFS — enqueue all initial rotten oranges, and spread rot level by level.
"""