# -*- coding: utf-8 -*-
"""CSS样式定义"""

def get_custom_css():
    """返回自定义CSS样式"""
    return """
    <style>
      /* ===== 简洁浅色主题变量 ===== */
      :root, [data-theme="light"], [data-theme="dark"] {
        --primary: #7CB9E8;
        --primary-light: #A8D4F0;
        --primary-dark: #5BA3D9;
        --primary-weak: #E8F4FC;
        --bg: #FAFBFC;
        --card: #FFFFFF;
        --text: #2C3E50;
        --text-secondary: #5D6D7E;
        --muted: #7F8C8D;
        --border: #E5E8EB;
        --success: #7DCEA0;
        --success-light: #E8F8F0;
        --error: #E8A09A;
        --error-light: #FDF2F2;
        --warning: #F9D79B;
        --warning-light: #FEF9E7;
        --info: #85C1E9;
        --info-light: #EBF5FB;
        
        --background-color: #FAFBFC !important;
        --secondary-background-color: #FFFFFF !important;
        --text-color: #2C3E50 !important;
      }

      @media (prefers-color-scheme: dark) {
        :root { color-scheme: light !important; }
      }

      html, body, .stApp, [data-testid="stAppViewContainer"] {
        background: #FAFBFC !important;
        color: #2C3E50 !important;
        color-scheme: light !important;
      }

      /* 隐藏 Streamlit 顶部原生框架（会覆盖页面内容，如右上角 Deploy / Rerun 等） */
      header, [data-testid="stHeader"], [data-testid="stDecoration"] {
        display: none !important;
        height: 0 !important;
      }

      [data-testid="stToolbar"] {
        display: none !important;
        height: 0 !important;
      }

      [data-testid="stAppViewContainer"] > .main {
        padding-top: 0 !important;
      }

      /* 侧边栏收起后的“打开”按钮（不同版本 testid 可能不同，做兼容） */
      [data-testid="collapsedControl"],
      [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        top: 12px !important;
        left: 12px !important;
        z-index: 99999 !important;
      }

      [data-testid="collapsedControl"] button,
      [data-testid="stSidebarCollapsedControl"] button {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.10) !important;
      }

      button[aria-label="Open sidebar"],
      button[title="Open sidebar"],
      button[aria-label="打开侧边栏"],
      button[title="打开侧边栏"] {
        display: inline-flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        position: fixed !important;
        top: 12px !important;
        left: 12px !important;
        z-index: 99999 !important;
        background: rgba(255, 255, 255, 0.95) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.10) !important;
      }

      .main, [data-testid="stMain"] {
        background: #FAFBFC !important;
      }

      .stApp p, .stApp span, .stApp div, .stApp label,
      .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
        color: #2C3E50;
      }

      input, textarea, select,
      [data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"] {
        background: #FFFFFF !important;
        color: #2C3E50 !important;
      }

      /* 侧边栏 - 简洁深色 */
      [data-testid="stSidebar"] {
        background: #3D4F5F;
      }

      [data-testid="stSidebarNav"] {
        display: none;
      }

      /* 侧边栏所有文字统一白色 */
      [data-testid="stSidebar"],
      [data-testid="stSidebar"] *,
      [data-testid="stSidebar"] label,
      [data-testid="stSidebar"] span,
      [data-testid="stSidebar"] p,
      [data-testid="stSidebar"] div {
        color: #FFFFFF !important;
      }

      [data-testid="stSidebar"] .stMarkdown h3 {
        color: #FFFFFF !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        margin-bottom: 12px !important;
      }

      [data-testid="stSidebar"] .stMarkdown p,
      [data-testid="stSidebar"] .stMarkdown span,
      [data-testid="stSidebar"] .stMarkdown div {
        color: #FFFFFF !important;
      }

      /* Radio 导航菜单样式 - 纯文字简洁风格 */
      [data-testid="stSidebar"] [data-testid="stRadio"] label,
      [data-testid="stSidebar"] [data-testid="stRadio"] label span,
      [data-testid="stSidebar"] [data-testid="stRadio"] label p,
      [data-testid="stSidebar"] [data-testid="stRadio"] label div,
      [data-testid="stSidebar"] .stRadio label,
      [data-testid="stSidebar"] .stRadio label span,
      [data-testid="stSidebar"] .stRadio label p {
        color: #FFFFFF !important;
      }

      [data-testid="stSidebar"] .stRadio > div > label,
      [data-testid="stSidebar"] [data-testid="stRadio"] > div > label {
        background: transparent !important;
        color: rgba(255,255,255,0.8) !important;
        padding: 12px 16px !important;
        border-radius: 6px !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        transition: all 0.15s ease !important;
        margin-bottom: 2px !important;
        border-left: 3px solid transparent !important;
      }

      [data-testid="stSidebar"] .stRadio > div > label:hover,
      [data-testid="stSidebar"] [data-testid="stRadio"] > div > label:hover {
        background: rgba(255,255,255,0.08) !important;
        color: #FFFFFF !important;
      }

      [data-testid="stSidebar"] .stRadio > div > label[data-checked="true"],
      [data-testid="stSidebar"] [data-testid="stRadio"] > div > label[data-checked="true"] {
        background: rgba(255,255,255,0.12) !important;
        color: #FFFFFF !important;
        border-left: 3px solid #7CB9E8 !important;
        font-weight: 500 !important;
      }

      [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.15) !important;
        margin: 16px 0 !important;
      }

      /* 侧边栏按钮 */
      [data-testid="stSidebar"] .stButton button {
        background: rgba(255,255,255,0.08) !important;
        color: rgba(255,255,255,0.9) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        font-size: 13px !important;
        font-weight: 400 !important;
      }

      [data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.15) !important;
        border-color: rgba(255,255,255,0.25) !important;
      }

      .block-container {
        max-width: 1400px;
      }

      /* ===== 简洁卡片设计 ===== */
      .card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
      }

      .card-header {
        padding-bottom: 12px;
        margin-bottom: 16px;
        border-bottom: 1px solid var(--border);
      }

      .card-title {
        font-size: 15px;
        font-weight: 600;
        color: var(--text);
      }

      .page-title {
        font-size: 22px;
        font-weight: 600;
        color: var(--text);
        margin-bottom: 8px;
      }

      .page-subtitle {
        font-size: 14px;
        color: var(--text-secondary);
        margin-bottom: 24px;
      }

      /* Hero区域 - 简化 */
      .hero-section {
        background: linear-gradient(135deg, #7CB9E8 0%, #5BA3D9 100%);
        border-radius: 12px;
        padding: 40px 32px;
        margin-top: 1px;
        margin-bottom: 32px;
        color: white;
        text-align: center;
      }

      .hero-title {
        font-size: 28px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #white;
      }

      .hero-slogan {
        font-size: 15px;
        margin-bottom: 0;
        color: rgba(255,255,255,0.9);
      }

      /* 功能卡片 - 简化 */
      .feature-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 20px;
        height: 100%;
        transition: all 0.15s ease;
      }

      .feature-card:hover {
        border-color: var(--primary);
        box-shadow: 0 2px 8px rgba(124,185,232,0.15);
      }

      .feature-title { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
      .feature-desc { font-size: 13px; color: var(--text-secondary); line-height: 1.5; }

      /* ===== 柔和按钮样式 ===== */
      .stButton button {
        border-radius: 6px !important;
        padding: 0.5rem 1rem !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        border: none !important;
        background: #7CB9E8 !important;
        color: #FFFFFF !important;
        transition: all 0.15s ease !important;
        height: 36px !important;
      }

      .stButton button:hover {
        background: #5BA3D9 !important;
        box-shadow: 0 2px 6px rgba(124,185,232,0.25);
      }

      /* 下载按钮与蓝色按钮文字统一为白色 */
      .stDownloadButton button {
        border: none !important;
        background: #7CB9E8 !important;
        color: #FFFFFF !important;
        box-shadow: none !important;
      }

      .stDownloadButton button:hover {
        background: #5BA3D9 !important;
      }

      /* 次要按钮 */
      .secondary-btn .stButton button {
        background: #FFFFFF !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
      }

      .secondary-btn .stButton button:hover {
        background: var(--primary-weak) !important;
        border-color: var(--primary) !important;
        color: var(--primary-dark) !important;
      }

      /* 危险按钮 */
      .danger-btn .stButton button {
        background: #E8A09A !important;
      }

      .danger-btn .stButton button:hover {
        background: #D98880 !important;
      }

      /* 成功按钮 */
      .success-btn .stButton button {
        background: #7DCEA0 !important;
      }

      .success-btn .stButton button:hover {
        background: #5DBD89 !important;
      }

      /* 小按钮 */
      .small-btn .stButton button {
        padding: 0.25rem 0.75rem !important;
        font-size: 12px !important;
        height: 30px !important;
      }

      /* 主分析按钮 - 柔和绿色 */
      .analyze-btn .stButton button {
        width: 100%;
        padding: 0.75rem 1rem !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        height: 44px !important;
        background: linear-gradient(135deg, #7DCEA0 0%, #5DBD89 100%) !important;
      }

      .analyze-btn .stButton button:hover {
        background: linear-gradient(135deg, #5DBD89 0%, #48B178 100%) !important;
      }

      /* 骨架屏动画 */
      @keyframes skeleton-loading {
        0% { background-position: -200px 0; }
        100% { background-position: calc(200px + 100%) 0; }
      }

      .skeleton {
        background: linear-gradient(90deg, #E5E8EB 0px, #F5F6F7 40px, #E5E8EB 80px);
        background-size: 200px 100%;
        animation: skeleton-loading 1.5s ease-in-out infinite;
        border-radius: 6px;
      }

      .skeleton-text { height: 14px; margin-bottom: 8px; }
      .skeleton-title { height: 20px; width: 60%; margin-bottom: 16px; }
      .skeleton-chart { height: 180px; margin-bottom: 16px; }

      /* 加载动画 */
      .loading {
        display: flex;
        align-items: center;
        gap: 10px;
        background: var(--primary-weak);
        border: 1px solid var(--primary-light);
        border-radius: 6px;
        padding: 12px 14px;
        color: var(--text);
        font-size: 13px;
        margin: 12px 0;
      }

      .loading .spinner {
        width: 16px;
        height: 16px;
        border-radius: 50%;
        border: 2px solid var(--primary-light);
        border-top-color: var(--primary);
        animation: spin 0.8s linear infinite;
      }

      @keyframes spin {
        to { transform: rotate(360deg); }
      }

      /* 结果卡片 */
      .result-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
      }

      .result-title {
        font-size: 12px;
        color: var(--muted);
        margin-bottom: 6px;
      }

      .result-value {
        font-size: 18px;
        font-weight: 600;
        color: var(--text);
        line-height: 1.4;
      }

      /* 建议卡片 - 简化 */
      .advice-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 8px;
        overflow: hidden;
      }

      .advice-header {
        padding: 12px 16px;
        background: var(--success-light);
        border-bottom: 1px solid #D5F5E3;
        font-weight: 600;
        font-size: 14px;
        color: #27AE60;
      }

      .advice-list { padding: 12px 16px; }

      .advice-item {
        display: flex;
        gap: 10px;
        padding: 10px 0;
        border-bottom: 1px solid var(--border);
        font-size: 13px;
        color: var(--text);
        line-height: 1.5;
        align-items: flex-start;
      }

      .advice-item:last-child { border-bottom: none; }
      .advice-number { 
        color: var(--success); 
        font-size: 13px; 
        font-weight: 600;
        min-width: 20px;
      }

      /* 右侧结果面板 */
      .result-panel {
        background: var(--card);
        border: none !important;
        border-radius: 8px;
        padding: 16px;
        height: 100%;
        box-shadow: none !important; /* 去掉阴影（若有） */
      }

      .panel-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 0;
        margin-bottom: 0;
        border-bottom: none;
        background: transparent !important;
      }

      .panel-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--text);
      }

      .panel-title-large {
        font-size: 26px;
        font-weight: 700;
        color: var(--text);
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
      }

      /* 图标按钮 - 通过 Streamlit 的 st-key-xxx 类名精准定位 */
      .st-key-fullscreen_btn button,
      .st-key-close_results_btn button,
      [class*="st-key-copy_advice_"] button {
        width: 28px !important;
        height: 28px !important;
        min-width: 28px !important;
        padding: 0 !important;
        border-radius: 6px !important;
        background: transparent !important;
        color: #64748B !important;
        border: none !important;
        font-size: 18px !important;
        line-height: 1 !important;
        box-shadow: none !important;
      }

      .st-key-fullscreen_btn button:hover,
      .st-key-close_results_btn button:hover,
      [class*="st-key-copy_advice_"] button:hover {
        color: var(--primary-dark) !important;
        background: rgba(124,185,232,0.12) !important;
      }

      /* 复制按钮：图二风格双叠文档图标，悬停只改背景色（与全屏/退出一致） */
      [class*="st-key-copy_advice_"] button {
        font-size: 0 !important;
        color: transparent !important;
        background-color: transparent !important;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24'%3E%3Cdefs%3E%3Cfilter id='s'%3E%3CfeDropShadow dx='1' dy='1' stdDeviation='0.4' flood-opacity='0.25'/%3E%3C/filter%3E%3C/defs%3E%3Crect x='6' y='4' width='14' height='18' rx='1' fill='%23fff' stroke='%23d1d5db' stroke-width='1' filter='url(%23s)'/%3E%3Crect x='4' y='6' width='14' height='18' rx='1' fill='%23fff' stroke='%23d1d5db' stroke-width='1'/%3E%3C/svg%3E") !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-size: 18px 18px !important;
      }
      [class*="st-key-copy_advice_"] button * {
        display: none !important;
      }
      [class*="st-key-copy_advice_"] button:hover {
        background-color: rgba(124,185,232,0.12) !important;
      }

      /* 底部标签页 - 简洁文字风格 */
      .bottom-tabs {
        display: flex;
        border-top: 1px solid var(--border);
        margin-top: 16px;
        padding-top: 12px;
      }

      .tab-btn {
        flex: 1;
        padding: 10px 0;
        text-align: center;
        font-size: 13px;
        color: var(--text-secondary);
        cursor: pointer;
        border-bottom: 2px solid transparent;
        transition: all 0.15s ease;
      }

      .tab-btn:hover {
        color: var(--text);
      }

      .tab-btn.active {
        color: var(--primary-dark);
        border-bottom-color: var(--primary);
        font-weight: 500;
      }

      /* 全局Tab样式修正 - 强制去除背景条 */
      .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: transparent !important;
        border-radius: 0 !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
      }

      /* 图标按钮 - 仅限 .icon-btn 内的按钮 */

      .stTabs [data-baseweb="tab"] {
        border-radius: 4px;
        padding: 8px 16px;
        font-weight: 500;
        font-size: 13px;
        color: var(--text-secondary) !important;
      }

      .stTabs [data-baseweb="tab"]:hover {
        color: var(--text) !important;
      }

      .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: transparent !important;
        color: var(--primary-dark) !important;
        border-bottom: 2px solid var(--primary) !important;
        box-shadow: none !important;
        border-radius: 0 !important;
      }

      /* FAQ - 简化 */
      .faq-item {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 6px;
        padding: 14px 16px;
        margin-bottom: 10px;
      }

      .faq-question { font-weight: 600; color: var(--text); font-size: 14px; margin-bottom: 6px; }
      .faq-answer { color: var(--text-secondary); font-size: 13px; line-height: 1.5; }

      /* 安全提示 */
      .security-notice {
        background: var(--warning-light);
        border: 1px solid #F7DC6F;
        border-radius: 6px;
        padding: 12px 14px;
        font-size: 12px;
        color: #7D6608;
      }

      /* 页脚 */
      .footer {
        margin-top: 28px;
        padding-top: 14px;
        border-top: 1px solid var(--border);
        color: var(--muted);
        font-size: 11px;
        text-align: center;
      }

      /* ===== 修复原生组件 ===== */
      [data-testid="stFileUploader"] section {
        background: #FFFFFF !important;
        border: 1px dashed #D5D8DC !important;
        border-radius: 6px !important;
      }

      [data-testid="stFileUploader"] section div,
      [data-testid="stFileUploader"] section span,
      [data-testid="stFileUploader"] section p {
        color: #5D6D7E !important;
      }

      [data-testid="stSelectbox"] label { color: #2C3E50 !important; font-weight: 500 !important; font-size: 13px !important; }

      [data-testid="stSelectbox"] > div > div,
      [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: #FFFFFF !important;
        border: 1px solid #E5E8EB !important;
        border-radius: 6px !important;
      }

      [data-testid="stSelectbox"] [data-baseweb="select"] span,
      [data-testid="stSelectbox"] [data-baseweb="select"] div {
        color: #2C3E50 !important;
      }

      [data-baseweb="popover"], [data-baseweb="menu"] {
        background: #FFFFFF !important;
        border: 1px solid #E5E8EB !important;
      }

      [data-baseweb="popover"] li, [role="option"] {
        color: #2C3E50 !important;
        background: #FFFFFF !important;
      }

      [data-baseweb="popover"] li:hover, [role="option"]:hover {
        background: var(--primary-weak) !important;
        color: var(--primary-dark) !important;
      }

      [data-testid="stTextInput"] label { color: #2C3E50 !important; font-weight: 500 !important; font-size: 13px !important; }
      [data-testid="stTextInput"] > div > div { background: #FFFFFF !important; border: 1px solid #E5E8EB !important; border-radius: 6px !important; }
      [data-testid="stTextInput"] input { background: #FFFFFF !important; color: #2C3E50 !important; }
      [data-testid="stTextInput"] input::placeholder { color: #AEB6BF !important; }

      [data-testid="stAlert"][kind="success"] { background: #E8F8F0 !important; border: 1px solid #7DCEA0 !important; }
      [data-testid="stAlert"][kind="success"] p { color: #1E8449 !important; }

      [data-testid="stAlert"][kind="warning"] { background: #FEF9E7 !important; border: 1px solid #F9D79B !important; }
      [data-testid="stAlert"][kind="warning"] p { color: #9A7D0A !important; }

      [data-testid="stAlert"][kind="info"] { background: #EBF5FB !important; border: 1px solid #85C1E9 !important; }
      [data-testid="stAlert"][kind="info"] p { color: #1A5276 !important; }

      [data-testid="stAlert"][kind="error"] { background: #FDF2F2 !important; border: 1px solid #E8A09A !important; }
      [data-testid="stAlert"][kind="error"] p { color: #922B21 !important; }

      [data-testid="stExpander"] { background: #FFFFFF !important; border: 1px solid #E5E8EB !important; border-radius: 6px !important; }
      [data-testid="stExpander"] summary { color: #2C3E50 !important; font-weight: 500 !important; }

      [data-testid="stDataFrame"] { background: #FFFFFF !important; }
      [data-testid="stDataFrame"] th { background: #F5F6F7 !important; color: #2C3E50 !important; font-weight: 600 !important; }
      [data-testid="stDataFrame"] td { background: #FFFFFF !important; color: #5D6D7E !important; }

      [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li { color: #2C3E50 !important; }

      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      /* 不隐藏 header，否则侧边栏收起后展开按钮会一起被隐藏 */
    </style>
    """
