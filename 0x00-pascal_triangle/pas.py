#!/usr/bin/env python3

def pascal_triangle(n):
    triangle = []
    for i in range(n + 1):# Loop to generate each row
        row = [1] * (i + 1)  # Start with all 1s
        print(i,"for starting")
        for j in range(1, i):  # Fill in the middle elements
            print(i)
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            print(triangle[i-1][j-1],"for t1")
            print(triangle[i-1][j],"for t2")
        triangle.append(row)
    return triangle

