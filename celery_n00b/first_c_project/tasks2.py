from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def split_iterate(delimitedlist):

    for s in delimitedlist:
        yield s

