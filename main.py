import requests
import time
import process as p


if __name__ == "__main__":

	n = 0
	token = ""
	url = "https://api.telegram.org/bot%s/" %(token)

	commands = {"/order":p.order}


	while True:
		try:
			data = requests.get(url+"getUpdates", data={"offset":n}).json()
			print(data)
			if(data["result"]):
				n = data["result"][0]["update_id"] + 1
				username = data["result"][0]["message"]["from"]['username']
				chatid = data["result"][0]["message"]["chat"]["id"]
				message = p.clean(data["result"][0]["message"]["text"])
				p.sendMsg(url,commands[message[0]](message),chatid)			
			time.sleep(1)
		except KeyError:
			p.sendMsg(url,"Invalid command.",chatid)
		except:
			pass
