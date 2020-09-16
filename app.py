import flask
import sys
import logging

app = flask.Flask(__name__)

logging.basicConfig(filename='/apps/logs/pypi/app_log/demo.log', level=logging.DEBUG)
app.logger.info('%s logged successfully','start - ')

@app.route('/')
def main():
    return "Hello world 11:32"

if __name__ == "__main__":
    print('name=main', flush=True)
    app.run()


print('reached bottom', flush=True)
