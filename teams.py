import pymsteams

myTeamsMessage = pymsteams.connectorcard("https://verisure.webhook.office.com/webhookb2/732ea580-3734-4c8f-8baf-1134c9d39d57@3055fa7f-a944-4927-801e-a62b63119e43/IncomingWebhook/80a6748c459149f0a36b15a71ff57118/c66d18de-3921-46fb-8c72-01691767c3b0")
myTeamsMessage.text("this is a test")
myTeamsMessage.send()
