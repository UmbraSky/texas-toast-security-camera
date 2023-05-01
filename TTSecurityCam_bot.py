# TTSecurityCam_Bot for Telegram

# Telegram bot to send notifications to Telegram account for detections

import requests

url = "https://v1.nocodeapi.com/teamtexastoast/telegram/bSlqudcGMeSmSmRt/sendText?text=!!! ALERT ALERT!!! SOMETHING SPOTTED ON CAMERA"
params = {}
r = requests.post(url = url, params = params)
result = r.json()
print(result)
