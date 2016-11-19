from endpoints import Controller

class Default(Controller):
    def GET(self):
        return "boom"

    def POST(self, **kwargs):
        return 'hello {}'.format(kwargs['name'])

class Foo(Controller):
    def GET(self):
        return "bang"