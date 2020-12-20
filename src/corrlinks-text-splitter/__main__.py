import logging
import sys

file_handler = logging.FileHandler(filename='text-split.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)
log = logging.getLogger(__name__)

if __name__ == '__main__':
    import main
    main.TextSplit()