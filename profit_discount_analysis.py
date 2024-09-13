import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 讀取CSV檔案
def load_data(file_path):
    return pd.read_csv(file_path)

# 分析折扣對利潤的影響
def analyze_discount_impact(df, target_category):
    # 篩選出 Technology 類別的產品
    tech_data = df[df['Category'] == target_category]
    
    # 計算每個產品的實際利潤率
    tech_data['Profit_Rate'] = tech_data['Profit'] / tech_data['Sales']
    
    # 計算平均利潤率
    avg_profit_rate = tech_data['Profit_Rate'].mean()
    
    # 統計不同折扣程度下的利潤情況
    discount_stats = tech_data.groupby('Discount').agg({
        'Profit': lambda x: (x < 0).mean() * 100, # (x < 0) 表示為負利潤的商品因此會有 array {[1, 1, 1, ..., 0, 0, 0]}，計算平均值可能會是0.2 表示有 20% 的商品是負利潤 
        'Profit_Rate': 'mean'
    }).reset_index()
    discount_stats.columns = ['Discount', 'Negative_Profit_Percentage', 'Average_Profit_Rate']
    discount_stats = discount_stats.sort_values('Discount')
    
    return avg_profit_rate, discount_stats

# 視覺化結果
def visualize_results(discount_stats):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(discount_stats['Discount'], discount_stats['Negative_Profit_Percentage'], 'b-')
    ax1.set_xlabel('Discount')
    ax1.set_ylabel('Percentage of Products with Negative Profit', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    ax2 = ax1.twinx()
    ax2.plot(discount_stats['Discount'], discount_stats['Average_Profit_Rate'], 'r-')
    ax2.set_ylabel('Average Profit Rate', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title('Impact of Discount on Profitability for Technology Products')
    plt.grid(True)
    plt.show()

# 主函數
def main():
    file_path = 'hypermarket_data.csv'  # 請替換為您的CSV檔案路徑
    df = load_data(file_path)

    target_category = 'Technology'
    avg_profit_rate, discount_stats = analyze_discount_impact(df, target_category)
    
    print(f"Average profit rate for {target_category} products: {avg_profit_rate:.2%}")
    print("\nProfit statistics by discount:")
    print(discount_stats)
    
    visualize_results(discount_stats)

if __name__ == "__main__":
    main()