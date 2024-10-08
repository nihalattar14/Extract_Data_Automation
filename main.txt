import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from communities import get_community_data
from available_home import get_avaialableHome_data


def start(url,state):
    url = url

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[contains(@class,'state-item-link')]/h6[contains(text(),'Arizona')]").click()
    driver.find_element(By.XPATH, "//a[contains(@class,'title-link')]/h6[contains(text(),'Arizona')]").click()
    driver.find_element(By.XPATH, "//span[contains(@class,'tabLabel') and contains(text(),'Communities')]").click()
    extract_communities(state,driver)
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[contains(@class,'tabLabel') and contains(text(),'Available homes')]").click()
    extract_avaialable_home(state,driver)

    driver.quit()

def extract_communities(state,drive):
    community_data = get_community_data(state,drive)
    community_data.to_csv('Assessment_NihalAttar_CommunityData.csv', index=False)
    dtype_reasons = {
        "State": "string, state abbreviation",
        "Name": "string, community name",
        "Notes": "list of strings, additional information about the community",
        "Latitude": "Not available",
        "Longitude": "Not available",
        "Address": "string, full address of the community",
        "Pricing": "string, price range of homes in the community",
        "Area": "string, area of the community in sq. ft.",
        "URL": "string, URL to the community page",
        "Specifications": "string, List of bed, bath, Garage",
    }
    with open('Assessment_NihalAttar_CommunityData_DTypeReason.docx', 'w') as file:
        for column, reason in dtype_reasons.items():
            file.write(f"{column}: {reason}\n")
    print("Community data have been saved.")

def extract_avaialable_home(state,drive):
    community_data = get_avaialableHome_data(state,drive)
    community_data.to_csv('Assessment_NihalAttar_AvailableHomeData.csv', index=False)

    dtype_reasons = {
        "Region (abbreviation for the state)": "Constant, due to the region is single but it can be take dynamic",
        "Community_Name": "string, community name",
        "Plan": "strings",
        "Location": "String",
        "Postal_Code": "string",
        "Estimated_Completion_Date": "string",
        "Price": "string, price range of homes in the community",
        "Discount": "string",
        "Address (street address only)": "string",
        "Latitude": "Not Available",
        "Longitude": "Not Available",
        "Area (in sq. ft.)": "string",
        "Beds": "string",
        "Baths": "string",
        "Garages": "string",
        "Stories": "string",
        "URL": "string, URL to the community page",
        "Status": "string, Availability status"
    }
    with open('Assessment_NihalAttar_AvailableHome_DTypeReason.docx', 'w') as file:
        for column, reason in dtype_reasons.items():
            file.write(f"{column}: {reason}\n")

    print("Available homes data have been saved.")



url = "https://www.taylormorrison.com/"
state = "Arizona"
start(url,state)