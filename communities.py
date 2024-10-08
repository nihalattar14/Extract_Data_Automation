import time
from selenium.webdriver.common.by import By
import pandas as pd

def get_community_data(state, driver):
    time.sleep(5)

    communities = []

    community_elements = driver.find_elements(By.XPATH,
                                              "//div[contains(@id, 'cards')]//div[contains(@id, 'search-page-map')]//section")

    for community in community_elements:
        print(community)
        state_abbr = state

        try:
            name = community.find_element(By.XPATH, ".//span[contains(@class,'titleContainer')]").text.strip()
        except:
            name = "N/A"

        try:
            notes = community.find_element(By.XPATH, ".//span[contains(@class,'communityMessage')]").text.strip()
        except:
            notes = "N/A"

        try:
            latitude = "N/A"
        except:
            latitude = "N/A"
        try:
            longitude = "N/A"
        except:
            longitude = "N/A"
        try:
            address = community.find_element(By.XPATH, ".//span[contains(@class,'location')]").text.strip()
        except:
            address = "N/A"
        try:
            pricing = community.find_element(By.XPATH, ".//span[contains(@class,'price')]").text.strip()
        except:
            pricing = "N/A"
        try:
            area = community.find_element(By.XPATH, ".//div/div[3]/span[contains(@class,'communityInfo')]").text.strip()
        except:
            area = "N/A"
        try:
            url = community.find_element(By.XPATH, ".//a[contains(@class,'home-detail-link')]").get_attribute('href')
        except:
            url = "N/A"

        try:
            spec_elements = community.find_elements(By.XPATH,
                                                    ".//div[contains(@class,'tm-community-card__center')]/span")
            spec_formating = [note.text.strip() for note in spec_elements]
            spec_dict = {}
            for i in range(0, len(spec_formating), 2):
                value = spec_formating[i]
                label = spec_formating[i + 1]
                spec_dict[label] = value

            formate_notes = ", ".join(f"{key}:{value}" for key, value in spec_dict.items())

            specifications = formate_notes
        except:
            specifications = "N/A"

        communities.append({
            "State": state_abbr,
            "Name": name,
            "Notes": notes,
            "Latitude": latitude,
            "Longitude": longitude,
            "Address": address,
            "Pricing": pricing,
            "Area": area,
            "URL": url,
            "Specifications": specifications,
        })

    return pd.DataFrame(communities)
