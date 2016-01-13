import web

db = web.database(dbn='mysql', db='d3b422e343b4b42b88d85706d06320d59', user='e4048619-c3c3', host='192.168.1.11', pw='b442e4ec-e842', port=3306,)

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
