# Machine Learning Stock Predictions | GT Data Science & Analytics Bootcamp | Final Project

## About The Project

In this project we set out to identify stock prices using machine learning algorithms. We want to leverage technologies like Pandas, Plotly, and Tableau to visualize graphs that compare report earnings to the increase or decrease of stock prices.   

## Data Sources

**Yahoo Finance Stock Data** (http://theautomatic.net/yahoo_fin-documentation/)
    - This is a link to the python docs for Yahoo Finance Stock Data (https://pypi.org/project/yahoo-finance/).


## Transform & Load

<!-- NEED TO UPDATE THIS SECTION!! -->
## Setup the application

Setup :

1. Clone the repo.
2. Create a functional user for the database.
Example:

``` sql
CREATE ROLE trends_project WITH
    LOGIN
    NOSUPERUSER
    INHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION
    ENCRYPTED PASSWORD 'XXXXXXX';  -- Choose your own !!....
```

3. Create a PostreSQL database.

``` sql
CREATE DATABASE trending_db
    WITH 
    OWNER = trends_project
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;  -- Tweak if you need
```

4. Update DB connection parameters in notebook to align to appropriate 

``` python
# Connect to Database 
rds_connection_string = "trends_project:XXXXX@localhost:5432/trending_db"
engine = create_engine(f'postgresql://{rds_connection_string}')
```

<!-- CONTRIBUTING -->
## Contributing Only Section

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Clone the Repo
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

None at this time.


<!-- CONTACT -->
## Contact

saibalchak
billyATGE
Obi-1-kenobi
danielle16

