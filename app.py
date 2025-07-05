import streamlit as st

st.set_page_config(page_title="LarkBase Extension", layout="wide")
st.title("🔗 Nhập liệu từ LarkBase")
st.write("Chào bạn! Đây là phần mở rộng custom cho LarkBase.")

data = st.text_area("Nhập nội dung", "")
if st.button("Xử lý"):
    st.success(f"✅ Bạn đã nhập: {data}")
