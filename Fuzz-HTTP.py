import requests as req
import sys


start=1
end=1000

# Only 0 through 1,114,111 (0x10FFFF in base 16) is supported by "chr".

url="http://127.0.0.1:8082/aFUZZb"
proxy={"http":"http://127.0.0.1:8080","https":"https://127.0.0.1:8080"}


global characters
characters=[]
def init():
	for index in range(start,end):
		characters.append(chr(index))


init()



for char in characters:
	sys.stdout.write("U+"+str(start)+"\n")
	sys.stdout.write("\033[F")
	sys.stdout.flush()
	start=start+1
	#response=req.get(url.replace("FUZZ",char),proxies=proxy) #Uncomment to apply proxy
	response=req.get(url.replace("FUZZ",char))

	status=response.status_code

	#Change as per your needs
	if status==200 and len(response.text)>=5:
		print("200 : "+char+" [U+"+str(start-1)+"]\n")
	
