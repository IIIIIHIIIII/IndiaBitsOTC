import requests
import time


if __name__ == "__main__":

	n = 0
	token = ""
	url = "https://api.telegram.org/bot%s/" %(token)

	while True:
		try:
			data = requests.get(url+"getUpdates", data={"offset":n}).json()
			if(data["result"]):
				n = data["result"][0]["update_id"] + 1
				username = data["result"][0]["message"]["from"]['username']
				chatid = data["result"][0]["message"]["chat"]["id"]
				message = data["result"][0]["message"]["text"]
			time.sleep(1)
		except:
			pass
