import logging
import logging.handlers
'''
日志模块
'''
LOG_DIR= 'log'
if not os.path.exists(LOG_DIR):
    print('no cookies in local path %s ' % LOG_DIR)
    os.makedirs(LOG_DIR)

LOG_FILENAME = LOG_DIR + '/jd_seckill.log'
logger = logging.getLogger()


def set_logger():
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

set_logger()