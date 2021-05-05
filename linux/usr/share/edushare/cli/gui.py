#!/usr/bin/python3
import datetime, socket, os, zipfile, http.server, socketserver, webbrowser, sys
from conf import *
from colors import *
from time import sleep
from pyngrok import ngrok, conf

#config
now = datetime.datetime.now() #datetime get time
path = "/usr/share/edushare/cli/"

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

def main():
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=23, cols=79))
	ngrokverify()
	clear()
	socket.socket().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	global module_name
	module_name = "Développé par Keany Vy KHUN"
	banner()
	print(YELLOW + """
      [1]. Partage     [2]. Réception     [3]. Compression
      [4]. Tunnels     [5]. Région        [6]. AuthToken
      [7]. Historique  [8]. Aide          [0]. Quitter
		""")
	menu = input(END + str("""
	  Entrez un numéro : """))
	if menu != "":
		if menu == "0":
			close()
		elif menu == "1":
			clear()
			send()
		elif menu == "2":
			clear()
			receive()
		elif menu == "3":
			clear()
			compress()
		elif menu == "4":
			clear()
			tunnels()
		elif menu == "5":
			clear()
			region()
		elif menu == "6":
			clear()
			authtoken()
		else:
			print(GREEN + """
	  Nombre invalide
			""")
			sleep(2)
			clear()
			main()

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

def tunnels():
	global module_name
	module_name = "Liste des tunnels actifs (Ngrok)"
	banner()
	print(GREEN + f"""
	   {ngrok.get_ngrok_process()}
	""")

def region():
	global module_name
	module_name = "Région par défaut (Ngrok)"
	banner()
	if conf.get_default().region != None:
		print(YELLOW + f"""
	   Région par défaut : {conf.get_default().region}
	   """)
	conf.get_default().region = input(END + str("""
	  Entrez une région (ISO-3166) : """))
	if conf.get_default().region != "":
		if not os.path.exists("data"):
 			os.makedirs("data")
 			os.chmod("data", 0o0777)
		reg = open("lang.txt", "w")
		reg.write(conf.get_default().region)
		reg.close()
		print(GREEN + f"""
	   La langue {conf.get_default().region} a été définie avec succès
		""")
		exit()
	else:
		conf.get_default().region = None
		print(RED + """
	   Entrez une valeur pour l'AuthToken...
		""")
		sleep(2)
		clear()
		region()

def compress():
	global module_name
	module_name = "Compression de fichiers (Zip)"
	banner()
	filezip = input(END + str("""
	  Entrez le nom du fichier zip : """))
	if ".zip" in filezip:
		zip = zipfile.ZipFile(filezip, 'w')
		filename = input(END + str("""
	  Entrez le chemin des fichiers à compresser : """))
		try:
			zip.write(filename)
			zip.close()
			print(GREEN + f"""
	   Compression des fichiers avec succès
	   		""")
		except:
			print(RED + f"""
	   Le fichier {filename} est introuvable...
        	""")
			sleep(2)
			zip.close()
			os.remove(filezip)
			clear()
			compress()
	else:
		filezip = str(f"{filezip}.zip")
		zip = zipfile.ZipFile(filezip, 'w')
		filename = input(END + str("""
	  Entrez le chemin des fichiers à compresser : """))
		try:
			zip.write(filename)
			zip.close()
			print(GREEN + f"""
	   Compression des fichiers avec succès
	   		""")
		except:
			print(RED + f"""
	   Le fichier {filename} est introuvable...
        	""")
			sleep(2)
			zip.close()
			os.remove(filezip)
			clear()
			compress()

def authtoken():
	global module_name
	module_name = "AuthToken par défaut (Ngrok)"
	banner()
	print(YELLOW + """
	   AuthToken sur : https://dashboard.ngrok.com/signup
	""")
	if conf.get_default().auth_token != None:
		print(YELLOW + f"""
	   AuthToken par défaut : {conf.get_default().auth_token}
	   """)
	conf.get_default().auth_token = input(END + str("""
	  Entrez un nouveau AuthToken : """))
	if conf.get_default().auth_token != "":
		if not os.path.exists("data"):
 			os.makedirs("data")
 			os.chmod("data", 0o0777)
		auth = open("data/token.txt", "w")
		auth.write(conf.get_default().auth_token)
		auth.close()
		print(GREEN + f"""
	   L'AuthToken {conf.get_default().auth_token} a été défini avec succès
		""")
		exit()
	else:
		conf.get_default().auth_token = None
		print(RED + f"""
	   Entrez une valeur pour l'AuthToken...
		""")
		sleep(2)
		clear()
		authtoken()