from django.shortcuts import render
import simplejson as json
from django.utils.safestring import mark_safe
# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request, room_name):
    return render(request, 'socket.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })