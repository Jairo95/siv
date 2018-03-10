from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from forum.models import WorryMessage, OpinionMessage


def index(request):
    latest_message_list = WorryMessage.objects.order_by('-publish_date')[:5]
    custom_message_list = [
        [worry_message_pub, [opinion_message for opinion_message
                             in OpinionMessage.objects.filter(messagerecord__worry_message__id=worry_message_pub.id)
                             ]
         ] for worry_message_pub in latest_message_list]
    context = {
        'custom_message_list': custom_message_list,
    }
    return render(request, 'forum/index.html', context)


def opinions_message(request, worry_message_id):
    return HttpResponse('Hola q ase')
