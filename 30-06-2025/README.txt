# Sales Data Analysis with Pandas

This project provides an automated analysis pipeline for synthetic sales data using Python, `pandas`, and `matplotlib`. It includes data generation, visualization, and a summary report.

## Features

- Generates realistic sample sales data (500 records)
- Calculates revenue, age groups, and monthly statistics
- Creates the following visualizations:
  - **Monthly Sales Revenue** (bar chart)
  - **Sales by Product Category** (pie chart)
  - **Sales by Age Group** (horizontal bar chart)
  - **Sales by Gender** (bar chart)
- Outputs a detailed sales report with key metrics and insights

## Output

All generated files are saved in the `sales_analysis_output/` directory:

- `monthly_sales.png`
- `product_sales.png`
- `age_sales.png`
- `gender_sales.png`
- `sales_report.txt`

## Requirements

- Python 3.7+
- `pandas`
- `numpy`
- `matplotlib`

Install the dependencies using pip:

```bash
pip install pandas numpy matplotlib
