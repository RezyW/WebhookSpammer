import requests
import time

def send_message(webhook_url, message, delay, message_count):
    for _ in range(amount_of_messages):
        data = {'content': message}
        response = requests.post(webhook_url, json=data)


        time.sleep(delay)

webhook_url = "https://discord.com/api/webhooks/1197588154014769236/qXJmlZLUDAV6zIvWmi1p9dFjp3jok4e0bLV-7Kc9jaJmDqKxyoSqVRSmD3uXYxn3qUGI"
message = "RezyW is the best @everyone"
delay = 0 
amount_of_messages = 5  

send_message(webhook_url, message, delay, amount_of_messages)
