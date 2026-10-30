from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    html_path = Path(__file__).resolve().parent.parent / "my-app" / "index.html"
    print("Путь к HTML:", html_path)
    print("Файл существует:", html_path.exists())

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get(html_path.as_uri())
    print("Заголовок страницы:", browser.title)
    print("Адрес страницы:", browser.current_url)

    yield browser

    browser.quit()

def test_add_task(driver):
    input_field = driver.find_element(By.ID, "taskInput")
    button = driver.find_element(By.ID, "addTaskBtn")
    input_field.send_keys("Не покупать билет на колобка")
    button.click()
    tasks = driver.find_elements(By.TAG_NAME, "li")

    assert len(tasks) == 1
    assert tasks[0].text == "Не покупать билет на колобка"

def test_add_multiple_tasks(driver):
    input_field = driver.find_element(By.ID, "taskInput")
    button = driver.find_element(By.ID, "addTaskBtn")
    input_field.send_keys("Первая задача")
    button.click()
    input_field.send_keys("Вторая задача")
    button.click()
    tasks = driver.find_elements(By.TAG_NAME, "li")

    assert len(tasks) == 2

def test_empty_task_not_added(driver):
    button = driver.find_element(By.ID, "addTaskBtn")
    button.click()
    tasks = driver.find_elements(By.TAG_NAME, "li")

    assert len(tasks) == 0