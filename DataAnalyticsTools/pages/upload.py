# -*- coding: utf-8 -*-
"""上传与提问页面"""

import streamlit as st
import pandas as pd
from datetime import datetime

from config import CANONICAL_FIELDS
from utils import suggest_field_mapping, check_fields_and_degrade, format_result, export_results
from analysis import handle_analysis


def render_upload_page():
    """渲染上传与提问页面 - 简洁核心版"""
    is_fullscreen = st.session_state.get("fullscreen_mode", False)
    has_results = st.session_state.get("show_results") and st.session_state.get("result") is not None
    
    if is_fullscreen and has_results:
        render_fullscreen_results()
        return
    
    # 简洁页面标题
    st.markdown('<div class="page-title">数据分析</div>', unsafe_allow_html=True)
    
    if has_results:
        # 有结果时：左侧65%，右侧35%
        left_col, right_col = st.columns([0.65, 0.35], gap="medium")
    else:
        # 无结果时：只显示左侧，右侧完全隐藏
        left_col = st.container()
        right_col = None
    
    with left_col:
        render_upload_main_panel()
    
    if right_col is not None:
        with right_col:
            render_results_panel()


def render_upload_main_panel():
    """渲染上传页面的主面板 - 简洁核心版"""
    
    # ===== 数据上传区域 =====
    if st.session_state.get("df") is not None:
        df = st.session_state["df"]
        col_info, col_reset = st.columns([0.8, 0.2])
        with col_info:
            st.markdown(f"**已加载数据：** {st.session_state.get('uploaded_file_name')}（{len(df)} 条）")
        with col_reset:
            if st.button("重置", key="reset_data", use_container_width=True):
                for key in ["df", "uploaded_file_name", "result", "code", "fig", "advice", "show_results", "missing_fields"]:
                    st.session_state[key] = None if key != "missing_fields" else []
                st.session_state["show_results"] = False
                st.rerun()
    else:
        uploaded_file = st.file_uploader(
            "上传数据文件", type=["xlsx", "xls", "csv"],
            key="file_uploader", label_visibility="collapsed",
            help="支持 Excel 和 CSV 格式"
        )
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith((".xlsx", ".xls")):
                    df = pd.read_excel(uploaded_file)
                elif uploaded_file.name.endswith(".csv"):
                    try:
                        df = pd.read_csv(uploaded_file, encoding="utf-8-sig")
                    except:
                        df = pd.read_csv(uploaded_file, encoding="gbk")
                
                # 自动字段映射
                suggested = suggest_field_mapping(df.columns.tolist(), CANONICAL_FIELDS)
                rename_map = {v: k for k, v in suggested.items() if v}
                df = df.rename(columns=rename_map)
                
                # 字段校验
                missing, degraded = check_fields_and_degrade(df)
                st.session_state["missing_fields"] = missing
                
                st.session_state["df"] = df
                st.session_state["uploaded_file_name"] = uploaded_file.name
                st.rerun()
                
            except Exception as e:
                st.error(f"文件解析失败：{str(e)}")
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    
    # ===== 分析需求输入框 =====
    question = st.text_input(
        "分析需求",
        value=st.session_state.get("question", ""),
        key="question_input",
        placeholder="输入您的分析需求，如：销量最高的商品是哪个",
        label_visibility="collapsed"
    )
    st.session_state["question"] = question
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    
    # ===== 开始分析按钮 =====
    st.markdown('<div class="analyze-btn">', unsafe_allow_html=True)
    submit_btn = st.button("开始分析", key="start_analyze", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submit_btn:
        handle_analysis()


def render_results_panel():
    """渲染右侧结果面板 - 简洁版，底部文字标签页"""
    
    
    
    # 顶部操作栏 - 简化
    st.markdown('<div class="panel-title-large">分析结果</div>', unsafe_allow_html=True)
    
    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    
    # 底部三个文字标签页 - 无图标，简洁风格
    tab1, tab2, tab3 = st.tabs(["结论", "图表", "建议"])
    
    with tab1:
        render_conclusion_tab()
    with tab2:
        render_chart_tab()
    with tab3:
        render_advice_tab()
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="result-panel-actions">', unsafe_allow_html=True)
    col_spacer, col_full, col_close = st.columns([0.8, 0.1, 0.1])
    with col_full:
        if st.button("⛶", key="fullscreen_btn", help="全屏"):
            st.session_state["fullscreen_mode"] = True
            st.rerun()
    with col_close:
        if st.button("✕", key="close_results_btn", help="关闭"):
            st.session_state["show_results"] = False
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_fullscreen_results():
    """渲染全屏结果页面 - 简洁版"""
    st.markdown('<div class="page-title">分析结果</div>', unsafe_allow_html=True)
    
    # 简洁文字标签页
    tab1, tab2, tab3 = st.tabs(["结论", "图表", "建议"])
    
    with tab1:
        render_conclusion_tab()
    with tab2:
        render_chart_tab()
    with tab3:
        render_advice_tab()
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        export_text = export_results()
        st.download_button(
            label="导出结果",
            data=export_text,
            file_name=f"分析报告_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            key="download_report",
            use_container_width=True
        )
    with col2:
        if st.button("退出全屏", key="exit_fullscreen_btn", use_container_width=True):
            st.session_state["fullscreen_mode"] = False
            st.rerun()
    with col3:
        if st.button("继续提问", key="continue_asking", use_container_width=True):
            st.session_state["fullscreen_mode"] = False
            st.session_state["question"] = ""
            st.rerun()


def render_conclusion_tab():
    """渲染结论标签页 - 简洁版"""
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


def render_chart_tab():
    """渲染图表标签页 - 简洁版"""
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


def render_advice_tab():
    """渲染建议标签页"""
    advice_list = st.session_state.get("advice")
    if not advice_list:
        st.info("暂无经营建议")
        return
    
    uploaded_file_name = st.session_state.get("uploaded_file_name")
    
    st.markdown('<div class="advice-card"><div class="advice-header">经营建议</div><div class="advice-list">', unsafe_allow_html=True)
    
    for i, advice in enumerate(advice_list):
        suffix = f"（依据：{uploaded_file_name}）" if uploaded_file_name else ""
        col_advice, col_copy = st.columns([0.9, 0.1])
        with col_advice:
            st.markdown(f"""
                <div class="advice-item">
                    <div class="advice-number">{i+1}.</div>
                    <div>{advice}{suffix}</div>
                </div>
            """, unsafe_allow_html=True)
        with col_copy:
            if st.button("📋", key=f"copy_advice_{i}", help="复制建议"):
                st.toast(f"已复制：{advice}")
    
    st.markdown('</div></div>', unsafe_allow_html=True)
