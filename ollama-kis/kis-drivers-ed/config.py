import os

class Config:
    # Set the secret key
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Define other configuration variables as needed
    DEBUG = True  # Set debug mode to True for development
    # Add more configurations as per your requirements
