import time
import os

def main_menu():
	print("\n\n\n\n     __________________     ")
	time.sleep (0.04)
	print("    /                  \    ")
	time.sleep (0.04)
	print("    | Sisteme Girdiniz |    ")
	time.sleep (0.04)
	print("    \__________________/    ")
	time.sleep (1)
	
def top_menu() :
	print ("###############################################################")
	print ("#      MObil                   ",time.asctime(),"     #")
	print ("###############################################################")

os_name = os.name
if os_name == 'posix' :
	os_clean = "clear"

def copadam_dansi() :
	time.sleep (2.5)
	print("\n\n\n\n\n   O ")
	print("  /|\ ")
	print(" / | \ ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n   O")
	print(" _/|\_ ")
	print("   | ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n___O___")
	print("   |")
	print("   | ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n   O")
	print(" _/|\_ ")
	print("   | ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n   O")
	print("  /|\ ")
	print(" / | \ ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	
	
menu1 = 1
menu11 = 11
menuC = 111
menu2 = 2
sifre = 123
cikis = 0

while True:
	os.system(os_clean)
	top_menu()
	sifre=input("\n\n\n\n\nŞifreyi gir\n>")
	if sifre=="123":
		break
	
while True :
	os.system(os_clean)
	top_menu()
	main_menu()
	
	menu1 = input("\n\nMasaüstü: 1:Bilgisayarım, 2:Oyunlar, 3:Pir'i, 4:Sistemi Kapat\n")
	
	if menu1 == "1" :
		print("--Bilgisayarım--")
		print("")
		time.sleep (1.5)
		print("1:Yerel Disk C")
		print("2:Yerel Disk D")
		menu11 = input("")
		
		while menu11 == "1":
			print("System 32.dll")
			print("")
			print("1:Sil 2:geri dön")
			menuC = input("")
			if menuC == "2" :
				break
			if menuC == "1":
				print("Erişim Engellendi")
				

	elif menu1 == "2" :
	
		print("--Oyunlar--")
		time.sleep (1.5)
		print("")
		print("1:Counter Strayk")
		print("2:Cop Adam.Avi")
		menu2 = input("")
		
		while menu2 == "2" :
			copadam_dansi()
			break
		while menu2 == "1" :
			top_menu()
			os.system(os_clean)
			print("\n\n/////////////////////////////")
			print("//     ////////////      ////")
			print("/ ////////////////  /////////")
			print("/ ////////////////      /////")
			print("/ ////////////////////  /////")
			print("/     ////////////      /////")
			print("/////////////////////////////")
			print("/Version 1.6/////////////////")
			print("/////////////////////////////")
			print("/////////////////////////////")
			print("/////////////////////////////")
			print("///OYNAMAK İÇİN 1'E BASIN////")
			print("/////////////////////////////")
			print("/////////////////////////////")
			print("/////////////////////////////")
			cs = input("")
			if cs == "1":
				top_menu()
				os.system(os_clean)
				print("\n\n\n\n\n\n")
				print(" _____________________  ")
				print("/ERROR:_______________\ ")
				print("|64BIT SYSTEM REQUIRED| ")
				print("|---SYSTEM  RESTART---| ")
				print("\_____________________/ ")
				time.sleep(2.5)
			else:
				os.system(os_clean)
				print("/////////////////////////////////////////////////////////////////////////////")
				print("//Bir hata meydana geldi :(//////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("///////////error:////////////////////////////////////////////////////////////")
				print("/////////////////QUICKSHUTDOWN://////////////////////////////////////////////")
				print("///////////////////////////////err:GreenScreen///////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("///////////////////////////////////////////////////////////////////// ///////")
				print("///////////////////////////////////////////////////////    //////// /////////")
				print("////////////////////////////////////////////////////////////////// //////////")
				print("////////////////////////////////////////////////////////////////// //////////")
				print("///////////////////////////////////////////////////////    //////// /////////")
				print("//////////////////////////////////////////////////////////////////// ////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				print("/////////////////////////////////////////////////////////////////////////////")
				time.sleep(5)
			break
			
	
	
	elif menu1 == "3" :
		top_menu()
		os.system(os_clean)
		soru = 1
		print("\n\n\n\n\n\n")
		print("PPPPP    İİ     RRRRR   ''   İİ")
		print("P   P           R    R ''      ")
		print("PPPP     İİ     RRRRR        İİ")
		print("P        İİ     RRR          İİ")
		print("P        İİ     R  RR        İİ")
		time.sleep(1)
		print("Hoş Geldiniz Pirim")
		time.sleep(0.5)
		print("Bana bir soru sorun. eğer soruların ne olduğunu bilmiyorsanız 'soru' yazın")
		soru = input("")
		if soru == "soru" :
			print("kaç yaşındasın, adın ne, kapat")
			time.sleep(1)
		
		
	
	elif menu1 == "4" :
	
		print("     __________________     ")
		time.sleep (0.04)
		print("    /                  \    ")
		time.sleep (0.04)
		print("    |    Görüşürüz     |    ")
		time.sleep (0.04)
		print("    \__________________/    ")
		time.sleep (1)
		cikis = 1
		break

if cikis == 1 :
	os.system("quit()")
