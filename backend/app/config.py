import os

class Config:
    # Flask Config
    SECRET_KEY = os.environ.get("SECRET_KEY", "FGJKJM44169899DGHA45")
    
    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "mysql+pymysql://etluser:angukanayo24@localhost/yourdatabase")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Databricks Config
    DATABRICKS_HOST = os.environ.get("DATABRICKS_HOST", "https://databricks-instance")
    DATABRICKS_TOKEN = os.environ.get("DATABRICKS_TOKEN", "rtbvb1267639ou46gskrz895")
