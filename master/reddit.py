from .audio import to_speech

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create Google Chrome driver
def create_driver(url: str) -> webdriver:
    options = Options()
    options.add_argument('--disable-notifications')
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get(url)

    return driver

# Check for NSFW alert and close it if it exists
def check_nsfw(driver: webdriver) -> None:
    content_gate = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid=\"content-gate\"]")
    if not content_gate: return False

    yes = content_gate[0].find_element(by=By.TAG_NAME, value="button")
    yes.click()

    see_nsfw = driver.find_elements(by=By.CLASS_NAME, value="gCpM4Pkvf_Xth42z4uIrQ")
    if not see_nsfw: return True

    see_nsfw[0].click()
    return True

# Set Reddit to darkmode
def set_darkmode(driver: webdriver) -> None:
    dropdown_button = driver.find_element(by=By.ID, value="USER_DROPDOWN_ID")
    dropdown_button.click()

    dropdown_menu = driver.find_element(by=By.CLASS_NAME, value="_2uYY-KeuYHKiwl-9aF0UiL")
    buttons = dropdown_menu.find_elements(by=By.TAG_NAME, value="button")
    settings_button = buttons[9]

    settings_button.click()

    darkmode_button = dropdown_menu.find_element(by=By.CLASS_NAME, value="nBh6t8H3UNZpI1Ce9s6yQ")
    
    darkmode_button.click()
    dropdown_button.click()

# Check whether given comment is from MOD
def is_mod(comment) -> bool:
    return bool(comment.find_elements(by=By.CLASS_NAME, value="LWgI-A6rN9Wajn1VLxu2A"))

# Get comments and return list with the path for their text-to-speech file and to their screenshot
def get_comments(driver: webdriver, n: int) -> list:
    data = []
    comments = driver.find_elements(by=By.CLASS_NAME, value="_1z5rdmX8TDr6mqwNv7A70U")

    saved = 0

    for i in range(len(comments)):
        c = comments[i]
        if is_mod(c): continue

        saved += 1

        text = '. '.join([i.text for i in c.find_elements(by=By.CLASS_NAME, value="_1qeIAgB0cPwnLhDF9XSiJM ")])

        audio_path = 'temp/audios/comment{}.mp3'.format(saved)
        screenshot_path = 'temp/pictures/comment{}.png'.format(saved)

        to_speech(text, audio_path)
        c.screenshot(screenshot_path)

        data.append({"audio": audio_path, "screenshot": screenshot_path})
        if saved + 1 > n: break
    return data

# Get title and return dictionary with path to its text-to-speech file and its screenshot
def get_title(driver: webdriver) -> dict:
    title = driver.find_element(by=By.CLASS_NAME, value="_1oQyIsiPHYt6nx7VOmd1sz")
    text = title.find_element(by=By.TAG_NAME, value="h1").text

    audio_path = 'temp/audios/title.mp3'
    screenshot_path = 'temp/pictures/title.png'

    to_speech(text, audio_path)
    title.screenshot(screenshot_path)

    return {"audio": audio_path, "screenshot": screenshot_path}

