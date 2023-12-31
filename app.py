import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random

# Загрузите модель
model = joblib.load('titanic-ml-from-disaster.joblib')

# Создайте функцию для обработки входных данных
def process_input(sex, age, fare, is_alone):
    # Преобразуйте пол в числовое значение
    if sex == 'Мужчина':
        sex = 0
    else:
        sex = 1
    # Верните DataFrame
    rdPclass = random.randint(1,3)
    rdSibSp = random.randint(0,11)
    rdEmbarked = random.randint(0,2)
    rdRelatives = random.randint(0,5)
    if(is_alone):
        rdSibSp = 0
    else:
        rdSibSp = 1
    rdParch = random.randint(0,2)
    if(sex == 0):
        rdTitle = 1;
    else:
        rdTitle = 2;
    rdDeck = random.randint(0,8)
    rdFare_per_person = random.randint(0,3)
    return pd.DataFrame({'Pclass': [rdPclass], 'Sex': [sex], 'Age': [age], 'SibSp': [rdSibSp], 'Parch': [rdParch], 'Fare': [fare], 'Embarked': [rdEmbarked], 'Relatives': [rdRelatives], 'Is_Alone': [is_alone], 'Title': [rdTitle], 'Deck': [rdDeck], 'Age_Class': [age * 1], 'Fare_per_Person': [rdFare_per_person]})

# Создайте форму для ввода данных
st.markdown("<h1 style='text-align: center; color: white;'>\"Рассказанная Немногими Выжившими История...\"</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>My Heart Will Go On - Céline Dion</h3>", unsafe_allow_html=True)
st.audio('My Heart Will Go On - Céline Dion.mp3')
st.markdown("<h2 style='text-align: center; color: white;'>Модель машинного обучения для предсказания исхода поездки на лайнере 'Титаник'</h2>", unsafe_allow_html=True)
st.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ca6c7bc7-3c52-482a-9d4c-5043d91da7c3/dfpb7y1-bfff4c04-4e77-4af6-bda0-a8060abb8097.png/v1/fill/w_900,h_1303,q_80,strp/my_titanic_poster_2023_editon_by_doodle_for_adventure_dfpb7y1-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTMwMyIsInBhdGgiOiJcL2ZcL2NhNmM3YmM3LTNjNTItNDgyYS05ZDRjLTUwNDNkOTFkYTdjM1wvZGZwYjd5MS1iZmZmNGMwNC00ZTc3LTRhZjYtYmRhMC1hODA2MGFiYjgwOTcucG5nIiwid2lkdGgiOiI8PTkwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.F4woajhvJRW4DDE3vk1GnDTVZ_-NKewPb2_IjUn4q2E', caption='Я считаю, что жизнь — это подарок, и я не собираюсь тратить его зря. Вы не знаете, какую руку вам раздадут следующей. Вы учитесь принимать жизнь такой, какая она есть... чтобы каждый день был важен. -Джек', use_column_width=True)

name = st.text_input('Имя')
sex = st.selectbox('Пол', ['Мужчина', 'Женщина'])
age = st.slider('Возраст', 1, 100, 30)

if(age <= 11):
    age = 0
elif(age > 11 and age <= 18):
    age = 1
elif(age > 18 and age <= 22):
    age = 2
elif(age > 22 and age <= 27):
    age = 3
elif(age > 27 and age <= 33):
    age = 4
elif(age > 33 and age <= 40):
    age = 5
elif(age > 40 and age <= 66):
    age = 6
elif(age > 66):
    age = 7

fare = st.slider('Недельный заработок', 0, 1000, 100)

if(fare <= 8):
    fare = 0
elif(fare > 8 and fare <= 14):
    fare = 1
elif(fare > 14 and fare <= 31):
    fare = 2
elif(fare > 31 and fare <= 99):
    fare = 3
elif(fare > 99 and fare <= 250):
    fare = 4
elif(fare > 250):
    fare = 5

is_alone = st.selectbox('Брак', [0, 1])

# Обработайте входные данные
input_df = process_input(sex, age, fare, is_alone)

# Сделайте прогноз
if st.button('Узнать'):
    prediction = model.predict(input_df)[0]
    # Выведите прогноз
    if prediction == 0:
        st.markdown("<h1 style='text-align: center; color: black;'>К сожалению, этот пассажир не выжил после крушения лайнера...</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: black;'>К счастью, пассажир выжил после крушения лайнера!</h1>", unsafe_allow_html=True)

quote = """
> Роуз : Я знаю, о чем ты, должно быть, думаешь. «Бедная маленькая богатая девочка, что она знает о страданиях?»
Джек : Нет-нет, я не об этом думал. Я думал о том, что могло случиться с этой девушкой, что заставило ее думать, что у нее нет выхода?
"""
st.markdown(quote)

quote = """
> Джек : [ с английским акцентом, сидит на переднем сиденье машины, посигналив ] Куда, мисс?
Роуз : [ опускает перегородку, шепчет ему на левое ухо ] К звездам.
"""
st.markdown(quote)

quote = """
> [ когда Джек рисует ее обнаженной ]
Роуз : Я думаю, вы краснеете, мистер Большой Артист. Я не могу себе представить, чтобы месье Моне покраснел.
Джек : [ забавился ее комментарием, больше сосредотачиваясь на набросках, отрицая, что краснеет, напоминая ей ] Он пишет пейзажи.
"""
st.markdown(quote)

quote = """
> Роуз : [ Джеку ] Когда корабль пришвартуется, я уйду с тобой.
Джек : Это безумие.
Роуз : Я знаю. Это не имеет никакого смысла. Вот почему я доверяю этому
[ Джек и Роуз начинают целоваться ]
"""
st.markdown(quote)

quote = """
> Роуз : [ собирается танцевать ирландскую джигу под взглядами многих людей ] Я не знаю шагов!
Джек : Я тоже! Просто идите с этим!
"""
st.markdown(quote)

quote = """
> Джек : [ Рут и другим гостям, обедающим за их столом ] Ну, да, мэм, я знаю... Я имею в виду, у меня есть все, что мне нужно, прямо здесь, со мной. В легкие попал воздух, несколько чистых листов бумаги. Я имею в виду, мне нравится просыпаться утром, не зная, что произойдет, или кого я встречу, где я окажусь. Буквально прошлой ночью я спал под мостом, а теперь я нахожусь на самом величественном корабле в мире и пью шампанское с вами, замечательные люди. Я считаю, что жизнь — это подарок, и я не собираюсь тратить его зря. Вы не знаете, какую руку вам раздадут следующей. Вы учитесь принимать жизнь такой, какая она есть... чтобы каждый день был важен.
Молли Браун : Хорошо сказано, Джек.
"""
st.markdown(quote)

quote = """
> Старая Роза : [ Броку, Лиззи и сотрудникам Брока ] Я видела всю свою жизнь так, как будто я ее уже прожила. Бесконечный парад вечеринок и котильонов, яхт и матчей в поло. Всегда одни и те же узкие люди, та же бессмысленная болтовня. У меня было такое чувство, словно я стою у огромной пропасти, и никто не мог меня вытащить, никто не заботился... или даже не замечал...
"""
st.markdown(quote)

quote = """
> Уоллес Хартли : [ оркестр закончил играть, и Хартли говорит группе, что они могут отправиться за лодками. Он остается и начинает играть «Ближе к тебе, мой Бог». Один за другим группа возвращается и играет, а сцены меняются. когда мелодия заканчивается, вода вот-вот их поглотит ] Джентльмены. Для меня было большой честью играть с вами сегодня вечером.
"""
st.markdown(quote)


quote = """
> Роуз : [ отпуская руку Джека ] Я никогда не отпущу, Джек. Я обещаю.
[ она целует ему руку и смотрит, как он тонет, почти разваливаясь, прежде чем она наконец забирается обратно в воду, чтобы позвать спасательную шлюпку обратно ]
"""
st.markdown(quote)
