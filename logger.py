import logging
import random

logging.basicConfig()
logger = logging.getLogger('retry_test')
logger.setLevel(logging.INFO)

def logger_test():
    rand_num = random.randint(0, 10)
    logger.info(f"rand_num={rand_num}")

if __name__ == "__main__":
    logger_test()