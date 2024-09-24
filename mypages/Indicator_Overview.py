import streamlit as st
import math
import pandas as pd
from streamlit_modal import Modal


def use_indicator_overview():

    data = pd.read_csv("./指标字典.csv")

    # 翻页回调
    def page_update(value):
        if value == 1:
            st.session_state.page += 1
        elif value == 0:
            st.session_state.page -= 1
        elif value == 2:
            st.session_state.page = 0

    if 'cmpage' not in st.session_state:  
        st.session_state['cmpage'] = 1  # 或者其他合适的默认值 
    
    if 'select_row' not in st.session_state:  
        st.session_state['select_row'] = 10

    # 构建分页管理
    if 'page' not in st.session_state:
        st.session_state['select_row'] = 10
        st.session_state['page'] = 1
    elif st.session_state.page == 0:
        st.session_state['page'] = st.session_state.cmpage
        
    page = st.session_state.page

    page = page #页码数
    limit = st.session_state.select_row #每页的数据量
    # limit = st.session_state.select_row if 'select_row' in st.session_state else 10

    # 数据初始化
    if 'data' not in st.session_state:
        st.session_state['form'] = -1
        st.session_state['all_checkbox'] = False
        st.session_state['data'] = data


    # 数据表查询 + 翻页 管理
    col1_head, col2_head, col3_head,col4_head,col5_head,col6_head,col7_head,col8_head,col9_head = st.columns([2.1,2,2,1.2,0.6,1.2,1.2,1.3,1])

    st_field = col1_head.selectbox(label='字段', options=['营销事业群', '战略企划部'], index= 0 , placeholder='字段', label_visibility='collapsed')
    st_filterate = col2_head.text_input(label='过滤', value='', placeholder='指标名称过滤', label_visibility='collapsed')
    st_indexsx = col3_head.text_input(label='过滤', value='', placeholder='指标属性过滤', label_visibility='collapsed')


    if st_filterate:
        filtered_data = st.session_state.data[  
        # 模糊匹配
        (st.session_state.data['指标名称'].str.contains(st_filterate, na=False)) &  
        (st.session_state.data['指标属性'].str.contains(st_indexsx, na=False)) &  
        # 精确匹配
        (st.session_state.data['归属部门'] == st_field)  
        ]   
        st.session_state['data_new'] = filtered_data
    else:
        filtered_data = st.session_state.data[  
        (st.session_state.data['指标属性'].str.contains(st_indexsx, na=False)) & 
        (st.session_state.data['归属部门'] == st_field)  
        ] 
        st.session_state['data_new'] = filtered_data
    data = st.session_state.data_new


    col4_head.button(label='上一页', key='onepage', on_click=page_update, kwargs={'value': 0}, disabled=True if page==1 else False)
    col5_head.number_input(key='cmpage', label='页码', label_visibility='collapsed', on_change=page_update, kwargs={'value': 2}, value=1, step=2)
    col6_head.button(label='下一页', key='morepage', on_click=page_update, kwargs={'value': 1}, disabled=True if page==math.ceil(len(data)/limit) else False)
    col7_head.selectbox(
        label='单页行数',
        options=[1, 5, 10, 20, 50],
        index=2,
        key='select_row',
        on_change=lambda : True,
        disabled=False,
        label_visibility='collapsed', 
    )
    col8_head.markdown(f'当前页：{page}')



    # 分页数据获取
    data_page = data[(int(page) - 1) * int(limit): (int(page) * int(limit))]
    # df 转 dict
    data = data_page.to_dict(orient='records')

    # 构建前端类数据表
    with st.container():
        # 表头
        col1,col2,col3,col4,col5 = st.columns([.7,.7,2,1,2], gap='small')
        # col0.checkbox(label='复选框', value=st.session_state.all_checkbox, key='all_checkbox', label_visibility='collapsed', on_change=st_all_checkbox)
        col1.markdown('**指标编码**')
        col2.markdown('**归属部门**')
        col3.markdown('**指标名称**')
        col4.markdown('**指标属性**')
        col5.markdown('**依赖指标**')

        # 数据表内容
    for dt in data:

        col1,col2,col3,col4,col5 = st.columns([.7,.7,2,1,2], gap='small')
        col1.markdown(dt['指标编码'])
        col2.markdown(dt['归属部门'])
        col3.markdown(dt['指标名称'])
        col4.markdown(dt['指标属性'])
        col5.markdown(dt['依赖指标'])
