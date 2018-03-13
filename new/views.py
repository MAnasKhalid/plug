from django.shortcuts import render
from .tasks import add


# Create your views here.
def helo(x, y):
    add.delay(4, 4)

    return 'Helo'
