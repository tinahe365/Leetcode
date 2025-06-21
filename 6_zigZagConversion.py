# def convert(s: str, numRows: int) -> str:
#     direction = 1
#     rows = [''] * numRows
#     step = 0
#     # result = ""

#     for item in s:
#         rows[step] += item
#         step += direction
#         if step > numRows-1 or step < 0:
#             step -= direction
#             direction *= -1
#             step += direction
#     # for row in rows:
#     #     result += row
#     # return result

#     return ''.join(rows)


# x = 2**5
# print(x)

# x  = str(x)
# # print(type(x[0]+x[1]))

# print(type(int(x[0]+x[1])))
# print(int(x[1]+x[0]))
print(int('00001'))