#!bin/bash
g="${b}\033[1;30m"
b="\033[0m"
b1="$b\033[1;37m"
r="${b}\033[1;31m"
r1="${b}\033[31m"
A="${b}\033[1;34m"
A1="${b}\033[34m"
ac="${b}\e[1;36m"
ac1="${b}\e[36m"
v="${b}\033[1;32m"
v1="${b}\033[32m"
m="$b\033[1;35m"
m1="$b\033[35m"
a="$b\033[1;33m"
a1="$b\033[33m"
cy="$b\033[38;2;23;147;209m"
#joker_808
       
pkg update
clear		
echo -e "$v[+]${cy}upgrade"
pkg upgrade
clear			
termux-setup-storage
clear		
echo -e "$v[+]${cy}wget"
pkg install wget
clear			
echo -e "$v[+]${cy}python"
pkg install python
clear			
echo -e "$v[+]${cy}python2"
pkg install python2
clear			
echo -e "$v[+]${cy}python3"
pkg install python3
clear	
echo -e "$v[+]${cy}w3m"
pkg install w3m
clear		
echo -e "$v[+]${cy}pip"
pkg install pip
clear		
echo -e "$v[+]${cy}pip2"
pkg install pip2
clear		
echo -e "$v[+]${cy}ruby"
pkg install ruby
clear		
echo -e "$v[+]${cy}perl"
pkg install perl
clear			
echo -e "$v[+]${cy}mechanize"
pip install mechanize
clear			
echo -e "$v[+]${cy}colorama"
pip install colorama
clear
sleep 2
clear
python alien.py