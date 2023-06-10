# MiniVault Application

This is a Python application called MiniVault, which provides basic banking functionality such as account creation, deposit, withdrawal, fund transfers, and viewing a passbook.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- `os` module
- `time` module
- `datetime` module
- `fpdf` module
- `pyttsx3` module
- `pwinput` module
- `json` module
- `encrypt` module
- `jarvis` module
- `re` module
- `speech_recognition` module
- `win32com.client` module
- `webbrowser` module


You can install these dependencies using pip:

```bash
pip install pyttsx3 pwinput PyPDF2
```

## Usage

To use the MiniVault application, follow these steps:

1. Run the `MiniVault.py` file using Python.
2. You will be prompted with the home screen of the application.
3. Choose your preferred input method: voice (V) or text (T).
4. If you select the voice input method, you will need a microphone connected to your system.
5. Select either to log in (L) or create a new account (C).
6. If you choose to create a new account, follow the instructions and provide the necessary details.
7. If you select to log in, enter your username and password when prompted.
8. Once logged in, you will see the MiniVault customer interface.
9. Use the following options to perform banking operations:
   - D: Deposit funds
   - W: Withdraw funds
   - TF: Transfer funds to another customer
   - VP: View passbook
   - LO: Log out
10. Follow the on-screen instructions and provide the required details for each operation.
11. You can choose to use voice input or text input for amount and username entries.
12. The application will provide voice prompts and display relevant information on the screen.
13. You can view your passbook as a PDF file.

## Features

- Create a new account with a unique username and password.
- Log in to an existing account.
- Deposit funds into your account.
- Withdraw funds from your account.
- Transfer funds to another customer's account.
- View a passbook that shows all transactions.
- Voice input option for user convenience.
- User-friendly interface and instructions.

## Voice Input
The application now supports voice input for a more convenient user experience. Here's how to use it:
- When prompted for input, say your response instead of typing it.
- Speak clearly and make sure you have a working microphone.
- Wait for the application to recognize and process your voice command.
- The application will provide voice feedback and carry out the requested action.


## Notes

- The application uses the `data.json` file to store user data, including account details and transaction history.
- The application utilizes external dependencies such as `pyttsx3` for text-to-speech conversion and `pwinput` for secure password input.
- Ensure that the required dependencies are installed before running the application.
- The passbook is generated as a PDF file using the `PyPDF2` library.
- Javis is an additional module used for voice recognition and processing.
- Encrypt is module developed for passwords data secure.



Feel free to explore and enhance the MiniVault application as per your requirements.
