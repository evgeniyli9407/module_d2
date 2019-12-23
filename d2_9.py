import os
from bottle import Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get("https://ae274fd01a924fab9de8fc708d4407eb@sentry.io/1858658"), integrations=[BottleIntegration()])

app = Bottle()


@app.route('/success')
def success():
    return ('Ошибки нет, ты перешёл в success')


@app.route('/fail')
def fail():
    raise RuntimeError("Ошибка!")


app.run(host='localhost', port=8080)