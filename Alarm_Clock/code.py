import ast,sys
import math
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

# write code here
for index, number in enumerate(input_list):
    nearestTensMultiple = round(number/10)*10
    input_list[index] = nearestTensMultiple
    print(nearestTensMultiple)
print(input_list)

# store the sum in the following variable
result = sum(input_list)
print(issubclass)
# do not change the following code
print(result)
