from operator import inv
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
import time


def test3():
    base_path = "https://ismetalp98.github.io/project3/"
    driver = webdriver.Chrome(config("CHROMEDRIVER_PATH"))
    driver.get(base_path)

    # Case 1: Check if the page for part c is loaded correctly
    driver.find_element(By.ID, "partc").click()
    lat_field = driver.find_element(By.ID, "lat_field")
    lon_field = driver.find_element(By.ID, "lon_field")
    year_field = driver.find_element(By.ID, "year")
    month_field = driver.find_element(By.ID, "month")
    day_field = driver.find_element(By.ID, "day")
    hour_field = driver.find_element(By.ID, "hour")
    minute_field = driver.find_element(By.ID, "minute")
    second_field = driver.find_element(By.ID, "second")
    assert lat_field.is_displayed()
    assert lon_field.is_displayed()
    assert year_field.is_displayed()
    assert month_field.is_displayed()
    assert day_field.is_displayed()
    assert hour_field.is_displayed()
    assert minute_field.is_displayed()
    assert second_field.is_displayed()

    # Case 2: Check if the given date is valid
    latitudes = ["40", "52.5", "42", "35.7", "38", "9"]
    longitudes = ["32.9", "13.4", "12.5", "139", "9", "23.7", "99"]

    years = ["2000", "l@nye", "-200", "2050", "183", "2022.0"]
    months = ["iammonth", "l@nth", "-200", "12", "183", "12.0"]
    days = ["iamday", "09", "-200", "31", "183", "31.0"]
    hours = ["iamhour", "59", "20", "24", "183", "24.0"]
    minutes = ["iamminute", "59", "20", "60", "183", "60.0"]
    seconds = ["iamsecond", "59", "20", "60", "183", "60.0"]

    sbmt_btn = driver.find_element(By.ID, "calculate")
    assert sbmt_btn.is_displayed()
    assert sbmt_btn.is_enabled()

    for i in range(len(latitudes)):
        lat_field.clear()
        lon_field.clear()
        year_field.clear()
        month_field.clear()
        day_field.clear()
        hour_field.clear()
        minute_field.clear()
        second_field.clear()
        lat_field.send_keys(latitudes[i])
        lon_field.send_keys(longitudes[i])
        driver.find_element(By.ID, "year").send_keys(years[i])
        driver.find_element(By.ID, "month").send_keys(months[i])
        driver.find_element(By.ID, "day").send_keys(days[i])
        driver.find_element(By.ID, "hour").send_keys(hours[i])
        driver.find_element(By.ID, "minute").send_keys(minutes[i])
        driver.find_element(By.ID, "second").send_keys(seconds[i])
        driver.find_element(By.ID, "calculate").click()
        invalid_date = driver.find_element(By.ID, "date-error")
        assert invalid_date.is_displayed()

    # Case 3: Check results with the device location
    latitudes = [40, 52.5, 42, 35.7, 38]
    longitudes = [32.9, 13.4, 12.5, 139, 9, 23.7]
    years = ["2022", "2022", "2022", "2022", "2018"]
    months = ["05", "05", "05", "05", "01"]
    days = ["24", "24", "24", "24", "30"]
    hours = ["15", "14", "14", "21", "11"]
    minutes = ["01", "06", "07", "09", "56"]
    seconds = ["41", "48", "46", "34", "30"]
    expected_results = ["394998", "394838", "394841", "396050", "374399"]
    for i in range(len(latitudes)):
        params = {"latitude": latitudes[i], "longitude": longitudes[i], "accuracy": 100}
        driver = webdriver.Chrome(config("CHROMEDRIVER_PATH"))
        driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

        driver.get(base_path)
        driver.find_element(By.ID, "partc").click()

        driver.find_element(By.ID, "usegps").click()

        latitude_out = driver.find_element(By.ID, "lat_field").get_attribute("value")
        longitude_out = driver.find_element(By.ID, "lon_field").get_attribute("value")

        driver.find_element(By.ID, "year").send_keys(years[i])
        driver.find_element(By.ID, "month").send_keys(months[i])
        driver.find_element(By.ID, "day").send_keys(days[i])
        driver.find_element(By.ID, "hour").send_keys(hours[i])
        driver.find_element(By.ID, "minute").send_keys(minutes[i])
        driver.find_element(By.ID, "second").send_keys(seconds[i])

        driver.find_element(By.ID, "calculate").click()
        distance = driver.find_element(By.ID, "distance").text

        assert str(latitudes[i]) == latitude_out
        assert str(longitudes[i]) == longitude_out
        assert distance == expected_results[i]


test3()
