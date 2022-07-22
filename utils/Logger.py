# This is a class with logging function.
# Time: 2022.7.22 
# Author: Joey

import logging
import os

def init_logger(save_dir, log_file, level=logging.DEBUG):
    # Dir Folder
    abs_dir = os.path.abspath(save_dir)
    if not os.path.exists(abs_dir):
        print('Log Dir Created.')
    else:
        print('Log Dir Exists.')
    os.makedirs(abs_dir, exist_ok=True)
    log_local_path = os.path.join(abs_dir, log_file)
    print(log_local_path)

    # init a logger
    logger = logging.getLogger(log_local_path)
    logger.setLevel(level)

    # define a fancy format of each row
    formatter = logging.Formatter(
        '[%(asctime)s %(levelname)s] %(message)s', 
        '%Y-%m-%d %H:%M:%S')

    # file handler: process log.txt, log level: logging.INFO (20)
    fh = logging.FileHandler(log_local_path)
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # stream (CMD) handler: process cmd log output
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    print('Init finished.')
    return logger
        

if __name__ == '__main__':
    logger = init_logger(
        save_dir='./logs',
        log_file='test.log'
    )
    logger.info(__file__)
    logger.info(f'1 + 2 = {1 + 2}')
    
