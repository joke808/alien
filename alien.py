import time
import os
from platform import system

R = "\033[31m"
B = "\033[34m"
V = "\033[32m"
T = "\033[39m"

#colores

("\x1b[1;33m")


print("▄▀█ █░░ █ █▀▀ █▄░█")
print("█▀█ █▄▄ █ ██▄ █░▀█")

print(V+"                  Disfruta Esta Herramienta:3")
print(T+"           https://github.com/joke808")
print("                           [✓] Listo Para Instalar")
print(R+" ")



print("1:Metasploit - 2:Sqlmap - 3:Sandmap - 4:Slowris ")
print(" ")
print("5:nikto")


print(T+" ")
preg=int(input(V+"Que Script Quieres Ejecutar? "))


#herramientas

if preg == 1:
    os.system( 'clear')
    time.sleep(1.5)
    print("Metasploit Se Esta Instalando")
    time.sleep(1.5)
    os.system( 'clear' )
    os.system( 'wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh' )
    os.system( 'chmod +x metasploit.sh' )
    os.system( 'bash ./metasploit.sh' )
    
elif preg == 2:
    os.system( 'clear' )
    time.sleep(1.5)
    print("Sqlmap Se Esta Instalando")
    time.sleep(1.5)
    os.system( 'clear' )
    os.system( 'git clone https://github.com/sqlmapproject/sqlmap' )


elif preg == 3:
	os.system('clear')
	time.sleep(1.5)
os.system('clear')

os.system('git clone --recursive https://github.com/trimstray/sandmap')

os.system('cd sandmap')


os.system('./setup.sh install')

os.system('sandmap')

if preg == 4:
	
	os.system('clear')
	time.sleep(1.5)
	os.system('clear')
	
	os.system('git clone https://github.com/gkbrk/slowloris.git')
		
os.system('cd slowloris')

os.system('python3 slowloris.py example.com')

if preg == 5:	
	os.system('clear')
	time.sleep('1.5')
	os.system('clear')
	
	os.system('git clone https://github.com/sullo/nikto')
	
os.system('cd nikto/program')

os.system('./nikto.pl -h http://www.example.com')

os.system('perl nikto.pl -h http://www.example.com')
