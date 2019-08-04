import ast,sys
input_str = sys.stdin.read()
n = ast.literal_eval(input_str)
sumOfSquaresUptoNumbern = 0
sumOfNumbers = 0
#find sum of squares upto n and sum of indivisual numbers
for number in range(1, n+1):
    sumOfSquaresUptoNumbern = sumOfSquaresUptoNumbern + number*number 
    sumOfNumbers = sumOfNumbers + number
#find square of  of all natural numbers
squareOfSumOfNumbers = sumOfNumbers*sumOfNumbers
# store the result in the following variable
abs_difference = abs(sumOfSquaresUptoNumbern-squareOfSumOfNumbers)

# print result --- do not change the following code
print(abs_difference)
