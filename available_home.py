import re
import time
from selenium.webdriver.common.by import By
import pandas as pd

def get_avaialableHome_data(state, driver):
    time.sleep(5)

    available_home = []

    available_elements = driver.find_elements(By.XPATH,
                                              "//div[contains(@id, 'search-page-map')]//div[contains(@id,'collapse')]/div")

    for available in available_elements:
        print(available)
        Region = "Arizona"

        try:
            communityName = available.find_element(By.XPATH, ".//p[contains(@class,'community-name')]").text.strip()
        except:
            communityName = "N/A"

        try:
            plan = available.find_element(By.XPATH, ".//p[contains(@class,'floorplan-title')]").text.strip()

        except:
            plan = "N/A"

        try:
            rawLocation = available.find_element(By.XPATH, ".//p[contains(@class,'address')]/span[2]").text.strip()
            parts = rawLocation.split()
            city_state = " ".join(parts[:-1])
            location = city_state
        except:
            location = "N/A"

        try:
            rawPostalCode = available.find_element(By.XPATH, ".//p[contains(@class,'address')]/span[2]").text.strip()
            postalCodePattern = r'\b\d{5}\b'
            postalCode = re.findall(postalCodePattern, rawPostalCode)[0]
        except:
            postalCode = "N/A"

        try:
            rawEstimatedCompletionDate = available.find_element(By.XPATH,
                                                                ".//h6[contains(@class,'status')]").text.strip()
            date = None
            if any(char.isdigit() for char in rawEstimatedCompletionDate):
                pattern = r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s*-\s*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{4}\b"
                match = re.search(pattern, rawEstimatedCompletionDate, re.IGNORECASE)
                date = match.group()
            else:
                date = "N/A"

            estimatedCompletionDate = date

        except:
            estimatedCompletionDate = "N/A"

        try:
            price = available.find_element(By.XPATH, ".//p[contains(@class,'price')]").text.strip()
        except:
            price = "N/A"

        try:
            discount = available.find_element(By.XPATH, ".//p[contains(@class,'previous-price')]/span[2]").text.strip()
            discountPattern = r"\$[\d,]+"
            discountMatch = re.search(discountPattern, discount)
            discount = discountMatch.group()
        except:
            discount = "N/A"

        try:
            finalPrice = available.find_element(By.XPATH, ".//p[contains(@class,'price')]").text.strip()
        except:
            finalPrice = "N/A"

        try:
            address = available.find_element(By.XPATH, ".//p[contains(@class,'address')]/span[1]").text.strip()
        except:
            address = "N/A"

        try:
            latitude = "N/A"
        except:
            latitude = "N/A"

        try:
            longitude = "N/A"
        except:
            longitude = "N/A"

        try:
            area = available.find_element(By.XPATH, ".//div[contains(@class,'specs-section')]/div[3]/p").text.strip()
        except:
            area = "N/A"

        try:
            bed = available.find_element(By.XPATH,
                                         ".//div[contains(@class,'specs-section')]/div[1]/p/span[1]").text.strip()
        except:
            bed = "N/A"

        try:
            bath = available.find_element(By.XPATH,
                                          ".//div[contains(@class,'specs-section')]/div[2]/p/span[1]").text.strip()
        except:
            bath = "N/A"

        try:
            garages = available.find_element(By.XPATH,
                                             ".//div[contains(@class,'specs-section')]/div[4]/p/span[1]").text.strip()
        except:
            garages = "N/A"

        try:
            stories = ""
        except:
            stories = "N/A"

        try:
            url = available.find_element(By.XPATH, ".//a[contains(@class,'home-detail-link')]").get_attribute('href')
        except:
            url = "N/A"

        try:
            status = available.find_element(By.XPATH, ".//h6[contains(@class,'status')]").text.strip()
        except:
            status = "N/A"

        available_home.append({
            "Region (abbreviation for the state)": Region,
            "Community_Name": communityName,
            "Plan": plan,
            "Location": location,
            "Postal_Code": postalCode,
            "Estimated_Completion_Date": estimatedCompletionDate,
            "Price": price,
            "Discount": discount,
            "Final_Price": finalPrice,
            "Address (street address only)": address,
            "Latitude": latitude,
            "Longitude": longitude,
            "Area (in sq. ft.)": area,
            "Beds": bed,
            "Baths": bath,
            "Garages": garages,
            "Stories": stories,
            "URL": url,
            "Status": status
        })

    return pd.DataFrame(available_home)
