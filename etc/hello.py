def app(environ, start_response):
    """Simplest possible application object"""
    #data = b'Hello, World!\n'
    data = environ["QUERY_STRING"]
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str())
    ]
    print(environ)
    start_response(status, response_headers)
    return iter["test"]