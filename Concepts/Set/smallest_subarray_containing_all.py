"""
Exercise 5 — Smallest Subarray Containing All Unique Elements

Given an array arr, find the length of the smallest contiguous subarray that contains all 
distinct elements present in arr.
Example: arr = [a, b, c, a, b, c, b, a] — the set of unique elements is {a,b,c}; 
the smallest window containing all is [a,b,c] length = 3.
Goal: use set plus two-pointer / sliding window technique for near O(n) time.

Hint: First compute required = len(set(arr)). Then use sliding window with a dictionary of counts 
(or another structure) to know when the window contains all required distinct elements.
"""