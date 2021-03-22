import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AZQiAqo_G8vygoAIT9tAL-Z6MQd49xERaY6a3N0ijCRXkubEyMnylsk1qjxNIFM2iAFomcSTfq4yW47O"
        self.client_secret = "EMrlopSA2IYTD_7_AHrvmmYqHp9CXHMr8zC1r00TOth3wZHvPaQcEuzW6FzW9PnqW3HP71YRT38mSgLu"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
