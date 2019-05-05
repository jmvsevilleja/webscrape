chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.binary_location = r'C:\Users\jmvse\AppData\Local\Google\Chrome SxS\Application\chrome.exe'
chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"),
                          options=chrome_options)

driver.get("https://www.duo.com")
driver.quit()