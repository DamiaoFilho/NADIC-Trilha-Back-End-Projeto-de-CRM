from celery import shared_task
import time 
from .models import CeleryTasks
@shared_task
def test(message_body):
    return f'{message_body}'

@shared_task
def atu():
    time.sleep(20)
    objects = CeleryTasks.objects.all()
    for obj in objects:
        obj.response = obj.message.upper()
        obj.save()

@shared_task
def task(id):
    time.sleep(10)
    object = CeleryTasks.objects.get(pk=id)
    object.response = object.message.upper()
    object.save()
    return object.message.upper()