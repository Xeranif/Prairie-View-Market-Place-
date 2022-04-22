import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AUGKHhzS1AWcChcyc2BPGJ0fhfJWgdjLNZlzdp7dZuqx-Fk-_J6AZ2lr4GwJg8VyIXLhRuri0Q5o9IwW"
        self.client_secret = "EGl7zmckNMmWhBy08Ybdf3mS7ltyY1uDT16UDS5yVG7Lm_2_OqmTT6wRy3hAUJ9Clv9OchoCYwzKBw79"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
