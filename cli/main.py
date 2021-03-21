#!/usr/bin/python3
import colorama, datetime, pyfiglet, socket, os, zipfile
from os import system, name
from sys import platform as _platform
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
from pyngrok import ngrok, conf

#config
colorama.init() #colorama init
font = Figlet(font='graffiti') #pyfiglet font
now = datetime.datetime.now() #datetime get time
#ngrok conf persistent
try:
	with open("lang.txt"):
		regconf = open("lang.txt", "r")
		conf.get_default().region = regconf.read()
		regconf.close()
except IOError:
	conf.get_default().region = None #ngrok default region

try:
	with open("token.txt"):
		authconf = open("token.txt", "r")
		conf.get_default().auth_token = authconf.read()
		authconf.close()
except IOError:
	conf.get_default().auth_token = None #ngrok default authtoken

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
     [4]. Tunnels     [5]. Région        [6]. AuthToken
     [7]. Historique  [8]. Aide          [0]. Quitter 
		""")
	menu = input(Fore.WHITE + str("""
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
	filename = input(Fore.WHITE + str("""
	  Entrez le chemin du fichier à partager : """))
	try:
 		with open(filename): pass
	except IOError:
		print(Fore.RED + f"""
	   Le fichier {filename} est introuvable...
        """)
		sleep(2)
		clear()
		send()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = '0.0.0.0'
	port = 8080
	s.bind((host,port))
	s.listen(1)
	url = ngrok.connect(port, "tcp").public_url
	url = str(url).replace("tcp://", "")
	print(Fore.YELLOW + f"""
	   Votre url de partage : {url}
	    Est en attente de connexion d'un récepteur...""")
	while True:
		conn, addr = s.accept()
		print(Fore.GREEN + f"""
	   {addr} est connecté en tant que récepteur""")
		try:
			file = open(filename, 'rb')
			octets = os.path.getsize(filename)
			print(octets)
			file_data = file.read(1024 * 1024)
			file_data = file_data.decode()
			filename = os.path.basename(filename)
			datafinal = bytes(f"{filename}:{file_data}", 'utf-8')
			conn.send(datafinal)
			file.close()
			print(Fore.GREEN + f"""
	   Réception du fichier avec succès pour {addr}""")
			print(Fore.YELLOW + """
	   En attente d'un autre récepteur...""")
		except:
			print(Fore.RED + f"""
	   Le fichier {filename} est introuvable...
        	""")
			sleep(2)
			s.close()
			break
			exit()

def receive():
	global module_name
	module_name = "Réception de fichiers (Socket)"
	banner()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = input(Fore.WHITE + str("""
	  Entrez l'url de partage de l'envoyeur : """))
	port = 8080
	if ":" in host:
		ngrok = host.split(":")
		host = str(ngrok[0])
		port = int(ngrok[1])
	s.connect((host,port))
	print(Fore.GREEN + f"""
	   Vous êtes connecté à {host}...""")
	file_data = s.recv(1024 * 1024)
	separate = file_data.decode()
	title = separate.split(":")
	filename = str(title[0])
	deletetitle = str(f"{filename}:")
	file = open(filename, "wb")
	if len(file_data.decode()) == 0:
		print(Fore.RED + """
	   L'envoyeur s'est déconnecté...
    	""")
		file.close()
		os.remove(filename)
		sleep(2)
		s.close()
		exit()
	else:
		file_data = file_data.decode()
		file_data = file_data.replace(deletetitle, "")
		file_data = file_data.encode()
		file.write(file_data)
		file.close()
		print(Fore.GREEN + f"""
	   Fichier {filename} reçu avec succès
	  	""")
		s.close()
		exit()

def tunnels():
	global module_name
	module_name = "Liste des tunnels actifs (Ngrok)"
	banner()
	print(Fore.GREEN + f"""
	   {ngrok.get_ngrok_process()}
	""")

def region():
	global module_name
	module_name = "Région par défaut (Ngrok)"
	banner()
	if conf.get_default().region != None:
		print(Fore.YELLOW + f"""
	   Région par défaut : {conf.get_default().region}
	   """)
	conf.get_default().region = input(Fore.WHITE + str("""
	  Entrez une région (ISO-3166) : """))
	if conf.get_default().region != "":
		reg = open("lang.txt", "w")
		reg.write(conf.get_default().region)
		reg.close()
		print(Fore.GREEN + f"""
	   La langue {conf.get_default().region} a été définie avec succès
		""")
		exit()
	else:
		conf.get_default().region = None
		print(Fore.RED + f"""
	   Entrez une valeur pour l'AuthToken...
		""")
		sleep(2)
		clear()
		region()

def compress():
	global module_name
	module_name = "Compression de fichiers (Zip)"
	banner()
	filezip = input(Fore.WHITE + str("""
	  Entrez le nom du fichier zip : """))
	if ".zip" in filezip:
		zip = zipfile.ZipFile(filezip, 'w')
		filename = input(Fore.WHITE + str("""
	  Entrez le chemin des fichiers à compresser : """))
		try:
			zip.write(filename)
			zip.close()
			print(Fore.GREEN + f"""
	   Compression des fichiers avec succès
	   		""")
		except:
			print(Fore.RED + f"""
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
		filename = input(Fore.WHITE + str("""
	  Entrez le chemin des fichiers à compresser : """))
		try:
			zip.write(filename)
			zip.close()
			print(Fore.GREEN + f"""
	   Compression des fichiers avec succès
	   		""")
		except:
			print(Fore.RED + f"""
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
	print(Fore.YELLOW + """
	   AuthToken sur : https://dashboard.ngrok.com/signup
	""")
	if conf.get_default().auth_token != None:
		print(Fore.YELLOW + f"""
	   AuthToken par défaut : {conf.get_default().auth_token}
	   """)
	conf.get_default().auth_token = input(Fore.WHITE + str("""
	  Entrez un nouveau AuthToken : """))
	if conf.get_default().auth_token != "":
		auth = open("token.txt", "w")
		auth.write(conf.get_default().auth_token)
		auth.close()
		print(Fore.GREEN + f"""
	   L'AuthToken {conf.get_default().auth_token} a été défini avec succès
		""")
		exit()
	else:
		conf.get_default().auth_token = None
		print(Fore.RED + f"""
	   Entrez une valeur pour l'AuthToken...
		""")
		sleep(2)
		clear()
		authtoken()

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