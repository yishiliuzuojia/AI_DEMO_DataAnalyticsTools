# -*- coding: utf-8 -*-
"""分析结果页面"""

import streamlit as st
from datetime import datetime

from utils import format_result, export_results


def render_results_page():
    """渲染分析结果页面"""
    st.markdown('<div class="page-title">分析结果</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">查看完整的数据分析结果与可视化图表</div>', unsafe_allow_html=True)
    
    if st.session_state.get("result") is None:
        st.warning("暂无分析结果，请先完成数据分析")
        if st.button("前往数据分析", key="goto_upload_from_results"):
            st.session_state["nav_page"] = "上传与提问"
            st.rerun()
        return
    
    tab1, tab2, tab3 = st.tabs(["结论", "图表", "建议"])
    
    with tab1:
        _render_conclusion()
    with tab2:
        _render_chart()
    with tab3:
        _render_advice()
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        export_text = export_results()
        st.download_button(
            label="导出报告",
            data=export_text,
            file_name=f"分析报告_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            key="download_report_page",
            use_container_width=True
        )
    with col2:
        if st.button("继续提问", key="continue_from_results", use_container_width=True):
            st.session_state["nav_page"] = "上传与提问"
            st.session_state["question"] = ""
            st.rerun()


def _render_conclusion():
    """渲染结论内容"""
    result = st.session_state.get("result")
    if result is None:
        st.info("暂无分析结果")
        return
    
    formatted_result = format_result(result)
    st.markdown(f"""
        <div class="result-card">
            <div class="result-title">分析结果</div>
            <div class="result-value">{formatted_result}</div>
        </div>
    """, unsafe_allow_html=True)
    
    uploaded_file_name = st.session_state.get("uploaded_file_name")
    df = st.session_state.get("df")
    if uploaded_file_name and df is not None:
        st.caption(f"数据来源：{uploaded_file_name}（{df.shape[0]} 条）")
    
    code = st.session_state.get("code")
    if code:
        with st.expander("查看分析代码", expanded=False):
            st.code(code, language="python")


def _render_chart():
    """渲染图表内容"""
    fig = st.session_state.get("fig")
    if fig is None:
        st.info("暂无可视化图表")
        return
    
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font={"family": "sans-serif", "size": 12, "color": "#2C3E50"},
        margin={"l": 16, "r": 16, "t": 40, "b": 16},
    )
    fig.update_xaxes(showgrid=True, gridcolor="#F5F6F7", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#F5F6F7", zeroline=False)
    
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def _render_advice():
    """渲染建议内容"""
    advice_list = st.session_state.get("advice")
    if not advice_list:
        st.info("暂无经营建议")
        return
    
    uploaded_file_name = st.session_state.get("uploaded_file_name")
    
    st.markdown('<div class="advice-card"><div class="advice-header">经营建议</div><div class="advice-list">', unsafe_allow_html=True)
    
    for i, advice in enumerate(advice_list, 1):
        suffix = f"（依据：{uploaded_file_name}）" if uploaded_file_name else ""
        st.markdown(f"""
            <div class="advice-item">
                <div class="advice-number">{i}.</div>
                <div>{advice}{suffix}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)
