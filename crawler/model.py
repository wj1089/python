class Model:
        def __init__(self):
            self._url = ''
            self._parser = ''
            self._path = ''
            self._api = ''

        @property
        def url(self) -> str: return self._url
        @url.setter
        def url(self, url): self._url = url

        @property
        def parser(self) -> str: return self._parser
        @url.setter
        def parser(self, parser): self._parser = parser

        @property
        def path(self) -> str: return self._path
        @url.setter
        def path(self, path): self._path = path

        @property
        def api(self) -> str: return self._api
        @url.setter
        def api(self, url): self._api = api