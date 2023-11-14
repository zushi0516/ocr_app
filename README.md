# ocr_app
スクショした画像の文字をコピペしやすくするWebアプリ
![例](images/example.png)

# 使い方

ターミナルを開いて

``` 
git clone https://github.com/zushi0516/ocr_app.git
```

ディレクトリ移動
``` 
cd ./path/ocr_app
```

ライブラリインストール

venv環境構築推奨

``` 
python -m venv .venv
```

``` 
#mac
. .venv/bin/activate

#windows
.venv\Scripts\activate.bat
```

.venv環境に入れたら、reqirement.txtをpip


``` 
python -m pip install -r requirements.txt
```

streamlitのpyファイルを立ち上げ、自動でブラウザが立ち上がって使えるようになる


``` 
streamlit run ocr_streamlit.py
```

