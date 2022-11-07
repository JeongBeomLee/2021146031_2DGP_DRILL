# layer 0 : 후경
# layer 1 : 전경
objects = [[], []]

def add_object(object, depth):
    objects[depth].append(object)

def add_objects(l_object, depth):
    objects[depth] += l_object

def remove_object(object):
    for layer in objects:
        if object in layer:
            layer.remove(object)
            del object
            return
    raise ValueError('삭제할 객체가 존재하지 않습니다.')

def all_objects():
    for layer in objects:
        for object in layer:
            yield object

def clear():
    for object in all_objects():
        del object
    for layer in objects:
        layer.clear()