
class alert():
    def __init__(self, API):
        self.API = API

    def alertViewAlert(self, **kwargs):

        params = {
            "id": kwargs.get("id")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/view/alert/',
            params=params
        )

        return r.json

    def alertViewAlerts(self, **kwargs):

        params = {
            "baseurl": kwargs.get("baseurl"),
"start": kwargs.get("start"),
"count": kwargs.get("count"),
"riskId": kwargs.get("riskId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/view/alerts/',
            params=params
        )

        return r.json

    def alertViewAlertsSummary(self, **kwargs):

        params = {
            "baseurl": kwargs.get("baseurl")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/view/alertsSummary/',
            params=params
        )

        return r.json

    def alertViewNumberOfAlerts(self, **kwargs):

        params = {
            "baseurl": kwargs.get("baseurl"),
"riskId": kwargs.get("riskId")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/view/numberOfAlerts/',
            params=params
        )

        return r.json

    def alertViewAlertsByRisk(self, **kwargs):

        params = {
            "url": kwargs.get("url"),
"recurse": kwargs.get("recurse")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/view/alertsByRisk/',
            params=params
        )

        return r.json

    def alertViewAlertCountsByRisk(self, **kwargs):

        params = {
            "url": kwargs.get("url"),
"recurse": kwargs.get("recurse")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/view/alertCountsByRisk/',
            params=params
        )

        return r.json

    def alertActionDeleteAllAlerts(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/action/deleteAllAlerts/',
        )

        return r.json

    def alertActionDeleteAlert(self, **kwargs):

        params = {
            "id": kwargs.get("id")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/alert/action/deleteAlert/',
            params=params
        )

        return r.json
