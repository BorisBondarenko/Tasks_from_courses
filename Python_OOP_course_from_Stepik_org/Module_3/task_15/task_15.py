class Handler:

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, func, request):
        return f"GET: {func(request)}"

    def post(self, func, request):
        return f"POST: {func(request)}"

    def __call__(self, func):
        def wrapper(request):
            method = request.get('method', 'GET')
            if method in self.methods:
                return self.__getattribute__(method.lower())(func, request)

        return wrapper


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
