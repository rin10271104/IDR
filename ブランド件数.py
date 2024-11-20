import pandas as pd

# ブランドIDリスト
matched_ids = [
    930.0, 1266.0, 2416.0, 229.0, 509.0, 2535.0, 1026.0, 474.0, 534.0, 365.0, 
    1044.0, 740.0, 2536.0, 1663.0, 3948.0, 1233.0, 954.0, 1478.0, 521.0, 
    4388.0, 798.0, 1284.0, 3999.0, 1716.0, 3907.0, 4330.0, 7505.0, 539.0, 
    1063.0, 262.0, 3969.0, 3844.0, 197.0, 1364.0, 6982.0, 606.0, 11595.0, 
    4019.0, 504.0, 7313.0, 7524.0, 947.0, 76.0, 5963.0, 3947.0, 16252.0, 
    5103.0, 1371.0, 10733.0, 5517.0, 4757.0, 4885.0, 7437.0, 3793.0, 5065.0
]

# サンプルデータフレームを用意（実データに置き換えてください）
# dff = pd.read_csv('your_data.csv')  # 商品データを読み込む場合
# brand_name_df = pd.read_csv('brand_name.csv')  # ブランド名データを読み込む場合

# IDと一致する行を抽出
filtered_data = dff[dff['brand_name'].isin(matched_ids)]

# ブランドごとに商品数を集計
brand_counts = filtered_data['brand_name'].value_counts()

# 結果をデータフレームとしてまとめる
result_df = brand_counts.reset_index()
result_df.columns = ['id', 'count']

# brand_name.csv を参照して name_ja を取得
# brand_name.csv には 'id' 列と 'name_ja' 列が含まれていると仮定
brand_name_df = pd.read_csv(r'C:\Users\atsus\OneDrive\デスクトップ\join_haru\work\JR-BigData\data\supplement\brand_names.csv')

# 結果データフレームに name_ja を結合
result_with_names = result_df.merge(brand_name_df[['id', 'name_ja']], on='id', how='left')

# 結果を表示
print(result_with_names)

# 必要に応じてCSVに保存
result_with_names.to_csv('brand_name_item_counts_with_names.csv', index=False)
