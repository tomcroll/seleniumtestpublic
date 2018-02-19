from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0

# Create a new instance of the Firefox driver
# driver = webdriver.Firefox()
driver = webdriver.Ie()

# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
print ("Driver used " + driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("Skywise!")

# submit the form (although google automatically searches now without
# submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be
    # updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("Skywise!"))

    # You should see "Skywise! - Google Search"
    print ("Driver used is " + driver.title)

except TimeoutException as ex:
    isrunning = 0
    print("Exception has been thrown " + str(ex))
    driver.close()

finally:
    driver.quit()
