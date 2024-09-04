import streamlit as st
import numpy as np
import pandas as pd
import streamlit_antd_components as sac



def use_derived_indicator():

    df_database = pd.read_csv("./指标字典.csv")

    selected_index_name = df_database[df_database['指标类型'] == '派生指标']['指标名称']

    row1_1, row1_2 ,row1_3= st.columns(3)

    with row1_1:
        selected_name = st.selectbox(
            "Which indicator do you want to choose?",
            selected_index_name
            
        )
    
    # 筛选后指标信息
    index_value = df_database[(df_database['指标类型'] == '派生指标') & (df_database['指标名称'] == selected_name)]

    # 基础属性
    sac.divider(label='基础属性', icon='house', align='center', color='gray',size= 'xs')

    row2_1,row2_2,row2_3,row2_4 = st.columns((2.4,9,2.4,9))

    with row2_1:
        st.markdown(':orange[指标名称 ：]')
        st.markdown(':orange[指标属性 ：]')
    
    with row2_2:
        st.markdown(index_value['指标名称'].values[0])
        st.markdown(index_value['指标属性'].values[0])
    with row2_3:
        st.markdown(':orange[指标编码 ：]')
        st.markdown(':orange[指标目录 ：]')
    with row2_4:
        st.markdown(index_value['指标编码'].values[0])
        st.markdown(index_value['指标目录'].values[0])

    # 业务属性
    sac.divider(label='业务属性', icon='house', align='center', color='gray')

    row3_1,row3_2 = st.columns((2.28,20.4))

    with row3_1:
        st.markdown(':orange[业务口径 ：]')    
    with row3_2:
        st.markdown(index_value['业务口径'].values[0])

    row4_1,row4_2 = st.columns((2.28,20.4))

    with row4_1:
        st.markdown(':orange[分析维度 ：]')
    with row4_2:
        st.markdown(index_value['分析维度'].values[0])

    row5_1,row5_2,row5_3,row5_4 = st.columns((2.4,9,2.4,9))

    with row5_1:
        st.markdown(':orange[计量单位 ：]')
        st.markdown(':orange[更新频率 ：]')
    with row5_2:
        st.markdown(index_value['计量单位'].values[0])
        st.markdown(index_value['更新频率'].values[0])
    with row5_3:
        st.markdown(':orange[计量精度 ：]')
        st.markdown(':orange[使用部门 ：]')
    with row5_4:
        st.markdown(index_value['计量精度'].values[0])
        st.markdown(index_value['使用部门'].values[0])
    
    row6_1,row6_2 = st.columns((2.28,20.4))

    with row6_1:
        st.markdown(':orange[应用范围 ：]')
    with row6_2:
        st.markdown(index_value['应用范围'].values[0])

    # 管理属性
    sac.divider(label='管理属性', icon='house', align='center', color='gray')

    row7_1,row7_2,row7_3,row7_4 = st.columns((2.4,9,2.4,9))

    with row7_1:
        st.markdown(':orange[版本号 ：]')
        st.markdown(':orange[归属部门 ：]')
        st.markdown(':orange[归属处室 ：]')
    with row7_2:
        st.markdown(index_value['版本号'].values[0])
        st.markdown(index_value['归属部门'].values[0])
        st.markdown(index_value['归属处室'].values[0])
    with row7_3:
        st.markdown(':orange[业务人员 ：]')
        st.markdown(':orange[技术人员 ：]')  
    with row7_4:
        st.markdown(index_value['业务人员'].values[0])
        st.markdown(index_value['技术人员'].values[0])

    # 技术口径
    sac.divider(label='技术属性', icon='house', align='center', color='gray')

    row8_1,row8_2,row8_3,row8_4 = st.columns((2.4,9,2.4,9))

    with row8_1:
        st.markdown(':orange[取整方式 ：]')  
        st.markdown(':orange[相关存过 ：]') 
    with row8_2:
        st.markdown(index_value['取整方式'].values[0])
        st.markdown(index_value['相关存过'].values[0])
    with row8_3:
        st.markdown(':orange[依赖指标 ：]')  
        st.markdown(':orange[数据源库 ：]')  
    with row8_4:
        st.markdown(index_value['依赖指标'].values[0])
        st.markdown(index_value['数据源库'].values[0])

    row9_1,row9_2 = st.columns((2.28,20.4))

    with row9_1:
        st.markdown(':orange[数据源表 ：]')
    with row9_2:
        st.markdown(index_value['数据源表'].values[0])
    

    st.markdown(':orange[指标加工SQL ：]')
    sql_code = index_value['指标加工SQL'].values[0]


    st.code(sql_code,line_numbers= True, language='sql')