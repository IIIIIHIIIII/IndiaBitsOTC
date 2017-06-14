import requests


def clean(text):
	text = text.split(" ")
	for i in range(text.count(' ')):
		text.remove(' ')
	return text

def sendMsg(url,message,chatid):
    requests.get(url + "sendMessage", data={"chat_id":chatid,"text":message})

def order(message):
	if len(message) < 4 or message[1].lower() not in ["buy","sell"]:
		return "Correct syntax : /order [buy/sell] [amount] [coin_ticker]"

	try:
		float(message[2])
	except ValueError:
		return "%s is not a valid amount." %(message[2])

		
