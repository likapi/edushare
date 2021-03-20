#!/usr/bin/python3
import colorama, datetime, pyfiglet, socket, os
from os import system, name
from sys import platform as _platform
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
from pyngrok import ngrok

#config
colorama.init() #colorama init
font = Figlet(font='graffiti') #pyfiglet font
now = datetime.datetime.now() #datetime get time

def sys():
	if _platform == "linux" or _platform == "linux2":
		main()
	elif _platform == "darwin":
		print(Fore.GREEN + """
	Mac Os détecté, vous devez utiliser linux...
		""")
		close()
	elif _platform == "win32" or _platform == "win64":
		print(Fore.GREEN + """
	Windows détecté, vous devez utiliser linux...
		""")
		close()
	else:
		print(Fore.GREEN + """
	Impossible d'identifier le système d'exploitation...
		""")
		close()

def banner():
	banner = font.renderText("        EduShare")
	print(Fore.RED + banner + """
		--- """,module_name,""" ---""")
	print(Fore.CYAN + """
	 Github: https://github.com/likapi
	  Documentation: https://likapi.github.io/docs""" + Fore.MAGENTA + """
	   Instagram: @likapi.sh - Twitter: @likapi_sh
	 """)

def main():
	socket.socket().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	global module_name
	module_name = "Développé par Keany Vy KHUN"
	banner()
	print(Fore.YELLOW + """
     [1]. Partage     [2]. Réception     [3]. Compression
     [4]. Historique  [5]. Aide          [0]. Quitter 
		""")
	menu = input(Fore.WHITE + """
	  Entrez un numéro : """)
	if menu != "":
		if menu == "0":
			close()
		elif menu == "1":
			clear()
			send()
		elif menu == "2":
			clear()
			receive()
		else:
			print(Fore.GREEN + """
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
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	url = str(ngrok.connect(8080).public_url)
	url = url.replace("http://","")
	host = '0.0.0.0'
	port = 8080
	s.bind((host,port))
	s.listen(1)
	print(Fore.YELLOW + f"""
	   Votre pc : {url}
	    Est en attente de connexion d'un récepteur...""")
	conn, addr = s.accept()
	print(Fore.GREEN + f"""
	   {addr} est connecté en tant que récepteur""")
	filename = input(Fore.WHITE + """
	  Entrez le chemin du fichier à partager : """)
	try:
		file = open(filename, 'rb')
		file_data = file.read(1024)
		conn.send(file_data)
		file.close()
		print(Fore.GREEN + """
	   Réception du fichier avec succès
		""")
	except:
		print(Fore.RED + f"""
	   Le fichier {filename} est introuvable...
        	""")
		sleep(2)
		exit()

def receive():
	global module_name
	module_name = "Réception de fichiers (Socket)"
	banner()
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = input(Fore.WHITE + """
	  Entrez le nom de l'envoyeur : """)
	port = 8080
	s.connect((host,port))
	print(Fore.GREEN + f"""
	   Vous êtes connecté à {host}...""")
	filename = "receveid_txt.txt"
	file = open(filename, "wb")
	file_data = s.recv(1024)
	if len(file_data) == 0:
		print(Fore.RED + """
       L'envoyeur s'est déconnecté...
    	""")
		file.close()
		os.remove(filename)
		sleep(2)
		exit()
	else:
		file.write(file_data)
		file.close()
		print(Fore.GREEN + f"""
	   Fichier {filename} reçu avec succès
	  	""")

def coming():
	print(Fore.GREEN + """
	   Bientôt disponible...
	 """)
	sleep(2)
	clear()
	main()


def close():
	print(Fore.GREEN + """
	   Fermeture du client EduShare...
		""")
	exit()

def clear():
	#clear la console
	_ = system('clear') 

if __name__ == "__main__":
	clear()
	sys()