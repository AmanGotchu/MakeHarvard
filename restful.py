from bottle import run, get
import requests
import watcher

animals = [{'name' : 'Ellie', 'type' : 'Elephant'},
           {'name': 'Python', 'type': 'Snake'},
           {'name': 'Zed', 'type': 'Zebra'}]


@get('/open')
def getAll():
    import kairosHandler
    print("Run script to open the door")

    return{'animals' : animals}

@get('/close')
def getOne(name):
    print("Keep the door locked")
    the_animal  = [animal for animal in animals if animal['name'] == name]
    return {'animal' : the_animal[0]}


run(reloader = True, debug = True)