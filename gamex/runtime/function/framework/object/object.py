from .object_id_allocator import ObjectID

class GObject:
    def __init__(self):
        self.id = ObjectID.alloc()
        self.components = dict()

    def tick(self, delta_time):
        for component in self.components.values:
            component.tick(delta_time)

    def has_component(self, name):
        return name in self.components

    def add_component(self, name, component):
        self.components[name] = component
