import streamlit as st
import pandas as pd

@st.chach_date
def load_date():
    part1 = pd.read_excel("SI接頭語.xlsx")
    part2 = pd.read_excel("単語ー長さ.xlsx")
    part3 = pd.read_excel("単語ー時間.xlsx")
    part4 = pd.read_excel("単語ー質量.xlsx")
    part5 = pd.read_excel("単語ー圧力.xlsx")
    part6 = pd.read_excel("単語ー仕事.xlsx")
    part7 = pd.read_excel("単語ー仕事率.xlsx")
    part8 = pd.read_excel("単語ー時速.xlsx")
    part9 = pd.read_excel("単語ー分速.xlsx")
    part10 = pd.read_excel("単語ー秒速.xlsx")
    part11 = pd.read_excel("単語ー面積.xlsx")
    part12 = pd.read_excel("単語ー体積.xlsx")
    part13 = pd.read_excel("単語ー電流.xlsx")
    return pd.concat([part1, part2, part3, part4,part5,part6,part7,part8,part9,part10,part11,part12,part13], ignore_index=True)

st.sidebar.title("単位を選択してください。")


problems=[
    {"question":r'\var{v}=\frac{Delta x}{Delta t}',"answer":"変位"}
] 


if 'current_problem_index' not in st.session_state:
    st.session_state.current_problem_index = 0

def check_answer(user_answer):
    return user_answer.strip() == problems[st.session_state.current_problem_index]["answer"]

def next_problem():
    if st.session_state.current_problem_index < len(problems) - 1:
        st.session_state.current_problem_index += 1
    else:
        st.session_state.current_problem_index = 0
    st.session_state.user_input = ''


st.title("物理基礎")

current_problem = problems[st.session_state.current_problem_index]

st.write(current_problem["question"])

user_input = st.text_input("空白に入れる言葉を入力してください:",key="user_input")

if st.button("答え合わせ"):
    if user_input:
        if check_answer(user_input):
            st.success("正解です！")
            next_problem()
        else:
            st.error("不正解です。もう一度試してみてください。")
    else:
        st.warning("回答を入力してください。")

if st.button("次の問題"):
    next_problem()


st.write("物理基礎の公式:")

st.write("変位")
st.latex(r'\bar{v}=\frac{\Delta x}{\Delta t}')


st.write("速度")
st.latex(r'\bar{v}=\frac{x_2-x_1}{t_2-t_1}=\frac{\Delta x}{\Delta t}')


st.write("等速直線運動")
st.latex(r'x=vt')


st.write("合成速度")
st.latex(r'\vec{v}=\vec{v_1}+\vec{v_2}')


st.write("相対速度")
st.latex(r'\vec{v_(ab)}=\vec{v_b}-\vec{v_a}')


st.write("加速度")
st.latex(r'a=\frac{x_2-x_1}{t_2-t_1}')


st.write("等加速度直線運動")
st.latex(r'v=v_o+at')
st.latex(r'x=v_ot+\frac{1}{2}at^2')
st.latex(r'v^2-v_o^2=2ax')


st.write("自由落下")
st.latex(r'v=gt')
st.latex(r'y=\frac{1}{2}gt^2')
st.latex(r'v^2=2gy')


st.write("鉛直投げ下ろし")
st.latex(r'v=v_o+gt')
st.latex(r'y=v_ot+\frac{1}{2}gt^2')
st.latex(r'v^2-v_o^2=2gy')


st.write("鉛直投げ上げ")
st.latex(r'v=v_o-gt')
st.latex(r'y=v_o-\frac{1}{2}gt^2')
st.latex(r'v^2-v_o^2=-agy')


st.write("水平投射")
st.latex(r'x=v_ot')
st.latex(r'y=\frac{1}{2}gt^2')


st.write("三角比")
st.latex(r'sin\theta=\frac{a}{c}')
st.latex(r'cos\theta=\frac{b}{c}')
st.latex(r'sin30°=\frac{1}{2}')
st.latex(r'sin45°=\frac{√2}{2}')
st.latex(r'sin60°=\frac{√3}{2}')
st.latex(r'cos30°=\frac{√3}{2}')
st.latex(r'cos45°=\frac{√2}{2}')
st.latex(r'cos60°=\frac{1}{2}')
st.latex(r'')
st.latex(r'')

st.write(10^-24)

st.title("単位の変換")
selected_item=st.selectbox("",[
                           "長さ","時間","質量","面積","体積","時速","分速","秒速","密度","圧力","仕事","仕事率","電流","SI接頭語"])

