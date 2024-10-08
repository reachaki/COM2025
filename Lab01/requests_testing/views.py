from django.http import HttpResponse


def hello_world(request):
    # Check for the MY-APPLICATION-MESSAGE header
    custom_message = request.headers.get('MY-APPLICATION-MESSAGE')
    if custom_message:
        # If the header is present, use it as the response
        response_message = custom_message
    else:
        # Otherwise, check for the message GET parameter
        response_message = request.GET.get('message', 'Hello world!')
    return HttpResponse(response_message)
