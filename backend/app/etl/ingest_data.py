import requests
from .db import db

def extract_data_from_mysql():
    # Example code to fetch data from MySQL
    result = db.session.execute("SELECT * FROM change_records")
    return result.fetchall()

def extract_data_from_azure_devops():
    # Example code to fetch data from Azure DevOps API
    response = requests.get("https://dev.azure.com/yourorg/_apis/.../pipelines", auth=("username", "token"))
    return response.json()
