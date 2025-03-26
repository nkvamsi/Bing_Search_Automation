# Bing Search Automation

Automate Bing searches to earn Microsoft Rewards points efficiently across multiple accounts.

## Features

- Supports multiple browsers: Edge, Chrome, Firefox, and Safari
- Performs automated searches using random, natural-looking search queries
- Completes daily quizzes and activities to maximize points
- Supports both PC and Mobile search rewards
- Secure credential management using environment variables
- Multi-account support with concurrent processing

## Setup

### Prerequisites

- Python 3.7+
- Web browsers (Edge, Chrome, Firefox, or Safari)
- Appropriate webdrivers for Selenium (handled automatically)

### Installation

1. Clone this repository

2. Install dependencies: pip install -r requirements.txt

3. Create a `.env` file in the project root with your credentials:3. Create a `.env` file in the project root with your credentials:

    BING_USER_EMAILS=email1@example.com,email2@example.com BING_USER_PASSWORDS=password1,password2


**Note:** Ensure you have an equal number of emails and passwords, separated by commas.

## Usage

### Basic Usage

Run with default settings (Edge browser, all accounts, both PC and mobile searches): python automate_mac.py


### Advanced Options

Specify browser: python automate_mac.py chrome

Run only PC searches: python automate_mac.py edge pc

Run only mobile searches: python automate_mac.py edge mobile

Run only quizzes: python automate_mac.py edge quiz

Run for specific accounts (by index, starting from 1): python automate_mac.py edge pc 1,3


### Security Notes

- The `.env` file containing your credentials is excluded from Git tracking via `.gitignore`
- For additional security, restrict file permissions: `chmod 600 .env`
- Never share your credential files or commit them to repositories

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with Microsoft's terms of service.
