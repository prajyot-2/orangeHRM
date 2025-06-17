
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
import time


def test_page():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.send_keys("Admin")
    password.send_keys("admin123")

    login_button = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    login_button.click()

    time.sleep(5)

    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
    time.sleep(5)
    # Adding an Employee

    add_employee_tab = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a")
    add_employee_tab.click()
    time.sleep(3)

    # Employee Details
    fname = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
    fname.send_keys("prajyot")
    mname = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input")
    mname.send_keys("s")

    lname = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
    lname.send_keys("rasal")

    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()

    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("pot123")

    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("password123")
    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("password231")

    try:
        error_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/span")
        error_text = error_element.text.strip()

        assert "passwords do not match" in error_text.lower()
        print("Error msg displayed as : Password do not match")
    except NoSuchElementException:
        print("Error is not displayed")
    time.sleep(5)

    # Task 2
    driver.refresh()
    time.sleep(5)
    fname = driver.find_element(By.XPATH,
                                "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
    fname.send_keys("prajyot")
    mname = driver.find_element(By.XPATH,
                                "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input")
    mname.send_keys("s")

    lname = driver.find_element(By.XPATH,
                                "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
    lname.send_keys("rasal")

    driver.find_element(By.XPATH,
                                   "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()

    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys(
        "p12347")

    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys(
        "password123")
    driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys(
        "password123")


    driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
    time.sleep(5)

    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
    print("Employee created successfully")

    # Logout as admin
    driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

    # Login as new employee
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("p12347")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify dashboard visible
    dashboard_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    assert dashboard_text.is_displayed()
    print("Dashboard page is displayed for new employee")

    # Close the browser
    driver.quit()
