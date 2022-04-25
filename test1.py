from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
import time


def test1():
    # open website
    base_path = "https://ismetalp98.github.io/project3/"
    driver = webdriver.Chrome(config("CHROMEDRIVER_PATH"))
    driver.get(base_path)

    # Case 1: Check if the page for calculation 1 is loaded correctly
    driver.find_element(By.ID, "parta").click()
    lat_field = driver.find_element(By.ID, "lat_field")
    lon_field = driver.find_element(By.ID, "lon_field")
    parta_visible = driver.find_element(By.ID, "calc1")
    assert lat_field.is_displayed()
    assert lon_field.is_displayed()
    assert parta_visible.is_displayed()

    # Case 2: Check if the given latitude and longitude are valid
    invalid_latitudes = ["iamlatitude", "l@titud€", "-91", "-92.0", "93", "94.0"]
    invalid_longitudes = ["iamlongitude", "l@ngitud€", "-181", "-182.0", "183", "184.0"]

    sbmt_btn = driver.find_element(By.ID, "calculate")
    assert sbmt_btn.is_displayed()
    assert sbmt_btn.is_enabled()

    for i in range(len(invalid_latitudes)):
        lat_field.send_keys(invalid_latitudes[i])
        lon_field.send_keys(invalid_longitudes[i])
        driver.find_element(By.ID, "calculate").click()
        invalid_lat = driver.find_element(By.ID, "latitude-error")
        invalid_lon = driver.find_element(By.ID, "longitude-error")
        assert invalid_lat.is_displayed()
        assert invalid_lon.is_displayed()

    # Case 3: Check if the given latitudes and longitudes are valid and the results are correct
    latitudes = ["37", "35", "51", "35", "40.5", "-18.8", "-18.8"]
    longitudes = ["40", "33", "10", "104", "-3.7", "-46.9", "46.9"]
    countries = ["TUR", "CYP", "DEU", "CHN", "ESP", "BRA", "MDG"]

    for i in range(len(latitudes)):
        lat_field.clear()
        lon_field.clear()
        lat_field.send_keys(latitudes[i])
        lon_field.send_keys(longitudes[i])
        driver.find_element(By.ID, "calculate").click()
        print(latitudes[i], longitudes[i])
        invalid_lat = driver.find_element(By.ID, "latitude-error")
        invalid_lon = driver.find_element(By.ID, "longitude-error")
        assert not invalid_lat.is_displayed()
        assert not invalid_lon.is_displayed()
        assert driver.find_element(By.ID, "country").text == countries[i]


test1()
