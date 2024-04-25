def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to a given number of rows (n).

  Args:
      n: An integer representing the number of rows in the Pascal's triangle.

  Returns:
      A list of lists containing the integers of Pascal's triangle, or an
      empty list if n is less than or equal to 0.
  """

  if n <= 0:
    return []

  triangle = []
  # Create the first row with 1
  triangle.append([1])

  # Iterate for remaining rows (up to n-1)
  for i in range(1, n):
    # Create a new row based on the previous row
    row = []
    # The first and last element of each row are always 1
    row.append(1)

    # Calculate the middle elements using the previous row's values
    for j in range(1, i):
      previous_row = triangle[i-1]
      element = previous_row[j-1] + previous_row[j]
      row.append(element)

    # Append the last 1
    row.append(1)
    triangle.append(row)

  return triangle
