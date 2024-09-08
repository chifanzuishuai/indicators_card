import pandas as pd  
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Graph
from streamlit_echarts import st_pyecharts

def use_Relationship_Graph():

    # 指定Excel文件路径  
    file_path = '指标关系图.xlsx'  
    
    # 使用pandas的read_excel函数读取数据，sheet_name参数指定要读取的sheet页名或索引  

    df_nodes = pd.read_excel(file_path, sheet_name='nodes')  # 使用sheet页名  
    df_links = pd.read_excel(file_path, sheet_name='links')  
    df_categories = pd.read_excel(file_path, sheet_name='categories')  

    df_nodes['id'] = df_nodes['id'].astype(str) 
    df_links['source'] = df_links['source'].astype(str) 
    df_links['target'] = df_links['target'].astype(str) 

    re_nodes = [{'id': row['id'], 'name': row['name'], 'symbolSize': row['symbolSize'], 'value': row['value'], 'category': row['category']} for index, row in df_nodes.iterrows()]
    re_links = [{'source': row['source'], 'target': row['target']} for index, row in df_links.iterrows()]
    re_categories = [{'name': row['name']} for index, row in df_categories.iterrows()]

    Relationship_Graph = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=re_nodes,
            links=re_links,
            categories=re_categories,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            #title_opts=opts.TitleOpts(title="Relationship Graph"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        )
    )

    st.markdown('## Relationship Graph')
    st.markdown('')

    st_pyecharts(Relationship_Graph,height="600px",width="1000px") 




