import requests
from .config import Config

def run_databricks_job():
    url = f"{Config.DATABRICKS_HOST}/api/2.0/jobs/run-now"
    headers = {"Authorization": f"Bearer {Config.DATABRICKS_TOKEN}"}
    data = {"job_id": "rwh934g189jhinbvc"}

    response = requests.post(url, headers=headers, json=data)
    return response.json()
