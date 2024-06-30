import os, requests, json, datetime, math, random
from time import sleep
kiemtra=''
win=lose=0
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;34m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;34m"
lam="\033[1;34m"
tim="\033[1;34m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
xanhnhat = "\033[1;36m"
trang1 = "\033[1;37m"
stop=0
checkk=requests.get('https://api.im2018.com/api/game/guess_Odd?page=1&limit=1&type=24').text
landau=checkk
os.system('clear')
if datetime.datetime.now().minute%2==0:
  print(f'{xanhla}Đang check cầu!! Đợi đợt sau!!')
  while True:
    sleep(0.5)
    if datetime.datetime.now().minute%2!=0:
      break
else:
  print(f'{xanhla}Đang check cầu!! Đợi đợt sau!!')
while True:
  tg=datetime.datetime.now()
  gio=tg.hour
  phut=tg.minute
  giay=tg.second
  if phut%2==0:
    if stop==0:
      os.system('clear')
      stop=1
      while True:
        check=requests.get('https://api.im2018.com/api/game/guess_Odd?page=1&limit=1&type=24').text
        if check!=checkk:
          giayy=datetime.datetime.now().second
          nano=int(datetime.datetime.now().strftime('%f'))
          break
      kq=json.loads(check)
      so=[entry['number'] for entry in kq['data']]
      result=[entry['result'] for entry in kq['data']]
      serial=[entry['serial'] for entry in kq['data']]
      tg+=datetime.timedelta(minutes=2)
      thang=tg.month
      ngay=tg.day
      gio=tg.hour
      phut=tg.minute
      #tinh=(thang+ngay+gio+phut)*(serial[0])*so[0]
      
      try:
        del tinh
      except:
        pass
      tinh=[]
      for j in range(0,nano%1000+1):
          random.seed(int((datetime.datetime.now().replace(second=giayy).replace(microsecond=nano//1000*1000)+datetime.timedelta(minutes=2)+datetime.timedelta(microseconds=j)).timestamp()))
          tinh.append(random.randint(1,80))
      le=chan=0
     # for digit in tinh:
      for digitt in tinh:
          if int(digitt)%2==0:
            chan+=1
          else:
            le+=1
            
            
            
      if chan>le:
        cau='Even'
        cl='Chẵn'
        tinh=chan/(chan+le)*100
      elif chan<le:
        cau='Odd'
        cl='Lẻ'
        tinh=le/(chan+le)*100
      else:
        if tinh[-1]%2==0:
            chan+=1
        else:
            le+=1
        if chan>le:
          cau='Even'
          cl='Chẵn'
          tinh=chan/(chan+le)*100
        elif chan<le:
          cau='Odd'
          cl='Lẻ'
          tinh=le/(chan+le)*100
      print(f'{xnhac}{cau} ({cl})   |  {int(tinh)}%     ({so[0]})    -({giayy}s + {nano})\n')
      if checkk!=landau:
        if kiemtra in result[0]:
          win+=1
          print(f'{xanhla}Win: {win}  (+1)')
          print(f'{do}Lose: {lose}')
        else:
          lose+=1
          print(f'{xanhla}Win:  {win}')
          print(f'{do}Lose: {lose}  (+1)')
      kiemtra=cau
      print('\n')
      checkk=check
  else:
    sleep(0.5)
    if stop==1:
      stop=0
    print(f'\r{vang}--- {gio}  :  {phut}  :  {giay} ---',end='')
