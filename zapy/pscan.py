
class pscan():
    def __init__(self, API):
        self.API = API

    def pscanViewScanOnlyInScope(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/view/scanOnlyInScope/',
        )

        return r.json

    def pscanViewRecordsToScan(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/view/recordsToScan/',
        )

        return r.json

    def pscanViewScanners(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/view/scanners/',
        )

        return r.json

    def pscanViewCurrentRule(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/view/currentRule/',
        )

        return r.json

    def pscanViewMaxAlertsPerRule(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/view/maxAlertsPerRule/',
        )

        return r.json

    def pscanActionSetEnabled(self, **kwargs):

        params = {
            "enabled": kwargs.get("enabled")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/setEnabled/',
            params=params
        )

        return r.json

    def pscanActionSetScanOnlyInScope(self, **kwargs):

        params = {
            "onlyInScope": kwargs.get("onlyInScope")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/setScanOnlyInScope/',
            params=params
        )

        return r.json

    def pscanActionEnableAllScanners(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/enableAllScanners/',
        )

        return r.json

    def pscanActionDisableAllScanners(self):

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/disableAllScanners/',
        )

        return r.json

    def pscanActionEnableScanners(self, **kwargs):

        params = {
            "ids": kwargs.get("ids")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/enableScanners/',
            params=params
        )

        return r.json

    def pscanActionDisableScanners(self, **kwargs):

        params = {
            "ids": kwargs.get("ids")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/disableScanners/',
            params=params
        )

        return r.json

    def pscanActionSetScannerAlertThreshold(self, **kwargs):

        params = {
            "id": kwargs.get("id"),
"alertThreshold": kwargs.get("alertThreshold")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/setScannerAlertThreshold/',
            params=params
        )

        return r.json

    def pscanActionSetMaxAlertsPerRule(self, **kwargs):

        params = {
            "maxAlerts": kwargs.get("maxAlerts")
        }

        r = self.API.HTTP.get(
            f'{self.API.url}/JSON/pscan/action/setMaxAlertsPerRule/',
            params=params
        )

        return r.json
