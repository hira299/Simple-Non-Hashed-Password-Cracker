---
# Simple Non-Hashed Password Cracker
---
## Overview
This is a simple password cracker application built using Streamlit. The application allows users to input a target password and a list of possible passwords. It uses a brute-force approach to find the target password by checking each password in the list.

## Features
- User-friendly interface to input the target password and possible passwords.
- Displays the cracked password and the number of attempts taken.
- Provides feedback if the password is not found in the list.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-cracker.git
   cd password-cracker
   ```

2. Install the required packages:
   ```bash
   pip install streamlit
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter the target password you want to crack.
2. In the text area, input a list of possible passwords (one per line).
3. Click the "Crack Password" button to start the cracking process.
4. The application will display the cracked password and the number of attempts taken or indicate if the password was not found.

## Example
```plaintext
Target Password: mysecretpassword
Possible Passwords:
password123
mysecretpassword
letmein
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or report issues.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the framework.
- Inspiration from various password cracking methodologies.

```
