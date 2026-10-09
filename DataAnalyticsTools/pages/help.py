# -*- coding: utf-8 -*-
"""帮助中心页面"""

import streamlit as st


def render_help_page():
    """渲染帮助中心页面"""
    st.markdown('<div class="page-title">帮助中心</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">使用指南、常见问题解答与数据安全说明</div>', unsafe_allow_html=True)
    
    st.markdown("### 使用指南")
    
    steps = [
        ("1. 上传数据", "支持 Excel (.xlsx, .xls) 和 CSV 格式，建议使用 UTF-8 编码。"),
        ("2. 字段映射", "系统会自动匹配字段，如不准确可手动调整。"),
        ("3. 输入问题", "用自然语言描述分析需求，如「销量最高的商品是哪个」。"),
        ("4. 查看结果", "系统自动生成分析结果、可视化图表和经营建议。"),
    ]
    
    for title, desc in steps:
        st.markdown(f'<div class="faq-item"><div class="faq-question">{title}</div><div class="faq-answer">{desc}</div></div>', unsafe_allow_html=True)
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.markdown("### 常见问题")
    
    faqs = [
        ("Q: 支持什么格式的数据？", "A: 支持 Excel (.xlsx, .xls) 和 CSV 格式，建议使用 UTF-8 编码。"),
        ("Q: 为什么分析结果不准确？", "A: 请检查字段映射是否正确，数据格式是否规范，问题描述是否清晰。"),
        ("Q: 可以分析多大的数据？", "A: 建议单次上传不超过 10 万行数据。"),
        ("Q: 如何导出分析结果？", "A: 在分析结果页面点击「导出报告」按钮即可下载 TXT 格式报告。"),
    ]
    
    for q, a in faqs:
        st.markdown(f'<div class="faq-item"><div class="faq-question">{q}</div><div class="faq-answer">{a}</div></div>', unsafe_allow_html=True)
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.markdown("### 数据安全说明")
    st.markdown("""
        <div class="security-notice">
            <strong>我们重视您的数据安全：</strong><br><br>
            • 数据仅用于本次分析会话，不会永久存储<br>
            • 分析过程中数据仅在内存中处理<br>
            • 我们不会将数据用于其他用途或与第三方共享
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.markdown("### 意见反馈")
    st.markdown("如有问题或建议，欢迎联系：support@xiaodianzhixi.com")
    
    st.markdown('<div class="footer">小店智析 © 2024 | 专为中小型商家打造的智能数据分析工具</div>', unsafe_allow_html=True)
