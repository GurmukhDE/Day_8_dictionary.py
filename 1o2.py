from loguru import logger

# Target = 'Data Engineer; Gurmukh is the best'

# logger.info(Target)

# l = [1,2,3,4,5,6,7,8,9]

# odd = []
# even = []

# for j in l:
#     if j%2 ==0:
#         even.append(j)
#     else:
#         odd.append(j)
# print(f'these numbers are odd: , {odd}')
# print(f'these numbers are even: , {even}')


# # #------------------------Let's begine the LC:

new_list = []

for i in range(1,21):
    if i %2==0:
        new_list.append(i)

logger.info(f' total even numbers in the list:, {len(new_list)}')


# new_lc = [i for i in range(1,11) if i % 2==0]
# logger.info(new_lc)

# #let's do a even odd operation on number list [1,31]

# even = [i for i in range(1,31) if i % 2==0 ]
# odd  = [i for i in range(1,31)  if i%2!=0 ]

# logger.info(even)
# logger.info(odd)

lis = [1,2,3,4,5]

new_lis = []

for j in lis:
    if j %2!=0:
        new_lis.append(j*2)

logger.info(new_lis)

new_lc = [j*2 for j in lis if  j % 2!=0 ]
logger.info(new_lc)









