# Sales Data Analysis with Pandas - Robust Version
import pandas as pd
import matplotlib

matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import os


def generate_sample_data():
    """Generate comprehensive sample sales data"""
    np.random.seed(42)
    num_records = 500

    dates = pd.date_range(start='2023-01-01', periods=num_records, freq='D')
    products = ['Electronics', 'Clothing', 'Home Goods', 'Grocery', 'Books']
    genders = ['Male', 'Female']
    regions = ['North', 'South', 'East', 'West']

    data = {
        'Date': dates,
        'Product': np.random.choice(products, num_records),
        'Customer_Age': np.random.randint(18, 70, num_records),
        'Customer_Gender': np.random.choice(genders, num_records),
        'Region': np.random.choice(regions, num_records),
        'Units_Sold': np.random.randint(1, 10, num_records),
        'Unit_Price': np.round(np.random.uniform(10, 200, num_records), 2)
    }

    df = pd.DataFrame(data)
    df['Revenue'] = df['Units_Sold'] * df['Unit_Price']
    df['Month'] = df['Date'].dt.month_name()

    # Create age groups
    bins = [0, 25, 35, 45, 55, 120]
    labels = ['18-25', '26-35', '36-45', '46-55', '55+']
    df['Age_Group'] = pd.cut(df['Customer_Age'], bins=bins, labels=labels, right=False)

    return df


def create_visualizations(df):
    """Create all visualizations with error handling"""
    try:
        # Set a valid style
        plt.style.use('ggplot')  # Using ggplot style which is always available

        # Create output directory if it doesn't exist
        os.makedirs('sales_analysis_output', exist_ok=True)

        # 1. Monthly Sales Trend
        plt.figure(figsize=(12, 6))
        monthly_sales = df.groupby('Month')['Revenue'].sum()
        monthly_sales.plot(kind='bar', color='teal')
        plt.title('Monthly Sales Revenue', pad=20)
        plt.xlabel('Month', labelpad=10)
        plt.ylabel('Total Revenue ($)', labelpad=10)
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig('sales_analysis_output/monthly_sales.png', dpi=300)
        plt.close()

        # 2. Sales by Product Category
        plt.figure(figsize=(10, 6))
        product_sales = df.groupby('Product')['Revenue'].sum()
        product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90,
                           colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0'])
        plt.title('Sales by Product Category', pad=20)
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig('sales_analysis_output/product_sales.png', dpi=300)
        plt.close()

        # 3. Sales by Age Group
        plt.figure(figsize=(10, 6))
        age_sales = df.groupby('Age_Group')['Revenue'].sum()
        age_sales.plot(kind='barh', color='darkorange')
        plt.title('Sales by Age Group', pad=20)
        plt.xlabel('Total Revenue ($)', labelpad=10)
        plt.ylabel('Age Group', labelpad=10)
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig('sales_analysis_output/age_sales.png', dpi=300)
        plt.close()

        # 4. Sales by Gender
        plt.figure(figsize=(6, 6))
        gender_sales = df.groupby('Customer_Gender')['Revenue'].sum()
        gender_sales.plot(kind='bar', color=['lightcoral', 'lightskyblue'])
        plt.title('Sales by Gender', pad=20)
        plt.xlabel('Gender', labelpad=10)
        plt.ylabel('Total Revenue ($)', labelpad=10)
        plt.xticks(rotation=0)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig('sales_analysis_output/gender_sales.png', dpi=300)
        plt.close()

        return True
    except Exception as e:
        print(f"Error creating visualizations: {str(e)}")
        return False


def generate_text_report(df):
    """Generate text report with insights"""
    try:
        # Calculate metrics
        total_revenue = df['Revenue'].sum()
        avg_transaction = df['Revenue'].mean()

        monthly_sales = df.groupby('Month')['Revenue'].sum()
        product_sales = df.groupby('Product')['Revenue'].sum()
        age_sales = df.groupby('Age_Group')['Revenue'].sum()
        gender_sales = df.groupby('Customer_Gender')['Revenue'].sum()

        report = f"""
        SALES ANALYSIS REPORT
        =====================

        Summary Statistics:
        - Total Revenue: ${total_revenue:,.2f}
        - Total Transactions: {len(df)}
        - Average Transaction Value: ${avg_transaction:,.2f}

        Key Insights:
        1. Best Performing Month: {monthly_sales.idxmax()} (${monthly_sales.max():,.2f})
        2. Top Product Category: {product_sales.idxmax()} (${product_sales.max():,.2f}, {product_sales.max() / total_revenue:.1%} of total)
        3. Highest Spending Age Group: {age_sales.idxmax()} (${age_sales.max():,.2f})
        4. Gender Distribution:
           - Male: ${gender_sales.get('Male', 0):,.2f} ({gender_sales.get('Male', 0) / total_revenue:.1%})
           - Female: ${gender_sales.get('Female', 0):,.2f} ({gender_sales.get('Female', 0) / total_revenue:.1%})
        """

        # Save report to file
        with open('sales_analysis_output/sales_report.txt', 'w') as f:
            f.write(report)

        return True
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        return False


def main():
    """Main execution function"""
    print("Starting sales analysis...")

    # Generate sample data
    print("Generating sample sales data...")
    sales_data = generate_sample_data()

    # Create visualizations
    print("Creating visualizations...")
    viz_success = create_visualizations(sales_data)

    # Generate report
    print("Generating report...")
    report_success = generate_text_report(sales_data)

    # Print results
    if viz_success and report_success:
        print("\nAnalysis completed successfully!")
        print("Generated files are saved in the 'sales_analysis_output' folder:")
        print("- monthly_sales.png")
        print("- product_sales.png")
        print("- age_sales.png")
        print("- gender_sales.png")
        print("- sales_report.txt")
    else:
        print("\nAnalysis completed with some errors. Check output files.")


if __name__ == "__main__":
    main()