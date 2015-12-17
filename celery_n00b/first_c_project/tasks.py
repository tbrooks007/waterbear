from __future__ import absolute_import

from first_c_project.celery import app

#app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task(name='tasks.add')
def add(x, y):
    return x + y
