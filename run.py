from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='test', renderer='string')
def test(request):
    return Response(request.matchdict['whatever'])

if __name__ == '__main__':
    config = Configurator()
    config.add_route('test', '/{whatever}')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 3000, app)
    server.serve_forever()
