from src.data_preprocessing import load_data, preprocess_transactions
from src.apriori_algorithm import apriori, generate_association_rules
from src.visualization import plot_top_items, plot_support_vs_confidence


def main():
    print("=== DỰ ÁN APRIORI - KHAI PHÁ LUẬT KẾT HỢP ===")

    # 1. Load và tiền xử lý dữ liệu
    print("📊 Đang tải dữ liệu...")
    df = load_data('data/Groceries_dataset.csv')

    # 2. Tiền xử lý
    print("🔄 Đang xử lý dữ liệu...")
    transactions = preprocess_transactions(df)

    # 3. Chạy Apriori
    print("🔍 Đang chạy thuật toán Apriori...")
    frequent_itemsets = apriori(transactions, min_support=0.01)

    # 4. Sinh luật kết hợp
    print("📈 Đang sinh luật kết hợp...")
    rules = generate_association_rules(frequent_itemsets, min_confidence=0.5)

    # 5. Trực quan hóa
    print("📊 Đang tạo biểu đồ...")
    plot_top_items(transactions)

    print("✅ Hoàn thành!")


if __name__ == "__main__":
    main()