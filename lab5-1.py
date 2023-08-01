"""
Question 1

Create a fully commented program to:
Complete this multiplication table:
X 2 4 6 8 10 12 14 16
11
7
3
"""
for i in range(2,17,2):
    j = [11, 7, 3]
    for k in j:
        print(i * k," ","\t", end=" ")
    print()