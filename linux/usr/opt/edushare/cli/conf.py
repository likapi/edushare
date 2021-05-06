import os, datetime
from pyngrok import ngrok, conf
from colors import *

#config
now = datetime.datetime.now() #datetime get time
path = "/opt/edushare/cli/"

def ngrokverify():
	#ngrok conf persistent
	try:
		with open("data/lang.txt"):
			regconf = open("data/lang.txt", "r")
			conf.get_default().region = regconf.read()
			regconf.close()
	except IOError:
		conf.get_default().region = None #ngrok default region

	try:
		with open("data/token.txt"):
			authconf = open("data/token.txt", "r")
			conf.get_default().auth_token = authconf.read()
			authconf.close()
	except IOError:
		conf.get_default().auth_token = None #ngrok default authtoken

#pas encore dispo
def coming():
	print(GREEN + """
	   Bientôt disponible...
	 """)
	sleep(2)
	clear()
	main()
	
#clear console
def clear():
	_ = os.system('clear')

def close():
	print(GREEN + """
	   Fermeture du client EduShare...
		""")
	exit()