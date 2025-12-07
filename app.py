
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="自分専用競馬予想", layout="wide")
st.title("🐎 自分だけの競馬予想アプリ")

tab1, tab2, tab3 = st.tabs(["今日のレース入力", "過去レース登録", "学習・設定"])

with tab1:
    st.subheader("今日のレースを入力して予想を見る")
    horses = []
    with st.form("today_race"):
        for i in range(18):
            with st.expander(f"{i+1}頭目　（馬名空欄で終了）", expanded=(i<6)):
                c1,c2,c3,c4 = st.columns([4,2,2,3])
                name = c1.text_input("馬名", key=f"n{i}")
                pop  = c2.number_input("人気", 1,18, i+1, key=f"p{i}")
                odds = c3.number_input("オッズ",1.0,500.0,10.0,0.1, key=f"o{i}")
                if name:
                    horses.append({"馬名":name, "人気":pop, "オッズ":odds})
        if st.form_submit_button("予想してもらう！", type="primary"):
            if horses:
                df = pd.DataFrame(horses)
                st.write("### 入力された出馬表")
                st.dataframe(df.style.format({"オッズ":"{:.1f}"}), use_container_width=True)
                st.success("データが貯まったらここにAI予想が出ます！")
            else:
                st.warning("1頭以上入力してください")

with tab2:
    st.subheader("過去の的中レースを登録（これでAIが賢くなる）")
    st.info("もうすぐ完成！今は手入力でOK")

with tab3:
    st.write("学習ボタン・設定などは順次追加します")
