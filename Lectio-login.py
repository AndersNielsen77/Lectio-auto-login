from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

Brugernavn = ("Changeme")
Adgangskode = ("Changeme")


#Skift til dit lectio login side.
driver.get("https://www.lectio.dk/lectio/523/login.aspx")
#Sikre den rigtige sted!
print(driver.current_url)


found_brugernavn = driver.find_element_by_id('m_Content_username2')
#found_brugernavn = driver.find_by_xpath('//*[@id="m_Content_username2"]').click
found_brugernavn.send_keys(Brugernavn)

#found_adgangskode = driver.find_by_xpath('//*[@id="password2"]')
found_adgangskode = driver.find_element_by_id('password2')
found_adgangskode.send_keys(Adgangskode)

#Hvor du skal hen på siden.
found_login = driver.find_element_by_id('s_m_HeaderContent_subnavigator_ctl07"')
found_login.send_keys(Keys.ENTER)

found_fravar = driver.find_element_by_id('s_m_HeaderContent_subnavigator_ctl02')
found_fravar.send_keys(Keys.ENTER)

#found_opgjort = driver.find_element_by_id('s_m_Content_Content_SFTabStudentAbsenceDataTable')

#print(found_opgjort)
#time.sleep(10)
exit()
