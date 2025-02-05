import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import pytest

# Generate random email
def generate_random_email():
    return ''.join(random.choices(string.digits, k=4)) + str(int(time.time())) + "@blondmail.com"

# Chrome options setup
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Credentials and URL
email_id = "superadmin@investment.com"
password = "Investment@2024"
login_url = "https://ims.mangosoftsolution.com/"

@pytest.fixture(scope="module")
def setup():
    driver.get(login_url)
    yield driver
    driver.quit()

def test_login(setup):
    try:
        # Login process
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email_id)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        sign_in_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "auth")))
        sign_in_button.click()
        WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        print("Login Test Passed")
    except TimeoutException as e:
        pytest.fail(f"Login failed: {str(e)}")

def test_navigation_to_portfolio_management(setup):
    try:
        # Navigate to Portfolio Management
        portfolio_management = WebDriverWait(driver, 12).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[2]/div'))
        )
        portfolio_management.click()
        print("Navigation to Portfolio Management page successful.")
    except TimeoutException as e:
        pytest.fail(f"Navigation failed: {str(e)}")

def test_transaction_tracker_page(setup):
    try:
        # Wait for Transaction tracker page to load
        transaction_tracker = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[3]/div'))
        )
        transaction_tracker.click()
        print("Navigation to Transaction Tracker page successful.")
    except TimeoutException as e:
        pytest.fail(f"Navigation failed: {str(e)}")

def test_add_transaction_tracker(setup):
    try:
        # Add transaction tracker
        add_tt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div[3]/div/button'))
        )
        add_tt.click()
        print("Add Transaction Tracker page opened successfully.")
        time.sleep(7)
    except TimeoutException as e:
        pytest.fail(f"Failed to add transaction tracker: {str(e)}")

def test_add_fd_tracker(setup):
    try:
        # Navigate to FD Tracker
        fd_tracker = WebDriverWait(driver, 12).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[4]'))
        )
        fd_tracker.click()
        WebDriverWait(driver, 10).until(EC.title_contains("FD Tracker"))
        print("Navigation to FD Tracker page successful.")

        # Add fixed deposit
        add_fd = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div[3]/div/button'))
        )
        add_fd.click()
        print("Add FD page opened successfully.")
    except TimeoutException as e:
        pytest.fail(f"Failed to navigate to FD Tracker or add FD: {str(e)}")

        def test_fd_tracker_actions(setup):
            try:
                # Navigate to FD Tracker
                print("Navigating to FD Tracker page...")
                fd_tracker = WebDriverWait(driver, 12).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[4]'))
                )
                fd_tracker.click()
                WebDriverWait(driver, 10).until(EC.title_contains("FD Tracker"))
                print("Navigation to FD Tracker page successful.")

                # Click sample download
                print("Downloading sample...")
                download = WebDriverWait(driver, 6).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div[1]/div/button'))
                )
                download.click()
                print("Download initiated successfully.")
                time.sleep(10)

                # Perform search
                search_text = "Civil Bank"
                print(f"Performing search for: {search_text}")
                search_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[1]/div/input')
                    )
                )
                search_input.send_keys(search_text)
                print("Search executed successfully.")
            except TimeoutException as e:
                pytest.fail(f"FD Tracker actions failed: {str(e)}")

def test_user_management(setup):
    try:
        # Navigate to User Management
        user_management = WebDriverWait(driver, 16).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[5]/div'))
        )
        user_management.click()
        WebDriverWait(driver, 16).until(EC.title_contains("User Management"))  # Ensure page is loaded
        print("Navigation to User Management page successful.")

        # Add User
        add_user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/main/div/div[1]/div[2]/div/button'))
        )
        add_user.click()
        print("Add user page opened successfully.")
    except TimeoutException as e:
        pytest.fail(f"Failed to navigate to User Management or add user: {str(e)}")

def test_add_user_details(setup):
    try:
        # User create form
        FirstName = "live"
        first = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[1]/div/div/input')
            )
        )
        first.send_keys(FirstName)
        print("First name entered successfully.")

        # Last name
        LastName = "test"
        last = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[3]/div/div/input')
            )
        )
        last.send_keys(LastName)
        print("Last name entered successfully.")

        # Generate and enter email
        email_id = generate_random_email()
        print(f"Generated email: {email_id}")
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[4]/div/div/input'))
        )
        email_input.send_keys(email_id)
        print("Email entered successfully.")
    except TimeoutException as e:
        pytest.fail(f"Failed to enter user details: {str(e)}")

        # Mobile number
        mobilenumber = "9867382590"
        mobile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[5]/div/div/input')
            )
        )
        mobile.send_keys(mobilenumber)
        print("Mobile number entered successfully.")

        time.sleep(9)

        # Department dropdown
        WebDriverWait(driver, 9).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[6]/div/div/div/div[1]/input"))
        ).click()

        # Wait for the option to be visible
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[6]/div/div/div/div[2]/div[2]"))
        ).click()
        print("Department 'Finance' entered successfully.")

        # Role dropdown
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[7]/div/div/div/div[1]/input"))
        ).click()

        # Wait for the option to be visible
        WebDriverWait(driver, 12).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[7]/div/div/div/div[2]/div[3]"))
        ).click()
        print("Role selected successfully.")

        # Click submit button
        submit = WebDriverWait(driver, 12).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[3]/div/div/div/button'))
        )
        submit.click()
        print("Submit button clicked successfully.")
    except TimeoutException as e:
        pytest.fail(f"Failed to enter user details: {str(e)}")



    if __name__ == "__main__":
        pytest.main()

