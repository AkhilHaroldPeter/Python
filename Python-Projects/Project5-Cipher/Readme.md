# Cipher

### To encrypt/decrypt your messages, please click here : https://replit.com/@akhilpeter/Project5-Cipher?v=1


## Description

The Cipher project provides implementations of two classical encryption techniques: the Caesar cipher and the Vigenère cipher. These ciphers allow users to encrypt and decrypt messages using simple substitution methods, providing basic data security.

### Caesar Cipher

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.

### Vigenère Cipher

The Vigenère cipher is a more advanced form of substitution cipher that uses a keyword to determine the shift for each letter in the plaintext. This makes it more secure than the Caesar cipher as it introduces variability in the encryption process.

### Dependencies
This project requires the following Python package:
- `text2art`: Used to create ASCII art for visual appeal. `pip install text2art`

## Installation

To use the Password Generator, follow these steps:

1. **Clone the Repository**: Clone or download the repository to your local machine.

## Python Installation

To run this project, you need to have Python installed on your system. If you haven't installed Python yet, follow these steps:

### Windows

1. Download Python installer from the [official website](https://www.python.org/downloads/).
2. Run the installer, ensuring that the option to add Python to your PATH is selected.
3. Follow the installation steps, and Python will be installed on your system.

### macOS

1. macOS usually comes with Python pre-installed. To check if Python is installed, open the Terminal and type `python3 --version`. If Python is installed, it will display the version number.
2. If Python is not installed, you can install it using [Homebrew](https://brew.sh/). Open Terminal and run the following command:
`brew install python@3.9`

### Linux

1. Python is often installed by default on Linux systems. To check if Python is installed, open a terminal and type `python3 --version`. If Python is installed, it will display the version number.
2. If Python is not installed, you can install it using your distribution's package manager. For example, on Ubuntu, you can use `apt`:
`sudo apt update`
`sudo apt install python3`


## After you have installed python you can run the code by following the below steps:
- Clone the repository to your local machine: https://github.com/AkhilHaroldPeter/Python.git (If this is your first time doing this, please follow through the following documentation: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- Navigate to the directory containing the Password_Generator files.
- Install the required packages using pip.
- Run the `Project5-Cipher.py` script.
- Please follow the prompts to utilize the application and select your desired options for generating passwords.
#### Alternatively, you can download the repository as a zip file, unzip it, and then use it on your local machine.


## Key Concepts

- Encryption Techniques: Implemented classical encryption methods, including the Caesar cipher and the Vigenère cipher, to encode and decode messages.
- Substitution Cipher: Utilized substitution techniques to replace plaintext characters with ciphertext characters based on specific rules and keys.
- Key Management: Managed encryption and decryption keys for the Vigenère cipher to ensure secure communication and message confidentiality.
- Modular Design: Designed the codebase with modularity in mind to allow for easy integration of additional encryption algorithms or enhancements.
- Error Handling: Implemented error handling mechanisms to gracefully handle invalid inputs, edge cases, and exceptions during encryption and decryption processes.


### Disclaimer
This Cipher project is provided for educational purposes only. While encryption techniques such as the Caesar and Vigenère ciphers offer basic data security, they are not suitable for use in sensitive or production environments. Users should exercise caution and use modern encryption methods for securing valuable data.
