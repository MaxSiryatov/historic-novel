﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define storyteller = Character('Рассказчик', color="#3c1f14")
define void = Character(None, kind = nvl)
define void_black = Character('', color = '#000000')
define vasiliy3 = Character('Василий Третий', color="#3c1f14")
define pskovich = Character('Пскович', color="#3c1f14")
define guards = Character('Стражники', color="#3c1f14")
define guard = Character('Стражник', color="#3c1f14")
define peasant_craftsman = Character('Стражники', color="#3c1f14")
define peasants_life = Character('Вырванная история о жизни крестьян:', color="#3c1f14")
define peasant_orator = Character('Староста деревни', color="#3c1f14")
define peasants_group = Character('Группа крестьян', color="#3c1f14")
define peasant_cattleman = Character('Крестьянин скотовод', color="#3c1f14")
define peasant_plowman = Character('Крестьянин пахарь', color="#3c1f14")
define peasant_baker = Character('Крестьянка пекарь', color="#3c1f14")
define peasant_craftsman = Character('Крестьянин ремесленник', color="#3c1f14")
define peasant_duty = Character('Крестьянин на посту', color="#3c1f14")
define peasant_fisher = Character('Крестьянин рыбак', color="#3c1f14")
define unknown_character = Character('Неизвестный', color="#3c1f14")
define n = Character(None, kind=nvl)

#Определение музыки

define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"


# Игра начинается здесь:
label start:

    play music gamemusic

    scene storyteller_house with fade

    storyteller "Здравствуй юный друг. Рад, что ты решил заглянуть к старику. Садись и послушай."
    storyteller "Вот так, уютно устроился? Вот и славно... Я с радостью поделюсь с тобой великой силой."
    storyteller "У тебя есть вопрос о какой силе может говорить этот ослабший старик? Хо-хо, о силе знаний, конечно. Ведь знания, они - как свет во мраке, как опора в бурю. Мир наш – сложная сетка переплетений, и в каждом узле этой сети живет кусочек прошлого."
    storyteller "И история – это своего рода карта. Карта, которая позволяет нам разгадывать загадки нашего прошлого, не повторять ошибок прошлого, и видеть пути, которые мы пройдем в будущем."
    storyteller "Именно поэтому я хочу помочь тебе погрузится в историю, пусть и совсем немного…"
    storyteller "Кхм… Думаю тебе понравится послушать про эпоху, когда наша Русь казалась склонной к разрыву. Я говорю про 16 век, про смутное время."
    
    scene smuta with fade
    show storyteller at right
    
    storyteller "Сму́та — период в истории России с 1598 по 1618 год, ознаменованный стихийными бедствиями, польско-шведской интервенцией, тяжелейшим государственно-политическим и социально-экономическим кризисом."
    storyteller "Ох и трудное тогда было время, власть то и дело менялась. Заговоры против царя почти стали обыденностью. Борьба в верхушке сказывалась на жизнях простых крестьян, да и вообще всего населения."
    
    scene pskov with fade
    show storyteller at right

    storyteller "Много интересных событий произошло в это время."
    storyteller "Так, например, к началу 16 века Псков — один из самых древних городов России, впервые упомянутый в «Повести временных лет» под 903 годом, фактически утратил свою независимость, но сохранял старые, вечевые порядки. Что такое вече?"
    
    scene veche with fade
    show storyteller at right
    
    storyteller "Вече — это всенародное собрание городских жителей, на котором они принимали решения по важным общественным вопросам, имело в основном законодательную функцию, но могло также принимать и приводить в действие судебные решения."
    storyteller "Между тем большинство русских земель к тому времени уже было объединено Москвой и образовалось единое Русское государство. Вот новый великий князь Василий Третий и решил, что пришло время покончить с остатками самостоятельности Пскова."
    
    scene vasiliy3_bg with fade
    
    storyteller "Васи́лий Третий Ива́нович - великий князь владимирский и московский в 1505—1533 годах, государь всея Руси. Сын Ивана Третьего Великого и отец Ивана Четвёртого Грозного." 
    storyteller "Василий Третий продолжил политику своего отца по “сбору” русских земель и постепенному упразднению удельных княжеств."
    
    scene ivan_mikhailovich with fade
    show storyteller at right
    
    storyteller "В 1509 году в Псков был послан наместник — Иван Михайлович Репня-Оболенский — князь, боярин, наместник и воевода на службе у московских князей Ивана Третьего и Василия Третьего, родоначальник князей Репниных-Оболенских."
    storyteller "Во время наместничества в Пскове он получил прозвище «Найдён»."
    storyteller "Он приехал тайно, не явился на вече и не принес ему присяги."
    storyteller "Новый наместник отказался признавать псковские законы, сам устанавливал и собирал налоги с населения, судил псковичей без участия представителей веча, словом, вёл себя, как обычный городской наместник «государя всея Руси»."
    
    scene novgorod with fade
    show storyteller at right
    
    storyteller "Узнав, что великий князь в Новгороде, одном из древнейших городов России, расположенным на ее Северо-Западе у истоков реки Волхов и озера Ильмень, псковские бояре отправили туда своих послов с жалобами на нового наместника Репню-Оболенского."
    storyteller "Репня же в свою очередь поехал к Василию Третьему жаловаться на псковичей."

    scene chapter_1 with fade
    window hide

    scene tsar_room with fade
    show vasiliy3 at left

    vasiliy3 "Как объединить Русские земли? Вопрос, который тревожит меня в эти дни. Псков... старый, древний город, со своими традициями, своими порядками. Он не вписывается в картину единого государства, к которой я стремлюсь."
    vasiliy3 "Псков отказывается принимать новых наместников, не признает Московскую власть, своенравно сохраняет свои вечевые порядки. Это нужно менять!"
    vasiliy3 "Приглашу псковичей в Кремль, на пир. Пусть они увидят, что мы стремимся к миру и согласию. Но и пусть они поймут, что отдельно от Московского княжества жить не смогут. Пусть видят силу, пусть поймут, что наместник — это не враг, а служитель закона." 
    vasiliy3 "Надо объединить, надо создать сильное, единое государство, которое будет стоять на страже всех своих земель и всех своих людей."
    vasiliy3 "Отправить посла в Псков! Желаю видеть псковичей на пиру в Москве!"

    scene moscow_street with fade
    show vasiliy3 at left

    vasiliy3 "Добро пожаловать, псковичи, в Москву. Я рад вас видеть здесь. Прошу, присядьте, давайте обсудим дела насущные."

    show pskovich_1 at right

    pskovich "Благодарим вас, великий князь, за ваше приглашение. Мы приехали сюда, чтобы выразить наше беспокойство по поводу назначения нового наместника в нашем городе."
    vasiliy3 "Могу понять ваше беспокойство, но и вы должны меня понять. Я стремлюсь к единству всех русских земель. Это необходимо для укрепления государства и обеспечения порядка."

    hide pskovich_1
    show pskovich_2 at right

    pskovich "Но, великий князь, мы не желаем утратить нашу самостоятельность. Мы уважаем ваше величество, но просим вас сохранить наши устои и традиции."
    vasiliy3 "Псковичи, я понимаю вашу привязанность к своим традициям, но должен напомнить, что все мы русские, и наше единство важно. Вместе мы станем сильнее и сможем защитить наши земли от любых угроз."

    hide pskovich_2
    show pskovich_3 at right

    pskovich "Но великий князь, мы не готовы потерять наш голос и нашу способность участвовать в управлении нашим городом."
    vasiliy3 "Ваше вече будет заменено, на ту форму управления, что вписывается в систему государственного управления Русского государства. Но это не означает, что ваш голос не будет услышан."

    hide pskovich_3
    show pskovich_1 at right

    pskovich "Но мы боимся, что наш город потеряет свою уникальность и самобытность под вашим правлением."
    vasiliy3 "Ваша уникальность и самобытность будут признаны и сохранены, но под общей государственной защитой. Мы стремимся к благополучию всех наших подданных, включая псковичей."

    hide pskovich_1
    show pskovich_2 at right

    pskovich "Мы все еще не уверены, великий князь. Позволь вернуться в Псков и обсудить это с народом."
    vasiliy3 "Видно, что сейчас мы к соглашению не придём. Нужно решать, как дальше влиять на Псков."

    jump choice_pskovich
        
    return


label agree_with_pskovich:

    scene moscow_street with fade
    show vasiliy3 at left
    show pskovich_1 at right

    vasiliy3 "Так и быть! Я жду, что вы сможете принять верное решение! Возвращайтесь в великий город Псков и передайте волю царя!"
    pskovich "Спасибо, царь батюшка, мы расскажем о вашей воле!"
    vasiliy3 "А теперь ступайте, вас ждёт длинная дорога!"
    void_black "*Псковичи уходят*"

    scene storyteller_house

    storyteller "Псковичи вернулись в свой город. Однако, несмотря на это, в течение очень долгого времени ничего не изменилось." 
    storyteller "Псков продолжал жить по своим древним традициям, вече продолжало собираться под звон вечевого колокола, и власть в городе оставалась в руках местных бояр."
    storyteller "Такая пассивность со стороны Пскова и неопределенность в политике присоединения сильно замедлили процесс интеграции города в Русское государство. В конечном итоге, это могло привести к неким неизвестным нам последствиям."
    storyteller "На самом же деле, Василий Третий не согласился с псковичами и посадил их под стражу!"
    storyteller "Давайте расскажу как это было"

    menu:
        "Вернуться назад":
            jump choice_pskovich

    return

label disagree_with_pskovich:

    scene moscow_street with fade
    show vasiliy3_angry at left
    show pskovich_1 at right

    vasiliy3 "Стража! Запереть псковичей в темнице!"
    pskovich "Подождите, царь батюшка! Что это значит!"

    hide pskovich_1
    show guard_right at right

    guard "Да, царь батюшка."
    void_black "*Стража выводит псковичей*"

    hide vasiliy3_angry
    show vasiliy3
    hide guard_right

    vasiliy3 "Теперь нужно решить, как присоединить этот город к России. Один из вариантов - упразднить вече и снять вечевой колокол. Это будет жестким, но необходимым шагом. "
    vasiliy3 "Псков должен понять, что теперь он часть Русского государства, что у нас есть общие законы и правила. Убрав вече, мы уберем источник его самостоятельности, сделаем его более прозрачным для нашего управления."
    vasiliy3 "Но это может вызвать протесты, сопротивление, и я не хочу видеть братоубийство на улицах этого города."
    vasiliy3 "А второй вариант - посетить город с мирным посылом. Показать, что мы стремимся к миру и согласию. Переговоры, убеждения, демонстрация нашей силы и одновременно мудрости. "
    vasiliy3 "Псков должен понять, что он не одинок, что у нас есть общие цели и задачи. Но это может затянуться, у Пскова есть своя гордость и самоуверенность, он может не желать слушать слова мудрости."
    vasiliy3 "Оба варианта имеют свои риски и свои выгоды. Упразднение вече — это решение 'железной руки', но оно может вызвать бурю недовольства."
    vasiliy3 "Посещение городов с мирным посылом — это путь дипломатии и убеждения, но это может затянуть процесс и дать Пскову время организоваться."
    vasiliy3 "Нужно решить... Что будет лучше для Русского государства?"

    menu:
        "Упразднить вече и снять вечевой колокол.":
            jump destroy_veche
        "Посетить города с мирным посылом.":
            jump visit_cities

    return

label choice_pskovich:

    scene moscow_street with fade
    show vasiliy3 at left
    show pskovich_1 at right

    menu: 
        "Согласиться с псковичами и позволить им вернуться и обсудить присоединение.":
            jump agree_with_pskovich
        "Нельзя ждать, нужно действовать. Посадить их под стражу!":
            jump disagree_with_pskovich

    return

label destroy_veche:

    scene storyteller_house with fade

    storyteller "Вы приняли историческое решение, оно увековечено в учебниках и архивах России! Сейчас я вам поведаю итог этого решения"
    storyteller "Псков присоединился к составу единого государства и указом великого князя Московского Василия Третьего пало вольное, шумное, свободолюбивое псковское вече — самый демократичный орган управления в средневековой Руси."
    storyteller "13 января 1510 года на глазах всего псковского люда «спустиша колокол вечевой у святыя Троица», то начали собравшиеся, «на колокол смотря, плакати по своей старине и по своей воли…». "
    storyteller "Как свидетельствовал современник событий, автор знаменитой «Повести о псковском взятии», не плакали только младенцы, сосущие молоко."
    storyteller "Выбранное твоё решение, отразится на будущей истории, а как именно, это мы узнаем в следующей главе"

    jump chapter_2

    return 

label visit_cities:

    scene storyteller_house with fade 

    storyteller "Принятое вами решение имеет место быть, может случись оно так и  история России была другой, но это мы не узнаем."
    storyteller "Давайте вместе подумаем над тем, что же могло произойти дальше."
    storyteller "Василий Третий посетил с добрым намерениям Псков и оставил его независимость, для псковичей это было радостное событие. Но позже пошли слухи, что сам царь оставил городу власть. "
    storyteller "Все близкие к Пскову города захотели такой же независимости, а это означает, что план по объединению Российских земель провалился. А это может очень плохо отразиться на будущем страны."
    storyteller "Настоящая же история была такова."
    storyteller "Псков присоединился к составу единого государства и указом великого князя Московского Василия Третьего пало вольное, шумное, свободолюбивое псковское вече — самый демократичный орган управления в средневековой Руси."
    storyteller "13 января 1510 года на глазах всего псковского люда «спустиша колокол вечевой у святыя Троица», то начали собравшиеся, «на колокол смотря, плакати по своей старине и по своей воли…». "
    storyteller "Как свидетельствовал современник событий, автор знаменитой «Повести о псковском взятии», не плакали только младенцы, сосущие молоко."

    jump chapter_2

    return

label chapter_2:

    scene chapter_2 with fade
    window hide

    scene storyteller_house with fade

    storyteller "Мы с вами, дорогие друзья свободно живём, а были и другие времена."
    
    scene map_fedor1 with fade
    show storyteller at right
    
    storyteller "В эпоху правления царя Фёдора Иоанновича, существовали крепостные крестьяне, которые бесплатно работали на своих хозяев и были их собственностью."
    storyteller "На годы правления царя Фёдора Иоанновича 1584-1598 пришлось много событий, но я расскажу о введение указа об “Урочных летах”. Дело было в 1597 году стремление остановить массовую миграцию крестьян."
    
    scene storyteller_house with fade
    
    storyteller "В поисках лучшей доли многие крестьяне снимались с насиженных мест и отправлялись в другие края. Это не устраивало землевладельцев, которые лишались рабочей силы и возможности планомерно развивать свое хозяйство."
    
    scene sky with fade

    window hide

    n '''Вырванная история о жизни крестьян:
    
    Неизвестные, измученные работой на полях крестьяне с низким уровнем жизни должны почти за бесплатно работать на своего хозяина.
    
    Летом в полях жара, осенью дождливо и приходится ещё собирать урожай, многие болеют и обесцениваются в глазах хозяина. 
    
    Зимой холодно, еды не хватает, дикие звери приходят из лесов. Весной земля ещё не отогрелась для посева, но подготавливать почву нужно.''' 

    nvl clear
    nvl hide

    scene pomestie with fade
    show peasant_orator

    peasant_orator "Надоело! Я не хочу больше пахать за бесплатно! Наши братья гибнут из-за работы, никто не знает, сколько нам осталось!"
    peasants_group "Да! Ты прав, долой бояр и им подобным, отныне мы власть, мы определяем свою судьбу"
    peasant_orator "Сегодня ночью, когда караульных не будет на посту мы со всеми необходимыми вещами уйдем далеко в леса"
    peasants_group "Да!"

    scene storyteller_house with fade

    storyteller "Крестьянам удалось сбежать, но куда же им пойти. Есть торговый тракт, по которому передвигаются торговцы и прочая знать, есть леса, дорога через которые трудна, но незаметна." 
    storyteller "Можно пойти через поля, самое видное место, но кто ещё путешествует по полям кроме крестьян."

    scene forest with fade
    show peasant_orator at left

    peasant_orator "Братья и Сёстры, нам нужно принять решение, какой же дорогой мы пойдём искать новый дом"
    
    show peasant_cattleman at right
    
    peasant_cattleman "Нужно идти полями и торговым трактом на, туда откуда солнце восходит!"

    hide peasant_cattleman 
    show peasant_plowman at right

    peasant_plowman "Пойдёмте лесом, там и еду добыть можно и никто нас не заметит!"

    hide peasant_plowman
    show peasant_baker at right

    peasant_baker "Идём вдоль реки, вода у нас всегда будет и прокормить мы себя сможем!"

    hide peasant_baker
    show peasant_craftsman at right

    peasant_craftsman "Пойдёмте по торговому тракту, так быстрее всего!"
    storyteller "Какое решение примут крестьяне, каждое из них может оказаться тяжёлым испытанием."

    menu:
        "Пойти по полям и торговым трактом":
            jump go_field
        "Пойти по лесам":
            jump go_forest
        "Пойти по берегу реки":
            jump go_riverside
        "Пойти по торговому тракту":
            jump go_traderoute

    return

label go_field:
    
    scene storyteller_house with fade
    
    storyteller "Крестьяне приняли решение идти по полям днём и ночью по торговому тракту."
    storyteller "Рассказчик: дорога лёгкая, только от палящего солнца днём не спрятаться, а ночью сил идти уже нет. Кажется путь крестьян затянется."

    scene forest_with_fire with fade
    show peasant_craftsman at right

    peasant_craftsman "Я не привык к таким долгим и изнуряющим походам, давайте сделаем ночной привал до утра, а потом дальше отправимся в путь."
    storyteller "Все приняли это решение, потому что каждый крестьянин был изнурён дорогой, но только они развели костёр и приготовились к отдыху."

    scene forest_night with fade
    show guard at left

    guards "Кажется там в поле горит костёр, давай проверим кто это."
    guard "Разбойников тут быть не должно, не так уж и далеко мы отошли от города, наверное бежавшие крестьяне разбили свой лагерь."
    guard "Тушите факела, нужно подойти незамеченными и схватить каждого крестьянина."

    scene storyteller_house with fade

    storyteller "Крестьяне от усталости потеряли бдительность, многие уже уснули, а оставшиеся сидели у костра в полусонном состоянии."

    scene forest_night with fade
    show guard at left

    guard "Окружаем лагерь и стрмительно наступаем, при оказанном сопротивлении можно калечить, но не убивать."

    scene forest_with_fire with fade
    show peasant_plowman at right

    peasant_plowman "Я слышу топот и звон доспех, СТРАЖА! Всем проснуться и бежать!"

    scene storyteller_house with fade

    storyteller "Рассказчик: Как бы не крестьяне не старались им не справиться с подготовленными людьми в сражении. Бегством никому спастись не удалось."
    storyteller "В эту ночь удача обошла крестьян стороной и все они были возвращены обратно."
    storyteller "Позже 24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."
    storyteller "Но нашим крестьянам так и не удалось сбежать повторно, а может удача просто отвернулась от них."

    return

label go_forest:

    scene storyteller_house with fade

    storyteller "Крестьяне приняли решение пойти через лес."
    storyteller "Тяжёлая дорога ждала крестьян, пробираться с вещами и едой трудно, много сил уходит на передвижение. Но несмотря на это крестьяне идут на встречу к свободе."

    scene forest_with_wheat with fade
    show peasant_cattleman at right

    peasant_cattleman "Нам нужен отдых, животные устали идти по лесу, им нужна вода."

    show peasant_orator at left

    peasant_orator "До реки ещё далеко, но мы сможем отдохнуть как только солнце опустится за горизонт."
    peasant_cattleman "Мне страшно, что дикие звери и тёмные духи нападут на нас."
    peasant_orator "Будем по очереди охранять животных ночью."

    scene storyteller_house with fade

    storyteller "Крестьяне всё таки нашли маленький ручей в лесу и решили обосновать свой лагерь."

    scene field_night with fade
    show peasant_baker 

    peasant_baker "Еду будем экономить, поэтому каждому достанется по куску хлеба и одной тарелке овощного супа."

    scene storyteller_house with fade

    storyteller "Крестьяне остались на ночь в лесу. И после полнолуния, появились странные звуки."

    scene field_night with fade
    show peasant_fisher

    peasant_duty "Слишком тихо сегодня ночью, нет не единого звука."
    void_black "*Топот*"
    peasant_duty "Что это было, неужели невесть какая или звери."
    void_black "*Затяжной вой*"
    peasant_duty "Неужели волки! Подъём крестьяне! Звери рядом!"
    storyteller "Сильный шум крестьян отпугнул волков, шагов зверей и шелеста травы никто не слышал, но длинный и голодный вой, говорил о том, что волки ещё вернутся."
    
    scene forest_with_wheat with fade

    void_black "*Уже утром*"
    
    show peasant_orator

    peasant_orator "Друзья мои, нужно отправляться в путь, смотрите внимательно по сторонам и если увидите протоптанные тропинки, то не молчите. Нужно избегать волчьих троп, дать отпор при неожиданной встрече мы не сможем."
    
    scene storyteller_house with fade

    storyteller "Крестьяне устало шли по лесу, озираясь по сторонам, сколько ещё бессонных ночей их ждёт."

    scene forest1 with fade
    show peasant_cattleman at right

    peasant_cattleman "Уже много ночей прошло, скотина исхудала, нужно где-то остановиться на долгое время."

    show peasant_orator at left

    peasant_orator "Как только мы дойдём до хорошего места у реки, мы примемся обустраиваться."

    scene storyteller_house with fade

    storyteller "Нашим крестьянам удалось найти ответвление от большого русла реки. Казалось бы, в непроходимом лесу, рядом с маленькой речкой."

    scene slavery with fade

    storyteller "Деревня росла и развивалась, но это было не долго. Крестьянам не удалось прожить долгую и счастливую жизнь, в один день всё изменилось и деревню обнаружили казаки, которые передвигались по берегу реки."
    storyteller "24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."

    scene storyteller_house with fade

    storyteller "Деревня была сожжена, а крестьян вернули владельцу."

    return

label go_riverside:

    scene storyteller_house with fade

    storyteller "Крестьяне приняли решение пойти вдоль реки."
    storyteller "Дорога предстояла тяжёлая, реки места духовные, много разных историй о тёмных духах было. Но есть и плюс, жажда не замучает и скотина будет бодрая."

    scene field_with_river with fade
    show peasant_fisher at left

    peasant_fisher "По берегу реки легко идти, к тому же русло обмелело и нам идти удобнее."

    show peasant_cattleman at right

    peasant_cattleman "Скотину рыбой не накормишь."

    show peasant_plowman 

    peasant_plowman "Скотина и в лесу пощипать травку может, но времени нет у нас, кто знает когда нас пойдут искать."

    hide peasant_fisher
    show peasant_orator at left

    peasant_orator "Как только начнёт темнеть нужно отходить от реки, чтобы духов не потревожить."

    hide peasant_plowman
    show peasant_fisher 

    peasant_fisher "Небылицы всё это, ни разу не пропал и никого не видел."

    hide peasant_orator
    show peasant_plowman at left

    peasant_plowman "Люди пропадали ночь у реки, даже казаки и бояре."
    peasant_cattleman "Даже скотина могла в один миг исчезнуть, а на утро одни кости по берегу разбросаны."
    peasant_plowman "Знаю такую историю, что кости есть, а следов нет. Дикие звери шкуру скотины не едят. Но в этот раз только обглоданные кости остались…"

    scene storyteller_house with fade

    storyteller "Дорога предстояла длинная, много разных историй есть с реками и все они страшные. Но есть кое-что страшнее духов и нечистой силы, это человек."

    scene field_with_river1 with fade
    show peasant_orator at left

    peasant_orator "Мы идём уже 5 ночей вдоль реки, предлагаю сегодня остановиться и хорошенько отдохнуть."

    show peasant_cattleman at right

    peasant_cattleman "Я согласен, скотина устала, отдых нужен."

    show peasant_fisher 

    peasant_fisher "Давайте разобьём лагерь, а я пройду дальше и в сильном течении покидаю сети."
    peasant_orator "Решено, разбиваем лагерь и готовимся к отдыху."

    scene storyteller_house with fade

    storyteller "Рыбак ушёл ловить сетями, но кто же знал, что сильное течение привлекает не только его одного."

    scene field_with_river_night with fade
    show peasant_plowman at left

    peasant_plowman "Что-то долго нет рыбака нашего."

    show peasant_cattleman at right

    peasant_cattleman "Наверное рыбы наловил и унести всё не может."
    peasant_plowman "Давайте пождём до заката, а потом сходим его проведать."

    scene storyteller_house with fade

    storyteller "Рыбак так и не вернулся, а фермер вместе со скотоводом пошли его искать."

    scene field_with_river_night with fade
    show peasant_plowman at left

    peasant_plowman "Ты это слышишь?"

    show peasant_cattleman at right

    peasant_cattleman "Что?"
    peasant_plowman "Шум воды, кажется мы уже близко."
    void_black "*Жуткий смех*"
    peasant_cattleman "Кто здесь?"
    void_black "*Топот*"
    peasant_plowman "Кажется я слышу голос."
    unknown_character "Хороший раб нам попался, крепкий, не больной, рыбачить умеет, его мы за дорого продадим."
    peasant_cattleman "Кто это может быть."
    void_black "*Шаги сзади*"
    peasant_plowman "Кто тут?"
    void_black "*Крики издалека*"
    peasant_cattleman "По реке хорошо приносится звук, кажется что-то случилось в лагере."

    scene storyteller_house with fade

    storyteller "Не успели добраться до лагеря наши друзья, их схватили разбойники, как и рыбака, как и весь лагерь. Кого-то сразу убили, женщин забрали себе, а самых крепких вернули хозяину."
    storyteller "Совсем скоро вышел указ."
    storyteller "24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."

    return

label go_traderoute:

    scene traderoute with fade
    show storyteller

    storyteller "Крестьяне приняли решение идти только по торговому тракту."
    storyteller "Самый лёгкий путь для крестьян, но самый опасный, потому что на встречу могут попасться бояре, казаки, торговцы и у каждого, будут вопросы к крестьянам."

    hide storyteller
    show peasant_orator at left

    peasant_orator "Друзья, нам нужно пройти по этой дороге очень быстро и как можно дальше, потому что мы можем напороться на неприятности."

    show peasant_cattleman at right

    peasant_cattleman "Скотина идёт быстро, но возможно жажда замучает."

    show peasant_plowman 

    peasant_plowman "Ничего с твоей скотиной не будет, она готова к таким испытаниям."

    hide peasant_cattleman
    show peasant_craftsman at right

    peasant_craftsman "Друзья, предлагаю меньше спорить и больше идти, я не хочу возвращаться назад, хочу свободу."
    peasant_orator "Решено! Быстро идём по дороге, потом попробуем куда нибудь свернуть."

    scene storyteller_house with fade

    storyteller "Прошло 7 ночей, а крестьяне не видели беды. Дорога была лёгкая, все успели расслабится. Это было фатальной ошибкой."

    scene pathway with fade
    show peasant_orator at left

    peasant_orator "Сегодня можно отдохнуть, 7 ночей прошло, а погони нет. Думаю теперь будет всё в порядке."

    show peasant_craftsman at right

    peasant_craftsman "Я буду сторожить полночи, а потом с кем нибудь поменяюсь."

    hide peasant_orator
    show peasant_plowman at left

    peasant_plowman "Можешь смело меня разбудить, сил полно и я готов подменить тебя."

    scene storyteller_house with fade

    storyteller "Именно так и началась ночь, которая снова определит судьбу крестьян."

    scene forest_night1 with fade
    show peasant_craftsman at right

    peasant_craftsman "Кажется я слышу топот копыт, хотя может быть я уже устал."
    peasant_craftsman "Вставай, вставай!"

    show peasant_plowman at left

    peasant_plowman "Что случилось?"
    peasant_craftsman "Ты слышишь топот копыт?"
    peasant_plowman "Тебе кажется, зачем ты меня так рано разбудил."
    peasant_craftsman "Я пойду посмотрю, а ты не засыпай, кажется нас преследуют."

    scene storyteller_house with fade

    storyteller "Крестьянин ремесленник вышел за пределы лагеря и увидел приближающиеся огоньки, кажется на поиски беглых крестьян отправили людей на лошадях."

    scene forest_night1 with fade
    show peasant_craftsman

    peasant_craftsman "Вставайте братцы, за нами погоня, на конях приближаются!"

    scene storyteller_house with fade

    storyteller "В созданной суматохе крестьяне не смогли сбежать и всех поймали и вернули хозяину."
    storyteller "Позже 24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."

    return


    