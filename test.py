# def trek_path(elevation_map, start_x, start_y):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
#     path = [elevation_map[start_x][start_y]]
#     visited = [(start_x, start_y)]

#     while True:
#         current_height = path[-1]
#         # Pre-completed: Find all possible moves from the current position, moving only to higher and not yet visited elevations.
#         possible_moves = [
#             (start_x + dx, start_y + dy) for dx, dy in directions
#             if (0 <= start_x + dx < len(elevation_map) and
#                 0 <= start_y + dy < len(elevation_map[0]) and
#                 elevation_map[start_x + dx][start_y + dy] > current_height)
#         ]
#         if not possible_moves:
#             break
        
        
#         # TODO: Implement logic to select the next position based on the highest elevation in the possible moves.
#         # Hint: Use a key function with the max() function to find the move leading to the highest elevation.
#         for r,c in possible_moves:
#             if (r,c) in visited:
#                 possible_moves = possible_moves.remove((r,c))
        
#             highest_ele = max(possible_moves, key=lambda x: mountain[x[0]][x[1]]) 
#         visited.append(highest_ele)
#         path.append(elevation_map[highest_ele[0]][highest_ele[1]])
     
        
#     return path
        
        

# mountain = [
#     [1, 2, 3],
#     [2, 3, 4],
#     [3, 5, 6]
# ]
# print(trek_path(mountain, 1, 1))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,1]
print(arr)
print(arr.discard(10))  # Removes the first occurrence of 1
print(arr)  # Should print the array without the first occurrence of 1
