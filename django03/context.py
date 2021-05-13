from django.conf import settings

def context_processors(request):
    ret = {}

    ret['settings'] = settings
    ret['variavel_da_sessao'] = request.session.get('variavel_da_sessao')
