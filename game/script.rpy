# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define storyteller = Character('Рассказчик', color="#3c1f14")
define void = Character(None, kind = nvl)
define void_black = Character('', color = '#000000')
define vasiliy3 = Character('Василий Третий', color="#3c1f14")
define pskovich = Character('Пскович', color="#3c1f14")
define guards = Character('Стражники', color="#3c1f14")
define guard = Character('Стражник', color="#3c1f14")
define peasant_craftsman = Character('Стражники', color="#3c1f14")
define peasants_life = Character('Вырванная история о жизни крестьян', color="#3c1f14")
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
define dmitri_ivanovich = Character('Дмитрий Иванович', color="#3c1f14")
define clerk = Character('Писарь', color="#3c1f14")
define boyar = Character('Боярин', color="#3c1f14")
define vasiliy_shuisky = Character('Василий Шуйский', color="#3c1f14")
define boyar_1 = Character('Боярин 1', color="#3c1f14")
define boyar_2 = Character('Боярин 2', color="#3c1f14")
define mariya_nagaya = Character('Мария Нагая', color="#3c1f14")
define conspirator = Character('Заговорщик', color="#3c1f14")
define lshgedmitri = Character('Лжедмитрий', color="#3c1f14")

#Определение музыки

define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"


# Игра начинается здесь:
label start:

    play sound chair
    scene storyteller_house with fade
    play music gamemusic
    play sound one_one
    storyteller "Здравствуй юный друг. Рад, что ты решил заглянуть к старику. Садись и послушай."
    stop sound
    play sound one_two
    storyteller "Вот так, уютно устроился? Вот и славно... Я с радостью поделюсь с тобой великой силой."
    stop sound
    play sound one_three
    storyteller "У тебя есть вопрос, о какой силе может говорить этот ослабший старик? Хо-хо, о силе знаний, конечно. Ведь знания, они - как свет во мраке, как опора в бурю. Мир наш – сложная сетка переплетений, и в каждом узле этой сети живет кусочек прошлого."
    stop sound
    play sound one_three_one
    storyteller "И история – это своего рода карта. Карта, которая позволяет нам разгадывать загадки нашего прошлого, не повторять ошибок прошлого, и видеть пути, которые мы пройдем в будущем."
    stop sound
    play sound one_four
    storyteller "Именно поэтому я хочу помочь тебе погрузится в историю, пусть и совсем немного…"
    stop sound
    play sound one_five
    storyteller "Кхм… Думаю тебе понравится послушать про эпоху, когда наша Русь казалась склонной к разрыву. Я говорю про 16 век, про Смутное время."
    stop sound
    
    scene smuta with fade
    play music fighting
    scene smuta with fade
    show storyteller at right
    play music gamemusic
    play sound one_six
    storyteller "Сму́та — период в истории России с 1598 по 1618 год, ознаменованный стихийными бедствиями, польско-шведской интервенцией, тяжелейшим государственно-политическим и социально-экономическим кризисом."
    stop sound
    play sound one_seven
    storyteller "Ох и трудное тогда было время, власть то и дело менялась. Заговоры против царя почти стали обыденностью. Борьба в верхушке сказывалась на жизнях простых крестьян, да и вообще всего населения."
    stop sound

    scene pskov with fade
    show storyteller at right

    play sound one_eight
    storyteller "Много интересных событий произошло в это время."
    stop sound
    play sound one_eight_one
    storyteller "Так, например, к началу 16 века Псков — один из самых древних городов России, впервые упомянутый в «Повести временных лет» под 903 годом, фактически утратил свою независимость, но сохранял старые, вечевые порядки. Что такое вече?"
    stop sound
    
    scene veche with fade
    show storyteller at right
    
    play sound one_nine
    storyteller "Вече — это всенародное собрание городских жителей, на котором они принимали решения по важным общественным вопросам, имело в основном законодательную функцию, но могло также принимать и приводить в действие судебные решения."
    stop sound
    play sound one_ten
    storyteller "Между тем большинство русских земель к тому времени уже было объединено Москвой и образовалось единое Русское государство. Вот новый великий князь Василий Третий и решил, что пришло время покончить с остатками самостоятельности Пскова."
    stop sound
    
    scene vasiliy3_bg with fade
    
    play sound one_eleven
    storyteller "Васи́лий Третий Ива́нович - великий князь владимирский и московский в 1505—1533 годах, государь всея Руси. Сын Ивана Третьего Великого и отец Ивана Четвёртого Грозного." 
    stop sound
    play sound one_eleven_one
    storyteller "Василий Третий продолжил политику своего отца по “сбору” русских земель и постепенному упразднению удельных княжеств."
    stop sound

    scene ivan_mikhailovich with fade
    show storyteller at right
    
    play sound one_twelve
    storyteller "В 1509 году в Псков был послан наместник — Иван Михайлович Репня-Оболенский — князь, боярин, наместник и воевода на службе у московских князей Ивана Третьего и Василия Третьего, родоначальник князей Репниных-Оболенских."
    stop sound
    play sound one_twelve_one
    storyteller "Во время наместничества в Пскове он получил прозвище «Найдён»."
    stop sound
    play sound one_thirteen
    storyteller "Он приехал тайно, не явился на вече и не принес ему присяги."
    stop sound
    play sound one_thirteen_one
    storyteller "Новый наместник отказался признавать псковские законы, сам устанавливал и собирал налоги с населения, судил псковичей без участия представителей веча, словом, вёл себя, как обычный городской наместник «государя всея Руси»."
    stop sound
    
    scene novgorod with fade
    show storyteller at right
    
    play sound one_fourteen
    storyteller "Узнав, что великий князь в Новгороде, одном из древнейших городов России, расположенным на ее Северо-Западе у истоков реки Волхов и озера Ильмень, псковские бояре отправили туда своих послов с жалобами на нового наместника Репню-Оболенского."
    stop sound
    play sound one_fourteen_one
    storyteller "Репня же в свою очередь поехал к Василию Третьему жаловаться на псковичей."
    stop sound

    scene chapter_1 with fade
    window hide

    scene tsar_room with fade
    show vasiliy3 at left

    vasiliy3 "Как объединить Русские земли? Вопрос, который тревожит меня в эти дни. Псков... старый, древний город, со своими традициями, своими порядками. Он не вписывается в картину единого государства, к которой я стремлюсь."
    hide vasiliy3
    show vasiliy3_serious at left
    vasiliy3 "Псков отказывается принимать новых наместников, не признает Московскую власть, своенравно сохраняет свои вечевые порядки. Это нужно менять!"
    hide vasiliy3_serious
    show vasiliy3_serious1 at left
    vasiliy3 "Приглашу псковичей в Кремль, на пир. Пусть они увидят, что мы стремимся к миру и согласию. Но и пусть они поймут, что отдельно от Московского княжества жить не смогут. Пусть видят силу, пусть поймут, что наместник — это не враг, а служитель закона." 
    vasiliy3 "Надо объединить, надо создать сильное, единое государство, которое будет стоять на страже всех своих земель и всех своих людей."
    vasiliy3 "Отправить посла в Псков! Желаю видеть псковичей на пиру в Москве!"

    scene moscow_street with fade
    play music city
    show vasiliy3_happy at left

    vasiliy3 "Добро пожаловать, псковичи, в Москву. Я рад вас видеть здесь. Прошу, присядьте, давайте обсудим дела насущные."

    show pskovich_1 at right

    pskovich "Благодарим вас, великий князь, за ваше приглашение. Мы приехали сюда, чтобы выразить наше беспокойство по поводу назначения нового наместника в нашем городе."
    vasiliy3 "Могу понять ваше беспокойство, но и вы должны меня понять. Я стремлюсь к единству всех русских земель. Это необходимо для укрепления государства и обеспечения порядка."

    hide pskovich_1
    show pskovich_2 at right

    pskovich "Но, великий князь, мы не желаем утратить нашу самостоятельность. Мы уважаем ваше величество, но просим вас сохранить наши устои и традиции."
    hide vasiliy3_happy
    show vasiliy3 at left
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
    play music city

    vasiliy3 "Так и быть! Я жду, что вы сможете принять верное решение! Возвращайтесь в великий город Псков и передайте волю царя!"
    pskovich "Спасибо, царь батюшка, мы расскажем о вашей воле!"
    vasiliy3 "А теперь ступайте, вас ждёт длинная дорога!"
    void_black "*Псковичи уходят*"

    play music gamemusic
    scene storyteller_house

    play sound two_one
    storyteller "Псковичи вернулись в свой город. Однако, несмотря на это, в течение очень долгого времени ничего не изменилось." 
    stop sound
    play sound two_one_one
    storyteller "Псков продолжал жить по своим древним традициям, вече продолжало собираться под звон вечевого колокола, и власть в городе оставалась в руках местных бояр."
    stop sound
    play sound two_two
    storyteller "Такая пассивность со стороны Пскова и неопределенность в политике присоединения сильно замедлили процесс интеграции города в Русское государство. В конечном итоге, это могло привести к неким неизвестным нам последствиям."
    stop sound
    play sound two_three
    storyteller "На самом же деле, Василий Третий не согласился с псковичами и посадил их под стражу!"
    stop sound
    play sound two_four
    storyteller "Давайте расскажу как это было."
    stop sound

    jump disagree_with_pskovich

    return

label disagree_with_pskovich:

    scene moscow_street with fade
    show vasiliy3_angry at left
    show pskovich_1 at right
    play music furious_music

    vasiliy3 "Стража! Запереть псковичей в темнице!"
    hide pskovich_1
    show pskovich_1_angry at right
    pskovich "Подождите, царь батюшка! Что это значит!"

    hide pskovich_1
    show guard_right at right

    guard "Да, царь батюшка."
    play sound shield
    void_black "*Стража выводит псковичей*"

    hide vasiliy3_angry
    show vasiliy3_serious
    hide guard_right

    vasiliy3 "Теперь нужно решить, как присоединить этот город к России. Один из вариантов - упразднить вече и снять вечевой колокол. Это будет жестким, но необходимым шагом. "
    vasiliy3 "Псков должен понять, что теперь он часть Русского государства, что у нас есть общие законы и правила. Убрав вече, мы уберем источник его самостоятельности, сделаем его более прозрачным для нашего управления."
    hide vasiliy3_serious
    show vasiliy3_serious1
    vasiliy3 "Но это может вызвать протесты, сопротивление, и я не хочу видеть братоубийство на улицах этого города."
    vasiliy3 "А второй вариант - посетить город с мирным посылом. Показать, что мы стремимся к миру и согласию. Переговоры, убеждения, демонстрация нашей силы и одновременно мудрости. "
    vasiliy3 "Псков должен понять, что он не одинок, что у нас есть общие цели и задачи. Но это может затянуться, у Пскова есть своя гордость и самоуверенность, он может не желать слушать слова мудрости."
    hide vasiliy3_serious1
    show vasiliy3
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
    play music gamemusic
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

    play music gamemusic
    scene storyteller_house with fade

    play sound two_five
    storyteller "Вы приняли историческое решение, оно увековечено в учебниках и архивах России! Сейчас я вам поведаю итог этого решения"
    stop sound
    play sound two_six
    storyteller "Псков присоединился к составу единого государства и указом великого князя Московского Василия Третьего пало вольное, шумное, свободолюбивое псковское вече — самый демократичный орган управления в средневековой Руси."
    stop sound
    play sound two_seven
    storyteller "13 января 1510 года на глазах всего псковского люда «спустиша колокол вечевой у святыя Троица», то начали собравшиеся, «на колокол смотря, плакати по своей старине и по своей воли…». "
    stop sound
    play sound two_eight
    storyteller "Как свидетельствовал современник событий, автор знаменитой «Повести о псковском взятии», не плакали только младенцы, сосущие молоко."
    stop sound
    play sound two_nine
    storyteller "Выбранное твоё решение, отразится на будущей истории, а как именно, это мы узнаем в следующей главе"
    stop sound

    jump chapter_2

    return 

label visit_cities:

    play music gamemusic
    scene storyteller_house with fade 

    play sound two_ten
    storyteller "Принятое вами решение имеет место быть, может случись оно так и  история России была другой, но это мы не узнаем."
    stop sound
    play sound two_eleven
    storyteller "Давайте вместе подумаем над тем, что же могло произойти дальше."
    stop sound
    play sound two_twelve
    storyteller "Василий Третий посетил с добрым намерениям Псков и оставил его независимость, для псковичей это было радостное событие. Но позже пошли слухи, что сам царь оставил городу власть. "
    stop sound
    play sound two_thirteen
    storyteller "Все близкие к Пскову города захотели такой же независимости, а это означает, что план по объединению Российских земель провалился. А это может очень плохо отразиться на будущем страны."
    stop sound
    play sound two_fourteen
    storyteller "Настоящая же история была такова."
    stop sound
    play sound two_fifteen
    storyteller "Псков присоединился к составу единого государства и указом великого князя Московского Василия Третьего пало вольное, шумное, свободолюбивое псковское вече — самый демократичный орган управления в средневековой Руси."
    stop sound
    play sound two_sixteen
    storyteller "13 января 1510 года на глазах всего псковского люда «спустиша колокол вечевой у святыя Троица», то начали собравшиеся, «на колокол смотря, плакати по своей старине и по своей воли…». "
    stop sound
    play sound two_seventeen
    storyteller "Как свидетельствовал современник событий, автор знаменитой «Повести о псковском взятии», не плакали только младенцы, сосущие молоко."
    stop sound

    jump chapter_2

    return

label chapter_2:

    play music gamemusic_2
    scene chapter_2 with fade
    window hide

    scene storyteller_house with fade
    play sound three_one
    storyteller "Мы с вами, дорогие друзья свободно живём, а были и другие времена."
    stop sound
    
    scene map_fedor1 with fade
    show storyteller at right
    
    play sound three_two
    storyteller "В эпоху правления царя Фёдора Иоанновича, существовали крепостные крестьяне, которые бесплатно работали на своих хозяев и были их собственностью."
    stop sound
    play sound three_three
    storyteller "На годы правления царя Фёдора Иоанновича 1584-1598 пришлось много событий, но я расскажу о введение указа об “Урочных летах”. Дело было в 1597 году стремление остановить массовую миграцию крестьян."
    stop sound
    
    scene storyteller_house with fade
    play sound three_four
    storyteller "В поисках лучшей доли многие крестьяне снимались с насиженных мест и отправлялись в другие края. Это не устраивало землевладельцев, которые лишались рабочей силы и возможности планомерно развивать свое хозяйство."
    stop sound

    scene library with fade
    show storyteller

    peasants_life "Неизвестные, измученные работой на полях крестьяне с низким уровнем жизни должны почти за бесплатно работать на своего хозяина."
    peasants_life "Летом в полях жара, осенью дождливо и приходится ещё собирать урожай, многие болеют и обесцениваются в глазах хозяина."
    peasants_life "Зимой холодно, еды не хватает, дикие звери приходят из лесов. Весной земля ещё не отогрелась для посева, но подготавливать почву нужно."

    scene pomestie with fade
    show peasant_orator

    peasant_orator "Надоело! Я не хочу больше пахать за бесплатно! Наши братья гибнут из-за работы, никто не знает, сколько нам осталось!"
    peasants_group "Да! Ты прав, долой бояр и им подобным, отныне мы власть, мы определяем свою судьбу."
    peasant_orator "Сегодня ночью, когда караульных не будет на посту мы со всеми необходимыми вещами уйдем далеко в леса."
    peasants_group "Да!"

    scene storyteller_house with fade

    play sound three_five
    storyteller "Крестьянам удалось сбежать, но куда же им пойти. Есть торговый тракт, по которому передвигаются торговцы и прочая знать, есть леса, дорога через которые трудна, но незаметна." 
    stop sound
    play sound three_six
    storyteller "Можно пойти через поля, самое видное место, но кто ещё путешествует по полям кроме крестьян."
    stop sound

    scene forest with fade
    show peasant_orator at left
    play music forest

    peasant_orator "Братья и Сёстры, нам нужно принять решение, какой же дорогой мы пойдём искать новый дом."
    
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

    play sound three_seven
    storyteller "Какое решение примут крестьяне, каждое из них может оказаться тяжёлым испытанием."
    stop sound

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
    
    play music gamemusic_2
    scene storyteller_house with fade
    
    play sound three_eight
    storyteller "Крестьяне приняли решение идти по полям днём и ночью по торговому тракту."
    stop sound
    play sound three_nine
    storyteller "Дорога лёгкая, только от палящего солнца днём не спрятаться, а ночью сил идти уже нет. Кажется путь крестьян затянется."
    stop sound

    scene forest_with_fire with fade
    show peasant_craftsman at right
    play music forest
    play sound fire

    peasant_craftsman "Я не привык к таким долгим и изнуряющим походам, давайте сделаем ночной привал до утра, а потом дальше отправимся в путь."

    play sound three_ten
    storyteller "Все приняли это решение, потому что каждый крестьянин был изнурён дорогой, но только они развели костёр и приготовились к отдыху."
    stop sound

    scene forest_night with fade
    show guard at left

    guards "Кажется там в поле горит костёр, давай проверим кто это."
    guard "Разбойников тут быть не должно, не так уж и далеко мы отошли от города, наверное бежавшие крестьяне разбили свой лагерь."
    guard "Тушите факела, нужно подойти незамеченными и схватить каждого крестьянина."

    hide guard
    play sound three_eleven
    storyteller "Крестьяне от усталости потеряли бдительность, многие уже уснули, а оставшиеся сидели у костра в полусонном состоянии."
    stop sound

    scene forest_night with fade
    show guard at left

    guard "Окружаем лагерь и стрмительно наступаем, при оказанном сопротивлении можно калечить, но не убивать."

    scene forest_with_fire with fade
    show peasant_plowman at right
    play sound armor_clink

    peasant_plowman "Я слышу топот и звон доспех, СТРАЖА! Всем проснуться и бежать!"

    stop sound
    scene storyteller_house with fade
    play music gamemusic_2

    play sound three_twelve
    storyteller "Как бы крестьяне не старались им не справиться с подготовленными людьми в сражении. Бегством никому спастись не удалось."
    stop sound
    play sound three_thirteen
    storyteller "В эту ночь удача обошла крестьян стороной и все они были возвращены обратно."
    stop sound
    play sound three_fourteen
    storyteller "Позже 24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    stop sound
    play sound three_fifteen
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."
    stop sound
    play sound three_sixteen
    storyteller "Но нашим крестьянам так и не удалось сбежать повторно, а может удача просто отвернулась от них."
    stop sound

    jump chapter_3
    return

label go_forest:

    play music gamemusic_2
    scene storyteller_house with fade

    play sound three_seventeen
    storyteller "Крестьяне приняли решение пойти через лес."
    stop sound
    play sound three_eighteen
    storyteller "Тяжёлая дорога ждала крестьян, пробираться с вещами и едой трудно, много сил уходит на передвижение. Но несмотря на это крестьяне идут на встречу к свободе."
    stop sound

    scene forest_with_wheat with fade
    show peasant_cattleman at right
    play music forest

    peasant_cattleman "Нам нужен отдых, животные устали идти по лесу, им нужна вода."

    show peasant_orator at left

    peasant_orator "До реки ещё далеко, но мы сможем отдохнуть как только солнце опустится за горизонт."
    peasant_cattleman "Мне страшно, что дикие звери и тёмные духи нападут на нас."
    peasant_orator "Будем по очереди охранять животных ночью."

    scene storyteller_house with fade

    play sound three_nineteen
    storyteller "Крестьяне всё таки нашли маленький ручей в лесу и решили обосновать свой лагерь."
    stop sound

    scene field_night with fade
    show peasant_baker 

    peasant_baker "Еду будем экономить, поэтому каждому достанется по куску хлеба и одной тарелке овощного супа."

    scene storyteller_house with fade

    play sound three_twenty
    storyteller "Крестьяне остались на ночь в лесу. И после полнолуния, появились странные звуки."
    stop sound

    scene field_night with fade
    show peasant_fisher

    peasant_duty "Слишком тихо сегодня ночью, нет не единого звука."
    play sound grass_sound
    void_black "*Шелест*"
    peasant_duty "Что это было, неужели невесть какая или звери."
    stop sound
    play sound wolf_howl
    void_black "*Затяжной вой*"
    peasant_duty "Неужели волки! Подъём крестьяне! Звери рядом!"
    stop sound
    play sound three_twentyone
    storyteller "Сильный шум крестьян отпугнул волков, шагов зверей и шелеста травы никто не слышал, но длинный и голодный вой, говорил о том, что волки ещё вернутся."
    stop sound
    
    scene forest_with_wheat with fade

    void_black "*Уже утром*"
    
    show peasant_orator

    peasant_orator "Друзья мои, нужно отправляться в путь, смотрите внимательно по сторонам и если увидите протоптанные тропинки, то не молчите. Нужно избегать волчьих троп, дать отпор при неожиданной встрече мы не сможем."
    
    scene storyteller_house with fade

    play sound three_twentytwo
    storyteller "Крестьяне устало шли по лесу, озираясь по сторонам, сколько ещё бессонных ночей их ждёт."
    stop sound

    scene forest1 with fade
    show peasant_cattleman at right

    peasant_cattleman "Уже много ночей прошло, скотина исхудала, нужно где-то остановиться на долгое время."

    show peasant_orator at left

    peasant_orator "Как только мы дойдём до хорошего места у реки, мы примемся обустраиваться."

    scene storyteller_house with fade
    play music gamemusic_2
    play sound three_twentythree
    storyteller "Нашим крестьянам удалось найти ответвление от большого русла реки. Казалось бы, в непроходимом лесу, рядом с маленькой речкой."
    stop sound

    scene slavery with fade

    play sound three_twentyfour
    storyteller "Деревня росла и развивалась, но это было не долго. Крестьянам не удалось прожить долгую и счастливую жизнь, в один день всё изменилось и деревню обнаружили казаки, которые передвигались по берегу реки."
    stop sound
    play sound three_twentyfive
    storyteller "24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    stop sound
    play sound three_twentysix
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."
    stop sound

    scene storyteller_house with fade

    play sound three_twentyseven
    storyteller "Деревня была сожжена, а крестьян вернули владельцу."
    stop sound

    jump chapter_3
    return

label go_riverside:

    play music gamemusic_2
    scene storyteller_house with fade

    play sound three_twentyseven_one
    storyteller "Крестьяне приняли решение пойти вдоль реки."
    stop sound
    play sound three_twentyeight
    storyteller "Дорога предстояла тяжёлая, реки места духовные, много разных историй о тёмных духах было. Но есть и плюс, жажда не замучает и скотина будет бодрая."
    stop sound

    scene field_with_river with fade
    show peasant_fisher at left
    play music river

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

    stop music
    scene storyteller_house with fade

    play sound three_twentynine
    storyteller "Дорога предстояла длинная, много разных историй есть с реками и все они страшные. Но есть кое-что страшнее духов и нечистой силы, это человек."
    stop sound

    play music river
    scene field_with_river1 with fade
    show peasant_orator at left

    peasant_orator "Мы идём уже 5 ночей вдоль реки, предлагаю сегодня остановиться и хорошенько отдохнуть."

    show peasant_cattleman at right

    peasant_cattleman "Я согласен, скотина устала, отдых нужен."

    show peasant_fisher 

    peasant_fisher "Давайте разобьём лагерь, а я пройду дальше и в сильном течении покидаю сети."
    peasant_orator "Решено, разбиваем лагерь и готовимся к отдыху."
    hide peasant_fisher

    play sound three_thirty
    storyteller "Рыбак ушёл ловить сетями, но кто же знал, что сильное течение привлекает не только его одного."
    stop sound

    scene field_with_river_night with fade
    show peasant_plowman at left
    play music crickets

    peasant_plowman "Что-то долго нет рыбака нашего."

    show peasant_cattleman at right

    peasant_cattleman "Наверное рыбы наловил и унести всё не может."
    peasant_plowman "Давайте пождём до заката, а потом сходим его проведать."

    scene storyteller_house with fade

    play sound three_thirtyone
    storyteller "Рыбак так и не вернулся, а фермер вместе со скотоводом пошли его искать."
    stop sound

    scene field_with_river_night with fade
    show peasant_plowman at left
    play sound river

    peasant_plowman "Ты это слышишь?"

    show peasant_cattleman at right

    peasant_cattleman "Что?"
    peasant_plowman "Шум воды, кажется мы уже близко."
    stop sound
    play sound laugh
    void_black "*Жуткий смех*"
    stop sound
    peasant_cattleman "Кто здесь?"
    play sound grass_sound
    void_black "*Шелест*"
    stop sound
    peasant_plowman "Кажется я слышу голос."
    unknown_character "Хороший раб нам попался, крепкий, не больной, рыбачить умеет, его мы за дорого продадим."
    peasant_cattleman "Кто это может быть?"
    play sound grass_sound
    void_black "*Шаги сзади*"
    peasant_plowman "Кто тут?"
    stop sound
    play sound people_scream
    void_black "*Крики издалека*"
    peasant_cattleman "По реке хорошо приносится звук, кажется что-то случилось в лагере."
    stop sound

    play music gamemusic_2
    scene storyteller_house with fade

    play sound three_thirtytwo
    storyteller "Не успели добраться до лагеря наши друзья, их схватили разбойники, как и рыбака, как и весь лагерь. Кого-то сразу убили, женщин забрали себе, а самых крепких вернули хозяину."
    stop sound
    play sound three_thirtythree
    storyteller "Совсем скоро вышел указ."
    stop sound
    play sound three_thirtyfour
    storyteller "24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    stop sound
    play sound three_thirtyfive
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."
    stop sound

    jump chapter_3
    return

label go_traderoute:

    play music gamemusic_2
    scene traderoute with fade
    show storyteller

    play sound three_thirtysix
    storyteller "Крестьяне приняли решение идти только по торговому тракту."
    stop sound
    play sound three_thirtyseven
    storyteller "Самый лёгкий путь для крестьян, но самый опасный, потому что на встречу могут попасться бояре, казаки, торговцы и у каждого будут вопросы к крестьянам."
    stop sound

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

    play sound three_thirtyeight
    storyteller "Прошло 7 ночей, а крестьяне не видели беды. Дорога была лёгкая, все успели расслабится. Это было фатальной ошибкой."
    stop sound

    scene pathway with fade
    show peasant_orator at left
    play music birds

    peasant_orator "Сегодня можно отдохнуть, 7 ночей прошло, а погони нет. Думаю теперь будет всё в порядке."

    show peasant_craftsman at right

    peasant_craftsman "Я буду сторожить полночи, а потом с кем нибудь поменяюсь."

    hide peasant_orator
    show peasant_plowman at left

    peasant_plowman "Можешь смело меня разбудить, сил полно и я готов подменить тебя."

    scene storyteller_house with fade

    play sound three_thirtynine
    storyteller "Именно так и началась ночь, которая снова определит судьбу крестьян."
    stop sound

    scene forest_night1 with fade
    show peasant_craftsman at right
    play music forest
    play sound hoov_sound

    peasant_craftsman "Кажется я слышу топот, хотя может быть я уже устал."
    peasant_craftsman "Вставай, вставай!"

    show peasant_plowman at left

    peasant_plowman "Что случилось?"
    peasant_craftsman "Ты слышишь топот копыт?"
    peasant_plowman "Тебе кажется, зачем ты меня так рано разбудил."
    peasant_craftsman "Я пойду посмотрю, а ты не засыпай, кажется нас преследуют."

    scene storyteller_house with fade

    play sound three_fourty
    storyteller "Крестьянин ремесленник вышел за пределы лагеря и увидел приближающиеся огоньки, кажется на поиски беглых крестьян отправили людей на лошадях."
    stop sound

    scene forest_night1 with fade
    show peasant_craftsman

    play sound hoov_sound_1
    peasant_craftsman "Вставайте братцы, за нами погоня, на конях приближаются!"
    stop sound

    scene storyteller_house with fade
    play music gamemusic_2
    play sound three_fourtyone
    storyteller "В созданной суматохе крестьяне не смогли сбежать и всех поймали и вернули хозяину."
    stop sound
    play sound three_fourteen
    storyteller "Позже 24 ноября 1597 г. вышел Указ царя Фёдора Иоанновича об «урочных летах», которым впервые устанавливался пятилетний срок сыска и возвращения владельцам беглых крестьян."
    stop sound
    play sound three_thirtyfive
    storyteller "Согласно Указу крестьяне, бежавшие от своих хозяев «до нынешнего... году за пять лет» подлежали сыску, суду и возвращению назад."
    stop sound

    jump chapter_3
    return

label final:

    scene sky with fade

    menu:
        "Выйти в главное меню":
            return

    return

label chapter_3:

    play music gamemusic_3
    scene chapter_3 with fade
    window hide

    scene storyteller_house with fade
    
    play sound four_one
    storyteller "Было и очень сложное время для Руси, время смуты и неразберихи.  А началось оно после внезапной кончины Бориса Годунова. На трон взошел 16-летний Фёдор, сын Бориса, и управлять огромной страной в столь юном возрасте ему было нелегко."
    stop sound
    play sound four_two
    storyteller "Но уже на третьей неделе правления Фёдор понял, что может рассчитывать только на верность нескольких бояр и благоразумие москвичей."
    stop sound
    play sound four_three
    storyteller "Измена войска решила судьбу молодого царя. Фёдор и его семья были арестованы, а через несколько дней и вовсе убиты."
    stop sound
    play sound four_four
    storyteller "Так, 20 июня 1605 года москвичи с восторгом встречали торжественно въезжающего в город царя. И вот что он предпринял получив власть…"
    stop sound
    
    scene tsar_room with fade
    show false_dmitry1

    dmitri_ivanovich "Наконец-то я в Москве! Всё выглядит так, как я и надеялся. Народ ликует, бояре склоняются передо мной. Теперь самое важное — удержать власть."
    dmitri_ivanovich "Легко было взять трон с помощью польских войск, но удержать его будет сложнее. Мне нужно склонить к себе Боярскую думу."
    dmitri_ivanovich "Эти старые лисы смотрят на меня с подозрением. И это беспокоит меня. Ведь я не Дмитрий, хотя это знает только горстка людей, и эти люди не здесь."
    dmitri_ivanovich "Моя манера, моё поведение, всё это выдаёт во мне чужака. Но я должен доказать им, что могу быть полезен, что под моим правлением они не потеряют свои привилегии и богатства."
    dmitri_ivanovich "Для этого мне необходимо укрепить свою власть, окружить себя верными людьми. И постепенно убрать старых бояр."
    dmitri_ivanovich "Также необходимо склонить на свою сторону духовенство. Церковь имеет огромное влияние на народ, и, если мне удастся заручиться поддержкой патриарха, это поможет укрепит моё положение."
    dmitri_ivanovich "Возможно, стоит щедро одарить монастыри, восстановить несколько разрушенных храмов. Пусть видят во мне не только правителя, но и благодетеля церкви."
    dmitri_ivanovich "Я также обязан полякам. Им я обещал передать Смоленскую и Чернигово-Северскую земли. Именно их поддержка привела меня к власти."
    dmitri_ivanovich "Тайно приняв католичество, я заручился поддержкой Католической церкви и пообещал им, что после восшествия на престол введу католичество на русских землях." 
    dmitri_ivanovich "Это опасное обещание, но оно помогло мне заручиться мощной поддержкой, без которой я не стал бы царём."
    dmitri_ivanovich "И, конечно, нельзя забывать о простом народе. Им нужны хлеб и зрелища. Снижение налогов, праздники, помощь в трудные времена — это то, что заставит их полюбить меня."
    dmitri_ivanovich "Да, я не Дмитрий, но я могу стать тем, кого они примут как своего царя. Главное — действовать быстро и решительно, не позволив врагам объединиться против меня."
    
    scene tsar_room with fade
    show false_dmitry1 at left
    show clerk at right
    play sound door_knock

    clerk "Вызывали царь батюшка?"
    dmitri_ivanovich "Писарь, готовь новый указ. Сегодня мы объявим о возвращении ко двору Романовых и других бояр, ранее отстранённых от власти."
    clerk "Да, государь. С кого начнем?"
    dmitri_ivanovich "Начнем с Фёдора Романова. Я хочу назначить его патриархом Ростовским."

    scene filaret with fade

    play sound four_five
    storyteller "Фёдор Романов, более известный как Филарет, был важной фигурой в истории России. Родился в 1553 году в семье знатного боярина Никиты Романова, он стал видным представителем рода Романовых."
    stop sound
    play sound four_six
    storyteller "После воцарения Годунова Фёдор и его семья впали в немилость. В 1600 году Фёдор Романов был пострижен в монахи под именем Филарет и сослан в Антониев-Сийский монастырь."
    stop sound

    scene tsar_room with fade
    show clerk at right

    clerk "Патриархом Ростовским... понял. Но разве Фёдор Романов не был раньше в опале?"

    scene library with fade
    show storyteller

    play sound four_seven
    storyteller "Опала - гнев, немилость царя к провинившемуся боярину, а также наказание, налагавшееся на такого боярина."
    stop sound

    scene tsar_room with fade
    show false_dmitry1 at left
    show clerk at right

    dmitri_ivanovich "Был, но времена меняются. Его опыт и влияние сейчас нужны нам."
    clerk "Записал. Что делать с нынешним патриархом Московским и всея Руси, Иовом?"
    dmitri_ivanovich "Иов был верным сторонником Годунова. Его нужно отправить под арест в отдалённый монастырь."
    clerk "Отправить под арест... в отдалённый монастырь. А кто займёт его место?"
    dmitri_ivanovich "Патриархом Московским и всея Руси будет мой ставленник — рязанский архиепископ Игнатий. Он грек по происхождению, и я уверен в его лояльности."
    clerk "Рязанский архиепископ Игнатий, понято."
    dmitri_ivanovich "Это всё! Пусть все видят, что новый царь приносит перемены и справедливость. Пусть почувствуют, что под моим правлением будет порядок."
    clerk "Будет исполнено, государь!"

    scene library with fade
    show storyteller

    play sound four_eight
    storyteller "С этого и началось правление Лжедмитрия. Он, казалось, достиг вершины власти, но впереди его ждали тяжелые испытания. 8 мая 1606 года Лжедмитрий обвенчался с Мариной Мнишек."
    stop sound

    scene mariya_mnishek with fade

    play sound four_nine
    storyteller "Марина Мнишек (1588–1614) была дочерью польского магната Юрия Мнишека, воеводы сандомирского, и одной из ключевых фигур в Смутное время в России."
    stop sound
    play sound four_ten
    storyteller "Это венчание произошло в пятницу и на Николин день, что противоречило уставу православной церкви. Это вызвало недовольство среди верующих, но Лжедмитрий был уверен, что его положение устойчиво."
    stop sound

    scene library with fade
    show storyteller

    play sound four_eleven
    storyteller "Однако Лжедмитрий не оправдал ни надежд Польши, ни собственного народа. Он оказался между двух огней: взяв обязательства перед поляками, он должен был их выполнить, но понимал, что это вызовет недовольство в России."
    stop sound
    play sound four_twelve
    storyteller "Поэтому Лжедмитрий не торопился ни отдавать русские территории Речи Посполитой, ни вводить в стране католичество. Вместо обещанных земель полякам он предложил денежный выкуп."
    stop sound
    play sound four_thirteen
    storyteller "Лжедмитрий потерял поддержку поляков."
    stop sound
    play sound four_fourteen
    storyteller "В это же время и у бояр начали появляться сомнения в подлинности царя. Его поведение сильно отличалось от поведения прошлых государей. Лжедмитрий не следовал многим традициям, вел себя слишком свободно и раскованно для русского царя."
    stop sound
    play sound four_fifteen
    storyteller "Начали распространяться слухи о его самозванстве. Узнав, что у Лжедмитрия больше нет поддержки польских союзников, бояре решили, что настало время действовать." 
    stop sound
    play sound four_fifteen_one
    storyteller "Они объединились и начали организовывать заговор против самозванца, стремясь вернуть себе власть и избавить страну от чужака, который, по их мнению, не имел права на престол."
    stop sound
    play sound four_sixteen
    storyteller "Так, правление Лжедмитрия быстро оказалось под угрозой. Боярский заговор становился всё более реальным, и судьба Лжедмитрия висела на волоске."
    stop sound

    scene boyar_room with fade
    show false_dmitry1 at left

    dmitri_ivanovich "Доброе утро, бояре. Что нового на нашей территории?"

    show boyar1 at right

    boyar "Государь, у нас возникли новые проблемы на юге. Казаки снова начали выходить из-под контроля, они отказываются платить налоги и начали грабить наши земли."
    dmitri_ivanovich "Это неприемлемо! Необходимо принять меры для восстановления порядка в этом регионе. Подготовить войска и отправить командиров для подавления восстания!"
    boyar "Будет исполнено, государь!"
    boyar "Ваше Величество, есть еще важная новость. Ходят слухи о готовящемся заговоре против вас."
    dmitri_ivanovich "Заговор?"

    menu:
        "Не позволю! Отыскать и схватить заговорщиков!":
            jump find_conspirators
        "Коль каждому слуху верить, голов в стране не останется.":
            jump leave_alone

    return
    

label find_conspirators:

    scene boyar_room with fade
    show boyar1 at right

    boyar "Сделаем, государь!"

    scene storyteller_house with fade

    play sound four_seventeen
    storyteller "Прошло время и заговорщиков удалось найти…"
    stop sound

    scene tsar_room with fade
    show boyar1 at right

    boyar "Государь, нам удалось выявить заговорщиков. Это Шуйские. Они являются инициаторами заговора."

    show false_dmitry1 at left

    dmitri_ivanovich "Шуйские? Велите привести не ладных!"
    boyar "Слушаюсь, царь батюшка."

    scene shyiskiy with fade

    play sound four_eighteen
    storyteller "Василий Иванович Шуйский (1552–1612) был представителем древнего боярского рода Шуйских, происходившего от суздальских князей. Занимал видное место при дворе и был одним из ведущих оппозиционеров Бориса Годунова."
    stop sound

    scene tsar_room with fade
    show false_dmitry1 at left
    show vasiliy_shyiskiy at right

    dmitri_ivanovich "Василий Шуйский, ты обвинён в заговоре против своего царя. Что ты скажешь в свою защиту?"
    vasiliy_shuisky "Ваше Величество, я верен России и народу. Если кто-то из бояр и подумывал о заговоре, я тут ни при чём. Это клевета!"
    dmitri_ivanovich "Клевета или правда, но ты отвечаешь за своих людей, Василий. Суд решит твою судьбу. Быть суду!"

    scene court with fade
    window hide
    scene tsar_room with fade
    show false_dmitry1 at left
    show boyar2 at right
    boyar_1 "Государь, суд приговорил Василия Шуйского к казни за измену и заговор против царя."
    hide boyar2
    show boyar3 at right
    boyar_2 "Царь батюшка, прежде чем приговор будет приведён в исполнение, я прошу вас выслушать нас. Мы собрались здесь, чтобы просить о помиловании для Василия Шуйского."
    boyar_2 "Несмотря на все его проступки, Василий Шуйский остаётся важной фигурой среди бояр. Его помилование может укрепить вашу репутацию и восстановить мир среди знати."
    hide boyar3
    show mariya_nagaya at right
    mariya_nagaya "Ваше Величество, я прошу вас проявить милосердие."
    mariya_nagaya "Помните, что великие правители часто проявляли снисходительность к своим врагам, показывая тем самым свою мудрость и великодушие. В конце концов, Василий Шуйский может ещё сослужить вам службу."
    show storyteller
    play sound four_nineteen
    storyteller "Мария Нагая (около 1553 – после 1608) была последней женой Ивана IV Грозного и матерью царевича Дмитрия Ивановича. Происходила из знатного, но не очень влиятельного рода Нагих." 
    stop sound
    play sound four_nineteen_one
    storyteller "Мария стала женой Ивана Грозного в 1581 году, а через год родила ему сына Дмитрия."
    stop sound
    play sound four_twenty
    storyteller "После смерти Бориса Годунова и прихода к власти Лжедмитрия I Мария Нагая признала в нём своего сына, что способствовало укреплению его легитимности."
    stop sound
    hide storyteller
    dmitri_ivanovich "Вы говорите разумно. Однако, я должен обдумать все последствия. Если я помилую Шуйского, это может укрепить мой авторитет среди бояр. Но если он снова предаст меня..."
    dmitri_ivanovich "Ладно, дайте мне время на размышления. Я приму решение завтра."
    hide mariya_nagaya
    show boyar3 at right
    boyar_2 "Благодарим вас, государь. Мы надеемся, что ваше решение будет мудрым и справедливым."
    hide boyar3
    show mariya_nagaya at right
    mariya_nagaya "Спасибо, Ваше Величество. Мы верим в ваше великодушие и мудрость."
    dmitri_ivanovich "На этом совещание окончено!"

    scene lonly_dmitry with fade
    window hide

    scene tsar_room with fade
    show false_dmitry1
    dmitri_ivanovich "Сложный выбор... Помиловать и рискнуть снова быть преданным, или казнить и навсегда избавиться от угрозы? Какую бы дорогу я ни выбрал, последствия будут значительными."

    menu:
        "Помиловать!":
            jump pardon
        "Казнить!":
            jump execute

    return

label pardon:

    scene storyteller_house with fade
    play sound four_twentyone
    storyteller "Василий Шуйский помилован! Но близкая смерть не отпугнула его, и он готовит новый заговор!"
    stop sound
    
    scene tsar_room with fade
    show false_dmitry1 at left
    show boyar1 at right
    boyar "Государь, слухи доходят, что поляки к нападению готовятся. Нам нужно усилить защиту!"
    dmitri_ivanovich "Все войска привести в боевую готовность!"
    scene sumatoha with fade
    window hide
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show vasiliy_shyiskiy at right
    play music furious_music
    play sound door_broken
    dmitri_ivanovich "Что здесь происходит? Шуйский, ты осмелился прийти ко мне с оружием?"
    vasiliy_shuisky "Время твое, самозванец, вышло. Мы решили положить конец твоему правлению."

    menu:
        "Попытаться сбежать!":
            jump try_to_escape
        "Договориться с заговорщиками!":
            jump negotiate_with_conspirators

    return

label try_to_escape:

    play music furious_music
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show vasiliy_shyiskiy at right
    lshgedmitri "Нет, вы не возьмёте меня так просто!"
    vasiliy_shuisky "Он пытается бежать! Хватайте его!"

    scene last_minutes with fade
    play sound glass
    play music gamemusic_3
    play sound four_twentytwo
    storyteller "При падении наш самозванец сломал ногу и сбежать у него не получилось. Убили Лжедмитрия!"
    stop sound

    scene death_dmitriy with fade
    play sound four_twentythree
    storyteller "Изуродованный труп самозванца оставили на Лобном месте, привели Нагую, у которой в очередной раз спросили — ее это сын или нет. Она мастерски вывернулась, сказав:"
    stop sound

    show mariya_nagaya at right

    mariya_nagaya "Теперь, какой есть, - конечно не мой."

    scene storyteller_house with fade

    play sound four_twentyfour
    storyteller "Тело Лжедмитрия сожгли, прах забили в пушку и выстрелили в сторону Польши. А Марина Мнишек бежала из Москвы."
    stop sound

    jump final

    return

label negotiate_with_conspirators:

    play music furious_music
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show vasiliy_shyiskiy at right

    lshgedmitri "Шуйский, подумай! Я могу предложить тебе богатства, земли, власть! Только не убивай меня!"
    vasiliy_shuisky "Не может быть никаких переговоров, самозванец. Ты обманул всех нас и незаконно захватил власть!"
    lshgedmitri "Подумай о будущем, Шуйский! Я могу быть полезен тебе! Вместе мы можем править этой страной!"
    vasiliy_shuisky "Слишком поздно. Твои дни сочтены!"

    scene last_minutes with fade
    play music gamemusic_3
    play sound four_twentyfive
    storyteller "Лжедмитрий убит!"
    stop sound
    play sound four_twentysix
    storyteller "На самом же деле самозванец из окна прыгал, но не спасло его и это от смерти."
    stop sound

    scene death_dmitriy with fade

    play sound four_twentyseven
    storyteller "Изуродованный труп самозванца оставили на Лобном месте, привели Нагую, у которой в очередной раз спросили — ее это сын или нет. Она мастерски вывернулась, сказав:"
    stop sound

    show mariya_nagaya at right

    mariya_nagaya "Теперь, какой есть, - конечно не мой."

    scene storyteller_house with fade

    play sound four_twentyeight
    storyteller "Тело Лжедмитрия сожгли, прах забили в пушку и выстрелили в сторону Польши. А Марина Мнишек бежала из Москвы."
    stop sound

    jump final

    return

label execute:

    play music gamemusic_3
    scene storyteller_house with fade

    play sound four_twentynine
    storyteller "Василий Шуйский казнён, но бояре всё также не могут принять лжецаря. Готовится второй заговор!"
    stop sound

    scene tsar_room with fade
    show false_dmitry1 at left
    show boyar1 at right
    play music furious_music

    boyar "Государь, слухи доходят, что поляки к нападению готовятся. Нам нужно усилить защиту!"
    dmitri_ivanovich "Все войска привести в боевую готовность!"

    scene sumatoha with fade
    window hide
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show consperator at right
    play sound door_broken

    dmitri_ivanovich "Что здесь происходит? Как вы смеете прийти ко мне с оружием!"
    conspirator "Время твое, самозванец, вышло. Мы решили положить конец твоему правлению."

    menu:
        "Попытаться сбежать!":
            jump try_to_escape_2
        "Договориться с заговорщиками!":
            jump negotiate_with_conspirators_2

    return

label try_to_escape_2:

    play music furious_music
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show consperator at right
    lshgedmitri "Нет, вы не возьмёте меня так просто!"
    conspirator "Он пытается бежать! Хватайте его!"

    scene last_minutes with fade
    play sound glass
    play music gamemusic_3
    play sound four_thirty
    storyteller "При падении наш самозванец сломал ногу и сбежать у него не получилось. Убили Лжедмитрия!"
    stop sound

    scene death_dmitriy with fade
    play sound four_thirtyone
    storyteller "Изуродованный труп самозванца оставили на Лобном месте, привели Нагую, у которой в очередной раз спросили — ее это сын или нет. Она мастерски вывернулась, сказав:"
    stop sound

    show mariya_nagaya at right

    mariya_nagaya "Теперь, какой есть, - конечно не мой."

    scene storyteller_house with fade

    play sound four_thirtytwo
    storyteller "Тело Лжедмитрия сожгли, прах забили в пушку и выстрелили в сторону Польши. А Марина Мнишек бежала из Москвы."
    stop sound
    play sound four_thirtythree
    storyteller "Только вот в истории сделал это всё помилованный Лжедмитрием Василий Шуйский."
    stop sound

    jump final

    return

label negotiate_with_conspirators_2:

    play music furious_music
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show consperator at right
    play sound door_broken

    lshgedmitri "Подождите! Давайте поговорим. Я могу предложить вам богатства, земли, власть! Только не убивайте меня!"
    conspirator "Мы пришли за твоей головой, а не за подарками, самозванец."
    lshgedmitri "Подумайте о будущем! Я могу быть полезен вам! Вместе мы можем править этой страной!"
    conspirator "*Хмммм* Возможно, ты прав. Может, стоит дать тебе шанс. Но ты подпишешь договор с нами!"

    play music gamemusic_3
    scene dogovor with fade
    window hide
    scene tsar_bedroom with fade

    lshgedmitri "Теперь мы можем работать вместе!"
    conspirator "Ладно, мы уходим. Надеюсь, ты сдержишь своё слово."

    play music furious_music
    scene ne_dogovor with fade
    window hide
    scene tsar_bedroom with fade
    show false_dmitry1 

    lshgedmitri "Стража! Схватить их и казнить немедленно!"

    scene last_minutes with fade

    play music gamemusic_3
    play sound four_thirtyfour
    storyteller "И кто знает, что было бы дальше, случись всё это на самом деле. Сейчас мы можем только догадываться."
    stop sound
    play sound four_thirtyfive
    storyteller "На самом же деле, Лжедмитрий помиловал Шуйского, но тот организовал второй заговор. Убили Лжедмитрия!"
    stop sound

    scene death_dmitriy with fade

    play sound four_thirtysix
    storyteller "Изуродованный труп самозванца оставили на Лобном месте, привели Нагую, у которой в очередной раз спросили — ее это сын или нет. Она мастерски вывернулась, сказав:"
    stop sound

    scene death_dmitriy with fade
    show mariya_nagaya at right

    mariya_nagaya "Теперь, какой есть, - конечно не мой."

    scene storyteller_house with fade

    play sound four_thirtyseven
    storyteller "Тело Лжедмитрия сожгли, прах забили в пушку и выстрелили в сторону Польши. А Марина Мнишек бежала из Москвы."
    stop sound
    play sound four_thirtyeight
    storyteller "Только вот в истории сделал это всё помилованный Лжедмитрием Василий Шуйский."
    stop sound

    jump final

    return


label leave_alone:
    
    scene boyar_room with fade
    show boyar1 at right
    show false_dmitry1 at left
    boyar "Как скажите, государь."

    scene opana with fade
    window hide
    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show vasiliy_shyiskiy at right
    play music furious_music
    play sound door_broken

    lshgedmitri "Что здесь происходит? Кто посмел войти ко мне без разрешения?"
    vasiliy_shuisky "Твоё время вышло, самозванец. Мы пришли положить конец твоей лжи и узурпации."

    scene shyiskiy with fade

    play sound four_thirtynine
    storyteller "Василий Иванович Шуйский (1552–1612) был представителем древнего боярского рода Шуйских, происходившего от суздальских князей. Занимал видное место при дворе и был одним из ведущих оппозиционеров Бориса Годунова."
    stop sound

    scene tsar_bedroom with fade
    show false_dmitry1 at left
    show vasiliy_shyiskiy at right

    lshgedmitri "Шуйский, ты смеешь явиться ко мне с обвинениями? Помни, я царь всея Руси!"
    vasiliy_shuisky "Ты никогда не был и не будешь настоящим царём. Ты обманул всех нас, взяв власть незаконно. Это конец, самозванец"
    lshgedmitri "Шуйский, я могу быть полезен тебе! Вместе мы можем править этой страной!"
    vasiliy_shuisky "Хватит слов. Твоё время вышло!"
    stop music
    scene last_minutes with fade
    play music gamemusic_3
    play sound four_fourty
    storyteller "Этот исход близок к истине, но всё было иначе. На самом деле самозванец пожил немного дольше."
    stop sound
    play sound four_fourtyone
    storyteller "Он поверил слухам и поймал Шуйского, но поддавшись убеждениям, простил заговорщика, за что позже и поплатился! Убили Лжедмитрия!"
    stop sound

    scene death_dmitriy with fade

    play sound four_fourtytwo
    storyteller "Изуродованный труп самозванца оставили на Лобном месте, привели Нагую, у которой в очередной раз спросили — ее это сын или нет. Она мастерски вывернулась, сказав:"
    stop sound

    scene death_dmitriy with fade
    show mariya_nagaya at right

    mariya_nagaya "Теперь, какой есть, - конечно не мой."

    scene storyteller_house with fade

    play sound four_fourtythree
    storyteller "Тело Лжедмитрия сожгли, прах забили в пушку и выстрелили в сторону Польши. А Марина Мнишек бежала из Москвы."
    stop sound

    jump final

    return


