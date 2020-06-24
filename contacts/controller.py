from contacts.model import Model
from contacts.service import Service

class Controller:
        def __init__(self):
            self._service = Service()

        def register(self, name, phone, email, addr):
            model = Model()
            model.name = name
            model.phone = phone
            model.email = email
            model.addr = addr
            self._service.add_contact(model)

        def search(self, name):
            return self._service.get_contact(name)

        def list(self):
            return self._service.get_contact(self)

        def remove(self):
            self._service.del_contact(self)




