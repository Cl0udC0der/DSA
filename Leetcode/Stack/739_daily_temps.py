# O(n) time and size, high runtime still
# Initialize an array results to store the number of days until a warmer day for each day's temperature.
# Initialize an empty stack to keep track of indices.
# Iterate through each temperature in the array.
    # While the stack is not empty and the current temperature is greater than the temperature at the index on the top of the stack:
        # Update the result for the index at the top of the stack with the difference between the current index and the index on the top of the stack.
        # Pop the index from the stack.
    # Push the current index onto the stack.
# After the iteration, the results array contains the number of days until a warmer day for each given day.


class Solution:
    def dailyTemperatures(self, temps):
        results = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                print(f"pop {stack[-1]}")
                index = stack.pop()
                results[index] = i - index
            print("append")
            stack.append(i)

        return results
    
# My alternative made it 90% of the way to this solution but ran out of time and energy before completion
# 1 major loop, 1 minor loop. Subtract indices and store when conditions are met. Otherwise, append to stack