from time import sleep
from selenium import webdriver
from config import ROUTER_PASSWORD, ROUTER_URL, ROUTER_USERNAME

DEBUG=False

chromedriver_location = "chromedriver"


def find_data_box(driver_object):
    """ returns the div with our information """
    boxes = driver_object.find_elements_by_class_name('content')

    for box in boxes:
        #print(dir(box))
        if "WAN Sensing" in box.text:
            #print("found it")
            #print(box.text)
            return box
    return False

def get_data():

    data = {
        'up' : -1,
        'down' : -1,
    }



    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(chromedriver_location, options=options)


    driver.get(ROUTER_URL)

    driver.implicitly_wait(5)
    

    if DEBUG: 
        print("Opened page")
        print("Setting username")
    driver.find_element_by_id('srp_username').clear()
    driver.find_element_by_id('srp_username').send_keys(ROUTER_USERNAME)

    if DEBUG:
        print("sending password to form")
    driver.find_element_by_id('srp_password').send_keys(ROUTER_PASSWORD)

    if DEBUG:
        print("clicking login button")
    loginbutton = driver.find_element_by_id('sign-me-in').click()

    # wait for the page to render
    while find_data_box(driver) == False:
        sleep(1)
    datadiv = find_data_box(driver)

    # get the lines we need
    textlines = [line.strip() for line in datadiv.text.split("\n") if line.strip() != ""]
    for num, line in enumerate(textlines):
        if "DSL" in line:
            data['status'] = line.split()[-1]
        if "Mbps" in line:
            if num == 2:
                data['up'] = float(line.split()[0])
            elif num == 3:
                data['down'] = float(line.split()[0])
            else:
                raise ValueError(f"line {num} shouldn't have data: {line}")

    if DEBUG:
        print(data)
    return data

if __name__ == '__main__':
    get_data()
