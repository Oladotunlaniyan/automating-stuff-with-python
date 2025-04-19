import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

if len(sys.argv) < 3:
    print("Usage: python emailer.py <recipient_email> <message>")
    sys.exit(1)

recipient_email = sys.argv[1]
message_body = " ".join(sys.argv[2:])

your_email = "myemail"
your_password = "yourpassword"

driver = webdriver.Chrome()
driver.get("https://mail.google.com")

time.sleep(2)
driver.find_element(By.ID, "identifierId").send_keys(your_email + Keys.ENTER)

time.sleep(3)
driver.find_element(By.NAME, "password").send_keys(your_password + Keys.ENTER)
time.sleep(5)

compose_button = driver.find_element(By.XPATH, "//div[text()='Compose]")
compose_button.click()
time.sleep(3)


driver.find_element(By.NAME, "to").send_keys(recipient_email)
driver.find_element(By.NAME, "subjectbox").send_keys("Automated Message")
driver.find_element(By.XPATH, "//div[@aria-label='Message Body]").send_keys(message_body)

send_button = driver.find_element(By.XPATH, "//div[text()='Send']")
send_button.click()

print("Email sent successfully!")

time.sleep(5)
driver.quit()