
class search():
    def __init__(self, API):
        self.API = API

    def searchViewUrlsByUrlRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/urlsByUrlRegex/',
            params=params
        )

        return r.json

    def searchViewUrlsByRequestRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/urlsByRequestRegex/',
            params=params
        )

        return r.json

    def searchViewUrlsByResponseRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/urlsByResponseRegex/',
            params=params
        )

        return r.json

    def searchViewUrlsByHeaderRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/urlsByHeaderRegex/',
            params=params
        )

        return r.json

    def searchViewMessagesByUrlRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/messagesByUrlRegex/',
            params=params
        )

        return r.json

    def searchViewMessagesByRequestRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/messagesByRequestRegex/',
            params=params
        )

        return r.json

    def searchViewMessagesByResponseRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/messagesByResponseRegex/',
            params=params
        )

        return r.json

    def searchViewMessagesByHeaderRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/search/view/messagesByHeaderRegex/',
            params=params
        )

        return r.json

    def searchOtherHarByUrlRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/OTHER/search/other/harByUrlRegex/',
            params=params
        )

        return r.json

    def searchOtherHarByRequestRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/OTHER/search/other/harByRequestRegex/',
            params=params
        )

        return r.json

    def searchOtherHarByResponseRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/OTHER/search/other/harByResponseRegex/',
            params=params
        )

        return r.json

    def searchOtherHarByHeaderRegex(self, **kwargs):

        params = {
            "regex": kwargs.get("regex"),
"baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/OTHER/search/other/harByHeaderRegex/',
            params=params
        )

        return r.json
