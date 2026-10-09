# -*- coding: utf-8 -*-
"""经营建议页面"""

import streamlit as st


def render_advice_page():
    """渲染经营建议页面"""
    st.markdown('<div class="page-title">经营建议</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">基于数据分析结果，为您生成可落地的经营优化建议</div>', unsafe_allow_html=True)
    
    advice_list = st.session_state.get("advice")
    
    if not advice_list:
        st.warning("暂无经营建议，请先完成数据分析")
        if st.button("前往数据分析", key="goto_upload_from_advice"):
            st.session_state["nav_page"] = "上传与提问"
            st.rerun()
        return
    
    uploaded_file_name = st.session_state.get("uploaded_file_name")
    
    # 一键复制所有建议
    all_advice = "\n".join([f"{i+1}. {a}" for i, a in enumerate(advice_list)])
    if st.button("复制所有建议", key="copy_all_advice"):
        st.toast("已复制所有建议到剪贴板")
    
    st.markdown("""
        <div class="advice-card" style="max-width: 800px;">
            <div class="advice-header">智能经营建议</div>
            <div class="advice-list">
    """, unsafe_allow_html=True)
    
    for i, advice in enumerate(advice_list, 1):
        suffix = f"（数据依据：{uploaded_file_name}）" if uploaded_file_name else ""
        st.markdown(f"""
            <div class="advice-item">
                <div class="advice-number">{i}.</div>
                <div><strong>建议 {i}：</strong>{advice}{suffix}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.info("以上建议基于您上传的数据自动生成，仅供参考。")
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("返回提问", key="back_from_advice", use_container_width=True):
            st.session_state["nav_page"] = "上传与提问"
            st.rerun()
    with col2:
        if st.button("查看结果", key="goto_results_from_advice", use_container_width=True):
            st.session_state["nav_page"] = "分析结果"
            st.rerun()
    with col3:
        if st.button("重新分析", key="reanalyze_from_advice", use_container_width=True):
            st.session_state["show_results"] = False
            st.session_state["result"] = None
            st.session_state["nav_page"] = "上传与提问"
            st.rerun()
