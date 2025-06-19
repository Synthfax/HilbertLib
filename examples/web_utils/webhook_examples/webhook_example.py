from hilbertlib.web_utils.webhook import Webhook

def example_webhook():
    # Use a testing webhook like https://webhook.site/ and put your URL here
    webhook_url = "https://webhook.site/your-unique-url"
    webhook = Webhook(webhook_url)
    data = {"event": "test", "message": "Hello from HilbertLib!"}
    response = webhook.send(data)
    print("Webhook response:", response)

# Uncomment to test with your actual webhook URL
# example_webhook()
