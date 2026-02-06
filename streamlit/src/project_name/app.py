from __future__ import annotations

import streamlit as st

from project_name.pages import dashboard, home, settings
from project_name.utils.state import init_session_state


def main() -> None:
    st.set_page_config(
        page_title="My App",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    init_session_state()

    pages = [
        st.Page(home.render, title="ホーム", icon="🏠", default=True),
        st.Page(dashboard.render, title="ダッシュボード", icon="📊"),
        st.Page(settings.render, title="設定", icon="⚙️"),
    ]

    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    main()
