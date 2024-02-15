import telebot
from telebot import types

API_TOKEN = '6970411627:AAHPzEVVDBE0MCBZ1t3IN1NgX5Cu0HqNgsk'
bot = telebot.TeleBot(API_TOKEN)
#Присвоєння відповідей константам меню Вступ до НАУ
Algotith_Bac = """
[1️⃣](https://imbt.ga/Wim4v9FDj6) Визначитися з спеціальністю (конкурсною пропозицією) куди плануєте [вступати](https://bit.ly/3dajqiH). [Перелік спеціальностей НАУ](https://pk.nau.edu.ua/spetsialnosti/)
 
2️⃣ Наступним кроком є визначення конкурсних предметів для обраної Вами спеціальності, з яких вступники мають подавати сертифікат ЗНО. [Перелік](https://bit.ly/3uJWdcO) конкурсних предметів
 
3️⃣ Далі Вам необхідно вдало скласти ЗНО з обраних предметів. Якщо є сумніви щодо готовності до складання ЗНО, Ви можете підготуватися на [курсах](https://bit.ly/2Qi5biw) підготовки до ЗНО та вступу до НАУ

4️⃣ Підготувати [перелік](https://bit.ly/3g02X2g) необхідних документів для вступу до НАУ

5️⃣ Реєстрація електронних [кабінетів](https://ez.osvitavsim.org.ua/) вступників та завантаження необхідних документів розпочинається 01 липня

6️⃣ Прийом заяв та документів у електронній формі через [кабінет](https://ez.osvitavsim.org.ua/) вступника з 14 по 23 липня.

7️⃣ Формування рейтингових [списків](https://pk.nau.edu.ua/) вступників, надання рекомендацій до зарахування та оприлюднення списку рекомендованих (бюджет) 28 липня. Надання рекомендацій до зарахування та оприлюднення списку рекомендованих для вступників (контракт) 10 серпня

8️⃣ Вступники, які отримали рекомендації, мають подати оригінали документів до НАУ

– до 18:00 02 серпня – на місця державного або регіонального замовлення (бюджет)

– до 31 серпня – за рахунок цільових пільгових державних кредитів, за кошти фізичних та/або юридичних осіб (контракт)

(Крім особистого подання оригіналів документів для зарахування можна: надіслати їх засобами поштового зв’язку з обов’язковим описом вкладень на адресу Приймальної комісії НАУ; надіслати їх скановані копії, з накладанням кваліфікованого електронного підпису вступника, через електронний [кабінет](https://ez.osvitavsim.org.ua/) вступника)

9️⃣ Після успішного подання оригіналів документів до НАУ, Ви – студент НАУ. Вітаємо!

➡️[Детальний алгоритм](https://pk.nau.edu.ua/alhorytm-vstupu-do-nau-2021/)️⬅️"""
Algotith_Mag = """ 
[1️⃣](https://imbt.ga/Wim4v9FDj6) Реєстрація вступників для складання єдиного вступного іспиту з іноземної мови та єдиного фахового вступного випробування розпочинається 11 травня та [закінчується](https://bit.ly/3g57qke) о 18:00 03 червня . Онлайн реєстрація для складання ЄВІ/ЄФВВ буде доступна незабаром. [Перелік спеціальностей НАУ](https://pk.nau.edu.ua/spetsialnosti/) 

2️⃣ Основна сесія єдиного вступного іспиту проводиться 30 червня для всіх спеціальностей НАУ.

На спеціальності 081 «Право» та 293 «Міжнародне право» основна сесія єдиного фахового вступного випробування проводиться 02 липня.

3️⃣ Реєстрація електронних [кабінетів](https://ez.osvitavsim.org.ua/) вступників, завантаження необхідних документів розпочинається 01 липня. (Реєстрація буде доступна напередодні початку вступної кампанії 2021)

4️⃣ Прийом заяв та документів через кабінет вступника розпочинається 15 липня, і закінчується о 18:00 23 липня для осіб, які вступають на основі результатів єдиного вступного іспиту та фахового вступного випробування.

5️⃣ Фахові вступні випробування на базі НАУ, проводяться з 19 липня по 30 липня. Графіки проведення та програми фахових вступних випробувань розміщені за [посиланням](https://pk.nau.edu.ua/vstup/mahistratura/)

6️⃣ Рекомендації для зарахування за державним замовленням надаються 02 серпня (повідомлення буде розміщено в електронному [кабінеті](https://ez.osvitavsim.org.ua/) вступника  та на офіційному [сайті](https://pk.nau.edu.ua/) Приймальної комісії НАУ )

7️⃣ Вступники, які отримали рекомендації, мають(подати оригінали документів до НАУ:

– до 18:00 07 серпня – на місця державного або регіонального замовлення

– до 31 серпня – за кошти фізичних та/або юридичних осіб

[Перелік](https://bit.ly/3uMjTx8) необхідних документів для вступу до магістратури

8️⃣ Після успішного подання оригіналів документів до НАУ, Ви – студент НАУ. Вітаємо!

➡️[Детальний алгоритм](https://pk.nau.edu.ua/alhorytm-vstupu-do-mahistratury-nau-u-2021-rotsi/)⬅️"""
Spec_NAU = """
[✈️ ](https://imbt.ga/HnCpKJ8l3e)011 «Освітні, педагогічні науки»

✈️ 022 «Дизайн»

✈️ 029 «Інформаційна, бібліотечна та архівна справа»

✈️ 033 «Філософія»

✈️ 035 «Філологія»

✈️ 051 «Економіка»

✈️ 052 «Політологія»

✈️ 053 «Психологія»

✈️ 054 «Соціологія»

✈️ 061 «Журналістика»

✈️ 071 «Облік і оподаткування»

✈️ 072 «Фінанси, банківська справа та страхування»

✈️ 073 «Менеджмент»

✈️ 075 «Маркетинг»

✈️ 076 «Підприємництво, торгівля та біржова діяльність»

✈️ 081 «Право»

✈️ 101 «Екологія»

✈️ 113 «Прикладна математика»

✈️ 121 «Інженерія програмного забезпечення»

✈️ 122 «Комп’ютерні науки»

✈️ 123 «Комп’ютерна інженерія»

✈️ 124 «Системний аналіз»

✈️ 125 «Кібербезпека»

✈️ 126 «Інформаційні системи та технології»

✈️ 134 «Авіаційна та ракетно-космічна техніка»

✈️ 141 «Електроенергетика, електротехніка та електромеханіка»

✈️ 142 «Енергетичне машинобудування»

✈️ 151 «Автоматизація та комп’ютерно-інтегровані технології»

✈️ 152 «Метрологія та інформаційно-вимірювальна техніка»

✈️ 153 «Мікро- та наносистемна техніка»

✈️ 161 «Хімічні технології та інженерія»

✈️ 162 «Біотехнології та біоінженерія»

✈️ 163 «Біомедична інженерія»

✈️ 171 «Електроніка»

✈️ 172 «Телекомунікації та радіотехніка»

✈️ 173 «Авіоніка»

✈️ 186 «Видавництво та поліграфія»

✈️ 191 «Архітектура та містобудування»

✈️ 192 «Будівництво та цивільна інженерія»

✈️ 193 «Геодезія та землеустрій»

✈️ 231 «Соціальна робота»

✈️ 242 «Туризм»

✈️ 262 «Правоохоронна діяльність»

✈️ 272 «Авіаційний транспорт»

✈️ 275 «Транспортні технології»

✈️ 281 «Публічне управління та адміністрування»

✈️ 291 «Міжнародні відносини, суспільні комунікації та регіональні студії»

✈️ 292 «Міжнародні економічні відносини»

✈️ 293 «Міжнародне право»

➡️[Детальна інформація про спеціальності НАУ](https://pk.nau.edu.ua/spetsialnosti/)⬅️

"""
Rules_PK = """[Правила прийому](https://pk.nau.edu.ua/pravyla-pryiomu-2021/)
"""
Contacts_PK = """☎️ (044) 497-41-05, (044) 406-70-38.

📬 pk@nau.edu.ua

🏢 03058, Україна, м.Київ, просп. Любомира Гузара,1


  💼 ГРАФІК РОБОТИ КОНСУЛЬТАЦІЙНОГО ЦЕНТРУ 💼

  ⏰  понеділок – четвер -- 8.00 – 17.00

  ⏰  п’ятниця -- 8.00 – 16.00

  🧘 субота, неділя -- вихідний

  ⏰  обідня перерва -- 12.00 – 13.00

[Детальна інформація](https://pk.nau.edu.ua/contacts/)"""

#Присвоєння відповідей константам меню Навчальний процес
Rozklad = """
[✈️](https://imbt.ga/wag8sP0mBq)*Розклади занять знаходяться на сайтах факультетів:*"""
Sites =  """

🚀Сайт [АКФ](http://aki.nau.edu.ua/)

🏛Сайт [ФАБД](http://iap.nau.edu.ua/)

🕹Сайт [ФАЕТ](http://ian.nau.edu.ua/)

💵Сайт [ФЕБА](http://feba.nau.edu.ua/)

🌳Сайт [ФЕБІТ](http://febit.nau.edu.ua/)

👅Сайт [ФЛСК](http://www.gmi.nau.edu.ua/)

🌍Сайт [ФМВ](http://fmv.nau.edu.ua/)

💻Сайт [ФККПІ](http://fccpi.nau.edu.ua/)

🚚Сайт [ФТМЛ](http://ftml.nau.edu.ua/)

👨‍⚖️Сайт [ЮФ](http://law.nau.edu.ua/)

🕴Сайт [КВП](http://kvp.nau.edu.ua/)

🎓Сайт [ННІНО](https://ino.nau.edu.ua/)"""
Rozklad_isp = """
[✈️](https://imbt.ga/rITcZW1CBA)*Розклади іспитів знаходяться на сайтах факультетів:*"""
Rozklad_dzv = """
⏰*Розклад дзвінків:*

1️⃣ Пара - 8:00 - 9:20
2️⃣ Пара - 9:40 - 11:00
3️⃣ Пара - 11:20 - 12:40
4️⃣ Пара - 13:00 - 14:20
5️⃣ Пара - 14:40 - 16:00
6️⃣ Пара - 16:20 - 17:40
7️⃣ Пара - 18:00 - 19:20
8️⃣ Пара - 19:40 - 21:00"""
Stypendia = """
[✈️](https://imbt.ga/LCfS5A09zz)*Стипендіальні списки знаходяться на сайтах факультетів:*"""

#Присвоєння відповідей константам меню Гуртожитків
Gurt_NAU = """
1️⃣*Гуртожиток*
Адреса: вул, Ніжинська, 12
Телефон: (044) 406-68-21
E-mail: hostelsmt1@nau.edu.ua

3️⃣*Гуртожиток* - ФККПІ
Адреса: вул. Гарматна, 51
Телефон: (044) 406-68-23
E-mail: hostelsmt3@nau.edu.ua

4️⃣*Гуртожиток* - ФМВ
Адреса: вул. Гарматна, 53
Телефон: (044) 406-68-24
E-mail: hostelsmt4@nau.edu.ua

5️⃣*Гуртожиток* - ФЛСК
Адреса: вул. Борщагівська,193
Телефон: (044) 497-17-93
E-mail: hostelsmt5@nau.edu.ua

6️⃣*Гуртожиток* - ФЕБА
Адреса: вул. Ніжинська,14
Телефон: (044) 406-68-26
E-mail: hostelsmt6@nau.edu.ua

7️⃣*Гуртожиток* - АКФ/ФТМЛ
Адреса: вул. Ніжинська 29,а
Телефон: (044) 406-68-27
E-mail: hostelsmt7@nau.edu.ua

8️⃣*Гуртожиток* - ФАБД/ФЕБІТ
Адреса: вул. Ніжинська 29, Б
Телефон: (044) 457-85-39
E-mail: hostelsmt8@nau.edu.ua

9️⃣*Гуртожиток* - ФАЕТ
Адреса: вул. Ніжинська 29,В
Телефон: (044) 457-84-78
E-mail: hostelsmt9@nau.edu.ua

1️⃣1️⃣*Гуртожиток* - ФККПІ
Адреса: вул. Ніжинська, 29-Д
Телефон: (044) 406-77-62
E-mail: hostelsmt11@nau.edu.ua

1️⃣3️⃣*Гуртожиток* - ЮФ
Адреса: вул. М.Голего, 7-а
Телефон: (044) 406-68-32
E-mail: hostelsmt13@nau.edu.ua"""
Price_Gurt = """
[💰](https://imbt.ga/M9ZFjo2T8R)*Ціна проживання:*

🏨На період навчального року - 520 грн/міс
🏨На період літніх канікул - 50-60 грн/доба

➡️[Детальніше](http://studcity.nau.edu.ua/price.php)⬅️
"""
Things_Gurt = """
[🎒](https://imbt.ga/dYPrnn8EdQ)*Що варто взяти із собою до гуртожитку:*

▫️Посуд (тарілки, столові прибори)
▫️Кастрюля
▫️Пательня
▫️Чайник
▫️Мультиварка
▫️Праска
▫️Подовжувач
▫️Рушник
▫️Вішаки для одягу
▫️Капці
▫️Засоби гігієни
"""
Map = """[Карта НАУ](https://www.google.com/maps/d/u/0/viewer?mid=1VDlRakwBo9f5-rBqx6bm4tMvt8bbu3pr&ll=0%2C0&z=13)
"""

#Присвоєння відповідей константам меню Відділів
Dekan ="""
[✈️](https://imbt.ga/Tj4I8qGj2t)*Деканати факультетів:*

ФККПІ - Дирекція: ауд. 5.206, тел.: +38 (044) 406-70-08;
ФАЕТ - Дирекція: ауд. 5.410, тел.: +38 (044) 408-58-43;
ФЛСК - Дирекція: ауд. 8.807, тел.: +38 (044) 406-70-36;
ФЕБІТ - Дирекція: ауд. 5.202, тел.: +38 (044) 406-74-88;
АКФ - Дирекція: ауд. 1.350, тел.: +38 (044) 406-74-10;
ФЕБА - Дирекція: ауд. 2.210 , тел.: +38 (044) 406-76-51;
ФТМЛ - Дирекція: ауд. 2.206, тел.: +38 (044) 406-78-41;
ФМВ - Дирекція: ауд. 7.206, тел.: +38 (044) 406-71-96;
ФАБД - Дирекція: ауд. 3.220, тел.: +38 (044) 406-77-94;
ЮФ - Дирекція: ауд. , тел.: +38 (044) 406-70-35;
КВП - Дирекція: ауд. , тел.: +38 (044) 451-48-74;
"""
Buch ="""
[✈️](https://imbt.ga/xnhr1Bcz88)*Бухгалтерії:*

Відділ розрахунків по стипендіях
Начальник – Болінчук Надія Павлівна
кабінет 1.243, тел. +38 (044) 406-78-81

Відділ обліку касових та розрахункових операцій
Начальник – Ковальчук Оксана Геннадіївна
кабінет 1.247, тел. +38 (044) 406-68-63

Бухгалтерія СМ (студмістечка)
Заступник головного бухгалтера – Муляр Галина Миколаївна
гуртожиток № 3, кабінет 14, тел. +38 (044) 406-79-65

Відділ організаційної роботи зі студентами
Заступник головного бухгалтера – Хмелюк Алла Анатоліївна
кабінет 8.001, тел. +38 (044) 497-72-53
"""
Viddil ="""
[✈️](https://imbt.ga/0xH7rIZ2OJ)*Відділи та служби НАУ:*

*Центр медіакомунікацій*
Тел.: 044-406-75-90; 406-68-34
E-mail: news@nau.edu.ua

*Навчально-методичний відділ*
Тел.: 044-406-70-50

*Відділ моніторингу якості вищої освіти*
Тел.: 044-406-75-69; 406-72-51

*Відділ по роботі зі студентами*
Тел.: 044-406-68-15

*Відділ запобігання корупції*
Тел.: 044-406-61-10, 406-61-10
E-mail: stopcor@nau.edu.ua

*Відділ безпекової діяльності*
Тел.: 044-406-75-23

*Авіаційний медичний центр*
Тел.: 044-497-50-05, 497-40-38
E-mail: amc@nau.edu.ua

*Центр культури та мистецтв*
Тел.: 044-408-33-00, 406-72-83, 406-77-37
"""
Studmisto = """
[✈️](https://imbt.ga/n4Oho5wob9) *Студмістечко:*

*Дирекція*
Тел.: (044) 406-70-41, 497-40-04

*Відділ організаційної роботи в гуртожитках*
Тел.: (044) 406-68-59

*Відділ розрахунків за проживання*
Тел.: (044) 406-79-65"""

#Присвоєння відповідей константам меню Про університет
Pidrozdil = """[✈️](https://imbt.ga/0xTq7rRLwJ)*Навчальні підрозділи НАУ:*"""
Rating = """
[✈️](https://imbt.ga/19NSd3nkWM)НАУ у рейтингах:

[Консолідований рейтинг університетів](https://osvita.ua/vnz/rating/51741/)

[Рейтинг Scopus](https://osvita.ua/vnz/rating/82316/)

[Рейтинг за результатами вступної кампанії](https://osvita.ua/vnz/rating/vstup-osvita/59047/)
"""
Contacts_NAU = """
✈️*Інформресурси НАУ:*

[Сайт](https://nau.edu.ua/ua/) НАУ
[Сайт](https://pk.nau.edu.ua/) ПК НАУ
[Фейсбук](https://www.facebook.com/officialnau) НАУ"""

#Присвоєння відповідей константам меню Корисні поради
SmartCard = """
[💳](https://imbt.ga/tMfEGxIcgN)*Як оформити студентський KyivSmartCard:*

Оформленням смарткардів в НАУ займається [ППОСА НАУ](https://t.me/profkom_nau)

Інформація про оформлення з'являється на їх каналі. Ціна проїзду по такій картці *~3,50 грн*
"""

#Опис головного меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('✈️ Вступ до НАУ')
    item2 = types.KeyboardButton('📚 Навчальний процес')
    item3 = types.KeyboardButton('🏨 Гуртожитки')
    item4 = types.KeyboardButton('💼 Відділи університету')
    item5 = types.KeyboardButton('🏢 Про університет')
    item6 = types.KeyboardButton('👨‍✈️ Корисна інформація')
    markup.add(item1, item2, item3, item4, item5, item6)
#Привітання з користувачем після команди /start
    bot.send_message(message.chat.id, 'Привіт, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        #Опис меню Вступ до НАУ
        if message.text == '✈️ Вступ до НАУ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('👨‍🎓Алгоритм вступу бакалавр')
            item2 = types.KeyboardButton('👨‍🔬Алгоритм вступу магістр')
            item3 = types.KeyboardButton('📘Спеціальності НАУ')
            item4 = types.KeyboardButton('📖Правила прийому до НАУ')
            item5 = types.KeyboardButton('📞Контакти ПК')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, item5, back)
            bot.send_message(message.chat.id, '✈️ Вступ до НАУ', reply_markup=markup)

        #Опис функцій кнопок меню Вступ до НАУ
        elif message.text == '👨‍🎓Алгоритм вступу бакалавр':
            bot.send_message(message.chat.id, Algotith_Bac, parse_mode='Markdown')
        elif message.text == '👨‍🔬Алгоритм вступу магістр':
            bot.send_message(message.chat.id, Algotith_Mag, parse_mode='Markdown')
        elif message.text == '📘Спеціальності НАУ':
            bot.send_message(message.chat.id, Spec_NAU, parse_mode='Markdown')
        elif message.text == '📖Правила прийому до НАУ':
            bot.send_message(message.chat.id, Rules_PK, parse_mode = 'Markdown')
        elif message.text == '📞Контакти ПК':
            bot.send_message(message.chat.id, Contacts_PK, parse_mode = 'Markdown')

        #Опис меню Навчальний процес
        elif message.text == '📚 Навчальний процес':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('📓 Розклад занять')
            item2 = types.KeyboardButton('📃 Розклад іспитів')
            item3 = types.KeyboardButton('🔔 Розклад дзвінків')
            item4 = types.KeyboardButton('💰 Стипендіальні списки')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, '📚 Навчальний процес', reply_markup = markup)

        #Опис функцій кнопок меню Навчальний процес
        elif message.text == '📓 Розклад занять':
            bot.send_message(message.chat.id, Rozklad + Sites, parse_mode='Markdown')
        elif message.text == '📃 Розклад іспитів':
            bot.send_message(message.chat.id, Rozklad_isp + Sites, parse_mode='Markdown')
        elif message.text == '🔔 Розклад дзвінків':
            bot.send_message(message.chat.id, Rozklad_dzv, parse_mode='Markdown')
        elif message.text == '💰 Стипендіальні списки':
            bot.send_message(message.chat.id, Stypendia + Sites, parse_mode='Markdown')

        #Опис меню Гуртожитки
        elif message.text == '🏨 Гуртожитки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🛏 Гуртожитки')
            item2 = types.KeyboardButton('💵 Ціна проживання')
            item3 = types.KeyboardButton('❓ Що брати в гуртожиток')
            item4 = types.KeyboardButton('🗺 Карта студмістечка')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, '🏨 Гуртожитки', reply_markup = markup)

        #Опис функцій меню Гуртожитки
        elif message.text == '🛏 Гуртожитки':
            bot.send_message(message.chat.id, Gurt_NAU, parse_mode='Markdown')
        elif message.text == '💵 Ціна проживання':
            bot.send_message(message.chat.id, Price_Gurt, parse_mode='Markdown')
        elif message.text == '❓ Що брати в гуртожиток':
            bot.send_message(message.chat.id, Things_Gurt, parse_mode='Markdown')
        elif message.text == '🗺 Карта студмістечка':
            bot.send_message(message.chat.id, Map, parse_mode='Markdown')

        #Опис меню Відділи універистету
        elif message.text == '💼 Відділи університету':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('💼 Деканати')
            item2 = types.KeyboardButton('💰 Бухгалтерії')
            item3 = types.KeyboardButton('🏢 Інші відділи')
            item4 = types.KeyboardButton('🏨 Студмістечко')
            item5 = types.KeyboardButton('🗺 Карта НАУ')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, '💼 Відділи університету', reply_markup = markup)

        #Опис функцій меню Відділи університету
        elif message.text == '💼 Деканати':
            bot.send_message(message.chat.id, Dekan, parse_mode='Markdown')
        elif message.text == '💰 Бухгалтерії':
            bot.send_message(message.chat.id, Buch, parse_mode='Markdown')
        elif message.text == '🏢 Інші відділи':
            bot.send_message(message.chat.id, Viddil, parse_mode='Markdown')
        elif message.text == '🏨 Студмістечко':
            bot.send_message(message.chat.id, Studmisto, parse_mode='Markdown')
        elif message.text == '🗺 Карта НАУ':
            bot.send_message(message.chat.id, Map, parse_mode='Markdown')

        #Опис меню Про університет
        elif message.text == '🏢 Про університет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🏢 Навчальні підрозділи')
            item2 = types.KeyboardButton('📈 Рейтинги НАУ')
            item3 = types.KeyboardButton('📲 Інформресурси НАУ')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, '🏢 Про університет', reply_markup = markup)

        #Опис функцій меню Про університет
        elif message.text == '🏢 Навчальні підрозділи':
            bot.send_message(message.chat.id, Pidrozdil+ Sites, parse_mode='Markdown')
        elif message.text == '📈 Рейтинги НАУ':
            bot.send_message(message.chat.id, Rating, parse_mode='Markdown')
        elif message.text == '📲 Інформресурси НАУ':
            bot.send_message(message.chat.id, Contacts_NAU, parse_mode='Markdown')

        #Опис меню Корисна інформація
        elif message.text == '👨‍✈️ Корисна інформація':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('💳 KyivSmartCard')
            item2 = types.KeyboardButton('❓ Що брати в гуртожиток')
            item3 = types.KeyboardButton('🗺 Карта НАУ')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, '👨‍✈️ Корисна інформація', reply_markup = markup)

        #Опис функцій меню Корисні поради
        elif message.text == '💳 KyivSmartCard':
            bot.send_message(message.chat.id, SmartCard, parse_mode='Markdown')
        elif message.text == '❓ Що брати в гуртожиток':
            bot.send_message(message.chat.id, Things_Gurt, parse_mode='Markdown')
        elif message.text == '🗺 Карта НАУ':
            bot.send_message(message.chat.id, Map, parse_mode='Markdown')

        #Опис повернення до головного меню
        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('✈️ Вступ до НАУ')
            item2 = types.KeyboardButton('📚 Навчальний процес')
            item3 = types.KeyboardButton('🏨 Гуртожитки')
            item4 = types.KeyboardButton('💼 Відділи університету')
            item5 = types.KeyboardButton('🏢 Про університет')
            item6 = types.KeyboardButton('👨‍✈️ Корисна інформація')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Ви повернулись в головне меню', reply_markup = markup)

bot.polling(none_stop=True)
