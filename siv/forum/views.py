from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from forum.custom_models.forum_forms import WorryMessageForm
from forum.custom_models.message_mapped import WorryMessageMapped, OpinionMessageMapped
from forum.models import WorryMessage, OpinionMessage, WorryUser, UserAction, WorryCategory, WorryType


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
    return render(request, 'forum/index.html', {'message_mapped': message_mapped, 'form': WorryMessageForm})


class MessageView(generic.edit.CreateView):
    form_class = WorryMessageForm
    template_name = 'forum/worry_message/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


def create_worry_message(request):
    if request.method == 'POST':
        print('SOMETHING: ', str(request.POST))
        print('CAT: ', str(request.POST['worry_category']))
        worry_message = WorryMessage()
        worry_category = WorryCategory.objects.get(id=request.POST['worry_category'])
        worry_type = WorryType.objects.get(id=request.POST['worry_type'])
        worry_message.worry_message = request.POST['worry_message']
        worry_message.worry_category = worry_category
        worry_message.worry_type = worry_type
        if worry_message:
            worry_message.save()
            user_action = UserAction()
            user_action.worry_message = worry_message
            user_action.action = 'PUBLISH'
            user_action.worry_user = WorryUser.objects.get(id=request.user.id)

            user_action.save()

            return redirect('home')
        else:
            return HttpResponse('error')
    else:
        return HttpResponse('Error')


def opinions_message(request, worry_message_id):
    return HttpResponse('Hola q ase')


def categories(request):
    return render(request, 'forum/category/index.html', {'': ''})
