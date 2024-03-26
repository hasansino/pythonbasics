# Python functionality study.
import os
import random
import asyncio

from my_class import MyClass
from config import LOGGER as LOG


def add(a: int, b: int) -> int:
    return a + b


async def async_print(msg: str):
    LOG.info("msg: {}".format(msg))


if __name__ == "__main__":

    # Variable declaration

    varInt = 25
    varString = "Hello World!"
    varBoolean = True
    varList = [varInt, varString, varBoolean]
    varTuple = (varInt, varString, varBoolean)

    varIntAnnotated: int = 25
    varStringAnnotated: str = "Hello World!"
    varBooleanAnnotated: bool = False

    varIntRand = random.randint(0, 100)

    # Control flow
    if varIntRand == 0:
        LOG.info("varIntRand < 0")
    elif varIntRand < 50:
        LOG.info("varIntRand < 50")
    else:
        LOG.info("varIntRand > 50")

    # Loop over list
    varFruits = ["apple", "banana", "watermelon"]
    for fruit in varFruits:
        LOG.info("varFruits -> " + fruit)

    # Loop over tuple
    varFruits = ("apple", "banana", "watermelon")
    for fruit in varFruits:
        LOG.info("varFruits -> " + fruit)

    # Counter with while
    varCounter = 0
    while varCounter < 5:
        varCounter += 1
    LOG.info("varCounter -> " + str(varCounter))

    # Function call
    LOG.info("2+2="+str(add(2,2)))

    # Access list by index
    LOG.info("varFruits[0] -> "+str(varFruits[0]))

    # Append and remove elements from list
    varMutableList = ["apple", "banana"]
    LOG.info("varMutableList -> "+str(varMutableList))
    varMutableList.append("orange")
    LOG.info("varMutableList -> " + str(varMutableList))
    varMutableList.remove("orange")
    LOG.info("varMutableList -> " + str(varMutableList))

    # Dictionary
    varDict = {
        "foo": 1,
        "bar": 2,
    }
    # Access dictionary item
    LOG.info("varDict[foo] -> " + str(varDict["foo"]))
    # Change dictionary item
    varDict["bar"] = 9
    LOG.info("varDict[bar] -> " + str(varDict["bar"]))

    # Working with FS
    varFileWriter = open("tmp/log.txt", "w+")

    for i in range(10):
        varFileWriter.write("line" + "\n")

    varFileWriter.flush()
    varFileWriter.close()

    varFileReader = open("tmp/log.txt", "r")
    LOG.info("fileContent -> " + str(varFileReader.read()))

    varFileReader.close()

    if os.path.exists("tmp/log.txt"):
        os.remove("tmp/log.txt")
    else:
        LOG.info("os.remove -> tmp/log.txt does not exist")

    # Exceptions
    try:
        varUndivisible = 10 / 0
    except ZeroDivisionError:
        LOG.info("10 / 0 -> ZeroDivisionError")

    try:
        varDivisible = 10 / 10
    finally:
        LOG.info("varDivisible -> " + str(varDivisible))

    oMyClass = MyClass("Hello ", "World")
    LOG.info("oMyClass.concat -> " + oMyClass.concat())

    # coroutines
    for i in range(10):
        msg = "This is routine number " + str(i)
        asyncio.run(async_print(msg))

    LOG.info("Python study.")
