# -*- coding: utf-8 -*-
"""首页"""

import streamlit as st


def render_home_page():
    """渲染首页 - 简洁版"""
    # Hero区域 - 简化
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">小店智析</div>
            <div class="hero-slogan">上传数据，用自然语言完成数据分析</div>
        </div>
    """, unsafe_allow_html=True)
    
    # 立即开始按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("开始使用", key="home_start_btn", use_container_width=True):
            st.session_state["nav_page"] = "上传与提问"
            st.rerun()
    
    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
    
    # 功能介绍卡片 - 简化，无图标
    cols = st.columns(4)
    features = [
        ("数据上传", "支持Excel和CSV格式，智能识别字段"),
        ("自然语言提问", "用日常语言描述分析需求"),
        ("智能可视化", "自动生成图表展示分析结果"),
        ("经营建议", "基于数据生成优化建议"),
    ]
    
    for col, (title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="security-notice" style="max-width: 500px; margin: 0 auto;">
            数据安全：您上传的数据仅用于本次分析，不会永久存储。
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="footer">小店智析 © 2024</div>', unsafe_allow_html=True)
