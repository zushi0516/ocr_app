import streamlit as st
from PIL import Image
import pytesseract

# Streamlitアプリのタイトル
st.title("OCRアプリ 画像の文字を抽出するよ！")

# 画像アップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 画像を読み込む
    image = Image.open(uploaded_file)
    st.image(image, caption='アップロードされた画像', use_column_width=True)
    
    # OCRを実行
    text = pytesseract.image_to_string(image, lang="jpn")

    # 結果を大きなテキストエリアに表示
    text_area = st.text_area("抽出されたテキスト:", text, height=500)

    # テキストファイルとしてダウンロード
    st.download_button(
        label="テキストをダウンロード",
        data=text,
        file_name='extracted_text.txt',
        mime='text/plain'
    )
