from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from forum.custom_models.forum_forms import WorryMessageForm, OpinionMessageForm
from forum.custom_models.message_mapped import WorryMessageMapped, OpinionMessageMapped
from forum.models import WorryMessage, OpinionMessage, WorryUser, UserAction, WorryCategory, WorryType, MessageRecord


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
                if (MessageRecord.objects.filter(opinion_message_id=opinion_message.id))
            ]
        )
        for worry_message in latest_message_list if(UserAction.objects.filter(worry_message__id=worry_message.id))
    ]
    return render(request, 'forum/index.html',
                  {'message_mapped': message_mapped,
                   'form': WorryMessageForm,
                   'opinion_message_form': OpinionMessageForm()})


class MessageView(generic.edit.CreateView):
    form_class = WorryMessageForm
    template_name = 'forum/worry_message/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


def create_worry_message(request):
    if request.method == 'POST':
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
            user_action.worry_user = WorryUser.objects.get(user_id=request.user.id)

            user_action.save()

            return redirect('home')
        else:
            return HttpResponse('error')
    else:
        return HttpResponse('Error')


def create_opinion_message(request, worry_message_id):
    if request.method == 'POST':
        opinion_message = OpinionMessage()
        opinion_message.opinion_message = request.POST['opinion_message']
        opinion_message.save()

        worry_user = WorryUser.objects.get(user_id=request.user.id)
        user_action = UserAction()
        user_action.opinion_message = opinion_message
        user_action.worry_user = worry_user
        user_action.action = 'RESPONSE'
        user_action.save()

        worry_message = WorryMessage.objects.get(id=worry_message_id)
        message_record = MessageRecord()
        message_record.opinion_message = opinion_message
        message_record.worry_message = worry_message
        message_record.save()

        return redirect('home')
    else:
        opinion_message_form = OpinionMessageForm()
        return render(request, 'forum/opinion_message/create.html',
                      {'opinion_message_form': opinion_message_form,
                       'worry_message_id': worry_message_id})


def categories(request):
    return render(request, 'forum/category/index.html', {'': ''})
