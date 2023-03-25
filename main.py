import socket
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

username = ""  # Enter your username here
password = ""  # Enter your password here


def detect_captive_portal():
    try:
        hostname = "connectivitycheck.gstatic.com"
        expected_ip = socket.gethostbyname(hostname)

        url = "http://connectivitycheck.gstatic.com/generate_204"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            actual_ip = resp.fp.raw._sock.getpeername()[0]

        if actual_ip == expected_ip:
            return False
        else:
            return True
    except:
        return True


while True:
    if detect_captive_portal():
        driver = webdriver.Firefox(executable_path="geckodriver")
        driver.get("https://iach.srmist.edu.in/Connect/PortalMain")

        sleep(3)

        username = driver.find_element(By.ID, "LoginUserPassword_auth_username")
        username.clear()

        password = driver.find_element(By.ID, "LoginUserPassword_auth_password")
        password.clear()

        username.send_keys(username)
        password.send_keys(password)

        driver.find_element(By.ID, "UserCheck_Login_Button_span").click()

        driver.close()
