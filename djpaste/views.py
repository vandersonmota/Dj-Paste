from djpaste.forms import SnippetForm
from djpaste.models import Snippet
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.create_update import create_object
from django.views.generic.list_detail import object_detail


def new(request):
    if request.method == 'POST':
        snippet_form = SnippetForm(request.POST)
        if snippet_form.is_valid():
            new_snippet = snippet_form.save()
            return HttpResponseRedirect("/view/"+str(new_snippet.id))            
    else:
        return create_object(request, form_class=SnippetForm, template_name='new.html')
        
def view_snippet(request, id, template_name='view_snippet.html'):
    queryset = Snippet.objects.filter(id=id)
    
    return object_detail(request, queryset, id, template_name=template_name)
        
    
def reply(request, id):
    
    snippet = Snippet.objects.get(id=id)
    
    return render_to_response('reply.html', {'snippet':snippet})
    
    