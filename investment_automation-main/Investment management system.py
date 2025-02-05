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

# generate a random mobile number
def generate_random_mobile_number():
    return "98" + str(random.randint(100000000, 999999999))
#generate FD ammount
fd_amount = str(random.randint(1000, 50000))

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
    
    #random company name select
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[3]/div/div/div/div[1]/input"))
).click()

# Wait for the dropdown options to be visible
    dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located(
        (By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[3]/div/div/div/div[2]/div"))
)

# Select a random company from the dropdown options
    random_company = random.choice(dropdown_options)
    random_company.click()

    print("Company name selected successfully.")

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

    # Wait for the dropdown options to be visible and select a random bank
    bank_options = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[1]/div/div/div/div/div[2]/div"))
    )
    random_bank = random.choice(bank_options)
    random_bank.click()
    print("Bank name selected successfully.")

    # select branch
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[1]/div/div/div/div[1]/input"))
    ).click()

    # Wait for the dropdown options to be visible and select a random branch
    branch_options = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, "/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[1]/div/div/div/div[2]/div"))
    )
    random_branch = random.choice(branch_options)
    random_branch.click()
    print("Branch selected successfully.")

    # FD Amount
    first = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[4]/div/div/input')
    )
)
    first.send_keys(fd_amount)
    print(f"FD Amount of {fd_amount} entered successfully.")

    #TDS
    TDS_rate = str(random.randint(-1, 99))

    amount = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[8]/div/div/input')
    )
)
    amount.send_keys(TDS_rate)
    print(f"TDS rate of {TDS_rate} entered successfully.")

    # FD Reference No
    fd_referenceNumber = str(random.randint(100, 9999))

# Locate the input field and enter the random FD reference number
    amount = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[6]/div/div/input')
    )
)
    amount.send_keys(fd_referenceNumber)
    print(f"FD Reference Number '{fd_referenceNumber}' entered successfully.")


    # # Interest Rate
    # interest_rate = "50"
    # amount = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[7]/div/div/input')
    #     )
    # )
    # amount.send_keys(interest_rate)
    # print("Interest Rate entered successfully.")
    
    #random Interest Rate
    interest_rate = random.randint(1, 100)

    amount = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[7]/div/div/input')
    )
)

    amount.send_keys(str(interest_rate))
    print(f"Interest Rate of {interest_rate}% entered successfully.")

    # FD Account no
    fd_accountNumber = str(random.randint(1000000, 9999999))

# Locate the input field and enter the random FD account number
    amount = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/fieldset/form/div[2]/div[5]/div/div/input')
    )
)
    amount.send_keys(fd_accountNumber)
    print(f"FD Account Number '{fd_accountNumber}' entered successfully.")

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
    file_path = r"C:\Users\admin\Pictures\image.jpg"

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
    banks = ["Civil Bank", "Nabil Bank", "Everest Bank Limited	", "Himalayan Bank","Nepal Infrastructure Bank Ltd.","Sanima Bank Ltd.","Manjushree Finance Limited"]

# search a random bank from the list
    search = random.choice(banks)
    first = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[1]/div/input')
    )
)
    first.send_keys(search)
    print(f"Search for {search} successfully.")
    
    FD_Report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[6]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", FD_Report)
    FD_Report.click()
    print("Clicked on FD Report.")
    time.sleep(10)
    
    
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
    FirstName = "demo"
    first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[1]/div/div/input')
        )
    )
    first.send_keys(FirstName)
    print("First name entered successfully.")
    
    #middle
    MiddleName = "live"
    middle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[2]/div/div/input')
        )
    )
    middle.send_keys(MiddleName)
    print("middle name entered successfully.")

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
    mobilenumber = generate_random_mobile_number()

    mobile = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div/fieldset/form/div[1]/div[5]/div/div/input')
    )
)

    mobile.send_keys(mobilenumber)
    print("Mobile number entered successfully:", mobilenumber)

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
    

    # Wait for FD Report page to load (check for unique element or title)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[6]'))
    )
    print("Navigation to FD Report page successful.")

    # Navigate to Bankwise Report
    Bankwise_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[7]/div'))
    )
    Bankwise_report.click()
    print("Clicked on Bankwise Report.")

    # Wait for Bankwise Report page to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[7]/div'))
    )
    print("Navigation to Bankwise Report page successful.")
    
        # search Bankwise Report
    banks = ["Civil Bank", "Karnali Development Bank Ltd.", "Kamana Sewa Bikas Bank Ltd.", "Shree Investment And Finance Co.Ltd","Nepal Infrastructure Bank Ltd.","NIC Asia Bank Limited","Best Finance Company Ltd."]

# search a random bank from the list
    search = random.choice(banks)
    first = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/div[1]/div/div/div[1]/div/input')
    )
)
    first.send_keys(search)
    print(f"Search for {search} successfully.")
    
    # calender BankWise Report
    driver.find_element(By.CLASS_NAME, "form-control").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "calender")))

    driver.find_element(By.XPATH,
                        "/html/body/div/div/div[2]/main/div/div/div/div/div[1]/div/div/div[2]/div/fieldset/form/div/div[1]/div[2]/div/div/div/div/table/tbody/tr[4]/td[6]").click()

    time.sleep(8)
    print("Date selected successfully.")
    
       # click Filter Data
    save = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/div[1]/div/div/div[2]/div/fieldset/form/div/div[2]/div/div/button'))
    )
    save.click()
    print("Filter Data button clicked successfully.")
    time.sleep(7)
    
        # Show dropdown result
    show_dropdown1 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/div[3]/div/select')
        )
    )
    show_dropdown1.click()
    print("Show drop down result successful.")

    

except TimeoutException as e:
    print("TimeoutException:", str(e))
    print("Current URL:", driver.current_url)
    print("Current Title:", driver.title)
except Exception as e:
    print("An error occurred:", str(e))
    

    

   # #remove popup box
    # WebDriverWait(driver, 9).until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[3]/div/div/div/button"))
    # ).click()
    # WebDriverWait(driver, 9).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH,
    #          "/html/body/div/div/div[2]/main/div/div[1]"))
    # ).click()
    # print("remove popup is successful.")
    
#     # Wait and close the first popup
#     cross1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/main/div/div/fieldset/form/div[3]/div/div/div/button")))
#     cross1.click()

# except Exception as e:
#     print("Remove popup is unsuccessful:", e)

    # # Navigate to User Management
    # user_management = WebDriverWait(driver, 16).until(
    #     EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[5]/div'))
    # )
    # user_management.click()
    # WebDriverWait(driver, 16).until(EC.title_contains("User Management"))
    # print("Navigation to User Management page successful.")

#     #Deleted users

#     deleted_user = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/main/div/div[1]/div[1]/div/button'))
#     )
#     deleted_user.click()
#     print("deleted user page opened successfully.")

#       #delete user
#     # Get a list of all the user rows in the table
#     user_rows = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, "/html/body/div/div/div[2]/main/div/div[3]/div[2]/div/table/tbody/tr"))
#     )

#     # Select a random user row from the table
#     random_user = random.choice(user_rows)

#     # Click the delete button
#     delete_button = random_user.find_element(By.XPATH, "html/body/div/div/div[2]/main/div/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div[1]/div[2]/svg")
#     delete_button.click()

#     # Wait for the delete confirmation button to be visible and click it
#     WebDriverWait(driver, 12).until(
#         EC.visibility_of_element_located(
#             (By.XPATH, "/html/body/div/div/div[2]/main/div/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/div/button"))
#     ).click()

#     print("Permanent delete successfully.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")


#master data 
    master_data = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[8]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", master_data)  
    master_data.click()
    WebDriverWait(driver, 16).until(EC.title_contains("master data"))
    print("Navigation to Master Data page successful.")
    
    #securities setup
    securities_setup = WebDriverWait(driver, 16).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[9]/div'))
    )
    securities_setup.click()
    WebDriverWait(driver, 16).until(EC.title_contains("securities setup"))
    print("Navigation to securities setup page successful.")

    # Add Securities
    add_securities = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div[2]/div/div/button')
        )
    )
    add_securities.click()
    print("Add Securities page opened successfully.")

# except TimeoutException as e:
#     print(f"An element was not clickable or not found within the timeout period: {e}")

# except Exception as e:
#     print(f"An error occurred: {e}")
    
    
finally:

    time.sleep(6)
    # driver.quit()