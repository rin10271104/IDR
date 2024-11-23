from PIL import Image

# 推論対象の画像のパスを指定（画像パスを適切に変更してください）
image_path = '/home/jupyter-team04/JR-BigData/0-22.jpg'

# 画像を読み込む
img = Image.open(image_path)

# 推論を実行
results = model(img)

# 結果を表示
results.show()  # 検出された物体を画像で表示

# 検出結果をコンソールに出力
results.print()  # 画像に検出された物体のラベルと信頼度をコンソールに表示

# 検出されたラベル（物体の種類）を取得
labels = results.names
# 検出された物体のクラスインデックス
detected_classes = results.xyxy[0][:, -1].cpu().numpy()

# 「person」のラベルが検出されているかどうかをチェック
detected_person = any(label == 'person' for label in [labels[int(cls)] for cls in detected_classes])

if detected_person:
    print("人物が含まれます")
    target_folder = os.path.join(output_dir, '人物着用')
else:
    print("人物は含まれていません")
    target_folder = os.path.join(output_dir, '平置き')

# 画像を保存
shutil.copy(image_path, target_folder)  # 画像をコピー
print(f"画像 '{image_path}' を '{target_folder}' に保存しました。")
