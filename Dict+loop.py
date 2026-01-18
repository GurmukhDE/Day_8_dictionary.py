
from loguru import logger
#LEVEL 1 — BASIC (Confidence build)

#Q1️⃣ Letter Count

word = "datascience"

letter_count = {}

for char in word:
    if char in letter_count:
        letter_count[char]+=1
    else:
        letter_count[char] =1
print(letter_count)

#👉 Har letter kitni baar aaya hai, dictionary banao.
#Q2️⃣ Word Length Dictionary

words = ["data", "python", "sql", "spark"]

len_count = {}

for word in words:
    len_count[word] = len(word)
logger.info(len_count)


#👉 Output:

{
 "data": 4,
 "python": 6,
 "sql": 3,
 "spark": 5
}

#Q3️⃣ Number Frequency

nums = [10, 20, 10, 30, 20, 10]

no_freq = {}

for i in nums:
    if i in no_freq:
        no_freq[i]+=1
    else:
        no_freq[i] =1
print(no_freq)


#👉 Har number kitni baar aaya?

#🟡 LEVEL 2 — LOGIC BUILDING (Yahin gap fill hota hai)
#Q4️⃣ Even–Odd Count

num = [1, 2, 3, 4, 5, 6, 2, 4]

count = {"even": 0, "odd":0}

for i in num:
    if i % 2==0:
        count["even"]+=1
    else:
        count["odd"]+=1
print(count)
        
        
#👉 Output:

{
 "even": 4,
 "odd": 4
}

#Q5️⃣ Student Marks Count

marks = [45, 67, 89, 45, 67, 45]

marks_count  ={}

for i in marks:
    if i in marks_count:
        marks_count[i]+=1
    else:
        marks_count[i] = 1
logger.info(marks_count)


#👉 Dictionary banao:

{
 45: 3,
 67: 2,
 89: 1
}

#Q6️⃣ Ignore Spaces

#👉 Letter count banao space ko ignore karke.
sentence = "big data engineering"

letter_count1 = {}

for char in sentence:
    if char == " ":
        continue
    if char in letter_count1:

        letter_count1[char] +=1
    else:
        letter_count1[char] = 1
logger.info(letter_count1)

#another way
for char in sentence:
    if char != " ":

        letter_count1[char] = letter_count1.get(char, 0) +1
logger.info(letter_count1)




#🔴 LEVEL 3 — INTERVIEW STYLE (Loop mastery)

#Q7️⃣ Group Words by Length

words = ["hi", "data", "sql", "python", "ai"]


#👉 Output:

{
 2: ["hi", "ai"],
 3: ["sql"],
 4: ["data"],
 6: ["python"]
}

#Q8️⃣ Character Type Count

text = "Data123!"


#👉 Count:

#alphabets

#digits

#special characters

#Q9️⃣ First Non-Repeating Character

word = "swiss"


#👉 Dictionary use karke first non-repeating character print karo.

#🔑 IMPORTANT INSTRUCTIONS (Isko follow karo)

#✅ Sirf:

#for loop

#if–else

#dictionary

#❌ Abhi:

#Counter

#collections

#advanced tricks
