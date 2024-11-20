#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:31:34 2024

@author: ikedaarisa
"""

import pandas as pd

# CSVファイルのパス
csv_path = '/home/jupyter-team04/output_csv/combined_1.csv'

# CSVファイルをデータフレームとして読み込む
df = pd.read_csv(csv_path)
# `path`列から`.jpg`を削除
df['path'] = df['path'].str.replace('.jpg', '', regex=False)
df['path'] = df['path'].apply(lambda x: x.split('folder_1/', 1)[-1] if 'folder_1/' in x else x)
df['path'] = df['path'].apply(lambda x: x.split('folder_2/', 1)[-1] if 'folder_2/' in x else x)
df['path'] = df['path'].apply(lambda x: x.split('folder_3/', 1)[-1] if 'folder_3/' in x else x)
df['path'] = df['path'].apply(lambda x: x.split('folder_4/', 1)[-1] if 'folder_4/' in x else x)
df.rename(columns={'path': 'anon_item_id'}, inplace=True)
# 結果を表示（最初の5行）
print(df.head())
display(df2)

# 結果を新しいCSVファイルとして保存（必要に応じて）
output_csv_path = '/home/jupyter-team04/output_csv/combined_3.csv'
df.to_csv(output_csv_path, index=False)