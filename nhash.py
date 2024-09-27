import streamlit as st

# Function to perform brute-force password cracking
def password_cracker(target_password, password_list):
    for index, password in enumerate(password_list):
        if password.strip() == target_password:
            return (password, index + 1)  # Return password and number of attempts
    return (None, len(password_list))  # Return None if not found, and total attempts

# Streamlit app setup
st.title("Simple Non-Hashed Password Cracker")
st.write("Enter the target password and possible passwords to crack it.")

# Input for the target password
target_password = st.text_input("Enter the target password:")

# Text area for entering the password list
password_input = st.text_area("Enter possible passwords (one per line):")

# Check if both target password and password list are provided
if target_password and password_input:
    # Split the password input into a list of passwords
    password_list = password_input.splitlines()
    
    # Button to start cracking
    if st.button("Crack Password"):
        # Call the cracking function
        cracked_password, attempts = password_cracker(target_password, password_list)
        
        # Display the result
        if cracked_password:
            st.success(f"Password cracked! The password is: '{cracked_password}'")
            st.info(f"Number of attempts: {attempts}")
        else:
            st.error("Password not found in the list.")
