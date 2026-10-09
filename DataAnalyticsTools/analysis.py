# -*- coding: utf-8 -*-
"""分析逻辑 - AI代码生成、可视化、经营建议"""

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import openai

from config import client
from utils import sanitize_generated_code, format_result, add_to_history


def generate_analysis_code(question, df_columns):
    """调用AI生成分析代码"""
    prompt = f"""
    你是数据分析助手，需将用户问题转化为可执行的Pandas分析代码（仅返回代码，无任何解释），严格遵循以下规则：
    1. 数据框变量名为df，columns为{df_columns}，可使用pd、np；日期字段按"YYYY-MM-DD"格式解析；
    2. 必须把最终需要展示的结果赋值给变量result；
    3. 禁止使用import语句；
    4. 涉及"利润"计算：按"销售数量×单价×0.3"；
    5. 结果需简洁：若为商品，result为商品名称；若为数值，result为计算结果（保留1位小数）。
    用户问题：{question}
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def generate_visualization(df, result, question):
    """根据提问类型自动生成可视化图表"""
    try:
        if any(keyword in question for keyword in ["销量最高", "销量排名", "卖得最好"]):
            if "商品名称" in df.columns and "销售数量" in df.columns:
                product_sales = df.groupby("商品名称")["销售数量"].sum().sort_values(ascending=False).head(5)
                fig = px.bar(
                    x=product_sales.index, y=product_sales.values,
                    title="商品销量TOP5",
                    labels={"x": "商品名称", "y": "销售数量（件）"},
                    color=product_sales.index,
                    color_discrete_sequence=px.colors.sequential.Blues_r,
                )
                return fig
        elif any(keyword in question for keyword in ["趋势", "每天", "每周", "每月"]):
            if "销售日期" in df.columns and "销售数量" in df.columns:
                df["销售日期"] = pd.to_datetime(df["销售日期"], errors="coerce")
                daily_sales = df.groupby("销售日期")["销售数量"].sum().reset_index()
                fig = px.line(
                    daily_sales, x="销售日期", y="销售数量",
                    title="销量时间趋势",
                    labels={"销售日期": "日期", "销售数量": "当日销量（件）"},
                )
                fig.update_traces(line_color='#3B82F6', line_width=2.5)
                return fig
        elif any(keyword in question for keyword in ["占比", "比例", "类别分布"]):
            if "商品类别" in df.columns and "销售数量" in df.columns:
                category_sales = df.groupby("商品类别")["销售数量"].sum()
                fig = px.pie(
                    values=category_sales.values, names=category_sales.index,
                    title="商品类别销量占比",
                    hole=0.4,
                    color_discrete_sequence=px.colors.qualitative.Set2,
                )
                return fig
    except Exception:
        pass
    return None


def generate_business_advice(df, result, question):
    """基于分析结果生成可落地经营建议"""
    advice_list = []
    try:
        if "销售日期" in df.columns:
            df["销售日期"] = pd.to_datetime(df["销售日期"], errors="coerce")

        if any(keyword in question for keyword in ["销量最高", "卖得最好"]):
            if "商品名称" in df.columns and "销售数量" in df.columns:
                top_product = result
                top_sales = df[df["商品名称"] == top_product]["销售数量"].sum()
                advice_list.append(f"增加{top_product}进货量（总销量{top_sales}件）")

        elif any(keyword in question for keyword in ["类别", "占比"]):
            if "商品类别" in df.columns and "销售数量" in df.columns:
                category_sales = df.groupby("商品类别")["销售数量"].sum().sort_values(ascending=False)
                if len(category_sales) > 0:
                    top_category = category_sales.index[0]
                    top_ratio = (category_sales[top_category] / category_sales.sum()).round(2) * 100
                    advice_list.append(f"重点推广{top_category}类（占比{top_ratio}%）")

        elif "促销" in question:
            if "是否促销" in df.columns and "销售数量" in df.columns:
                promo_sales = df[df["是否促销"] == "是"]["销售数量"].sum()
                non_promo_sales = df[df["是否促销"] == "否"]["销售数量"].sum()
                if promo_sales > non_promo_sales * 1.2:
                    advice_list.append("扩大促销范围（促销销量提升显著）")
                else:
                    advice_list.append("优化促销策略（提升不足20%）")

        if "销售日期" in df.columns and "销售数量" in df.columns:
            daily_sales = df.groupby("销售日期")["销售数量"].sum()
            if len(daily_sales) >= 2:
                sales_change = daily_sales.pct_change().abs()
                abnormal_dates = sales_change[sales_change > 0.5].index
                if len(abnormal_dates) > 0 and pd.notna(abnormal_dates[0]):
                    abnormal_date = abnormal_dates[0].strftime("%Y-%m-%d")
                    advice_list.append(f"排查{abnormal_date}销量异常（波动超50%）")
    except Exception:
        pass

    return advice_list


def handle_analysis():
    """处理分析逻辑"""
    uploaded_file_name = st.session_state.get("uploaded_file_name")
    df = st.session_state.get("df")
    question = st.session_state.get("question", "")
    
    if not uploaded_file_name:
        st.error("❌ 请先上传数据文件！")
        return
    elif not question:
        st.error("❌ 请输入分析需求！")
        return
    elif df is None:
        st.error("❌ 数据解析失败，请重新上传文件！")
        return
    
    # 显示骨架屏
    loading_area = st.empty()
    loading_area.markdown("""
        <div class="card">
            <div class="skeleton skeleton-title"></div>
            <div class="skeleton skeleton-text" style="width: 80%;"></div>
            <div class="skeleton skeleton-text" style="width: 60%;"></div>
            <div class="skeleton skeleton-chart"></div>
        </div>
    """, unsafe_allow_html=True)
    
    try:
        code = generate_analysis_code(question, df.columns.tolist())
        sanitized_code = sanitize_generated_code(code)
        
        safe_builtins = {"round": round, "len": len, "sum": sum, "min": min, "max": max, "abs": abs, "int": int, "float": float, "str": str}
        exec_globals = {"__builtins__": safe_builtins}
        exec_locals = {"df": df.copy(), "pd": pd, "np": np}
        exec(sanitized_code, exec_globals, exec_locals)
        
        if "result" not in exec_locals:
            raise ValueError("生成的代码未设置result变量")
        
        result = exec_locals["result"]
        
        st.session_state["code"] = code
        st.session_state["result"] = result
        st.session_state["fig"] = generate_visualization(df, result, question)
        st.session_state["advice"] = generate_business_advice(df, result, question)
        st.session_state["show_results"] = True
        
        add_to_history(question, result)
        
        st.rerun()
        
    except openai.AuthenticationError:
        st.error("❌ API Key 无效或无权限")
    except openai.RateLimitError:
        st.error("❌ 请求过于频繁，请稍后重试")
    except openai.APIConnectionError:
        st.error("❌ 网络连接失败")
    except Exception as e:
        st.error(f"❌ 分析失败：{str(e)}")
    finally:
        loading_area.empty()
