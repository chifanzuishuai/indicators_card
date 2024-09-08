import streamlit as st
import streamlit_antd_components as sac
from mypages.Conception import  use_conception  # 概念页面
from mypages.Atomic_Indicator import use_atomic_indicator   # 原子指标页面
from mypages.Derived_Indicator import use_derived_indicator   # 派生指标页面
from mypages.Composite_Indicator import use_composite_indicator   # 复合指标页面
from mypages.Coding_specifications import use_coding_specifications
from mapage.Relationship_Graph import use_Relationship_Graph #  指标关系图页面



st.set_page_config(
    page_title="Indicators Card",    
    page_icon='📈',    
    layout='wide',    
    initial_sidebar_state='expanded' 
   )


# 隐藏右边的菜单以及页脚, 去掉Deploy按钮
hide_st_style = """  
<style>  
    MainMenu {visibility: hidden;}  
    footer {visibility: hidden;}  
    header {visibility: hidden;}  
    root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}  
</style>  
"""  
st.markdown(hide_st_style, unsafe_allow_html=True) 




with st.sidebar.container():


    st.title('Indicators Card')

    menu = sac.menu([
        sac.MenuItem('home', icon='house-fill',children= [
            sac.MenuItem('相关概念'),
            sac.MenuItem('指标编码规范')
            sac.MenuItem('指标关系图')
        ]),
        sac.MenuItem('indicators', icon='app-indicator', children=[
            sac.MenuItem('原子指标'),
            sac.MenuItem('派生指标'),
            sac.MenuItem('复合指标'),
        ]),
        sac.MenuItem(type='divider'),
        sac.MenuItem('link', type='group', children=[     
            sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
        ]),
    ], 
    index= 1,
    key = 'menu'  ,
    open_all=True,
    indent = '20',
    format_func='title'
    )

# 左侧菜单

if menu == '相关概念':
    use_conception()

elif menu == '指标编码规范':    
    use_coding_specifications()
    
elif menu == '指标关系图':    
    use_relationship_graph()

elif menu == '原子指标':    
    use_atomic_indicator()

elif menu == '派生指标':    
    use_derived_indicator()

elif menu == '复合指标':  
    use_composite_indicator()
