# -*- coding: utf-8 -*-
"""
小店智析 - 智能数据分析助手
主入口文件
"""

import sys

# 强制设置默认编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import streamlit as st

# 导入配置和样式
from config import PAGE_CONFIG, PAGES, PAGE_KEYS
from styles import get_custom_css
from utils import init_session_state

# 导入页面
from pages import (
    render_home_page,
    render_upload_page,
    render_results_page,
    render_advice_page,
    render_help_page
)

# 页面基础配置
st.set_page_config(**PAGE_CONFIG)

# 应用自定义CSS样式
st.markdown(get_custom_css(), unsafe_allow_html=True)

# 初始化 session_state
init_session_state()


# ===================== 侧边栏导航 =====================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 24px 0 32px 0;">
            <div style="font-size: 18px; font-weight: 700; color: #FFFFFF; letter-spacing: 1px;">小店智析</div>
            <div style="font-size: 11px; color: #94A3B8; margin-top: 6px;">数据分析助手</div>
        </div>
    """, unsafe_allow_html=True)
    
    current_idx = PAGE_KEYS.index(st.session_state.get("nav_page", "首页")) if st.session_state.get("nav_page", "首页") in PAGE_KEYS else 0
    
    selected = st.radio("", PAGES, index=current_idx, key="nav_radio", label_visibility="collapsed")
    
    selected_key = PAGE_KEYS[PAGES.index(selected)]
    if st.session_state.get("nav_page") != selected_key:
        st.session_state["nav_page"] = selected_key
    
    st.markdown("---")
    
    # 侧边栏快捷操作
    if st.session_state.get("df") is not None:
        if st.button("重置数据", key="sidebar_reset", use_container_width=True):
            for key in ["df", "uploaded_file_name", "result", "code", "fig", "advice", "show_results", "history", "missing_fields"]:
                st.session_state[key] = None if key != "history" and key != "missing_fields" else []
            st.session_state["show_results"] = False
            st.session_state["question"] = ""
            st.rerun()
    
    st.markdown("""
        <div style="padding: 12px 0; color: #64748B; font-size: 10px; text-align: center;">
            © 小店智析
        </div>
    """, unsafe_allow_html=True)


# ===================== 主程序路由 =====================
page = st.session_state.get("nav_page", "首页")

if page == "首页":
    render_home_page()
elif page == "上传与提问":
    render_upload_page()
elif page == "分析结果":
    render_results_page()
elif page == "经营建议":
    render_advice_page()
elif page == "帮助中心":
    render_help_page()
else:
    render_home_page()
