i = 4
d = 4.0
s = 'HackerRank '

#Input Format

#The first line contains an integer that you must sum with .
#The second line contains a double that you must sum with .
#The third line contains a string that you must concatenate with .

#Output Format

#Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line,and then the two concatenated strings on the third line.

#Sample Input

#12
#4.0
#is the best place to learn and practice coding!

#Sample Output

#16
#8.0
#HackerRank is the best place to learn and practice coding!

input_int = int(input())  # For Int Value

input_double = float(input()) # For Float Value

input_string = str(input()) # For String

print(i + input_int)

print(d + input_double)

print(s+ " " + input_string)





               
