# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define gg = Character("[player_name]", color="#FF0000")
define iw = Character('Интервьюер', color="#FFFFFF")
define boss = Character('Начальник', color="#FFFFFF")
define wife =  Character('Жена', color="#FFFFFF")
label splashscreen:
    $ renpy.movie_cutscene('videos/1234.webm')
    return

screen map:
    modal True
    zorder 100
    fixed:
        xsize 1920 ysize 1080
        add "images/wow.jpg" align (.5,.5)
    fixed:
        xsize 1920 ysize 1080
        text "[player_name]" at transform:
            xpos 430 ypos 250

label start:
    scene bg laptop_screen
    $ player_name =  renpy.input(("Введите имя персонажа"), default="Alex")
    iw"Итак, вы волнуетесь?"
    gg"У-м-м... да. Я просто немного нервничаю..."
    iw"Не волнуйтесь! На собеседованиях нервничают все – даже профессионалы."
    iw"Давайте теперь взглянем на ваше резюме"
    show screen map
    iw"Приятно познакомиться, имя игрока! Я так понимаю вы хотите стать киберкриминалистом?"
    scene bg laptop_screen
    gg"Да, так оно и есть"
    iw"Ну тогда мы начинаем как только вы будете готовы"
    menu:
        "Приступить к игре":
            pass

    $ timeout = 3.0
    $ timeout_label = "start_interview_question2"
    menu:
        "Что такое генератор в python?"
        "не знаю":
            pass
        "...":
            pass
        "хз":
            pass
label start_interview_question2:
    play sound "audio/sfx/punch.wav"
    $ timeout_label = "start_interview_question3"
    "Следующий вопрос.."
    iw"Как вы относитесь к API?"
    menu:
        iw"Как вы относитесь к API?"

        "Не знаю":
            pass
        "...":
            pass
        "хз":
            pass

label start_interview_question3:
    play sound 'audio/sfx/punch.wav'
    $ timeout_label = "start_after_interview"
    "Третий вопрос"
    menu:
        iw"Что такое форензика?"
        "Не знаю":
            pass
        "...":
            pass
        "хз":
            pass

label start_after_interview:
    $ timeout_label = None
    play sound 'audio/sfx/punch.wav'
    iw"Спасибо, что нашли время пройти наше собеседование" 
    iw"Прежде чем уйти, пожалуйста, уделите некоторое время заполнению основной информации, чтобы мы могли лучше узнать вас."
    menu:
        "откуда вы узнали о нас?"
        "От":
            pass
        "почта":
            pass
        "123":
            pass
    menu:
        "Хотите подписаться на нашу рассылку?"
        "Да":
            "Так держать! Мы будем уведомлять вас обо всех событиях и возможностях."
        "Нет":
            iw"Ну и пожалуйста"
    iw"И это будет все! Большое спасибо, что пришли, имя игрока"
    gg"Н-нет, спасибо, я ценю ваше время."
    iw"Мы вам перезвоним."
    gg"(Удивительно, как мне вообще удалось это пройти)"
    gg"(Честно говоря, не так давно я был абсолютным новичком. И посмотрите, где я сейчас!)"
    gg"(Такое ощущение, что я будто вчера только узнал, что такое форензика)"
    scene bg living_room
    return