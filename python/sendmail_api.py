import os, requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

with open("config.json") as json_file:
    config_data = json.load(json_file)
sendgrid_apikey = config_data['sendgrid_key']
custom_apikey = config_data['cachigo_key']


def sendgrid_send(to_email,message):
	message = Mail(
		from_email='Terminal One Client<sendgrid@pretendtobe.terminalone.com>',
		to_emails=to_email,
		subject='This is Terminal 1 assessment from Primay Email Server:SendGrid',
		html_content=message)
	try:
		sg = SendGridAPIClient(sendgrid_apikey)
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e.message)

          

def custom_send(to_email,message):
        requests.post(
        "https://send-mail-t1-php.herokuapp.com/custom_sent.php",
        data={"email": to_email,
              "message": message,
              "key": custom_apikey})
