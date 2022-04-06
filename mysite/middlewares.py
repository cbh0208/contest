from django.utils.deprecation import MiddlewareMixin

class SolveCrossDomainMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Headers']='authorization,Content-Type'
        return response
