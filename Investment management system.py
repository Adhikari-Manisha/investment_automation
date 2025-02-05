import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

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

try:
    driver.get(login_url)

    # Login process
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email_id)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    sign_in_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "auth")))
    sign_in_button.click()
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
    print("Login Test Passed")

    # Navigate to Portfolio Management
    portfolio_management = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[2]/div'))
    )
    portfolio_management.click()
    print("Navigation to Portfolio Management page successful.")

    # Show dropdown result
    show_dropdown1 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[3]/div[1]/select/option[2]')
        )
    )
    show_dropdown1.click()
    print("Show drop down result successful.")

    # Wait for Transaction tracker page to load
    transaction_tracker = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[3]/div'))
    )
    transaction_tracker.click()
    print("Navigation to Transaction Tracker page successful.")

    # Add tt
    add_tt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div[3]/div/button'))
    )
    add_tt.click()
    print("Add Transaction Tracker page opened successfully.")
    time.sleep(7)

    # company name
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[3]/div/div/div/div[1]/input"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[3]/div/div/div/div[2]/div[3]"))
    ).click()
    print("company name select successfully.")

    # transaction type
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[1]/div/div/div/div[1]/input"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[1]/div/div/div/div[2]/div[1]"))
    ).click()
    print("transaction type select successfully.")

    # quantity
    quantity = "2"
    first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[4]/div/div/input')
        )
    )
    first.send_keys(quantity)
    print("quantity entered successfully.")

    # effective rate
    effective_rate = "100"
    first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[5]/div/div/input')
        )
    )
    first.send_keys(effective_rate)
    print("Effective Rate entered successfully.")

    # calender
    driver.find_element(By.CLASS_NAME, "form-control").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "calender")))

    driver.find_element(By.XPATH,
                        "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[5]").click()

    time.sleep(8)
    print("Date selected successfully.")

    # click save button
    save = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[2]/div/div/div[1]/div/button'))
    )
    save.click()
    print("save button clicked successfully.")
    time.sleep(7)

    # Navigate to FD Tracker
    fd_tracker = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[4]'))
    )
    fd_tracker.click()
    WebDriverWait(driver, 10).until(EC.title_contains("FD Tracker"))
    print("Navigation to fd tracker page successful.")

    # add fixed deposite
    add_fd = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div[3]/div/button'))
    )
    add_fd.click()
    print("Add fd page opened successfully.")
    time.sleep(4)

    # select bank
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[1]/div/div/div/div/div[1]/input"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[1]/div/div/div/div/div[2]/div[1]"))
    ).click()
    print("bank name select successfully.")

    # select branch
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
            By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[1]/div/div/div/div[1]/input"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[1]/div/div/div/div[2]/div[5]"))
    ).click()
    print("branch select successfully.")

    # FD Amount
    fd_amount = "5000"
    first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[4]/div/div/input')
        )
    )
    first.send_keys(fd_amount)
    print("FD Amount entered successfully.")

    #TDS

    TDS_rate = "-4"
    amount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[8]/div/div/input')
        )
    )
    amount.send_keys(TDS_rate)
    print("TDS entered successfully.")


    # FD Reference No
    fd_referenceNumber = "900"
    amount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[6]/div/div/input')
        )
    )
    amount.send_keys(fd_referenceNumber)
    print("FD Reference No entered successfully.")


    # Interest Rate
    interest_rate = "50"
    amount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[7]/div/div/input')
        )
    )
    amount.send_keys(interest_rate)
    print("Interest Rate entered successfully.")

    # FD Account no
    fd_acountNumber = "4325623"
    amount = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[5]/div/div/input')
        )
    )
    amount.send_keys(fd_acountNumber)
    print("FD Amount No entered successfully.")

    # fiscal year
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[2]/div/div/div/div[1]/input"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[2]/div/div/div/div[2]/div[2]"))
    ).click()
    print("select fiscal year successfully.")


    # select interest posting frequency
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[9]/div/div/div/div[1]/input"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[9]/div/div/div/div[2]/div[2]"))
    ).click()
    print("interest posting frequency select successfully.")

    # issued date of FD

    driver.find_element(By.CLASS_NAME, "form-control").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "calender")))

    (driver.find_element(By.XPATH,
                         "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[3]/div/div/div/div")
     .click())

    time.sleep(8)
    print("Date selected successfully.")

    # Tenure
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[10]/div/div/div/div[1]/input"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[10]/div/div/div/div[2]/div[4]"))
    ).click()
    print("Tenure select successfully.")

    # upload file
    file_input = driver.find_element(By.ID, "file-upload")

    # Provide the full path to the file (not just the folder)
    file_path = r"C:\Users\admin\Pictures\Screenshots\your-file-name.png"

    # Upload the file
    file_input.send_keys(file_path)

    print("File uploaded successfully.")
    time.sleep(10)

    # click save button
    save = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[3]/div/div/div[1]/div/button'))
    )
    save.click()
    print("save button clicked successfully.")
    time.sleep(6)

    # Navigate to FD Tracker
    fd_tracker = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[4]'))
    )
    fd_tracker.click()
    WebDriverWait(driver, 10).until(EC.title_contains("FD Tracker"))
    print("Navigation to fd tracker page successful.")


    # click sample download
    download = WebDriverWait(driver, 6).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div[1]/div/button'))
    )
    download.click()
    print("download successfully.")
    time.sleep(10)

    # search
    search = "Civil Bank"
    first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[1]/div/input')
        )
    )
    first.send_keys(search)
    print("search successfully.")


 # Navigate to User Management
    user_management = WebDriverWait(driver, 16).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[5]/div'))
    )
    user_management.click()
    WebDriverWait(driver, 16).until(EC.title_contains("User Management"))
    print("Navigation to User Management page successful.")

    # Add User
    add_user = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/main/div/div[1]/div[2]/div/button'))
    )
    add_user.click()
    print("Add user page opened successfully.")

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
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[6]/div/div/div/div[1]/input"))
    ).click()

    # Wait for the option to be visible
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[6]/div/div/div/div[2]/div[2]"))
    ).click()
    print("Department 'Finance' entered successfully.")

    # Role dropdown
    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[7]/div/div/div/div[1]/input"))
    ).click()

    # Wait for the option to be visible
    WebDriverWait(driver, 12).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[7]/div/div/div/div[2]/div[3]"))
    ).click()
    print("Role selected successfully.")

    # Click submit button
    submit = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[3]/div/div/div/button'))
    )
    submit.click()
    print("Submit button clicked successfully.")

   # #remove popup box
   #  remove_popup = WebDriverWait(driver, 10).until(
   #      EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/main/div/div[1]/div/div[2]/div/div/button'))
   #  )
   #  remove_popup.click()
   #  print("remove popup is successful.")

    WebDriverWait(driver, 9).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[3]/div/div/div/button"))
    ).click()
    WebDriverWait(driver, 9).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "/html/body/div/div/div[2]/main/div/div[1]"))
    ).click()
    print("remove popup is successful.")

    # Navigate to User Management
    user_management = WebDriverWait(driver, 16).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[5]/div'))
    )
    user_management.click()
    WebDriverWait(driver, 16).until(EC.title_contains("User Management"))
    print("Navigation to User Management page successful.")

    #Deleted users

    deleted_user = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/main/div/div[1]/div[1]/div/button'))
    )
    deleted_user.click()
    print("deleted user page opened successfully.")

      #delete user
    WebDriverWait(driver, 8).until(
       EC.element_to_be_clickable(
           (By.XPATH, "/html/body/div/div/div[2]/main/div/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div[1]/div[2]/svg"))
   ).click()

   # Wait for the option to be visible
    WebDriverWait(driver, 12).until(
       EC.visibility_of_element_located(
           (By.XPATH, "/html/body/div/div/div[2]/main/div/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/div/button"))
).click()
    print("permanent delete successfully.")

    # Click on "Master Data" dropdown
    master_data = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[8]'))
    )
    master_data.click()
    WebDriverWait(driver, 16).until(EC.title_contains("master data"))
    print("Navigation to master data page successful.")

    # Click Securities Setup
    Securities_setup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[9]/div'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", Securities_setup)
    Securities_setup.click()
    WebDriverWait(driver, 16).until(EC.title_contains("Securities setup"))
    print("Securities setup page successful.")

        # Add Securities
    add_securities = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div/div/button'))
    )
    add_securities.click()
    print("Add securities page opened successfully.")

finally:

    time.sleep(6)
    #driver.quit()