from logger import logging

def add(a,b):
    logging.debug(f"adding {a} and {b}")

    return a+b

logging.debug("the add function is called")

add(1,10)