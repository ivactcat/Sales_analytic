Analysis Sales - Iowa Liquor Dataset

#  Analysis Objective

The objective of this project is to perform a regional sales analysis, identify consumption trends, and design a structured database by defining and inserting relevant fields to effectively manage liquor sales data.

#  Dataset Description

This dataset contains wholesale liquor sales records by Class “E” licensees in Iowa (grocery stores, liquor stores, convenience stores).  

Key Columns:

- `date`: Date of the sale
- `store_number`, `store_name`: Store identification
- `city`, `county`, `zip_code`: Location of the store
- `category_name`: Liquor category
- `item_description`: Product description
- `bottle_volume_ml`: Volume per bottle
- `state_bottle_cost`, `state_bottle_retail`: Cost and retail price
- `bottles_sold`, `sale_dollars`: Units sold and total revenue
- `volume_sold_liters`, `volume_sold_gallons`: Volume sold


# Repository Structure
GitHub Repository: Includes a .gitignore file to control which files and folders should be uploaded.
• Folder Structure:

    o data/: To store data files. 
        	iowa_liquor_sales_2019.parquet
    o jupyter/: To store Jupyter Notebook files. 
        	analytic.ipynb
        	clean.ipynb
        	basedate.ipynb
                   	basedate.ipynb

    o data_transformation
        	categorical_and_numerical_analysis.parquet   
        	dataset_cleaned.parquet    
       

    • Creating the Virtual Environment:
        1.	Navigate to the project folder.
        2.	Create a virtual environment: 
        3.	py -m venv venv
        4.	Activate the environment: 
        5.	venv/bin/activate
        6   Install required libraries: 
        7.	pip install pandas numpy jupyter
        8.	Create a requirements file: 
        9.	pip freeze > requirements.txt

#	Data Cleaning:
Data homogenization:
Standardize the dataset by cleaning column names (e.g., stripping spaces, converting to lowercase), and ensuring data types are consistent.

Change the format of the date column:
Convert the date column to a consistent datetime format (e.g., YYYY-MM-DD).

Transform the price_value column:
Clean the price_value column by removing any non-numeric characters (like $ or ,) and convert it to a numeric data type (float).

Decompose the store_columns column:
Split the store_columns into multiple separate columns, for example extracting city, store_name.

Null value analysis:
Analyze the dataset for missing values (nulls), summarizing how many nulls exist in each column and their percentage relative to the dataset.



#   Data Visualization:
Creation of subplots for numeric category columns

creation of column correlation matrix

creation of sales evolution chart

creation of sales scatter map

study of correlation between different variables.






