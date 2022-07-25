from Logger import init_logger

logger = init_logger(
    save_dir='./logs',
    log_file='test.txt'
)
logger.info(f'This is the logging msg from {__file__}!')