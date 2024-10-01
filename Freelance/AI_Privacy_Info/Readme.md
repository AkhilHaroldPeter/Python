# AI Privacy Information Fetcher

The **AI Privacy Information Fetcher** is a Python script designed to dynamically retrieve missing AI-related information from the privacy policy pages of specified domains. This tool is particularly useful for gathering compliance and transparency details from various AI services.

## Features

- Scrapes privacy policy pages to find data retention periods, training data usage, and review policies.
- Supports dynamic URL fetching to gather relevant information.
- Handles HTTP requests and responses with error management.
- Outputs updated information in a specified CSV format.

## Requirements

To run this tool, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- Required Python libraries:
  - `pandas`
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using pip:

```bash
pip install pandas requests beautifulsoup4
```
## Directory Structure
Before you start, ensure your project folder looks like this:
``` bash
ai_privacy_info_fetcher/
│
├── input_file.csv              # Place your input CSV file here
│
├── output_file.csv             # The output file will be saved here
│
└── src/                         # Source code folder
    └── fetch_ai_privacy_info.py # Main script for fetching information
```
## Step 1: Prepare Your Input File
Supported File Types Place your input CSV file in the ```ai_privacy_info_fetcher directory```. The tool expects the following columns:

```reference_url```: URLs of the privacy policy pages
Other columns for storing fetched information, such as data retention and training data usage.

## File Names
You can use any valid file name for your input CSV, but it's helpful to keep it descriptive.

## Step 2: Running the Tool
Once your input file is in place, you can run the script:

1. Open a terminal or command prompt.
2. Navigate to the ```src``` directory.
3. Execute the following command:
   ``` bash
   python fetch_ai_privacy_info.py
   ```
   After running the script, you will find the updated output file in the main directory, containing the fetched information based on the specified URLs.
## Error Handling
The tool has basic error handling mechanisms to manage potential issues, such as network errors or inaccessible URLs. Any errors encountered during processing will be logged to the console for user review.

## Contributing
Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any inquiries or support, please reach out to akhilharold97@gmail.com
