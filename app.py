from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

import streamlit as st

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "posts.json"
DEFAULT_USERS = ["yujiro", "alice", "bob", "charlie"]


def ensure_data_file() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_posts() -> list[dict[str, Any]]:
    ensure_data_file()
    try:
        raw = DATA_FILE.read_text(encoding="utf-8")
        data = json.loads(raw)
        if isinstance(data, list):
            return data
    except (json.JSONDecodeError, OSError):
        pass
    return []


def save_posts(posts: list[dict[str, Any]]) -> None:
    ensure_data_file()
    DATA_FILE.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def make_post(author: str, content: str, image_url: str = "") -> dict[str, Any]:
    return {
        "id": str(uuid4()),
        "author": author,
        "content": content.strip(),
        "image_url": image_url.strip(),
        "likes": [],
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


def like_post(posts: list[dict[str, Any]], post_id: str, user: str) -> None:
    for post in posts:
        if post["id"] == post_id:
            likes = set(post.get("likes", []))
            if user in likes:
                likes.remove(user)
            else:
                likes.add(user)
            post["likes"] = sorted(likes)
            break


def delete_post(posts: list[dict[str, Any]], post_id: str, user: str) -> list[dict[str, Any]]:
    return [p for p in posts if not (p["id"] == post_id and p["author"] == user)]


def render_post_card(post: dict[str, Any], current_user: str, posts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    with st.container(border=True):
        st.markdown(f"### @{post['author']}")
        st.caption(post.get("created_at", ""))
        st.write(post.get("content", ""))

        image_url = post.get("image_url", "").strip()
        if image_url:
            st.image(image_url, use_container_width=True)

        likes = post.get("likes", [])
        like_count = len(likes)
        has_liked = current_user in likes
        like_label = f"{'Unlike' if has_liked else 'Like'} ({like_count})"

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(like_label, key=f"like_{post['id']}", use_container_width=True):
                like_post(posts, post["id"], current_user)
                save_posts(posts)
                st.rerun()

        with col2:
            if post["author"] == current_user:
                if st.button("Delete", key=f"delete_{post['id']}", use_container_width=True):
                    posts = delete_post(posts, post["id"], current_user)
                    save_posts(posts)
                    st.rerun()

    return posts


def main() -> None:
    st.set_page_config(page_title="Mini SNS", page_icon="📝", layout="centered")
    st.title("Mini SNS")
    st.caption("Streamlitで作ったシンプルなSNSアプリ")

    current_user = st.sidebar.selectbox("ログインユーザー", DEFAULT_USERS)

    posts = load_posts()

    with st.form("post_form", clear_on_submit=True):
        st.subheader("投稿を作成")
        content = st.text_area("本文", placeholder="いま何してる？", max_chars=280)
        image_url = st.text_input("画像URL（任意）", placeholder="https://...")
        submitted = st.form_submit_button("投稿する", use_container_width=True)

    if submitted:
        if not content.strip():
            st.warning("本文を入力してください。")
        else:
            posts.append(make_post(current_user, content, image_url))
            save_posts(posts)
            st.success("投稿しました。")
            st.rerun()

    st.subheader("タイムライン")
    if not posts:
        st.info("まだ投稿がありません。最初の投稿を作ってみてください。")
        return

    sorted_posts = sorted(posts, key=lambda p: p.get("created_at", ""), reverse=True)
    for post in sorted_posts:
        posts = render_post_card(post, current_user, posts)


if __name__ == "__main__":
    main()
    import streamlit as st
    st.title("RIZINファイター図鑑")
    if"show_record_mikuru" not in st.session_state:
        st.session_state.show_record_mikuru=False
    if"show_record_akimoto"not in st.session_state:
        st.session_state.show_record_akimoto=False
    if"show_record_kubo"not in st.session_state:
        st.session_state.show_record_kubo=False
    if"show_record_satoshi"not in st.session_state:
        st.session_state.show_record_satoshi=False
    if"show_record_ando"not in st.session_state:
        st.session_state.show_record_ando=False

    st.header("選手紹介")
    Name=st.text_input("裕二朗")
    

fighter=st.selectbox("選手を選んでください",["朝倉未来","秋元強真","久保優太","ホベルト・サトシ・ソウザ","安藤達也"])
if fighter == "朝倉未来":
    st.write("超人気ファイター")
    st.subheader("得意技　右フック")
    if st.button("戦績"):
        st.session_state.show_record_mikuru= not st.session_state.show_record_mikuru
    if st.session_state.show_record_mikuru:
       st.table({"項目":["勝ち","負け","得意技"],"内容":["19","6","右フック"]})
    st.image("/Users/yujiro/Documents/mikuru.jpg")
elif fighter == "秋元強真":
    st.write("打撃が得意なファイター")
    if st.button("戦績"):
        st.session_state.show_record_akimoto= not st.session_state.show_record_akimoto
    if st.session_state.show_record_akimoto:
       st.write("12勝1敗")
    st.image("/Users/yujiro/Documents/akimoto.jpg")
elif fighter  ==  "久保優太":
    st.write("距離感が上手いファイター")
    if st.button("戦績"):
        st.session_state.show_record_kubo= not st.session_state.show_record_kubo
    if st.session_state.show_record_kubo:
       st.write("5勝3敗")
    st.image("/Users/yujiro/Documents/kubo.jpg")
elif fighter  ==  "ホベルト・サトシ・ソウザ":
    st.write("圧倒的な極め力があるファイター")
    if st.button("戦績"):
        st.session_state.show_record_satoshi= not st.session_state.show_record_satoshi
    if st.session_state.show_record_satoshi:
       st.write("20勝4敗")
    st.image("/Users/yujiro/Documents/satoshi.jpg")
elif fighter  ==  "安藤達也":
    st.write("全体的に華があるファイター")
    if st.button("戦績"):
        st.session_state.show_record_ando= not st.session_state.show_record_ando
    if st.session_state.show_record_ando:
       st.write("16勝5敗")
    st.image("/Users/yujiro/Documents/ando.jpg")                              

