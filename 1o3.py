
from loguru import logger

l = [1,2,3,4,54,56,6,7, 'guru', 'singh']


ints = [x for x in l if  isinstance(x, int)]

logger.info(ints)
l = [1,2,3,4,54,56,6,7]
even = []
odd = []

for i in l:
    if i%2==0:
       even.append(i)
    else:
        odd.append(i)
logger.info(even)
logger.info(odd)
#-------------------------------------

less_than = []
grtr_than = []
for x in l:
    if x<11:
        less_than.append(x)
    else:
        grtr_than.append(x)
logger.info(less_than)
logger.info(grtr_than)

l = [1,2,4,5,67,7,8]

for idx, value in enumerate(l):
    if value <= 11:
        print(f"value {value} at index {idx} is <= 11")

#------------------------------------------------------------------------
#let's design a right angle triangle using loops * Pattern



for i in range(5):
        
        logger.info((i+1) * '* ')

#--------------------------------------------

even = []

for i in range(101):
    if i %2==0:
         even.append(i)
         logger.info(even)
         logger.info(len(even))

#----------------
 
for numbers in range(101):
      if numbers %3 == 0:
            logger.info(numbers)
       
#------------------------------------

paragraph = """When working with strings like URLs, using split() repeatedly on the same string
with different delimiters is not true “multiple splitting” and can break the logical structure
of the data. The correct approach is to split step by step on the result of previous split, 
preserving meaning such as domain, path, and query parameters. While split() is useful for learning
and simple cases, in real-world and production scenarios it’s better to use standard libraries like 
urllib.parse, which safely and reliably parse URLs without losing structure or order."""


list_format = paragraph.lower().split(" ")

logger.info(list_format)
count =0
for letter in list_format:
    if letter == 'the':
        count+=1
    else:
        continue
logger.info(f"letter 'the' count is {count}")


l = [1,5,3,2,6]
sort_l = l.sort()
new = l.insert(3,4)

logger.info(l)

records = [1200, 1500, 1800, 2000, 1700]
print(sum(records))

total_record = 0

for i in records:
    total_record +=i
print(total_record)

   





