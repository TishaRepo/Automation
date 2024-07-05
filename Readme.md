
## Automated Web Interaction and Traffic Generation Script  
  
This repository contains scripts designed to automate various web interactions using Selenium and generate network traffic in a virtual environment. The primary script (`traffic_generator.sh`) sets up a Vagrant environment, starts a VNC server, and executes a traffic generation script within the Vagrant environment.  
  
---  
  
### Prerequisites  
  
Before running the script, ensure you have the following installed:  
  
- Vagrant  
- VirtualBox  
- VNC Viewer  (in host machine)
- Python 3.x  (in vagrant as well as host machine)
- Selenium package for Python  
- Chrome WebDriver (compatible with your Chrome browser version in both machines)  
- Google Chrome browser  (in both machines)
  
---  
  
### Setup

1. **Set Vagrant** :
        Refer [here](https://github.com/spring-iitd/Cellular-Security/blob/main/docs/vagrant_cheatsheet.md) for  the vagrant setup and installation.

2. **Install Selenium**:  

    ```bash
        python3 -m venv venv # make an environment
        source ./venv/bin/activate
        pip3 install selenium  # install selenium for it
    ```  

    <!-- 3. **Download Chrome WebDriver**:  
    Download the appropriate Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Ensure the downloaded `chromedriver` executable is in your system PATH or specify its location in the script.   -->

3. **Download Chrome WebBrowser**:

 Refer [this] (<https://www.wikihow.com/Install-Google-Chrome-Using-Terminal-on-Linux>) article to download chrome via terminal in a linux environment.

  ```bash
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
  ```

4. Install tight-vnc-viewer
 sudo -E apt install xtightvncviewer


---  
  
### Script Overview  
  
### `traffic_generator.sh`  
  
This script performs the following actions:  
  
1. **Reloads the Vagrant environment**:  
  
    ```bash  
    vagrant reload  
    ```  
  
2. **Starts a VNC server on the `ran_ue_nw` virtual machine**:  
  
    ```bash  
    vagrant ssh ran_ue_nw -c 'nohup vncserver & sleep 2'  
    ```  
  
3. **Opens the VNC viewer and connects to the VNC server**:  
  
    ```bash  
    (vncviewer 127.0.0.1:5911 -passwd pass.txt &)  
    ```  
  
4. **Executes the `traffic_generator_guest.py` script within the Vagrant environment using Python 3**:  
  
    ```bash  
    vagrant ssh ran_ue_nw -c 'python3 /home/vagrant/traffic_generator_guest.py > /home/vagrant/traffic_generator.log 2>&1'  
    ```  
### `traffic_generator_guest.py`  
  
  
### Main Functions  
  
1. **YouTube Video Player**:  
  
    - Visits YouTube, searches for a keyword,  and plays the first video.  
    - Utilizes search functionality and waits for the first video to become clickable before playing it.  
  
    ```python  
    def visit_youtube_and_play_video(driver,keyword):  
        # Function implementation  
        # ...  
      
    # Usage  
    keyword="AI"
    visit_youtube_and_play_video(driver, keyword)  
    ```  
  
2. **Imgur Link Visitor**:  
  
    - Searches for multiple keywords on Imgur and visits links containing those keywords.  
    - Extracts links from the search results and visits those that match the specified keywords.  
  
    ```python  
    def visit_imgur_and_visit_links(driver, keywords):  
        # Function implementation  
        # ...  
      
    # Usage  
    keywords = ["happy", "funny", "sad", "anime", "cry"]  
    visit_imgur_and_visit_links(driver, keywords)  
    ```  
  
3. **Wikipedia Link Visitor**:  
  
    - Searches for "AI" on Wikipedia and visits links containing the specified keyword in their URLs.  
    - Extracts and filters links based on the keyword, then visits relevant articles.  
  
    ```python  
    def visit_wikipedia_and_visit_links(driver, keyword):  
        # Function implementation  
        # ...  
      
    # Usage  
    visit_wikipedia_and_visit_links(driver, "computer")  
    ```  
  
4. **Gmail Login and Email Viewer**:  
  
    - Logs into Gmail using provided credentials and views the first email containing a specified subject keyword.  
    - Navigates through the Gmail interface to locate and open the desired email.  
  
    ```python  
    def gmail_view(driver, gmail_id, password):  
        # Function implementation  
        # ...  
      
    # Usage  
    gmail_view(driver, "your_email@gmail.com", "your_password")  
    ```  
  
5. **Google Docs Document Creator**:  
  
    - Logs into Google Docs, creates a blank document, and renames it.  
    - Handles the document creation interface and performs renaming operations.  
  
    ```python  
    def visit_google_docs(driver, gmail_id, password):  
        # Function implementation  
        # ...  
      
    # Usage  
    visit_google_docs(driver, "your_email@gmail.com", "your_password")  
    ```  
  

  
### Utility Functions  
  
1. **Login to Gmail**:  
  
    - Logs into a Gmail account using provided credentials.  
    - Handles the login process including entering the email and password, and navigating through any additional security steps.  
  
    ```python  
    def login_using_gmail(driver, url, gmail_id, password):  
        # Function implementation  
        # ...  
      
    # Usage  
    login_using_gmail(driver, "https://accounts.google.com/signin", "your_email@gmail.com", "your_password")  
    ```  
  
2. **View Gmail Email**:  
  
    - Views an email with a specific subject keyword.  
    - Searches through the inbox to find and open an email that matches the provided keyword.  
  
    ```python  
    def view_email(driver, subject_keyword):  
        # Function implementation  
        # ...  
      
    # Usage  
    view_email(driver, "Important")  
    ```  
  
3. **Create and Rename Google Docs Document**:  
  
    - Creates a blank Google Docs document and renames it.  
    - Manages the Google Docs interface to create a new document and change its title.  
  
    ```python  
    def create_blank_document_and_rename(driver):  
        # Function implementation  
        # ...  
      
    # Usage  
    create_blank_document_and_rename(driver)  
    ```  
  
4. **Extract Links from Current Page**:  
  
    - Extracts all hyperlinks from the current page.  
    - Gathers all URLs present on the page for further processing or navigation.  
  
    ```python  
    def extract_links_currentPage(driver):  
        # Function implementation  
        # ...  
      
    # Usage  
    links = extract_links_currentPage(driver)  
    ```  
  
5. **Extract Links from a Given URL**:  
  
    - Extracts all hyperlinks from a specified URL.  
    - Opens the given URL, retrieves all links on the page, and filters them as necessary.  
  
    ```python  
    def extract_links(driver, url):  
        # Function implementation  
        # ...  
      
    # Usage  
    links = extract_links(driver, "https://www.example.com")  
    ```  
 ---   
### Usage  
  
To run the script, follow these steps:  
  
1. **Ensure the Vagrant environment is set up and running**:  
  
    Make sure the Vagrant environment is properly configured and running. You can check the status of the Vagrant machines using the following command:  
  
    ```bash  
    vagrant status  
    ```  
  
2. **Execute the script**:  
  
    Run the `traffic_generator.sh` script to automate the setup and execution process:  
  
    ```bash  
    ./traffic_generator.sh  
    ```  
  
    This will reload the Vagrant environment, start the VNC server, open the VNC viewer, and execute the `traffic_generator_guest.py` script within the Vagrant environment.  
  
---  
  
## Additional Information  
  
- **Environment Variables**: The script may set environment variables necessary for running the VNC server and accessing the virtual machine such as proxy.  
- **Log Files**: The output of the `traffic_generator_guest.py` script is redirected to `/home/vagrant/traffic_generator.log` within the Vagrant environment for debugging and analysis.  
  
By following this README, you will be able to set up and run the script to automate various web interactions and generate network traffic efficiently. For more detailed instructions and customization, refer to the comments within the scripts themselves.
