#!/usr/bin/env python
# coding: utf-8

# **Bu çalışma Pycharm ve Chrome üzerinden anlatılmıştır. Whatsapp web üzerinde belirlenen bir konuşmada istenilen mesajı otomatik olarak yazan bir bot geliştirilmeye çalışılmıştır.**

# Öncelikle _**selenium library**_ kurmalıyız. Bunun için terminalimize;
pip install selenium
# yazıp, kurulumun tamamlanmasını bekliyoruz. Ardından kullandığımız web tarayıcımız (chrome,mozilla,opera vb.) için sürüm bilgilerini almalıyız. Tarayıcımıza göre _**Chromium**_ kurulumu yapmalıyız. Bunu tarayıcınızda ufak bir araştırma sayesinde elde edebilirsiniz. Örnek olarak _**chrome**_ kullanıyoruz diyelim. Chrome ayarlarından sürüm bilgilerimizi aldıktan sonra _**chromedriverchromium.org**_ üzerinden sürümümüze uygun olanı indiriyoruz. 

# 
# İndirdiğimiz dosyaları ayıkladıktan sonra _**chromedriver.exe**_ dosyasını Pycharm üzerindeki **venv** içine yapıştıracağız. Virtualenv (yani venv olarak görülen dosya)  bize çalışmalarımızda kullanmak istediğimiz modülleri bilgisayarımızdan bağımsız olarak kurma ve çalıştırma imkanı sağlar. Şimdi sıra işimize yarayacak araçları _import_ etmede, aşağıdaki kodları yazıyoruz veya copy-paste yapalım; 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver,600)
driver.maximize_window()
input("QR Kodu bekle")
# Whatsapp üzerinde botu çalıştırmak istediğimiz grup veya kişinin adı olarak ben **"Test"** olarak adlandırdığım bir grup kurdum. Yazmasını istediğim mesaj da **"Bu bir deneme mesajıdır"** dedim. Kurduğumuz grup isminin site üzerinde göründüğünden emin olmalıyız yani arşivlenenlerde olmaması lazım. İsim ile yakalayıp oraya girmesini sağlayacağız. Mesaj yazdığımız kutuya ise selenium XPATH metodu ile ulaşacağız. Site içerisinde bir bölgenin (yazının veya sekmenin) xpath uzantısına ulaşmak için ilgili bölgeye sağ tıklayıp incele sekmesini seçtikten sonra açılan kod penceresinde ilgili yere sağ tıklayıp _**copy>copy xpath**_ yolunu seçmeniz gerekir.  
# 
# Mesaj kutusunun xpath değerini : "//*[@id="main"]/footer/div[1]/div[2]/div/div[2]" olarak aldım.
isim = "Test" 
grup = driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
grup.click()
box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

box.send_keys("Bu bir deneme mesajıdır" + Keys.ENTER)
# Şimdi bir çalıştıralım.

# Sıra geldi gelen mesaja göre cevap vermesini ayarlamaya yani kodumuza gelen mesajı okutalım. Bunun için öncelikle gelen mesajın koordinatlarına ulaşacağız. Fare imlecimizi gelen mesaj kutusunun üzerine getirip bunun ekrandaki koordinatlarını elde edeceğiz. Bunun için _**pyautogui**_ aracını kullanacağız. Şimdiye kadar yazdığımız kodları silelim ve alttaki kodları çalıştıralım. Beliren koordinat bilgilerini not almayı unutmayın! 
import pyautogui
import time

a= 0
while True:
    print(pyautogui.position())
    time.sleep(1)
    a = a+1
    if a == 10:
        break
# Örnek olarak çıkan koordinatlarımız **(544,736)** olsun. Notumuzu aldıktan sonra tekrar tüm kodları silelim ve aşağıdaki kodları çalıştıralım.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver,600)
driver.maximize_window()
input("QR Kodu bekle")

isim = "Test" 
grup = driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
grup.click()
box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

box.send_keys("Bu bir deneme mesajıdır" + Keys.ENTER)

time.sleep(10)
pyautogui.click(544,736)
pyautogui.coubleClick(544,736)
pyautogu.hotkey('ctrl','c')
# Bilgisayarda CTRL+C klavye kombinasyonu ile yaptığımız kopyalama işlemi sonucu aldığımız değeri python’da bir değişkene atamak için kullanacağımız kütüphane _**pyperclip**_. Öncelikle kütüphaneyi kuralım.
pip install pyperclip
# Artık yüklememiz gereken tüm kütüphaneleri yükledik, geriye sadece gelen mesajın ne olduğunda ne yazmasını istediğimizi belirlemeliyiz. Ben _**"Merhaba"**_ diyerek atılan bir mesaja _**"Merhabalar..."**_ olarak cevap vermesini istiyorum. Şimdi yazdığımız tüm kodları silelim ve son olarak alttaki kodu çalıştıralım.
# 
# Dikkat ederseniz her eklediğimiz kütüphaneyi başlangıçta _import_ ettiğimizi göreceksiniz. 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time
import pyperclip

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver,600)
driver.maximize_window()
input("QR Kodu bekle")

--------------------
isim = "Test" 
grup = driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
grup.click()
box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

box.send_keys("Bu bir deneme mesajıdır" + Keys.ENTER)

--------------------
time.sleep(10)
pyautogui.click(544,736)
pyautogui.coubleClick(544,736)
pyautogu.hotkey('ctrl','c')

--------------------
gelen_mesaj = pc.paste()
print(gelen_mesaj)

if gelen_mesaj == "Merhaba":
  box.send_keys("Merhabalar...")+Keys.ENTER