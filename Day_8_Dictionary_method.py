# -1. dict.get(key, default)

data = {"id": 101, "name": "Rahul"} #Safely get a value (no error if key missing)

print(data.get("name"))        # Rahul
print(data.get("salary", 0))   # 0
#------------------------------------------

#-2 - Returns all keys
data = {"a": 1, "b": 2}

print(data.keys())   # dict_keys(['a', 'b'])#Often used in loops.

#--------------------------

#3. dict.values()

print(data.values())  # dict_values([1, 2])
#-----------------------

#4. dict.items()

for k, v in data.items():
    print(k, v) #Very common in ETL / data processing

#---------------------------------
#5. dict.update()
data = {"a": 1}
data.update({"b": 2, "c": 3})

print(data)

#-------------------------

#6. dict.pop(key)
data = {"a": 1, "b": 2}
x = data.pop("a")

print(x)     # 1
print(data)  # {'b': 2}

#--------------------------------------

#7. dict.popitem()
data = {"a": 1, "b": 2}
data.popitem()

print(data)  # {'a': 1}

#-------------------------------

#8. dict.clear()
data.clear()
print(data)  # {}

#---------------------------

#9. dict.setdefault(key, default)

#Get value; if key missing → insert default
data = {"a": 1}

data.setdefault("b", 10)
print(data)#Used in grouping logic
#---------------------------------------------
#10. dict.copy()

Creates a shallow copy

d1 = {"a": 1}
d2 = d1.copy()

print(d2)
#--------------------------

#. dict.fromkeys(keys, value)

Create dictionary from keys

keys = ["id", "name", "salary"]
data = dict.fromkeys(keys, None)

print(data)

#---------------------------------------

#12. in keyword (IMPORTANT)

#Check if key exists

if "id" in data:
    print("Key exists")
#-------------------------------

#13- 

records = [{"dept": "IT"}, {"dept": "HR"}, {"dept": "IT"}]

count = {}
for r in records:
    count[r["dept"]] = count.get(r["dept"], 0) + 1

print(count)
#-----------------------------------------------------------------

