import duckdb

# SQLクエリを定義
sql = '''\
SELECT *
FROM items
LEFT JOIN item_categories
ON items.category_id = item_categories.id
WHERE (name0 = 'レディース' AND name1 = 'トップス')
'''

# SQLクエリを実行し、結果を取得
rel = duckdb.sql(sql)

# 結果をデータフレームに変換
df = rel.to_df()

# データフレームを表示
print(df)
# name列に「様」または「専用」を含むデータを除外
dff = df[~df['name'].str.contains('様|専用', na=False)]
print(df)
