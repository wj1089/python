class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload) -> object:
        for item in self._contacts:
            if payload == item.name:
                return item

    def get_contacts(self) -> []:
        contacts = []
        for item in self._contacts:
            contacts.append(item.to_string())
        return ' '.join(contacts)

    def del_contact(self, payload):
        for item, t in enumerate(self._contacts):
            if payload == t.name:
                del self._contacts[item]
