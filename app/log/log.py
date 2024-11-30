import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {'DEBUG': '\033[94m', 'INFO': '\033[92m', 'WARNING': '\033[93m',
              'ERROR': '\033[91m', 'CRITICAL': '\033[95m'}

    def format(self, record):
        log_fmt = f"{self.COLORS.get(record.levelname, '')}[%(asctime)s | %(levelname)s]: %(message)s\033[0m"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def init_logging():
    # if os.path.exists('logs') == False:
    #     os.mkdir('logs')
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()

    logging.basicConfig(handlers=(file_log, console_out), 
                        format='[%(asctime)s | %(levelname)s]: %(message)s', 
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)

    for handler in logging.getLogger().handlers:
        handler.setFormatter(ColoredFormatter())
