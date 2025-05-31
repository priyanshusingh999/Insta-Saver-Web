import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver

st.title("Instagram Downloader")
st.image("https://www.fonelab.com/images/tips/download-instagram.png", caption="Instagram Reel Story Photo Downloader")

by_user = st.text_input("Enter URL to download:")
resolution = st.selectbox("Select what do you want to download:", ["Reel", "Story", "Photo"])

if st.button("Click to Downloading"):
    progress_bar = st.progress(0)
    driver = create_driver()
    try:
        progress_bar.progress(10)
        if resolution == "Reel":
            driver.get("https://fastdl.app/video")
        elif resolution == "Story":
            driver.get("https://fastdl.app/story-saver")
        elif resolution == "Photo":
            driver.get("https://fastdl.app/photo")
        else:
            st.error("Invalid selection")
            driver.quit()
            st.stop()

        progress_bar.progress(30)
        wait = WebDriverWait(driver, 10)
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-form-input"]')))
        input_box.clear()
        input_box.send_keys(by_user)

        progress_bar.progress(60)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[1]/form/button')))
        download_button.click()

        progress_bar.progress(80)
        download_link_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/div/div/ul[1]/li/div[2]/a')))
        download_link = download_link_element.get_attribute("href")

        progress_bar.progress(100)
        if download_link:
            st.markdown(f"[Click to Download]({download_link})")
            st.success("Download link generated successfully!")
        else:
            st.error("Download link not found.")
    except Exception as e:
        st.error(f"An error occurred while downloading")
    finally:
        driver.quit()
        progress_bar.empty()
