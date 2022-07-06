class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, *args, **kwargs):
        rqst = self.request.get("method", "GET")
        if rqst == 'GET':
            return f'{rqst}: {self.func(self.request)}'
        else:
            return None

    def __call__(self, request, *args, **kwargs):
        self.request = request
        return self.get(request)


@HandlerGET
def contact(request):
    return "Сергей Балакирев"
