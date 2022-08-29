from mongoengine import connect

def global_init():
    # connect('core', host='mongodb://localhost:27017/core')
    connect(db = 'SIH' ,alias = "core" , host = "mongodb+srv://yatharthk2:Bazinga#1702@cluster0.f1topxl.mongodb.net/?retryWrites=true&w=majority")