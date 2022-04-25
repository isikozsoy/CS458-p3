from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
import time

def test2():

    base_path = "https://ismetalp98.github.io/project3/"

    

    # Case 2: Starting with a different Location
    # Case 2.1
    params = {
        "latitude": 50.1109,
        "longitude": 8.6821,
        "accuracy": 100
    }
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))
    driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
    driver.get(base_path)

    latitude = 50.1109
    longitude = 8.6821
    expected_result = 4440
    expected_result_1 = expected_result

    driver.find_element(By.ID, "partb").click()
    driver.find_element(By.ID, "usegps").click()
    longitude_out = driver.find_element(By.ID, "lon_field").get_attribute('value')
    latitude_out = driver.find_element(By.ID, "lat_field").get_attribute('value')

    assert str(latitude) == str(latitude_out)
    assert str(longitude) == str(longitude_out)

    driver.find_element(By.ID, "calcdist").click()
    distance = driver.find_element(By.ID, "distance").text
    assert distance == str(expected_result)

    driver.close()


    # Case 2.2
    params = {
        "latitude": 50.1109,
        "longitude": 50.1109,
        "accuracy": 100
    }
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))
    driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
    driver.get(base_path)
    latitude = 50.1109
    longitude = 50.1109
    expected_result = 4440

    driver.find_element(By.ID, "partb").click()
    driver.find_element(By.ID, "usegps").click()
    longitude_out = driver.find_element(By.ID, "lon_field").get_attribute('value')
    latitude_out = driver.find_element(By.ID, "lat_field").get_attribute('value')

    assert str(latitude) == str(latitude_out)
    assert str(longitude) == str(longitude_out)

    driver.find_element(By.ID, "calcdist").click()
    distance = driver.find_element(By.ID, "distance").text
    assert distance == str(expected_result)
    # check changing latitude does not affect the distance
    assert str(expected_result_1) == distance

    driver.close()

    # Case 2.3
    params = {
        "latitude": 8.6821,
        "longitude": 8.6821,
        "accuracy": 100
    }
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))
    driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
    driver.get(base_path)

    latitude = 8.6821
    longitude = 8.6821
    expected_result = 9052

    driver.find_element(By.ID, "partb").click()
    driver.find_element(By.ID, "usegps").click()
    longitude_out = driver.find_element(By.ID, "lon_field").get_attribute('value')
    latitude_out = driver.find_element(By.ID, "lat_field").get_attribute('value')

    assert str(latitude) == str(latitude_out)
    assert str(longitude) == str(longitude_out)

    driver.find_element(By.ID, "calcdist").click()
    distance = driver.find_element(By.ID, "distance").text
    assert distance == str(expected_result)

    driver.close()

    # Case 2.4
    params = {
        "latitude": 90,
        "longitude": 0,
        "accuracy": 100
    }
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))
    driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
    driver.get(base_path)

    latitude = 90
    longitude = 0
    expected_result = 0

    driver.find_element(By.ID, "partb").click()
    driver.find_element(By.ID, "usegps").click()
    longitude_out = driver.find_element(By.ID, "lon_field").get_attribute('value')
    latitude_out = driver.find_element(By.ID, "lat_field").get_attribute('value')

    assert str(latitude) == str(latitude_out)
    assert str(longitude) == str(longitude_out)

    driver.find_element(By.ID, "calcdist").click()
    distance = driver.find_element(By.ID, "distance").text
    assert distance == str(expected_result)

    driver.close()
    
test2()