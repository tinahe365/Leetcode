def path_traverse(grid, start_row, start_col):
    # Get the number of rows and columns in the grid
    rows, columns = len(grid), len(grid[0])

    # Check the validity of the input
    if start_row < 0 or start_row >= rows or start_col < 0 or start_col >= columns:
        return "Invalid input"

    # Define all four possible directions of movement
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    # Start with the value at the starting cell
    visited = [grid[start_row][start_col]]

    # Start an infinite loop until we break it when there are no more moves
    while True:
        # Initialize a current maximum as negative one 
        curr_max = -1

        # Look at each adjacent cell in all the directions
        for dir in directions:
            print(f"Checking direction: {dir}")
            # Calculate the new cell's row and column indices
            new_row = start_row + dir[0]
            new_col = start_col + dir[1]
            
            # If the new cell is out of the grid boundary, ignore it
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= columns:
                continue

            # If the value of the new cell is greater than the current maximum
            if grid[new_row][new_col] > curr_max:
                # Save it as the next cell to go to
                next_row, next_col, curr_max = new_row, new_col, grid[new_row][new_col]
                print(f"Next cell to visit: ({next_row}, {next_col}) with value {curr_max}")

        # If we don't have any valid cell we can go to, break from the loop   
        if curr_max <= grid[start_row][start_col]: 
            break
          
        # Otherwise, go to the next cell
        start_row, start_col = next_row, next_col

        # Append the value of the next cell to the result list
        visited.append(curr_max)

    # Return the list of visited cells' values    
    return visited

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 7]
]

print(path_traverse(grid, 1, 1))  