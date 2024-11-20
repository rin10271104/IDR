#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:46:38 2024

@author: ikedaarisa
"""

import shutil
import os

# 圧縮したいフォルダのパス
folder_to_zip = "/home/jupyter-team04/output_base_folder/folder_1"

# 出力zipファイルのパス
output_zip_file = "/home/jupyter-team04/output_base_folder/folder_1.zip"

# フォルダをzipファイルに圧縮
shutil.make_archive(folder_to_zip, 'zip', os.path.dirname(folder_to_zip), os.path.basename(folder_to_zip))

print(f"{folder_to_zip} を {output_zip_file} に圧縮しました。")