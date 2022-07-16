class RenderList:
    """This class describes the objects """
    def __init__(self, type_list='ul'):
        self.type_list = f'<{type_list}>'

    def __call__(self, some_list, *args, **kwargs):
        res = self.type_list
        for i in some_list:
            res += f"\n<li>{i}</li>"
        res += f'\n</{self.type_list[1:3]}>'
        return res

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList()