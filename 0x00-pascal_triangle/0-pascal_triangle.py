def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n.
    
    Parameters:
    - n (int): The height of the triangle.
    
    Returns:
    - List[List[int]]: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # The first row is always [1].
    
    for i in range(1, n):
        row = [1]  # Every row starts with 1.
        for j in range(1, i):
            # Each element is the sum of the two elements above it.
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1.
        triangle.append(row)
    
    return triangle

# The code snippet provided for testing
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
