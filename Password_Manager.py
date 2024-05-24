from cryptography.fernet import Fernet
import os

# Function to generate and load the encryption key
def load_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    with open('key.key', 'rb') as key_file:
        return key_file.read()

# Function to encrypt data
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

# Function to view stored passwords
def view_passwords():
    try:
        with open('password.txt', 'r') as f:
            for line in f:
                username, encrypted_password = line.strip().split("|")
                decrypted_password = decrypt_data(encrypted_password.strip(), load_key())
                print("Username:", username, "\tPassword:", decrypted_password)
    except FileNotFoundError:
        print("No passwords stored yet.")

# Function to add a new password
def add_password():
    username = input("Enter account username: ")
    password = input("Enter account password: ")
    encrypted_password = encrypt_data(password, load_key())
    with open('password.txt', 'a') as f:
        f.write(username + "|" + encrypted_password + "\n")
    print("Password added successfully!")

# Main function to interact with the user
def main():
    print("Welcome to the Password Manager!")
    while True:
        print("\nMenu:")
        print("1. View stored passwords")
        print("2. Add a new password")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            view_passwords()
        elif choice == "2":
            add_password()
        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
