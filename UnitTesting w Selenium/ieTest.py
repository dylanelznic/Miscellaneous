import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# navigate to the application home page
driver = webdriver.Ie("C:/Users/DJ/Master/Environments/seleniumTutorial/Scripts/IEDriverServer.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# curretnly on result page using find_elements_by_class_name method
lists = driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# the name of the search

i = 0
for listItem in lists:
	print(listItem)
	i = i + 1
	if i > 10:
		break

# close the browser window
driver.quit()