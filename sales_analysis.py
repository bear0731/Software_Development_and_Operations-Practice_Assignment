import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 讀取CSV檔案
def load_data(file_path):
    return pd.read_csv(file_path)

# 銷售表現分析
def sales_performance_analysis(df):
    # 總銷售額隨時間變化
    sales_over_time = df.groupby('Order Date')['Sales'].sum().sort_index()
    
    # 按地區的總銷售額
    sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    
    # 按產品類別的總銷售額
    sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    
    # 識別表現最佳的產品
    top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
    
    return {
        'sales_over_time': sales_over_time,
        'sales_by_region': sales_by_region,
        'sales_by_category': sales_by_category,
        'top_products': top_products
    }

# 視覺化結果
def visualize_results(results):
    # 總銷售額隨時間變化
    plt.figure(figsize=(12, 6))
    results['sales_over_time'].plot()
    plt.title('Total Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.tight_layout()  # 自動調整佈局以適應標籤
    plt.savefig('total_sales_over_time.png')  # 保存圖表
    plt.close()  # 關閉圖表

    # 按地區的總銷售額
    plt.figure(figsize=(10, 6))
    results['sales_by_region'].plot(kind='bar')
    plt.title('Total Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()  # 自動調整佈局以適應標籤
    plt.savefig('total_sales_by_region.png')  # 保存圖表
    plt.close()  # 關閉圖表

    # 按產品類別的總銷售額
    plt.figure(figsize=(10, 6))
    results['sales_by_category'].plot(kind='bar')
    plt.title('Total Sales by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()  # 自動調整佈局以適應標籤
    plt.savefig('total_sales_by_category.png')  # 保存圖表
    plt.close()  # 關閉圖表

    # 表現最佳的前10個產品
    plt.figure(figsize=(12, 6))
    results['top_products'].plot(kind='bar')
    plt.title('Top 10 Best-Performing Products')
    plt.xlabel('Product Name')
    plt.ylabel('Sales')
    plt.xticks(rotation=45, ha='right')  # 旋轉標籤並右對齊
    plt.tight_layout()  # 自動調整佈局以適應標籤
    plt.savefig('top_10_best_performing_products.png')  # 保存圖表
    plt.close()  # 關閉圖表

# 主函數
def main():
    file_path = 'hypermarket_data.csv'  # 請替換為您的CSV檔案路徑
    df = load_data(file_path)
    results = sales_performance_analysis(df)
    visualize_results(results)

if __name__ == "__main__":
    main()