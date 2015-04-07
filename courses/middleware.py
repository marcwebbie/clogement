from django.conf import settings


class LanguageCodeMiddleware(object):

    def process_request(self, request):
        lang = request.META.get('HTTP_ACCEPT_LANGUAGE', settings.LANGUAGE)
        if lang:
            request.LANG = lang.split(',')[0]
        else:
            request.LANG = settings.LANGUAGE
