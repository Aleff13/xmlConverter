import json
from django.http import HttpResponse
from .xmlObjects import XML
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('hello')

@csrf_exempt
def convert(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # content = body['content']
        # print(str(content))
        XML.generateXml(body, 'produtos')
        return HttpResponse(open('produtos.xml').read(), content_type='application/xml')

    return HttpResponse('Send a post with your itens to convert')
