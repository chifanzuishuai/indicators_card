import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import  option_menu


def use_conception():

    st.markdown('#####  :rainbow[什么是指标？]')
    st.markdown('指标意思是衡量目标的参数;预期中打算达到的:orange[指数]、:orange[规格]、:orange[标准]，一般用数据表示。')

    st.markdown('')
    st.markdown('#####  :rainbow[维度]')
    st.markdown('维度是度量的环境，用来反映业务的⼀类属性，这类属性的集合构成⼀个维度，也可以称为实体对象。维度属于⼀个数据域，如地理维度（其中包括国家、地区、省市等）、时间维度（其中包括年、季、月、周、日等级别内容）。维度是帮助度量值使用者理解度量值含义的上下文。')

    st.markdown('')
    st.markdown('#####  :rainbow[维度属性]')
    st.markdown('维度属性隶属于⼀个维度,如地理维度里面的国家名称、国家ID、省份名称等都属于维度属性。')
 
    st.markdown('')
    st.markdown('#####  :rainbow[度量]')
    st.markdown('⼀般来说，度量是数据表中的数值数据。度量就是被聚合的统计值，也是聚合运算的结果，它⼀般是连续的值，如销售额，或销售商品的总件数。 ')

    st.markdown('')
    st.markdown('#####  :rainbow[原子指标]')
    st.markdown('原子指标和度量含义相同，也叫基础指标，是基于某⼀业务事件行为下的度量，是业务定义中不可再拆分的指标，具有明确业务含义的名称，如⽀付⾦额。')

    st.markdown('')
    st.markdown('#####  :rainbow[派生指标]')
    st.markdown('派生指标=:orange[1 个原子指标]+:orange[多个修饰词(可选)]+:orange[时间周期]。可以理解为原子指标业务统计范围的圈定。如原子指标：支付金额，最近 1 天海外买家支付金额则为派⽣指标。')

    st.markdown('')
    st.markdown('#####  :rainbow[复合指标]')
    st.markdown('复合指标是在事务性指标和存量型指标的基础上复合成的。例如，浏览 UV- 下单买家数转化率，销售额-库存。')



    # st.markdown('''
    # :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    # :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')