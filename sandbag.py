import streamlit as st
import streamlit.components.v1 as components
st.markdown("""
<style>
.fade-in {
    animation: fadeIn 2s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="殴り屋", layout="wide")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Yuji+Syuku&display=swap" rel="stylesheet">           
<div style="text-align:center; max-width:900px; margin:auto; position:relative; left:30px;">

<h1 style="
font-size:100px;
font-family:'Yuji Syuku', serif;
letter-spacing:8px;
text-shadow:2px 2px 4px #333;
">
殴り屋
</h1>
<h4 style="margin-top:-15px; font-family:'Yuji Syuku', serif; letter-spacing:2px;">
完全個室サンドバッグジム
</h4>

</div>
""", unsafe_allow_html=True)

st.markdown('<div class="fade-in">', unsafe_allow_html=True)


# st.image(
#     "ad439703-fb54-4255-a3b0-923d385af538.png",
#     width="stretch"
# )


st.markdown("""
<div style="
background: linear-gradient(
to top,
rgba(0,0,0,0.8),
rgba(0,0,0,0.3),
rgba(0,0,0,0)
);
padding:40px;
margin-top:-120px;
position:relative;
z-index:10;
color:white;
text-align:center;
">

st.markdown(
    """
    <h2>誰にも見られず、思いっきり発散。</h2>
    <br><br>
    """,
    unsafe_allow_html=True
)

st.success("📲 LINEで24時間予約受付中")

st.link_button(
    "🟢 LINEで今すぐ予約する",
    "https://lin.ee/WgzkVj4",
    use_container_width=True
)

    <br><br>
    """,
    unsafe_allow_html=True
)
            
<p>
ストレス発散・運動不足解消・初心者歓迎
</p>

</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.success("完全予約制（当日予約OK）｜初心者大歓迎｜手ぶらOK！")

st.header("POINT")

col1, col2 = st.columns(2)

with col1:
    st.info("🔒 完全個室")

    st.write("""
        周囲を気にせず、
        自分だけの空間で利用可能。
        """)

    st.info("🛡️ 安心・安全")

    st.write("""
    防犯カメラ設置で
    安心して利用可能。
    """)

with col2:
    st.info("✨ 清潔・快適")

    st.write("""
    定期清掃・換気で
    快適な空間。
    """)

    st.info("😊 初心者歓迎")

    st.write("""
    女性や未経験の方でも
    安心して利用可能。
    """)

st.divider()
st.header("PRICE")
st.success("💰 1時間 1,200円〜")

st.subheader("🥊 完全個室 1時間利用")

st.info("""
👥 追加1名ごとに +1,000円
🧤 手ぶらOK
🔒 完全個室
""")

st.success("""
🥊 1名利用　　1,200円

🥊 2名利用　　2,200円

🥊 3名利用　　3,200円
""")

st.caption("※料金は仮設定です。変更する可能性があります。")

st.divider()

st.header("FLOW")

st.info("① LINE・Instagramから予約")
st.info("② 来店")
st.info("③ 完全個室で発散")


st.divider()
st.header("VOICE")

st.caption("💬 お客様の声")
with st.expander("👨 20代男性（会社員）"):
    st.write("仕事終わりのストレス発散で利用しています。完全個室なので周りを気にせず思い切り打てるのが最高です。")

with st.expander("👩 30代女性（事務職）"):
    st.write("初めての利用で不安でしたが、誰にも見られないので気軽に運動できました。運動不足解消にもおすすめです。")

with st.expander("👨 40代男性（自営業）"):
    st.write("短時間でもしっかり汗をかけます。ジムに通うほどではないけど体を動かしたい人にぴったりです。")

st.caption("※個人の感想です。")

st.divider()
st.header("FAQ")

with st.expander("初心者でも利用できますか？"):
    st.write("もちろん可能です。")

with st.expander("予約は必要ですか？"):
    st.write("完全予約制です。")

with st.expander("何人まで利用できますか？"):
    st.write("最大3名まで利用可能です。")

with st.expander("服装は何でも大丈夫ですか？"):
    st.write("動きやすい服装をおすすめしています。")

with st.expander("女性でも利用できますか？"):
    st.write("もちろん可能です。完全個室なので安心してご利用いただけます。")

with st.expander("手ぶらで利用できますか？"):
    st.write("グローブは無料で貸出しています。")
st.divider()
st.header("FACILITY")

col1, col2, col3 = st.columns(3)

with col1:
    # st.image("/Users/yujiro/Downloads/sandbag2.jpg", width=160)
    st.markdown("#### 🥊 サンドバッグ")
    st.write("本格サンドバッグを設置")

with col2:
    # st.image("/Users/yujiro/Downloads/gurove.jpg", width=220)
    st.markdown("### 🥊 グローブ")
    st.write("無料で貸出")

with col3:
    # st.image("/Users/yujiro/Downloads/kositu.jpg", width=220)
    st.markdown("### 🚪 完全個室")
    st.write("周囲を気にせず利用可能")

st.caption("※掲載画像はイメージです。実際の設備・内装とは異なる場合があります。")

st.divider()
st.header("ACCESS")

st.info("""
🚧 COMING SOON 🚧

神戸市内でオープン準備中

詳細は決まり次第お知らせします
""")


st.divider()
st.header("CONTACT")

st.subheader("ご予約はこちら")

st.info("ご予約・お問い合わせはLINEまたはInstagramからお願いします。")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "💬 LINEで予約する",
        "https://lin.ee/WgzkVj4",
        use_container_width=True
    )

with col2:
    st.link_button(
        "📷 Instagramを見る",
        "https://www.instagram.com/sandbag_naguriya/",
        use_container_width=True
    )