import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the file paths
input_file_path = "ai info empty file - Sheet1.csv"  # Change this to your input CSV file path
output_file_path = "ai info empty file - output.csv"  # Change this to your desired output file path

# Load the CSV file
df = pd.read_csv(input_file_path)

# Function to scrape the privacy policy page
def scrape_privacy_info(reference_url):
    try:
        response = requests.get(reference_url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Logic to extract required information
        data_retention = "Unknown"
        user_data_train_model = "Unknown"
        user_data_train_model_raw_text = "N/A"
        humans_can_review_data = "Unknown"
        option_to_configure_training = "Unknown"
        option_to_configure_retention = "Unknown"

        # Search for common phrases in the privacy policy
        # Adjust the selectors or logic based on the page structure
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            text = paragraph.get_text().lower()

            if 'data retention' in text or 'retain' in text:
                data_retention = text
            if 'train' in text and 'data' in text:
                user_data_train_model = 'Yes'
                user_data_train_model_raw_text = text
            if 'review' in text and 'data' in text:
                humans_can_review_data = 'Yes'
            if 'configure' in text and 'training' in text:
                option_to_configure_training = 'Yes'
            if 'configure' in text and 'retention' in text:
                option_to_configure_retention = 'Yes'

        return (data_retention, user_data_train_model, user_data_train_model_raw_text, 
                humans_can_review_data, option_to_configure_training, option_to_configure_retention)

    except requests.RequestException as e:
        print(f"Error fetching {reference_url}: {e}")
        return ("Error", "Error", "N/A", "Error", "Error", "Error")

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    if pd.isna(row['User Data Trains Model']):  # Only scrape if data is missing
        reference_url = row['reference_url']
        (data_retention, user_data_train_model, user_data_train_model_raw_text, 
         humans_can_review_data, option_to_configure_training, option_to_configure_retention) = scrape_privacy_info(reference_url)

        # Fill the missing columns with scraped data
        df.at[index, 'Data Retention Period'] = data_retention
        df.at[index, 'User Data Trains Model'] = user_data_train_model
        df.at[index, 'User Data Trains Model Raw Text'] = user_data_train_model_raw_text
        df.at[index, 'Humans Can Review Data'] = humans_can_review_data
        df.at[index, 'Option to Configure Training'] = option_to_configure_training
        df.at[index, 'Option to Configure Retention'] = option_to_configure_retention

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print("Missing AI information has been filled and saved to the output file.")
