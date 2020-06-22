from celery import Celery, shared_task
from dotenv import load_dotenv
import datetime
import json


#def initialize_broker():
    #broker_url = 'amqp://{user}:{pass}@{url}/{host}'.format(user=USER, pass=PASS, url=URL, host=HOST)
#    broker_url = 'ampq://'

app = Celery('tasks', broker='amqp://localhost')



@app.task
def add(x, y):
    return x + y



@shared_task 
def register_command(command):
    now = datetime.datetime.now()
    print('command: {}  -- at: {}:{}'.format(command, now.hour, now.minute))


