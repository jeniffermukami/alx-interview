#!/usr/bin/python3
"""
This module contains the function 'pascal_triangle' which generates
Pascal's triangle up to 'n' levels. It includes a 'print_triangle'
function to display the triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    List[List[int]]: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            # Ensure line length does not exceed 79 characters
            sum_pair = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(sum_pair)
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle.

    Parameters:
    triangle (list of lists of ints): The Pascal's triangle to print.
    """
    for row in triangle:
        # Use f-string for improved readability
        print(f"[{','.join([str(x) for x in row])}]")


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
