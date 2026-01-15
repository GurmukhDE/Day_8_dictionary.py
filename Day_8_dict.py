from loguru import logger

dic = { "name": "gurmukh",
        "age":32,
        "city": "gurgaon"
}

logger.info(dic)

dic["hometown"] = "Bareilly"

logger.info(dic)

#Important dict methods
 logger.info(dic.keys())
 logger.info(dic.values())
 logger.info(dic.items())

logger.info(dic["name"])

for x in dic:
    print(x, dic[x])# here logger.info will not work for that we have to convert it into a f' string

    logger.info(f'{x},{dic[x]}')#here is converted version for print in f'string


#one more method to iterate the items of a dict.
 for key, value in dic.items():
    print(key, value)
    logger.info(f'{key},{value}')

data  = {"color1":"red","value1":"#f00","color2":"green","value2":"#0f0","color3":"blue","value3":"#00f","color4":"cyan", "value4":"#0ff"}

for colors in data:
    print(colors, data[colors])#method 1

for colors, hex_value in data.items():
    print(colors, hex_value)    #method 2
    logger.info(f'{colors},{hex_value}')



