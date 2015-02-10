from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
    # Request the context of HTTP request
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key content is the same as {{ content }} in the template!
    post_list = post.objects.order_by('-date')[:5]
    context_dict = {'posts': post_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)

def add_post(request):
    return render_to_response('add_post.html')
