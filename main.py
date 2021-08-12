import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

# st.write('DataFrame')
st.write('Interactibe Widgets')

left_column,right_column = st.beta_columns(2)

button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右からむ')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('趣味は？')
# 'あなたの趣味は',text

# condition = st.slider('元気度',0,100,50)
# 'コンディション：',condition



# option = st.selectbox(
#     '好きな数字',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'

# if st.checkbox('Show Dataframe'):      
#     df = pd.DataFrame(
#         np.random.rand(100,2)/[50,50] + [35.69,139.70],
#         columns=['lat','lon']
#     )
#     st.map(df)

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.table(df)

# """
# # 賞
# ## 節
# ### 項

# ```
# python
# import streamlit as st
# import numpy as no
# import pandas as pd
# ```
# """