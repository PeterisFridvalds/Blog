from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostForm

def index(request):
    # Get the context from the request
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key content is the same as {{ content }} in the template!
    #post_list = post.objects.order_by('-date')[:5]
    context_dict = {'content':"cintent"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)

def add_post(request):
    # Get the context from the request
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = PostForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new post to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        #else:
            # The supplied form contained errors - just print them to the terminal.
            #print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = PostForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('add_post.html', {'form': form}, context)
