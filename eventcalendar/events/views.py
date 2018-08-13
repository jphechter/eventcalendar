from django.http import HttpResponse
from django.template import loader

from .models import Event, Venue

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    event_list = Event.objects.order_by('-pub_date')
    template = loader.get_template('events/index.html')
    context = {
        'event_list': event_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # return render(request, 'events/<int:event_id>', {'event': event})
    template = loader.get_template('events/details.html')
    context = {'event': event}
    return HttpResponse(template.redner(context, request))