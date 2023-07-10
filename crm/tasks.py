from celery import shared_task
from .models import Stock
from rest_framework.generics import get_object_or_404


@shared_task
def get_stocks():
    return Stock.objects.all()