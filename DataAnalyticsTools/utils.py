# -*- coding: utf-8 -*-
"""工具函数 - 数据处理、字段映射等"""

import difflib
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime
from config import FIELD_SYNONYMS, REQUIRED_FIELDS


def _normalize_field_name(s: str) -> str:
    """标准化字段名称"""
    return "".join(str(s).strip().lower().split()).replace("（", "(").replace("）", ")")


def suggest_field_mapping(df_columns, canonical_fields):
    """智能字段映射建议"""
    normalized_to_original = {_normalize_field_name(c): c for c in df_columns}
    normalized_cols = list(normalized_to_original.keys())

    suggested = {}
    for canonical in canonical_fields:
        candidates = FIELD_SYNONYMS.get(canonical, []) + [canonical]
        hit = None
        for cand in candidates:
            cand_norm = _normalize_field_name(cand)
            if cand_norm in normalized_to_original:
                hit = normalized_to_original[cand_norm]
                break
        if not hit:
            cand_norms = [_normalize_field_name(x) for x in candidates]
            matches = difflib.get_close_matches(" ".join(cand_norms), normalized_cols, n=1, cutoff=0.55)
            if matches:
                hit = normalized_to_original[matches[0]]
        suggested[canonical] = hit
    return suggested


def check_fields_and_degrade(df):
    """检查字段并返回降级信息"""
    missing = [f for f in REQUIRED_FIELDS if f not in df.columns]
    
    degraded_features = []
    if "商品名称" not in df.columns or "销售数量" not in df.columns:
        degraded_features.append("销量排名分析")
    if "销售日期" not in df.columns:
        degraded_features.append("趋势分析")
    if "商品类别" not in df.columns:
        degraded_features.append("类别占比分析")
    if "是否促销" not in df.columns:
        degraded_features.append("促销效果分析")
    
    return missing, degraded_features


def sanitize_generated_code(raw: str) -> str:
    """清理和验证生成的代码"""
    s = (raw or "").strip()
    if s.startswith("\ufeff"):
        s = s.lstrip("\ufeff")
    s = s.replace("\r\n", "\n").replace("\r", "\n").replace("\u00a0", " ")
    if s.startswith("```"):
        lines = s.splitlines()
        if lines: lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"): lines = lines[:-1]
        s = "\n".join(lines).strip()
    if s.lower().startswith("python\n"):
        s = s.split("\n", 1)[1].strip()
    cleaned_lines = [line for line in s.split("\n") if not line.strip().startswith(("import ", "from "))]
    s = "\n".join(cleaned_lines).strip()
    if "import " in s or "from " in s:
        raise ValueError("生成的代码包含import语句，已被禁止")
    return s


def format_result(result):
    """将分析结果格式化为用户友好的显示格式"""
    if result is None:
        return "暂无结果"
    
    # 处理 pandas Series
    if isinstance(result, pd.Series):
        if len(result) <= 5:
            formatted_items = []
            for idx, val in result.items():
                if hasattr(idx, 'strftime'):
                    idx_str = idx.strftime('%Y-%m-%d')
                else:
                    idx_str = str(idx)
                if isinstance(val, float):
                    val_str = f"{val:,.1f}"
                else:
                    val_str = str(val)
                formatted_items.append(f"{idx_str}: {val_str}")
            return " | ".join(formatted_items)
        else:
            return f"共 {len(result)} 条数据，最大值: {result.max():.1f}，最小值: {result.min():.1f}"
    
    # 处理 pandas DataFrame
    if isinstance(result, pd.DataFrame):
        return f"数据表格（{result.shape[0]} 行 × {result.shape[1]} 列）"
    
    # 处理字典
    if isinstance(result, dict):
        if len(result) <= 5:
            formatted_items = []
            for k, v in result.items():
                if hasattr(k, 'strftime'):
                    k_str = k.strftime('%Y-%m-%d')
                else:
                    k_str = str(k)
                if isinstance(v, float):
                    v_str = f"{v:,.1f}"
                else:
                    v_str = str(v)
                formatted_items.append(f"{k_str}: {v_str}")
            return " | ".join(formatted_items)
        else:
            return f"共 {len(result)} 项数据"
    
    # 处理列表
    if isinstance(result, (list, tuple)):
        if len(result) <= 5:
            return ", ".join([str(item) for item in result])
        else:
            return f"共 {len(result)} 项: {', '.join([str(item) for item in result[:3]])}..."
    
    # 处理数字
    if isinstance(result, (int, float, np.integer, np.floating)):
        if isinstance(result, float) or isinstance(result, np.floating):
            return f"{result:,.2f}"
        return f"{result:,}"
    
    # 处理 Timestamp
    if hasattr(result, 'strftime'):
        return result.strftime('%Y-%m-%d')
    
    # 其他类型直接转字符串
    return str(result)


def add_to_history(question, result):
    """添加到历史记录"""
    history = st.session_state.get("history", [])
    history.insert(0, {
        "question": question,
        "result": format_result(result),
        "time": datetime.now().strftime("%H:%M")
    })
    st.session_state["history"] = history[:10]


def export_results():
    """导出分析结果"""
    result = format_result(st.session_state.get("result"))
    advice = st.session_state.get("advice", [])
    question = st.session_state.get("question", "")
    
    export_text = f"""小店智析 - 分析报告
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
========================

【分析问题】
{question}

【核心结论】
{result}

【经营建议】
"""
    for i, a in enumerate(advice, 1):
        export_text += f"{i}. {a}\n"
    
    return export_text


def init_session_state():
    """初始化 session_state"""
    defaults = {
        "df": None,
        "uploaded_file_name": None,
        "result": None,
        "code": None,
        "fig": None,
        "advice": None,
        "show_results": False,
        "fullscreen_mode": False,
        "nav_page": "首页",
        "question": "",
        "history": [],
        "is_analyzing": False,
        "analysis_cancelled": False,
        "missing_fields": [],
        "feature_degraded": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
