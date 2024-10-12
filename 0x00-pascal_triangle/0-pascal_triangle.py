#!/usr/bin/python3
"""
    This is the printing of a Pascal Triangle using
    Additional Method of previous row
"""

def pascal_triangle(n):

    """
    Function for processing the data
    """

    triangle = []
    for i in range(n):# Loop to generate each row
        row = [1] * (i + 1)  # Start with all 1s
        for j in range(1, i):  # Fill in the middle elements
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

