import requests
import time
import sys
from time import gmtime, strftime
from sys import exit

"""cic.py: Search IP malicious in malwareworld site api."""
__author__      = "Kelvem Sousa - k4m3"
__copyright__   = "Copyright 2019"

hora = strftime("%H-%M-%S")

print("\033[94m CIC - Search IP and Domain Intelligence \033[00m")
#print("\033[91m"+line.rstrip('\n')+ " - Malicious"+"\033[00m")


if len(sys.argv) != 2:
        print ("Modo de usar: \r\n")
        print ("python3 "+sys.argv[0]+" lista_ips.txt \r\n")
        exit();

with open(sys.argv[1]) as file:
        for line in file:
                API_ENDPOINT = "https://malwareworld.com/api/check"
                data = {"host":line.rstrip('\n')}
                r = requests.post(url = API_ENDPOINT, data = data)
                malwareworld = r.json()
                time.sleep(2)
                result = malwareworld ["malicious"]
                if result == True:
                    print(line.rstrip('\n'), file=open("malicioso."+hora, "a"))
                    print("\033[91m"+line.rstrip('\n')+ " - Malicious"+"\033[00m")

#               As linhas abaixo imprime na tela os ips que nao sao maliciosos,
#               para ativar, basta descomentar.

                else:
                    print("\033[92m"+line.rstrip('\n')+ " - Clean"+"\033[00m")
                    print(line.rstrip('\n'), file=open("nao_malicioso."+hora, "a"))
        file.close()

print("\033[95m Fim do Scan \033[00m")
print("Lista de IP's maliciosos     ==> \033[91m malicioso."+hora+"\033[00m")
print("Lista de IP's nao maliciosos ==> \033[92m nao_malicioso."+hora+"\033[00m")
