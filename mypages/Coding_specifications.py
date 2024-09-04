import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import  option_menu


def use_coding_specifications():

    st.markdown('#####  :rainbow[编码原则]')
    st.divider()
    st.markdown('- 指标代码应该具有唯一性、适用性、规范性、简明性。')
    st.markdown('- 一个指标应只有一个代码，一个代码只标识一个指标，指标代码一经产生，永久有效，不得变更。')
    st.markdown('- 编码应留有适当冗余，以利扩展。对收容项之前未定义编码的扩展，应在已确定的编码后按顺序统一增加。')


 
