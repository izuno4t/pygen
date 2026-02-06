"""Form components."""

from __future__ import annotations

import streamlit as st


def render_contact_form() -> None:
    with st.form("contact_form"):
        st.text_input("メール", key="contact_email")
        st.text_area("メッセージ", key="contact_message")
        submitted = st.form_submit_button("送信")
        if submitted:
            st.success("送信しました")
