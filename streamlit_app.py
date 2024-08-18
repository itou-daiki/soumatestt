import streamlit as st
import random

st.header("物理基礎の公式")


options = ['平均の速度','速度','等速直線運動','合成速度','相対速度','加速度','等加速度直線運動','鉛直投げ下ろし','鉛直投げ上げ','自由落下','水平投射','斜方投射','重力','フックの法則','圧力','水圧','浮力']

def kousiki():
    selection = st.selectbox("表示したい公式を選んでください:",options)
    if selection == '平均の速度':
       st.title("平均の速度")
       st.write("一定区間における単位時間あたりの変位")
       st.latex(r'\bar{v}=\frac{\Delta x}{\Delta t}=\frac{x_2-x_1}{t_2-t_1}')
       st.write(" ")
       st.write("ｖ：速度　　 Δｘ：変位　　Δｔ：経過時間")
    elif selection == '速度':
       st.title("速度")
       st.write("単位時間当たりの移動距離")
       st.latex(r'\bar{v}=\frac{x_2-x_1}{t_2-t_1}=\frac{\Delta x}{\Delta t}')
       st.write(" ")
       st.write("　　ｖ：速さ　　ｘ：移動距離　　ｔ：経過時間")
       st.write(" ")
       st.text("単位：ｍ／ｓ（メートル毎秒）etc")
    elif selection == '等速直線運動':
       st.title("等速直線運動")
       st.write("一直線上を一定の速さで進む運動のこと")
       st.latex(r'x=vt')
       st.write(" ")
       st.write("　　ｘ：移動距離　　ｖ：速さ　　ｔ：経過時間")
       st.write(" ")
       st.text("単位：ｍ／ｓ（メートル毎秒）etc")
    elif selection == '合成速度':
       st.title("合成速度")
       st.write("速さ１と速さ２の和の速さ")
       st.latex(r'\vec{v}=\vec{v_1}+\vec{v_2}')
       st.write(" ")
       st.write("ｖ：速さ　　ｖ１：速度１　　ｖ２：速度２")
       st.write(" ")
       st.text("単位：ｍ／ｓ（メートル毎秒")
    elif selection == '相対速度':
       st.title("相対速度")
       st.write("動く物体Ａから観察したほかの物体Ｂの速度のこと")
       st.latex(r'\vec{v_(ab)}=\vec{v_b}-\vec{v_a}')
       st.write(" ")
       st.write("Ｖab：Ａに対するＢの相対速度　　Ｖa：物体Ａ（観察者）の速度　　Ｖb：物体Ｂ（相手）の速度")
       st.write(" ")
       st.text("単位：ｍ／ｓ（メートル毎秒）")
    elif selection == '加速度':
       st.title("加速度")
       st.write("単位時間あたりの速度の変化")
       st.latex(r'a=\frac{\Delta x}{\Delta t}=\frac{x_2-x_1}{t_2-t_1}')
       st.write(" ")
       st.write("a：加速度　　Δｘ：速度の変化　　Δｔ：経過時間")
       st.write(" ")
       st.text("単位：ｍ／ｓ^2（メートル毎秒毎秒）  ")
    elif selection == '等加速度直線運動':
       st.title("等加速度直線運動")
       st.write("一直線上を一定の加速度で進む運動")
       st.latex(r'v=v_o+at')
       st.latex(r'x=v_ot+\frac{1}{2}at^2')
       st.latex(r'v^2-v_o^2=2ax')
       st.write(" ")
       st.write("Ｖ：速度　　Ｖo：初速度　　a：加速度　　t：経過時間　　x：変位")
    elif selection == '自由落下':
       st.title("自由落下")
       st.write("物体が重力だけを受け、初速度０で鉛直下向きに落下する運動")
       st.latex(r'v=gt')
       st.latex(r'y=\frac{1}{2}gt^2')
       st.latex(r'v^2=2gy')
       st.write(" ")
       st.write("V：速度　　g：重力加速度　　t：経過時間　　y：変位")
    elif selection == '鉛直投げ下ろし':
       st.title("鉛直投げ下ろし")
       st.write("鉛直下向きに初速度Voで投げる運動")
       st.latex(r'v=v_o+gt')
       st.latex(r'y=v_ot+\frac{1}{2}gt^2')
       st.latex(r'v^2-v_o^2=2gy')
       st.write(" ")
       st.write("V：速度　　Vo:初速度　　g：重力加速度　　t：経過時間　　y：変位")
    elif selection == '鉛直投げ上げ':
       st.title("鉛直投げ上げ")
       st.write("")
       st.latex(r'v=v_o-gt')
       st.latex(r'y=v_o-\frac{1}{2}gt^2')
       st.latex(r'v^2-v_o^2=-2ag')
       st.write(" ")
       st.write("V：速さ　　Vo：初速度　　g：重力加速度　　t：経過時間　　y：変位")
    elif selection == '水平投射':
       st.title("水平投射")
       st.write("物体をある高さから水平方向に投げ出す運動")
       st.latex(r'x=v_ot')
       st.latex(r'y=\frac{1}{2}gt^2')
       st.write(" ")
       st.write("x：水平方向の変位　　y：鉛直方向の変位　　Vo：初速度　　t：経過時間　　g：重力加速度")
    elif selection == '斜方投射':
       st.title("斜方投射")
       st.write("物体を斜め上方に投げる運動")
       st.latex(r'v_x=v_ocosθ')
       st.latex(r'x=v_otcosθ')
       st.latex(r'v_y=v_osinθ-gt')
       st.latex(r'y=v_otsinθ-\frac{1}{2}gt^2')
       st.latex(r'v_y^2-(v_osinθ)^2=-2gy')
       st.latex(r'y=tanθx-\frac{g}{2v_o^2cos^2θ}x^2')
       st.write(" ")
       st.write("v：速度　　Vo：初速度　　Vx：速度vのx成分　　Vy：速度vのy成分　　x：水平方向の変位　　y：鉛直方向の変位　　t：経過時間　　g：重力加速度　　θ:水平方向となす角度")
    elif selection == '重力':
       st.title("重力")
       st.write("物体が地球からうける力。鉛直下向きにはたらく")
       st.latex(r'w=mg')
       st.write(" ")
       st.write("w：重力の大きさ（重さ）　　m：物体の質量　　g：重力加速度")
       st.write(" ")
       st.text("単位：N（ニュートン）")
    elif selection == 'フックの法則':
       st.title("フックの法則")
       st.write("弾性力の大きさはバネの伸びに比例する。")
       st.latex(r'F=kx')
       st.write(" ")
       st.write("F：弾性力　　k：バネ定数　　x：バネの伸び")
    elif selection == '圧力':
       st.title("圧力")
       st.write("単位面積あたりの力")
       st.latex(r'P=\frac{F}{S}')
       st.write(" ")
       st.write("P：圧力　　F：力　　S：面積")
       st.write(" ")
       st.text("単位：Pa（パスカル）,hPa（ヘクトパスカル）etc")
    elif selection == '水圧':
       st.title("水圧")
       st.write("水による圧力")
       st.latex(r'P=phg')
       st.write(" ")
       st.write("P：水圧　　p：水の密度　　h：水深　　g：重力加速度")
       st.write(" ")
       st.text("単位：Pa（パスカル）")
    elif selection == '浮力':
       st.title("浮力")
       st.write("流体から物体へ、重力と反対向きにはたらく力")
       st.latex(r'F=pVg')
       st.write(" ")
       st.write("F：浮力の大きさ　　p：流体の密度　　V：物体が排除した流体の体積　　g：重力加速度")
       st.write(" ")
       st.text("単位：N（ニュートン）")    

def test():
   problems = [
      {"question":"$x = vt$","answer":["等速直線運動"]},
      {"question":"$a=\\frac{Delta x}{Delta t}=\\frac{x_2-x_1}{t_2-t_1}$","answer":["加速度"]},
      {"question":"$\\vec{v_(ab)}=\\vec{v_b}-\\vec{v_a}$","answer":["相対速度"]},
      {"question":"$v=v_o+at$","answer":["等加速度直線運動"]},
      {"question":"$x=v_ot+\\frac{1}{2}at^2$","answer":["等加速度直線運動"]},
      {"question":"$v^2-v_o^2=2ax$","answer":["等加速度直線運動"]},
      {"question":"$F=pVg$","answer":"[浮力]"},
      {"question":"$p=phg$","answer":"[水圧]"},
      {"question":"$P=\\frac{F}{S}$","answer":"[圧力]"},
      {"question":"$F=kx$","answer":"[フックの法則]"},
      {"question":"$W=mg$","answer":"[重力]"},
      {"question":"$v_x=v_ocosΘ$","answer":"[斜方投射]"},
      {"question":"$x=v_otcosΘ$","answer":"[斜方投射]"},
      {"question":"$v_y=v_osinΘ-gt$","answer":"[斜方投射]"},
      {"question":"$y=v_otsinΘ-\\frac{1}{2}gt^2$","answer":"[斜方投射]"},
      {"question":"$v_y^2-(v_osinΘ)^2=-2gy$","answer":"[斜方投射]"},
      {"question":"$y=tanΘx-\\frac{g}{2v_o^2cos^2Θ}x^2$","answer":"[斜方投射]"},
      {"question":"$\\vec{v}=\\vec{v_1}+\\vec{v_2}$","answer":"[合成速度]"},
      {"question":"$\\bar{v}=\\frac{x_2-x_1}{t_2-t_1}=\\frac{Δx}{Δt}$","answer":"[速度][平均の速さ]"}, 
      {"question":"$v=gt$","answer":"[自由落下]"}, 
      {"question":"$y=\\frac{1}{2}gt^2$","answer":"[自由落下]"}, 
      {"question":"$v^2=2gy$","answer":"[自由落下]"}, 
      {"question":"$v=v_o+gt$","answer":"[鉛直投げ下ろし]"}, 
      {"question":"$y=v_ot+\\frac{1}{2}gt^2$","answer":"[鉛直投げ下ろし]"},
      {"question":"$v^2-v_o^2=2gy$","answer":"[鉛直投げ下ろし]"},

   ]
   
   if 'question_index' not in st.session_state:
      st.session_state.question_index = random.randint(0, len(problems) - 1)
      st.session_state.total_questions = 0
      st.session_state.correct_answers = 0
      st.session_state.wrong_questions = []
   
   def next_question():
      st.session_state.question_index = random.randint(0, len(problems) - 1)
      st.session_state.user_answer = ""
   
   st.title("テスト")

   current_question = problems[st.session_state.question_index]

   st.subheader("問題")
   st.subheader("次の公式は何を求める公式か？")
   st.latex(current_question["question"])

   st.write(" ")
   st.write(" ")

   user_answer = st.selectbox("解答を選択", options, key="user_answer")
   
   if st.button('答え合わせ'):
      answer = current_question["answer"]
      st.session_state.total_questions += 1  # 総問題数をカウント
      if user_answer in answer:
         st.write("正解です。")
         st.session_state.correct_answers += 1  # 正解数をカウント
      else:
         st.write("不正解です。")
         st.write(f"正しい答えは: {answer}です。")
         st.session_state.wrong_questions.append(current_question)  # 間違えた問題を記録
      
      if st.button("次の問題"):
         next_question()
         st.experimental_rerun()
   
   # 成績表示
   st.sidebar.subheader("成績")
   st.sidebar.write(f"総問題数: {st.session_state.total_questions}")
   st.sidebar.write(f"正解数: {st.session_state.correct_answers}")
   if st.session_state.total_questions > 0:
      accuracy = (st.session_state.correct_answers / st.session_state.total_questions) * 100
      st.sidebar.write(f"正答率: {accuracy:.2f}%")
   
   # 間違えた問題の表示
   if st.sidebar.checkbox("間違えた問題を表示"):
      st.sidebar.subheader("間違えた問題")
      for q in st.session_state.wrong_questions:
         st.sidebar.latex(q["question"])
         st.sidebar.write(f"正解: {q['answer']}")

selection = st.sidebar.selectbox(
   "メニュー",
   ["公式","テスト"]
)
if selection == "公式":
   kousiki()
elif selection == "テスト":
   test()

