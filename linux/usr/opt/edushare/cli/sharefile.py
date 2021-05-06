import socket, os, http.server, socketserver, webbrowser, sys
from conf import *
from gui import *
from time import sleep
from pyngrok import ngrok, conf

def banner():
	print("    _______  ______   __   __  _______  __   __  _______  ______    _______ ")
	print("   |       ||      | |  | |  ||       ||  | |  ||   _   ||    _ |  |       |")
	print("   |    ___||  _    ||  | |  ||  _____||  |_|  ||  |_|  ||   | ||  |    ___|")
	print("   |   |___ | | |   ||  |_|  || |_____ |       ||       ||   |_||_ |   |___ ")
	print("   |    ___|| |_|   ||       ||_____  ||       ||       ||    __  ||    ___|")
	print("   |   |___ |       ||       | _____| ||   _   ||   _   ||   |  | ||   |___ ")
	print("   |_______||______| |_______||_______||__| |__||__| |__||___|  |_||_______|\n")
	print(RED + """
		--- """,module_name,""" ---""")
	print(CYAN + """
	 Github: https://github.com/likapi
	  Documentation: https://likapi.github.io/docs""" + PURPLE + """
	   Instagram: @likapi.sh - Twitter: @likapi_sh
	 """)

def tunnels():
	global module_name
	module_name = "Liste des tunnels actifs (Ngrok)"
	banner()
	print(GREEN + f"""
	   {ngrok.get_ngrok_process()}
	""")

def send():
	ngrok.get_ngrok_process().stop_monitor_thread()
	global module_name
	module_name = "Partage de fichiers (Socket)"
	banner()
	if not os.path.exists("partage"):
 		os.makedirs("partage")
 		os.chmod("partage", 0o0777)
	print(YELLOW + """
	   Glissez vos fichiers à partager dans le dossier partage...""")
	sleep(2)
	webbrowser.open('partage')
	port = 8080
	web_dir = os.path.join(os.path.dirname(__file__), 'partage')
	os.chdir(web_dir)
	http_tunnel = ngrok.connect(port, bind_tls=True).public_url
	address = ("0.0.0.0", port)
	handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(address, handler)
	print(GREEN + f"""
	   Votre url de partage : {http_tunnel}
	    Est en attente de connexion d'un récepteur...
	""" + YELLOW)
	httpd.serve_forever()

def receive():
	global module_name
	module_name = "Réception de fichiers (Socket)"
	banner()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = input(END + str("""
	  Entrez l'url de partage : """))
	port = 8080
	if "ngrok.io" in host:
		print(GREEN + f"""
	   Vous êtes connecté à {host}...
		""")
		sleep(2)
		webbrowser.open(host)
		exit()
	else:
		print(RED + """
	   Url de partage invalide...
		""")
		sleep(2)
		clear()
		receive()