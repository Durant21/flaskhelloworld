from app import app
import sys
import logging


logging.basicConfig(filename='/apps/logs/pypi/app_log/demo.log', level=logging.DEBUG)
app.logger.info('inside wsgi.py')


root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
formatter = logging.Formatter(FORMAT)
ch.setFormatter(formatter)
root.addHandler(ch)

logging.debug("I am sent to standard out.")

#try:
from app import main
#except:
#    app.logger.error('error loading main()')

if __name__ == '__main__':

    app.logger.info('calling main')
    main()