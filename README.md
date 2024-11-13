# Change Management ETL Project

## Overview
This project builds a centralized data warehouse for Change Management reporting using Databricks for ETL, MySQL for data storage, and a Flask web app for data visualization. The main goals are to extract data from ITSM databases and Azure DevOps, transform it, and store it in Databricks in Parquet format for easy analysis and reporting.

## Project Structure
- **Backend**: The Flask app provides API endpoints, handles data ingestion, and integrates with Databricks.
- **Database**: SQL files define the schema and initial data setup for the MySQL database.
- **ETL**: Scripts for extracting, transforming, and loading data.
- **Databricks**: Notebooks and job scripts to automate ETL and analysis processes.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/ChangeManagementazuredatabricksETL.git
    ```

2. Navigate into the project directory:
    ```bash
    cd ChangeManagementazuredatabricksETL
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your database by running the SQL files in the `database/` folder.

5. Configure Databricks access in `app/config.py`.

## Usage

- **Run Flask App**:
    ```bash
    python main.py
    ```
- **Access Web Interface**:
    - Open a browser and navigate to `http://127.0.0.1:5000` to view the dashboard.

- **Automated ETL**:
    - Use the Databricks notebooks and pipeline scripts in `databricks/` to automate data processing.

## Contributing
Please feel free to open issues or submit pull requests with improvements.

## License
This project is licensed under the MIT License.
