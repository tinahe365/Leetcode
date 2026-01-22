# def solution(arrA, arrB):
#     # TODO: implement the solution here
#     n = len(arrA)
   
#     diffA_B, diffB_A = {}, {}
    
#     for i in range(n):
#         a = arrA[i] - arrB[i]
#         if a not in diffA_B :
#             diffA_B[a] = [i]
#         else:
#             diffA_B[a].append(i)

#         if -a not in diffB_A:
#             diffB_A[-a] = [i]
#         else:
#             diffB_A[-a].append(i)

#     for diff in diffA_B:
#         if diff in diffB_A:
#             for i in diffA_B[diff]:
#                 for j in diffB_A[diff]:
#                     if i != j:
#                         return [i, j]
    


#     # for i in range(n-1):
#     #     for j in range(i+1, n):
#     #         sumA = arrA[i] + arrA[j]
#     #         sumB = arrB[i] + arrB[j]
#     #         if sumA == sumB:
#     #             return [i,j]
            
            
# # arrA = [2, 5, 1, 4]  
# # arrB = [3, 6, 3, 2]
# # print(solution(arrA, arrB))  

# arrA = [62, 56, 54, 2, 42, 68, -53, 65, 31, -52, 56, -33, 16, 69, -19, 44]
# arrB = [62, 50, 54, 2, 42, 68, -53, 65, 31, -52, 56, -33, 16, 69, -19, 44]
# print(solution(arrA, arrB))  # Expected output: [0, 1] or [1, 0] since both pairs have the same sum
    



# optimized brute force solution
def solution(arrA, arrB): # this function is used to find two indices i and j such that arrA[i] + arrA[j] == arrB[i] + arrB[j]
    seen = {}
    best_i = best_j = None
    for j, (a,b) in enumerate(zip(arrA, arrB)):
        print(j,a,b)
    #     d = a - b
    #     c = -d
    #     if c in seen:
    #         i = seen[c]
    #         if best_i is None or i < best_i or (i == best_i and j < best_j):
    #             best_i, best_j = i, j
    #             if best_i == 0:
    #                 return [best_i, best_j]
        
    #     if d not in seen:
    #         seen[d] = j
        
   

    # return [best_i, best_j]

arrA = [2, 5, 1, 4]  
arrB = [3, 6, 3, 2]
print(solution(arrA, arrB))