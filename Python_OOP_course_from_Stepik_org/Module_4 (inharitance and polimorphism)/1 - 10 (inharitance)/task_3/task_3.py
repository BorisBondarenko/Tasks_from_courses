class GenericView:
    """This class describes the instances for processing web-request.
    Every method here exists just for example (for each type of request).
    This class using as parent-class for another child-classes."""

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    """This class describes the instances for processing the web-requests.
    This class come as child-class of GenericView - basic class."""

    def __init__(self, methods=None):
        super().__init__()
        if methods:
            self.methods = methods

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return self.__getattribute__(method.lower())(request)

    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"


v = DetailView(methods=('GET', 'POST'))
res = v.render_request({'url': 'https://site.ru/home'}, 'GET')