import os
import time
import sys
Naranja='\033[38;5;214m'
Rosa='\033[38;5;213m'
Rojo='\033[1;31m'
Verde='\033[1;32m'
Amarillo='\033[33m'
Azul_claro='\033[38;5;39m'
Azul='\033[34m'
Morado='\033[35m'
Blanco='\033[1;37m'
Cyan='\033[1;36m'
os.system('clear')
###############
def sistema():
	sis=input('>> '+Blanco)
	if sis == '1':
		#kali
		os.system('pkg install wget -y openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
	elif sis == '2':
		#ubuntu
		os.system('pkg install wget -y openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh')
	elif sis == '3':
		os.system('pkg install wget -y openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh')
	elif sis == '4':
		os.system('pkg install wget -y openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh')
	elif sis == '5':
		os.system('pkg install wget -y openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh')
	else:
		print()
##################
def efecto(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0/125)

############
def meta():
	print()
	print(Cyan+'[1] ANDROID 5.0/6.0')
	print(Cyan+'[2] ANDROID 7.0')
	print()
	met=input(Rojo+'VERSION >> '+Blanco)
	if met == '1':
		os.system('bash /data/data/com.termux/files/usr/etc/Metasploit-Android/Metasploit-Android.sh')
	elif met == '2':
		os.system('bash /data/data/com.termux/files/usr/etc/Termux-Metasploit/Termux-Metasploit.sh')
#############
print ()
print (Cyan+"      Akatsuki - Security")
print (Rojo+"-------------------------------")
print (Cyan+"[1] SISTEMAS OPERATIVOS        ")
print (Rojo+"-------------------------------")
print (Rojo+"-------------------------------")
print (Cyan+"[2] INSTALACION DE NGROK       ")
print (Rojo+"-------------------------------")
print (Rojo+"-------------------------------")
print (Cyan+"[3] INSTALACION DE METASPLOIT  ")
print (Rojo+"-------------------------------")
print (Rojo+"-------------------------------")
print (Cyan+"[4] INSTALACION DE PACK-CARDING")
print (Rojo+"-------------------------------")
print (Rojo+"-------------------------------")
print (Cyan+"[5] INSTALACION DE PACK-BOTS   ")
print (Rojo+"-------------------------------")
print()
x=input(Rojo+'>> '+Blanco)
if x == '1':
	os.system('clear')
	print()
	efecto(Rojo+"-------------------------------")
	efecto(Cyan+"[1]        KALI LINUX          ")
	efecto(Rojo+"-------------------------------")
	efecto(Rojo+"-------------------------------")
	efecto(Cyan+"[2]          UBUNTU            ")
	efecto(Rojo+"-------------------------------")
	efecto(Rojo+"-------------------------------")
	efecto(Cyan+"[3]         ARCH LINUX         ")
	efecto(Rojo+"-------------------------------")
	efecto(Rojo+"-------------------------------")
	efecto(Cyan+"[4]          DEBIAN            ")
	efecto(Rojo+"-------------------------------")
	efecto(Rojo+"-------------------------------")
	efecto(Cyan+"[5]       KALI NETHUNTER       ")
	efecto(Rojo+"-------------------------------")
	sistema()
elif x == '3':
	meta()
else:
	print()
print()

