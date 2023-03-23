import urllib


class HttpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get(self, path, params=None):
        url = self._build_url(path, params)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')

    def post(self, path, data=None, params=None):
        url = self._build_url(path, params)
        data = self._encode_data(data)
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')

    def put(self, path, data=None, params=None):
        url = self._build_url(path, params)
        data = self._encode_data(data)
        req = urllib.request.Request(url, data, method='PUT')
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')

    def _build_url(self, path, params=None):
        url = f'http://{self.host}:{self.port}/{path}'
        if params:
            url += '?' + urllib.parse.urlencode(params)
        return url

    def _encode_data(self, data):
        if data:
            if isinstance(data, dict):
                data = urllib.parse.urlencode(data).encode('utf-8')
            elif isinstance(data, str):
                data = data.encode('utf-8')
        return data
