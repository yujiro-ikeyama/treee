# Mini SNS (Streamlit)

Streamlitで作ったシンプルなSNSアプリです。ローカルで投稿・タイムライン表示・いいね・削除ができます。

## 機能

- ユーザー切り替え（疑似ログイン）
- 投稿作成（本文 + 画像URL）
- タイムライン表示（新しい順）
- いいね / いいね解除
- 投稿者本人のみ削除可能
- `data/posts.json` へローカル保存

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 実行

```bash
streamlit run app.py
```

ブラウザで表示されたURL（通常は `http://localhost:8501`）を開いて使います。
