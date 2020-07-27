import time, random
from selenium import webdriver
 
driver = webdriver.Chrome('chromedriver.exe')  
 
def login():
    driver.get('http://localhost/med_system/login.php')
    time.sleep(3) 
    username = driver.find_element_by_name('user')
    username.send_keys('urdea')
    password = driver.find_element_by_name('parola')
    password.send_keys('test')
    button = driver.find_element_by_name('submit')
    button.click()
    time.sleep(3) 
 
def add_patient():
    driver.get("http://localhost/med_system/adauga_pacient.php")
    nume = driver.find_element_by_name('nume')
    adresa = driver.find_element_by_name('adresa')
    telefon = driver.find_element_by_name('telefon')
    email = driver.find_element_by_name('email')
    alergii = driver.find_element_by_name('alergii')
    button = driver.find_element_by_name('submit')
    time.sleep(3) 
    nume.send_keys("Oprisan Flavius")
    adresa.send_keys("Oprisan Flavius")
    telefon.send_keys("Oprisan Flavius")
    email.send_keys("Oprisan Flavius")
    alergii.send_keys("Oprisan Flavius")
    time.sleep(3) 
    button.click()
 
login()
add_patient()
