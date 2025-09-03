import logging

## logging setting 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("ArithmeticApp")


def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def substract(a,b):
    result = a-b
    logger.debug(f"substract {a} - {b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result


def division(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero error: {a}/{b}")
        return None
    



add(10,14)
substract(20,14)
multiply(10,2)
division(10,5)