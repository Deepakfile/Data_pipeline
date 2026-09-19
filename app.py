from __future__ import annotations
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="DataFlow AI", page_icon="📊", layout="wide")

PAGES = {
    "📊 Dashboard": "dashboard",
    "📤 Upload Data": "upload",
    "🔍 Data Profiler": "profiler",
    "🛠️ Cleaning Pipeline": "pipeline",
    "📈 AI Insights Studio": "insights",
    "✅ Validation": "validation",
    "📝 Change Log": "changelog",
    "📦 Export": "export",
    "⚙️ Settings": "settings",
}

def sidebar():
    with st.sidebar:
        st.markdown("# 📊 DataFlow AI")
        st.caption("Universal Data Cleaning & Analytics Pipeline")
        page = st.radio("Navigate", list(PAGES), label_visibility="collapsed")
        st.divider()
        df = st.session_state.get("df_raw")
        if df is not None:
            meta = st.session_state.get("file_meta", {})
            st.success(f"📁 {meta.get('filename', 'Loaded dataset')}")
            st.caption(f"{len(df):,} rows · {len(df.columns)} columns")
            if st.session_state.get("pipeline_ran"):
                st.metric("Quality Score", f"{st.session_state.get('clean_quality', 0):.1f}/100")
        else:
            st.info("Upload a dataset to begin.")
        st.divider()
        st.caption("DataFlow AI v2.0")
    return PAGES[page]

def main():
    page = sidebar()
    if page == "dashboard":
        from ui.dashboard import render; render()
    elif page == "upload":
        from ui.upload import render; render()
    elif page == "profiler":
        from ui.profiler import render; render()
    elif page == "pipeline":
        from ui.pipeline import render; render()
    elif page == "insights":
        from ui.insights import render; render()
    elif page == "validation":
        from ui.validation import render; render()
    elif page == "changelog":
        from ui.changelog import render; render()
    elif page == "export":
        from ui.export import render; render()
    elif page == "settings":
        from ui.settings import render; render()

if __name__ == "__main__":
    main()
