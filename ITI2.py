import requests,os,re,sys,random,subprocess,json,time
from datetime import datetime
from time import strftime
from rich.panel import Panel as panel
from rich.console import Console
from rich.text import Text
from rich.progress import track
from rich.columns import Columns
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
import halo

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

warna = ['[#FF0000]','[#00FF00]','[#00C8FF]','[#AF00FF]','[#FF00FF]','[#00FFFF]','[#FFFFFF]','[#FF8F00]','[#AAAAAA]']
for i in range(10):
    jadi_aungthor = random.choice(warna)
numList = [1000, 2350, 2222, 3415, 1217, 1897, 1999, 2024, 2026, 2030]
for i in range(11):
    bil = random.choice(numList)
menuju = ['https://www.facebook.com/Dailylemons','https://instagram.com/mask_private1457?igshid=OGY3MTU3OGY1Mw==','https://wa.link/xd1tqg','mailto:hubungikami123456@gmail.com']
for i in range(4):
	lubanghidung = random.choice(menuju)
			
def clear():
	os.system('clear')
def Baris_Baru():
	print('\n')
def LoadingTime():
	time.sleep(0.10)
def LoadingTime2():
	time.sleep(0.05)

def logo_bapakkau():
	cetak(panel(f"""{jadi_aungthor}\t\t\t        _____________________  _________
{jadi_aungthor}\t\t\t        \__    ___/\______   \/   _____/
{jadi_aungthor}\t\t\t          |    |    |     ___/\_____  \ 
{jadi_aungthor}\t\t\t          |    |    |    |    /        \
{jadi_aungthor}
{jadi_aungthor}\t\t\t          |____|    |____|   /_______  /
{jadi_aungthor}\t\t\t                                     \/ 
\t\t\t             {K2}Termux {H2}Plugin {P2}Support""",width=100,title=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}BANNER {H2}▪︎{K2}▪︎{M2}▪︎",title_align='center',style=f"bold green"))
    
class Menu_Makan_Bapak_Mu:
	def __init__(self):
		self. Menu_Utama_Ibu_Mu()
	def Menu_Utama_Ibu_Mu(self):
		try:
			clear()
			logo_bapakkau()
			self.GetDeviceUserInfo()
			cetak(panel(f"       {K2}[{H2}01{K2}] INSTALL FULL TERMUX INTERIOR                    {K2}[{H2}03{K2}] INSTALL TERMUX SUPPORT\n       {K2}[{H2}02{K2}] INSTALL SOME TERMUX                             {K2}[{H2}04{K2}] INSTALL ALL TERMUX",width=100,title_align='center',title=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}MENU {H2}▪︎{K2}▪︎{M2}▪︎",style="bold green"))
			os.popen("play-audio WELCOMEBELL.mp3")
			Input_Makanan = input('\33[m[\x1b[1;92m?\33[m] PILIH > \x1b[1;92m')
			if Input_Makanan in ['01','1','INSTALL FULL TERMUX INTERIOR']:
				try:
					spinner = halo.Halo(text='Currently Installing...', spinner='dots')
					spinner.start()
					
					clear();Baris_Baru()
					cetak(panel(f"{K2}\t\t\t         SEDANG MENGINSTAL DALAMAN TERMUX",width=100,style="bold green"))
					os.system('pkg install php -y && pkg install python -y && pkg install mc -y && pkg install figlet -y && pkg install screenfetch -y && pkg install neofetch -y && pkg install toilet -y && pip install colorama && pip install stdiomask && pip install bs4 && pip install rich && pip install instaloader && pip install yt_dlp && pip install pyqrcode && apt install python make wget termux-exec clang libjpeg-turbo freetype -y && env INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow && pip install prompt_toolkit && pip install email_validator && pip install googlesearch_python && pip install pypng && pip install pytz && pkg install mpv -y && pip install removebg && pip install tqdm && pip install pycryptodome && pip install requests && pip install mechanize && pip install halo')
					
					spinner.stop()
					cetak(panel(f"{K2}\t\t\t        BERHASIL MENGINSTAL DALAMAN TERMUX",width=100,title_align='center',title=f"{P2}[ {K2}DONE ! {P2}]",style="bold green"))
					Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
					if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
						Menu_Makan_Bapak_Mu()
					elif Jangan_Lupa in ['n','no','N','NO']:
						os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
						for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2()
						exit()
					else:
						os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
				except requests.exceptions.ConnectionError:
					os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
				except Exception as e:
					os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
			elif Input_Makanan in ['02','2','INSTALL SOME TERMUX']:
				try:
					spinner = halo.Halo(text='Currently Installing...', spinner='dots')
					spinner.start()
					
					clear();Baris_Baru()
					cetak(panel(f"{K2}\t\t\t         SEDANG MENGINSTAL SEBAGIAN TERMUX",width=100,style="bold green"))
					os.system('pkg install php -y && pkg install python -y && pkg install mc -y && pkg install figlet -y && pkg install screenfetch -y && pkg install neofetch -y && pip install colorama && pip install stdiomask && pip install bs4 && pip install rich && apt install python make wget termux-exec clang libjpeg-turbo freetype -y && env INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow && pip install pytz && pkg install mpv && pip install tqdm && pip install pycryptodome && pip install requests && pip install mechanize && pip install halo')
					
					spinner.stop()
					cetak(panel(f"{K2}\t\t\t        BERHASIL MENGINSTAL SEBAGIAN TERMUX",width=100,title_align='center',title=f"{P2}[ {K2}DONE ! {P2}]",style="bold green"))
					Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
					if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
						Menu_Makan_Bapak_Mu()
					elif Jangan_Lupa in ['n','no','N','NO']:
						os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
						for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2()
						exit()
					else:
						os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
				except requests.exceptions.ConnectionError:
					os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
				except Exception as e:
					os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
			elif Input_Makanan in ['03','3','INSTALL TERMUX SUPPORT']:
				try:
					spinner = halo.Halo(text='Currently Installing...', spinner='dots')
					spinner.start()
					
					clear();Baris_Baru()
					cetak(panel(f"{K2}\t\t\t         SEDANG MENGINSTAL TERMUX SUPPORT",width=100,style="bold green"))
					os.system('pkg install nano -y && pkg install vim -y && pkg install inetutils -y && pkg install python -y && pkg install php -y && pkg install python-pip -y && pkg install git -y && pkg install nodejs -y')
					
					spinner.stop()
					cetak(panel(f"{K2}\t\t\t        BERHASIL MENGINSTAL TERMUX SUPPORT",width=100,title_align='center',title=f"{P2}[ {K2}DONE ! {P2}]",style="bold green"))
					Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
					if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
						Menu_Makan_Bapak_Mu()
					elif Jangan_Lupa in ['n','no','N','NO']:
						os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
						for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2()
						exit()
					else:
						os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
				except requests.exceptions.ConnectionError:
					os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
				except Exception as e:
					os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
			elif Input_Makanan in ['04','4','INSTALL ALL TERMUX']:
				try:
					cetak(panel(f"     {K2}[{H2}01{K2}] INSTALL ALL TERMUX ANDROID {P2}[{H2}6 +{P2}]            {K2}[{H2}02{K2}] INSTALL ALL TERMUX ANDROID {P2}[{H2}5 +{P2}]",width=100,style="bold green"))
					awokawok = input('\33[m[\x1b[1;92m?\33[m] PILIH > \x1b[1;92m')
					if awokawok in ['01','1']:
						self.blokade1()
					elif awokawok in ['02','2']:
						self.blokade2()
					else:
						os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
				except requests.exceptions.ConnectionError:
					os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
				except Exception as e:
					os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
			elif Input_Makanan in [f'{bil}']:
				try:
					print("\33[m[\x1b[1;92m!\33[m] MENUJU \x1b[1;92mSOSIAL MEDIA \33[mADMIN SCRIPT...")
					time.sleep(3)
					animation = [f"\x1b[1;92m[\x1b[1;91m■\x1b[1;910m□□□□□□□□□\x1b[1;92m]",f"\x1b[1;92m[\x1b[1;92m■■\x1b[1;99m□□□□□□□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;93m■■■\x1b[1;98m□□□□□□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;94m■■■■\x1b[1;97m□□□□□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;95m■■■■■\x1b[1;96m□□□□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;96m■■■■■■\x1b[1;95m□□□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;97m■■■■■■■\x1b[1;94m□□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;98m■■■■■■■■\x1b[1;93m□□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;99m■■■■■■■■■\x1b[1;92m□\x1b[1;92m]", f"\x1b[1;92m[\x1b[1;910m■■■■■■■■■■\x1b[1;91m\x1b[1;92m]"]
					for i in range(20):
						time.sleep(0.1)
						sys.stdout.write("\r\33[m[\x1b[1;92m+\33[m] LOADING " + animation[i % len(animation)])
						sys.stdout.flush()
					os.popen("play-audio OPEN.mp3");os.system(f"xdg-open {lubanghidung}")
					os.popen("play-audio BELL.mp3");print('\n\33[m[\x1b[1;92m+\33[m] DONE !')
					time.sleep(3)
					exit()
				except requests.exceptions.ConnectionError:
					os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
				except Exception as e:
					os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
			elif Input_Makanan in ['05','5','06','6','help','HELP','information','INFORMATION']:
				self.information()
			else:
				os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
		except requests.exceptions.ConnectionError:
			os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
		except Exception as e:
			os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
	def information(self):
		try:
			clear();logo_bapakkau()
			self.GetDeviceUserInfo()
			cetak(panel(f"        {K2}[{H2}01{K2}] TYPE MANUAL ALL COMMAND                            {K2}[{H2}02{K2}] INFORMATION SCRIPT",width=100,title_align='center',title=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}VERSION 1.1.0 {H2}▪︎{K2}▪︎{M2}▪︎",style="bold green"))
			pixi = input('\33[m[\x1b[1;92m?\33[m] PILIH > \x1b[1;92m')
			if pixi in ['01','1']:
				try:
					Console().print(Text('\nType Manual Command \x1b[1;92m01\n\npkg install php\npkg install python\npkg install mc\npkg install figlet\npkg install screenfetch\npkg install neofetch\npkg install toilet\npip install colorama\npip install stdiomask\npip install bs4\n,pip install rich\npip install instaloader\npip install yt_dlp\npip install pyqrcode\napt install python make wget termux-exec clang libjpeg-turbo freetype -y\nenv INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow\npip install prompt_toolkit\npip install email_validator\npip install googlesearch_python\npip install pypng\npip install pytz\npkg install mpv\npip install removebg\npip install tqdm\npip install pycryptodome\npip install requests\npip install mechanize\npip install halo\n\nType Manual Command \x1b[1;92m02\n\npkg install php\npkg install python\npkg install mc\npkg install figlet\npkg install screenfetch\npkg install neofetch\npip install colorama\npip install stdiomask\npip install bs4\npip install rich\napt install python make wget termux-exec clang libjpeg-turbo freetype -y\nenv INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow\npip install pytz\npkg install mpv\npip install tqdm\npip install pycryptodome\npip install requests\npip install mechanize\npip install halo\n\nType Manual Command \x1b[1;92m03\n\npkg install nano\npkg install vim\npkg install inetutils\npkg install python\npkg install install php\npkg install python-pip\npkg install git\npkg install nodejs\n\nType Manual Command \x1b[1;92m04\n\npkg install php\npkg install python\npkg install mc\npkg install figlet\npkg install screenfetch\npkg install neofetch\npkg install toilet\npip install colorama\npip install stdiomask\npip install bs4\npip install rich\npÃ¬p install instaloader\npip install yt_dlp\npip install pyqrcode\napt install python make wget termux-exec clang libjpeg-turbo freetype -y\nenv INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow\npip install prompt_toolkit\npip install email_validator\npip install googlesearch_python\npip install pypng\npip install pytz\npkg install mpv\npip install removebg\npip install tqdm\npip install pycryptodome\npip install requests\npip install mechanize\npip install halo\npkg install inetutils\npkg install vim\npkg install nano\npkg install nodejs\npkg install python-pip\\n\n', style='bold underline'))
					Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
					if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
						Menu_Makan_Bapak_Mu()
					elif Jangan_Lupa in ['n','no','N','NO']:
						os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
						for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2()
						exit()
					else:
						os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
				except requests.exceptions.ConnectionError:
					os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
				except Exception as e:
					os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
			elif pixi in ['02','2']:
				self.aungthor()
			else:
				os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
		except requests.exceptions.ConnectionError:
			os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
		except Exception as e:
			os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
	def aungthor(self):
		try:
			tap = me()
			tap.add_column(f'{K2}PEMBUAT', justify='center', width=25) 
			tap.add_column(f'{K2}WHATSAPP', justify='center', width=20)
			tap.add_column(f'{K2}FACEBOOK', justify='center', width=21)
			tap.add_column(f'{K2}INSTAGRAM', justify='center', width=21)
			tap.add_row(f'{P2}Demias Syihab Aldino				 	',f' {P2}0895320372281',f' {P2}Demias Syihab Aldino',f'{P2}@mask_private1457')
			sol().print(tap, justify='left', style='bold green')
			Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
			if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
				Menu_Makan_Bapak_Mu()
			elif Jangan_Lupa in ['n','no','N','NO']:
				os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
				for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2() 
				exit()
			else:
				os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
		except requests.exceptions.ConnectionError:
			os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
		except Exception as e:
			os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
	def blokade1(self):
		try:
			spinner = halo.Halo(text='Currently Installing...', spinner='dots')
			spinner.start()
			
			clear();Baris_Baru()
			cetak(panel(f"{K2}\t\t\t         SEDANG MENGINSTAL SEMUA TERMUX",width=100,style="bold green"))
			os.system('pkg install git -y && pkg install python -y && pkg install python2 -y && pkg install php -y && pkg install ruby -y && pkg install mc -y && pkg install figlet -y && pkg install screenfetch -y && pkg install neofetch -y && pkg install toilet -y && pip install  --upgrade pip && pip install colorama && pip install stdiomask && pip install requests && pip install mechanize && pip install bs4 && pip install rich && apt install python make wget termux-exec clang libjpeg-turbo freetype -y && env INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow && pip install instaloader && pip install yt_dlp && pip install pyqrcode && pip install prompt_toolkit && pip install email_validator && pip install googlesearch_python && pip install pypng && pkg install mpv -y&& pip install halo && pip install pytz && pip install removebg && pip install tqdm && pip install pycryptodome')
			
			spinner.stop()
			cetak(panel(f"{K2}\t\t\t        BERHASIL MENGINSTAL SEMUA TERMUX",width=100,title_align='center',title=f"{P2}[ {K2}DONE ! {P2}]",style="bold green"))
			Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
			if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
				Menu_Makan_Bapak_Mu()
			elif Jangan_Lupa in ['n','no','N','NO']:
				os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
				for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2()
				exit()
			else:
				os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
		except requests.exceptions.ConnectionError:
			os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
		except Exception as e:
			os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
	def blokade2(self):
		try:
			spinner = halo.Halo(text='Currently Installing...', spinner='dots')
			spinner.start()
			
			clear();Baris_Baru()
			cetak(panel(f"{K2}\t\t\t         SEDANG MENGINSTAL SEMUA TERMUX",width=100,style="bold green"))
			os.system('cd $PREFIX/etc/apt/ && echo "deb https://packages.termux.dev/termux-main-21/ stable main" > sources.list && pkg install git -y && pkg install python -y && pkg install python2 -y && pkg install php -y && pkg install ruby -y && pkg install mc -y && pkg install figlet -y && pkg install screenfetch -y && pkg install neofetch -y && pkg install toilet -y && pip install  --upgrade pip && pip install colorama && pip install stdiomask && pip install requests && pip install mechanize && pip install bs4 && pip install rich && apt install python make wget termux-exec clang libjpeg-turbo freetype -y && env INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow && pip install instaloader && pip install yt_dlp && pip install pyqrcode && pip install prompt_toolkit && pip install email_validator && pip install googlesearch_python && pip install pypng && pkg install mpv -y&& pip install halo && pip install pytz && pip install removebg && pip install tqdm && pip install pycryptodome')
			
			spinner.stop()
			cetak(panel(f"{K2}\t\t\t        BERHASIL MENGINSTAL SEMUA TERMUX",width=100,title_align='center',title=f"{P2}[ {K2}DONE ! {P2}]",style="bold green"))
			Jangan_Lupa = input('\33[m[\x1b[1;92m?\33[m] APAKAH ANDA INGIN KEMBALI KE \x1b[1;92mMENU \33[m/ \x1b[1;91mKELUAR \33[m? \33[m[\x1b[1;92mY\33[m/\x1b[1;91mN\33[m] \33[m> \x1b[1;92m')
			if Jangan_Lupa in ['y','ya','yes','Y','Ya','Yes']:
				Menu_Makan_Bapak_Mu()
			elif Jangan_Lupa in ['n','no','N','NO']:
				os.popen("play-audio OPEN.mp3");os.system("xdg-open https://youtube.com/@tutorialtermux?si=G2rEFl2TYcNAAlxl")
				for _ in track(range(100), description=f'{P2}Sedang Keluar Dari Program...'):LoadingTime2()
				exit()
			else:
				os.popen('play-audio ERROR.mp3');print('\33[m[\x1b[1;91mX\33[m] PILIH YANG BENER !');exit()
		except requests.exceptions.ConnectionError:
			os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
		except Exception as e:
			os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
	def GetDeviceUserInfo(self):
		try:
			output = subprocess.check_output(['neofetch', '--json']).decode('utf-8')
			info = json.loads(output)
			try:OperatingSystem = info['OS']
			except KeyError:OperatingSystem = ('-')
			try:Hosting = info['Host']
			except KeyError:Hosting = ('-')
			try:Kernel = info['Kernel']
			except KeyError:Kernel = ('-')
			try:Uptime = info['Uptime']
			except KeyError:Uptime = ('-')
			try:Packages = info['Packages']
			except KeyError:Packages = ('-')
			try:Shell = info['Shell']
			except KeyError:Shell = ('-')
			try:CentralProcessingUnit = info['CPU']
			except KeyError:CentralProcessingUnit = ('-')
			try:Memori = info['Memory']
			except KeyError:Memori = ('-')
			try:Versi = info['Version']
			except KeyError:Versi = ('-')
			response = requests.get("http://ip-api.com/json/").text
			info = json.loads(response)
			try:Negara = info['country']
			except KeyError:Negara = ('-')
			try:CountryCode = info['countryCode']
			except KeyError:CountryCode = ('-')
			try:Region = info['region']
			except KeyError:Region = ('-')
			try:Kota = info['city']
			except KeyError:Kota = ('-')
			try:Latitude = info['lat']
			except KeyError:Latitude = ('-')
			try:Longitude = info['lon']
			except KeyError:Longitude = ('-')
			try:ZonaWaktu = info['timezone']
			except KeyError:ZonaWaktu = ('-')
			try:Asep = info['isp']
			except KeyError:Asep = ('-')
			try:Ip = info['query']
			except KeyError:Ip = ('-')
			try:As = info['as']
			except KeyError:As = ('-')
			try:Zip = info['zip']
			except KeyError:Zip('-')
			try:GmapsURL = 'https://www.google.com/maps/place/' + str(Latitude) + '+' + str(Longitude)
			except KeyError:GmapsURL = ('-')
			jam = strftime('%H:%M:%S')
			bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10': 'Oktober', '11': 'November', '12': 'Desember'}
			tgl = datetime.now().day
			bln = bulan[(str(datetime.now().month))]
			thn = datetime.now().year
			tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
			hari   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
			sekarang = ''+str(tgl)+'-'+str(bln)+'-'+str(thn)
			cetak(panel(f"              {K2}KETIK {H2}{bil} {K2}UNTUK MELAPOR JIKA ADA KESALAHAN SINTAKS/LAIN SEBAGAINYA",title_align='center',title=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}{jam} {H2}▪︎{K2}▪︎{M2}▪︎",subtitle_align='center',subtitle=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}{hari}, {sekarang} {H2}▪︎{K2}▪︎{M2}▪︎",width=100,style=f"bold green"))
			Berotak_Senku = []
			Berotak_Senku.append(panel(f'\n{K2}[{H2}+{K2}] {H2}OS       : {K2}{OperatingSystem}\n{K2}[{H2}+{K2}] {H2}HOST     : {K2}{Hosting}\n{K2}[{H2}+{K2}] {H2}KERNEL   : {K2}{Kernel}\n{K2}[{H2}+{K2}] {H2}UPTIME   : {K2}{Uptime}\n{K2}[{H2}+{K2}] {H2}PACKAGES : {K2}{Packages}\n{K2}[{H2}+{K2}] {H2}SHELL    : {K2}{Shell}\n{K2}[{H2}+{K2}] {H2}MEMORI   : {K2}{Memori}\n{K2}[{H2}+{K2}] {H2}VERSI    : {K2}{Versi}\n',width=50,title=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}INFORMASI DEVICE {H2}▪︎{K2}▪︎{M2}▪︎",title_align='center',padding=(0,3),style=f"bold green"))
			Berotak_Senku.append(panel(f'\n{K2}[{H2}+{K2}] {H2}KARTU     : {K2}{Asep}\n{K2}[{H2}+{K2}] {H2}NEGARA    : {K2}{Negara}\n{K2}[{H2}+{K2}] {H2}KOTA      : {K2}{Kota}\n{K2}[{H2}+{K2}] {H2}TIMEZONE  : {K2}{ZonaWaktu}\n{K2}[{H2}+{K2}] {H2}IP        : {K2}{Ip}\n{K2}[{H2}+{K2}] {H2}LATITUDE  : {K2}{Latitude}\n{K2}[{H2}+{K2}] {H2}LONGITUDE : {K2}{Longitude}\n{K2}[{H2}+{K2}] {H2}WILAYAH   : {K2}{Region}\n',width=50,title=f"{M2}▪︎{K2}▪︎{H2}▪︎ {K2}INFORMASI PENGGUNA {H2}▪︎{K2}▪︎{M2}▪︎",title_align='center',padding=(0,3),style=f"bold green"))
			Console().print(Columns(Berotak_Senku))
		except requests.exceptions.ConnectionError:
			os.popen("play-audio NETWORK.mp3");print('\33[m[\x1b[1;91mX\33[m] KONEKSI TIDAK ADA !');exit()
		except Exception as e:
			os.popen('play-audio ERROR.mp3');print(f"\33[m[\x1b[1;91mX\33[m] SYNTAX : \x1b[1;92m{str(e).title()}");exit()
		
if __name__ == '__main__':
	Menu_Makan_Bapak_Mu()