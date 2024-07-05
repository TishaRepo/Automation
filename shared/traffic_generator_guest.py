from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import os


def set_environment():

    """
    set proxy according to the user
    """
    os.environ['DISPLAY'] = ':1'
    os.environ['XAUTHORITY'] = os.path.expanduser('~/.Xauthority')
    os.environ['http_proxy'] = 'http://proxy62.iitd.ac.in:3128/'
    os.environ['https_proxy'] = 'http://proxy62.iitd.ac.in:3128/'


# Function to visit YouTube and play a video on AI
def visit_youtube_and_play_video(driver, keyword):
    driver.get("https://www.youtube.com")
    time.sleep(5)  # Wait for the page to load

    # Search for a topic
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for search results to load

    # Play the first video
    first_video = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "video-title")))
    first_video.click()
    time.sleep(60)  # Watch the video for 60 seconds


def extract_links(url):
    """
    Function to extract all links from a given URL.

    Args:
    - url (str): The URL of the page to extract links from.

    Returns:
    - list: A list of URLs extracted from the page.
    """
    try:
        # Navigate to the URL
        driver.get(url)

        # Wait for some time for the page to load (you can adjust this time as needed)
        time.sleep(5)

        # Find all links on the page
        links = driver.find_elements(By.TAG_NAME, "a")

        # Extract URLs of all links
        all_links = []
        for link in links:
            href = link.get_attribute("href")
            if href and "http" in href:  # Ensure it's a valid HTTP link
                all_links.append(href)

        return all_links

    except Exception as e:
        print(f"Error extracting links from {url}: {e}")
        return []


# Function to visit Imgur, scroll through feed, and visit 2 links
def visit_imgur_and_visit_links(driver, keywords):
    # Step 1: Initialize Chrome driver instance and visit Imgur
    imgur_url = "https://imgur.com/"

    try:
        # Visit Imgur homepage
        driver.get(imgur_url)

        # Wait for the search input field to be visible
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
        )

        # Visit up to three links of different keywords
        visited_count = 0
        for keyword in keywords:
            if visited_count >= 3:
                break

            print(f"Searching for '{keyword}' on Imgur...")
            search_input.clear()
            search_input.send_keys(keyword)
            search_input.submit()

            # Wait for the search results page to load
            time.sleep(5)

            # Extract links from the search results page
            search_links = extract_links_currentPage()
            print(f"Extracted links from search results for '{keyword}': {search_links}")

            # Filter articles containing the keyword in their URL
            keyword_articles = [link for link in search_links if keyword in link]
            if keyword_articles:
                # Visit the first article found for the keyword
                article_url = keyword_articles[0]
                print(f"Visiting article containing '{keyword}': {article_url}")

                # Visit the keyword article URL
                driver.get(article_url)

                # Wait for the page to load
                time.sleep(5)

                # Optionally perform actions on the page

                # Navigate back to the search results page for the next iteration
                driver.get(imgur_url)
                search_input = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
                )

                visited_count += 1
            else:
                print(f"No articles found containing '{keyword}' in the URL.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser after visiting all articles
        time.sleep(10)


def extract_links_currentPage():
    """
    Function to extract all links from the current page using Selenium.

    Returns:
    - list: A list of URLs extracted from the page.
    """
    try:
        # Find all links on the page
        links = driver.find_elements(By.TAG_NAME, "a")

        # Extract URLs of all links
        all_links = []
        for link in links:
            href = link.get_attribute("href")
            if href:
                all_links.append(href)

        return all_links

    except Exception as e:
        print(f"Error extracting links: {e}")
        return []


def visit_wikipedia_and_visit_links(driver, keyword):
    #  Initialize Chrome driver instance and visit Wikipedia
    wiki_url = "https://www.wikipedia.org/"
    search_term = "AI"

    try:
        # Visit Wikipedia homepage
        driver.get(wiki_url)

        # Wait for the search input field to be visible
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "searchInput"))
        )

        # Type the search term "AI" into the search input field
        search_input.clear()
        search_input.send_keys(search_term)

        # Submit the search
        search_input.submit()

        # Wait for the search results page to load
        time.sleep(5)

        # Extract links from the search results page
        search_links = extract_links(driver.current_url)
        print(f"Extracted links from search results: {search_links}")

        # Filter and visit up to three articles containing "keyword" in their URL
        if search_links:
            computer_articles = [link for link in search_links if keyword in link]
            if computer_articles:
                for i in range(min(3, len(computer_articles))):
                    computer_article_url = computer_articles[i]
                    print(f"Visiting article {i + 1} containing 'computer': {computer_article_url}")

                    # Visit the computer article URL
                    driver.get(computer_article_url)

                    # Wait for the page to load
                    time.sleep(5)

                    # Optionally perform actions on the page

                    # Navigate back to the search results page for the next iteration
                    driver.back()
                    time.sleep(3)  # Adjust waiting time as needed

            else:
                print("No articles found containing 'computer' in the URL.")
        else:
            print("No article links found.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser after visiting all articles
        time.sleep(10)


def login_using_gmail(driver, url, gmail_id, password):
    try:

        # Open Gmail login page
        driver.get(url)

        # Wait for the email input field to be visible and enter Gmail ID
        email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email_field.send_keys(gmail_id)

        # Click on the "Next" button
        next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]')
        next_button.click()

        time.sleep(2)  # Wait for the password input field to be visible

        # Wait for the password input field to be visible and enter password
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        password_field.send_keys(password)

        # Click on the "Next" button to login
        next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]')
        next_button.click()

        time.sleep(5)  # Wait for login to complete

        print('Login Successful...!!')

        return driver

    except Exception as e:
        print(f'Login Failed: {e}')
        return None


def view_email(driver, subject_keyword):
    try:
        # Wait for the Gmail inbox to load
        time.sleep(5)  # Adjust timing as needed

        # Locate the search input field to search for emails
        search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search mail"]')

        # Enter the subject keyword to search for emails
        search_input.send_keys(f'subject:{subject_keyword}')
        search_input.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for search results

        # Click on the first email (assuming it's the one we're interested in)
        first_email = driver.find_element(By.XPATH, '//div[@role="main"]//tr[1]')
        first_email.click()

        time.sleep(5)  # Wait for the email to open

        # Now you can extract or interact with the email content as needed

    except Exception as e:
        print(f'Error viewing email: {e}')


def gmail_view(driver, gmail_id, password):
    url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&amp;service=mail&amp;sacu=1&amp;rip=1&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin"
    # Login to Gmail account
    driver = login_using_gmail(driver, url, gmail_id, password)

    if driver:
        try:
            # Example: View an email with subject containing "Important"
            view_email(driver, "Important")

        finally:
            # Close the browser session
            time.sleep(5)


def create_blank_document_and_rename(driver):
    try:
        # Wait for the "Blank" document option to be clickable
        blank_doc_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//img[contains(@src, "docs-blank")]'))
        )
        blank_doc_button.click()

        # Wait for the new document to load
        time.sleep(5)

        # Rename the document with double click
        rename = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'docs-title-input'))
        )
        actions = ActionChains(driver)
        actions.double_click(rename).perform()  # Double click to rename

        docname = "test" + str(random.randint(1, 600))
        rename.clear()
        rename.send_keys(docname)
        rename.send_keys(Keys.RETURN)

        # Wait for the document name to be saved
        time.sleep(5)

        print("Document renamed successfully.")

    except Exception as e:
        print(f"Error creating blank document or renaming it: {e}")


def visit_google_docs(driver, gmail_id, password):
    # Replace with your Gmail account credentials

    google_docs_url = "https://docs.google.com/document/"

    # Login to Google Docs account  if not already logged in else set the driver for GoogleDocs here itself

    # driver = login_using_gmail(driver,google_docs_url,gmail_id, password)

    driver.get("https://docs.google.com/document/")
    if driver:
        try:
            # Rename the document without typing anything into the body
            create_blank_document_and_rename(driver)

        finally:
            # Close the browser session
            driver.quit()


if __name__ == "__main__":
    set_environment()
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Visit YouTube and play a video of the searched keyword
    keyword = "AI"
    visit_youtube_and_play_video(driver, keyword)
    time.sleep(20)  # Wait for 20 seconds before the next site
    print("Done visiting YOuTUbe !!!")

    # Visit Imgur fot the keywords from the list
    keywords = ["happy", "funny", "sad", "anime", "cry", "day", "new", "ai", "cartoon", "computer"]
    visit_imgur_and_visit_links(driver, keywords)
    time.sleep(20)
    print("Done visiting Imgur !!!")

    # Visit Wikipedia for the links that contain the keyword set
    keyword = "computer"
    visit_wikipedia_and_visit_links(driver, keyword)
    time.sleep(20)
    print("Done visiting Wikipedia !!!")

    # Credentials for gmail-account that needs to be visited
    gmail_id = "fiveg4099@gmail.com"
    password = "fivegsecurity"

    # Visit Gmail
    gmail_view(driver, gmail_id, password)
    time.sleep(20)
    print("Done visiting Gmail !!!")

    # Visit GoogleDocs
    visit_google_docs(driver, gmail_id, password)
    time.sleep(20)
    print("Done visiting GoogleDocs !!!")

