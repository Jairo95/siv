from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from forum.custom_models.message_mapped import WorryMessageMapped, OpinionMessageMapped
from forum.models import WorryMessage, OpinionMessage, WorryUser, UserAction


def index(request):
    latest_message_list = WorryMessage.last_active_messages().order_by('-publish_date')[:5]
    message_mapped = [
        WorryMessageMapped(
            WorryUser.objects.get(useraction__worry_message__id=worry_message.id),
            worry_message,
            [
                OpinionMessageMapped(
                    WorryUser.objects.get(useraction__opinion_message_id=opinion_message.id),
                    opinion_message
                )
                for opinion_message in OpinionMessage.objects.filter(messagerecord__worry_message__id=worry_message.id)
            ]
        )
        for worry_message in latest_message_list
    ]
    '''
    custom_message_list = [
        [worry_message_pub, [opinion_message for opinion_message
                             in OpinionMessage.objects.filter(messagerecord__worry_message__id=worry_message_pub.id)
                             ]
         ] for worry_message_pub in latest_message_list]
    context = {
        'custom_message_list': custom_message_list,
    }
    return render(request, 'forum/index.html', context)
    '''
    return render(request, 'forum/index.html', {'message_mapped': message_mapped})


def opinions_message(request, worry_message_id):
    return HttpResponse('Hola q ase')


def categories(request):
    return render(request, 'forum/category/index.html', {'': ''})
