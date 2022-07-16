#!/usr/bin/python3
#coding=utf-8

import os
import sys
import time
import json
import random
import socket
import shutil
import webbrowser
import concurrent.futures

try:
  __import__('requests')
except ModuleNotFoundError:
  os.system ('pip3 install requests')
finally:
  import requests

try:
  __import__('bs4')
except ModuleNotFoundError:
  os.system ("pip3 install bs4")
finally:
  from bs4 import BeautifulSoup as parser

UPDATE = "06-16-2022 18.01"

if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""

try:
  print (f"{p}[{y}!{p}] {r}Menghubungkan Ke Server")
  data = requests.get("https://www.mediafire.com/api/1.4/folder/get_content.php?content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=ueti9cij4zf3i&response_format=json").json()
  files = data['response']['folder_content']['files']
except requests.exceptions.RequestException:
  exit(f"{p}[{y}!{p}] {r}Tidak Ada Koneksi!{a}")


try:
  os.mkdir('virtex')
except FileExistsError:
  pass

def Moya(file):
   with requests.Session() as sesi:
     print (f"{p}[{y}!{p}] {y}Downloading {file['filename']}")
     a = sesi.get(file['links']['normal_download'])
     b = parser(a.content,'html.parser').find('a',class_ = 'popsok')['href']
     c = sesi.get(b).content
     d = os.path.join('virtex',file['filename'])
     e = os.open(d,os.O_CREAT | os.O_WRONLY)
     os.write(e,c)
     os.close(e)

colors = lambda : random.choice([r,g,y,p,P,c,w])
logo = f"{r}{p}╔═════════════════════════════════════╗\n[{y}•{p}] {c}Coded : {g} ▄▅▆千卂乙尺ㄚ 丂         {p}\n[{y}•{p}] {c}GitHub : {w}github.com/FazryS  {p}\n[{y}•{p}] {c}WA.    : {y}+6283109115523        {p}\n[{y}•{p}] {c}UPDATE : {UPDATE}      {p}  \n[{y}•{p}] {c}Python : {colors()}{sys.version[0:6]}                {p}  \n[{y}•{p}] {c}OS     : {colors()}{sys.platform}{' '*(23 - len(sys.platform))}{p} \n[{y}•{p}] {c}Host   : {colors()}{socket.gethostname()}{' '*(24 - len(socket.gethostname()))}{p}\n[{y}•{p}] {c}Team.  : {colors()}꧁卩尺ㄖᎶ尺卂爪 匚ㄖᗪ乇S》 {colors()}\n╚═════════════════════════════════════╝{a}"

def main():
  try:
    os.system ('clear')
    print (logo)
    print ("%sPILIH JENIS VIRTEX" % (g))
    print ("%s%s%s" % (c,'='*43,a))
    for khaneysia,rahmat in enumerate(files, start = 1):
      print (f"{p}[{r}{str(khaneysia).zfill(2)}{p}] {colors()}{os.path.splitext(rahmat['filename'])[0]}")
    print (f"{p}[{r}AL{p}] {c}UNDUH SEMUA VIRTEX\n{p}[{r}BA{p}] {y}KEMBALI KE MENU UTAMA\n{p}[{r}EX{p}] {r}EXIT THE PROGRAM")
    echa = input("%s>>>> %s" % (g,c)).lower()
    if echa == 'al':
      with concurrent.futures.ThreadPoolExecutor(15) as executor:
        executor.map(Moya, files)
      shutil.make_archive('virtex-master','zip','virtex')
      print ("{p}[{g}✓{p}] {g}Download Complete")
      exit ("{p}[{g}✓{p}] {g}Download Results Saved In : {os.path.realpath('virtex')}")
    elif echa == 'ba':
      menu()
    elif echa == 'ex':
      os.abort()
    elif int(echa) in range(1,len(files) + 1):
      rahmet = files[int(echa) - 1]
      kntl = 0
      print (f"{p}[{y}!{p}] {y}Downloading {rahmet['filename']}")
      while True:
        try:
          ses = requests.Session()
          req = ses.get(rahmet['links']['normal_download'])
          res = parser(req.content,'html.parser')
          print (f"{p}[{y}✓{p}] {y}URL/Link : {req.url}")
          print (f"{p}[{y}✓{p}] {y}Status : {req.status_code}")
          url = res.find('a',class_ = 'popsok')['href']
          path = os.path.join('virtex',rahmet['filename'])
          file = os.open(path,os.O_CREAT | os.O_WRONLY)
          txt = ses.get(url).content
          os.write(file,txt)
          os.close(file)
          byte = os.stat(path).st_size
          for b in ['B','KB','MB','GB','TB']:
            if byte < 1024.0:
              byte = "%3.2f %s" % (byte,b)
              break
            else:
              byte /= 1024.0
          print (f"{p}[{y}✓{p}] {g}Nama File : {os.path.basename(path)}")
          print (f"{p}[{y}✓{p}] {g}Ukuran File : {byte}")
          print (f"{p}[{y}✓{p}] {g}File Path : {os.path.realpath(path)}")
          show = input(f"{p}[{y}?{p}] {w}Lihat Hasil Download? [{g}Y/{w}{r}n{w}] {P}").lower() == 'y'
          if show:
            os.system (f"xdg-open --view virtex/'{rahmet['filename']}'")
          time.sleep(1)
          main()
          break
        except requests.exceptions.RequestException as su:
          kntl += 1
          if kntl >= 5:
            print (f"{p}[{y}!{p}] {y}Gagal Terhubung Ke Server\n\n\tCoba :\n\t\t• Nonaktifkan mode pesawat\n\t\t• Aktifkan data seluler atau Wi-Fi\n\t\t• Periksa sinyal di area Anda{a}")
            break
          else:
            print (f"{p}[{y}!{p}] {y}Mencoba Menghubungkan ulang ke server")
            time.sleep(1.5)
    else:
      raise ValueError()

  except ValueError:
    print (f"{y}[🖕🏼] Jangan Kosong Goblok!")
    time.sleep(1)
    main()

def menu():
  os.system('clear')
  print (logo)
  print (g + "MENU UTAMA")
  print ("%s%s" % (c,"="*37))
  print (f'{p}[{y}1{p}] {g}DOWNLOAD FILE VIRTEX\n{p}[{y}2{p}] {y}LAPORKAN BUG\n{p}[{y}3{p}] {y}ABOUT\n{p}[{y}0{p}] {r}KELUAR')
  choice = input("%s>>> %s" % (y,c))
  if choice == '1' or choice == '01':
    main()
  elif choice == '2' or choice == '02':
    url = "https://wa.me/6283109115523"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      memu()
    else:
      os.system ("xdg-open "+url)
  elif choice == '3' or choice == '03':
    os.system('clear')
    print (f"{logo}\n{g}INFO SCRIPT\n========================\n{p}[{y}✓{p}] {c}Coded : {g}▄▅▆千卂乙尺ㄚ 丂\n{p}[{y}✓{p}] {c}Team  : {colors()}꧁卩尺ㄖᎶ尺卂爪 匚ㄖᗪ乇S》\n{p}[{y}✓{p}] {c}Script: {colors()}{os.path.basename(sys.argv[0])}\n{p}[{y}✓{p}] {c}Path  : {os.path.realpath(sys.argv[0])}\n{p}[{y}✓{p}] {c}Size  : {os.stat(os.path.realpath(sys.argv[0])).st_size} Byte\n{p}[{y}✓{p}] {c}Link  : {colors()}https://github.com/FazryS/Virtex\n{p}[{y}✓{p}] {c}Update: {colors()}{UPDATE}\n{p}[{y}✓{p}] {c}Versi : 1.1\n\n{g}Contact Me ^_^\n==================\n{p}[{y}✓{p}] {c}Github: {colors()}https://github.com/Pazrysablenk/\n{p}[{y}✓{p}] {c}Fb.   : {colors()}https://www.facebook.com/Fazry\n{p}[{y}✓{p}] {c}Wa.   : {colors()}+6283109115523\n{p}[{y}✓{p}] {c}Email : {colors()}fazrimk1@gmail.com\n{a}")
  elif choice == '00' or choice == '0':
    os.abort()
  else:
    print ("%s[🖕🏼] Jangan Kosong Goblok!" % (y))
    time.sleep(0.9)
    menu()

if __name__ == "__main__":
  menu() 
