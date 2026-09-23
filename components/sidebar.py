"""
sidebar.py — Premium sidebar navigation with logo, nav links, and footer.
"""
import streamlit as st
from utils.constants import NAV_ITEMS, PROJECT_NAME


def render_sidebar() -> str:
    """Render the sidebar and return the selected page name."""
    with st.sidebar:
        # Logo & branding
        st.markdown(
            f"""
            <div style="padding: 20px 8px 24px; border-bottom: 1px solid var(--border); margin-bottom: 16px;">
                <div style="display:flex;align-items:center;gap:12px;">
                    <div style="width:40px;height:40px;background:linear-gradient(135deg,#2563EB,#7C3AED);
                        border-radius:10px;display:flex;align-items:center;justify-content:center;
                        font-size:18px;font-weight:800;color:#fff;">LP</div>
                    <div>
                        <div style="font-size:16px;font-weight:700;color:#1E293B;">{PROJECT_NAME}</div>
                        <div style="font-size:11px;color:#64748B;font-weight:500;">ML Dashboard</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Navigation
        st.markdown(
            '<p style="font-size:11px;font-weight:600;color:#64748B;text-transform:uppercase;'
            'letter-spacing:1px;padding:0 8px;margin-bottom:8px;">Navigation</p>',
            unsafe_allow_html=True,
        )

        labels = [f"{icon}  {name}" for icon, name in NAV_ITEMS]
        selection = st.radio("Nav", labels, label_visibility="collapsed")



    # Extract the page name from selection
    selected_page = selection.split("  ", 1)[1] if "  " in selection else selection
    return selected_page
