import streamlit as st

st.set_page_config(layout="wide")

st.title("🧾 Hóa đơn bán hàng")
st.markdown("#### Giao diện đặt hàng giống Kiot")

col1, col2 = st.columns([2, 1])

with col1:
    st.text_input("🔍 Tìm sản phẩm (F3)", key="search_bar")
    st.table([
        {"Mã SP": "MAZVE10", "Tên": "Sony ZV-E10", "SL": 1, "Đơn giá": 15700000}
    ])

with col2:
    st.text_input("👤 Tên khách hàng")
    st.text_input("📞 Số điện thoại")
    st.text_area("🏠 Địa chỉ giao hàng")
    st.checkbox("COD")
    st.markdown("### 💰 Tổng cộng: **15,700,000**")
    st.button("💳 THANH TOÁN")

st.markdown("---")
st.caption("PU Studio - LarkBase Extension")
