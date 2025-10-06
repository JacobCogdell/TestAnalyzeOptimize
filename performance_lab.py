# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    most_common = max(freq, key=freq.get)
    return most_common

#Testing
print("Testing Problem 1:")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent([4, 4, 1, 2, 2, 3, 3, 4]))
print(most_frequent([5, 5, 5, 6, 6, 7, 7, 7]))  
print(most_frequent([1, 2, 3, 4, 5]))  
print(most_frequent([1, 1, 1, 1, 1]))  
print(most_frequent([]))


"""
Time and Space Analysis for problem 1:
- Best-case: The empty input is O(1)
- Worst-case: The worst case is driven by the for loop and the max command.  In both cases, there is a single execution for each item in the list so 
              the worst case is O(n)
- Average-case: Following the logic of the worst case explanation, the average case is also O(n)
- Space complexity: The worst case arises when all input numbers are unique.  In this case, space complexity will be O(n)
- Why this approach? This coding approach utilizes standard Python functions which are optimized.  This allows the code 
                     to be efficient while also allowing it to be well structured and easy to read
- Could it be optimized? I think the biggest opportunity would be in the implementation of the max function.  If there is a way for that to 
                         be executed faster.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    allnums = set()
    uniquenums = []
    for num in nums:
        if num not in allnums:
            allnums.add(num)
            uniquenums.append(num)
    return uniquenums

#Testing
print("Testing Problem 2:")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([1, 1, 1, 1, 1]))
print(remove_duplicates([5, 4, 3, 2, 1]))
print(remove_duplicates([]))
"""
Time and Space Analysis for problem 2:
- Best-case: The best case is the empty input set with a time of O(1)
- Worst-case:  The worst case happens when the input is the same number repeatedly.  This is still O(n)
- Average-case:  The average case and the worst case follow similar reasoning.  The code is going to execute the primary loop 
                 one time for every input.  Within the loop the executions are all O(1) - this is true of the if statement because 
                 the allnums data structure checks existing using a lookup and does not touch each element every time it is called.  So 
                 the average case is also O(n)
- Space complexity: The worst case for space complexity is when the inputs contain no duplicates.  This is O(n)
- Why this approach?  By making allnums a set you can take advantage of the built in function of python sets.  These include
                      built-in uniqueness and fast lookups
- Could it be optimized?  Maybe by someone with more experience but I think it's pretty optimized
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    allnums = set()

    for num in nums:
        match_num = target - num
        if match_num in allnums:
            pairs.append((match_num, num))
        allnums.add(num)
    return list(set(pairs))
    
#Testing
print("Testing Problem 3:")
print(find_pairs([1, 2, 3, 4], 5))
print(find_pairs([0, -1, 2, -3, 1], -2))
print(find_pairs([5, 5, 5, 5], 10))
print(find_pairs([1, 2, 3, 4, 5], 10))
print(find_pairs([], 5))
"""
Time and Space Analysis for problem 3:
- Best-case: The best case is the empty input set where time complexity is O(1)
- Worst-case: The worst case happens when there are no duplicates pairs.  In this case, the code executes in O(n) for the main loop and 
              O(n) for the enumeration of the pairs array when creating the set.
- Average-case: Following the logic in the worst-case scenario, the average case is O(n) 
- Space complexity: The two primary elements that take up space are allnums which will be O(n) and pairs which will be O(n/2).  Overall 
                    this gives us a space complexity of O(n)
- Why this approach? The individual calculations are core python routines that are optimized.  The loops are easy to follow and perform well
- Could it be optimized? Assuming that the list contains no duplicates, if the input is sorted, then you could stop the main loop early 
                         as soon as the number exceeds the target.  The return list(set(pairs)) works to get unique values but seems a good candidate for optimization.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    print(f"Adding {n} items")
    capacity = 1
    size = 0
    items = []

    for item in range(n):
        if size == capacity:
            new_capacity = capacity * 2            
            print(f"Increasing Capacity from {capacity} to {new_capacity}")
            capacity = new_capacity
            print(f"Copying {size} items")
        items.append(item)
        size += 1
    print(f"Final Array has capacity: {capacity}")
    print(f"Final Array has items: {items}")

#Testing
print("Testing Problem 4")
add_n_items(1)
add_n_items(5)
add_n_items(6)
add_n_items(18)
add_n_items(0)

"""
Time and Space Analysis for problem 4:
- When do resizes happen?  Resizes happen when it needs additional space to store the input values.
- What is the worst-case for a single append? The worst case for a single append is the case where the value is capacity/2 + 1.  
                                              In this case, you will increase the capacity and have to copy n values into the new array
- What is the amortized time per append overall? The amortized time per append is only O(1)
- Space complexity: The overall complexity is O(n)
- Why does doubling reduce the cost overall? The more costly part of the algorithm is the copy of the existing elements into the new 
                                             array.  By only increasing the capacity when it goes over double, you reduce the number
                                             of times that this most expensive step occurs.  
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    sum_list = []
    running_sum = 0

    for num in nums:
        running_sum += num
        sum_list.append(running_sum)

    return sum_list

#Testing
print("Testing Problem 5:")
print(running_total([1]))
print(running_total([]))
print(running_total([1, 2, 3, 4, 5]))
print(running_total([1, 3, 5, 7, 11]))
print(running_total([2, 4, 6, 8, 10, 100]))

"""
Time and Space Analysis for problem 5:
- Best-case: The best case is the empty input list and is O(1)
- Worst-case: The worst case and average case are the same for this one.  The loop must execute n times and all of the calculations within 
              the loop are O(1).  This makes the worst case O(n)
- Average-case: For the same reasoning as in the worst case, the average case is also O(n)
- Space complexity: The space of the sum_list will always be n and is therefore considered O(n)
- Why this approach? Every input must be handled and the loop is as efficient as possible.  All computations are core O(1) python calls.
- Could it be optimized? I do not believe so.  I believe this code is optimum.
"""
