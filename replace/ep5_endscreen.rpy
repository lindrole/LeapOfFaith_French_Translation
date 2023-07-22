$ credits_show = True

screen ep5_endscreen:

    if steambuild:
        $ ach_liarliar += 1
        if ach_liarliar == 0:
            if steambuild:
                if not achievement.has("INEVERLIE"):
                    $ achievement.grant("INEVERLIE")
#                    init:
#                        $ achievement.register("INEVERLIE")
#                        $ achievement.sync()
                    $ achievement.sync()
        if ach_nuke_it:
            if not achievement.has("NUKE_IT"):
                $ achievement.grant("NUKE_IT")
#                init:
#                    $ achievement.register("NUKE_IT")
#                    $ achievement.sync()
                $ achievement.sync()
        $ ach_friendly_length = len(ach_friendly)
        if ach_friendly_length >= 5:
            if not achievement.has("FRIENDLY"):
                $ achievement.grant("FRIENDLY")
#                init:
#                    $ achievement.register("FRIENDLY")
#                    $ achievement.sync()
                $ achievement.sync()

    tag ep5_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep5_bonusscene = 0
    if persistent.scene01:
        $ ep5_bonusscene += 1
    if persistent.scene02:
        $ ep5_bonusscene += 1
    if persistent.scene03:
        $ ep5_bonusscene += 1
    if persistent.scene04:
        $ ep5_bonusscene += 1
    if persistent.scene05:
        $ ep5_bonusscene += 1
    else:
        if ep4Dawgs:
            $ persistent.scene05 = True
            $ ep5_bonusscene += 1

    $ ep5_opportunity = 0 #non
    $ ep5_op_none = "."


    if not ep5HugSea:
        $ ep5_opportunity += 1
#        $ ep5_op_none = "\nYou did not try to set up Chris with anybody."

    $ meFlirtyName = "-"
    if meFlirty <= 1:
        $ meFlirtyName = "Faible"
    elif meFlirty == 2:
        $ meFlirtyName = "Moyen"
    elif meFlirty >= 3:
        $ meFlirtyName = "Elevé"

    $ meRomanticName = "-"
    if meRomantic <= 1:
        $ meRomanticName = "Faible"
    elif meRomantic == 2:
        $ meRomanticName = "Moyen"
    elif meRomantic >= 3:
        $ meRomanticName = "Elevé"

    $ meSportyName = "-"
    if meSporty <= 1:
        $ meSportyName = "Faible"
    elif meSporty == 2:
        $ meSportyName = "Moyen"
    elif meSporty >= 3:
        $ meSportyName = "Elevé"

    imagebutton:
        focus_mask True
        idle Transform("endscreen_cece")
        hover Transform("endscreen_cece_on")
        action (ToggleScreen("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep5_endscreen_kira"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep5_endscreen_lexi"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep5_endscreen_robin"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    if Impact_Steph:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_stephanie")
            hover Transform("endscreen_stephanie_on")
            action (ToggleScreen("ep5_endscreen_stephanie"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
            xpos 1200
            ypos 350

        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"))
            xpos 1400
            ypos 350
    else:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"))
            xpos 1200
            ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"), Jump("credits"))
#        action (Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"), Jump("credits7"))
#        xpos 1560
#        ypos 900

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_discord")
        hover Transform("ph_ic_discord_h")
        action OpenURL("https://discord.gg/2jqGPuD")
        xpos 1660
        ypos 780

    if not steambuild:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_patreon")
            hover Transform("ph_ic_patreon_h")
            action OpenURL("https://www.patreon.com/DriftyGames")
            xpos 1760
            ypos 780

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_youtube")
        hover Transform("ph_ic_youtube_h")
        action OpenURL("https://www.youtube.com/c/DriftyGames")
        xpos 1660
        ypos 900

    if renpy.loadable("script06.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep5_endscreen"), Hide("ep5_endscreen_updateinfo"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Jump("ch6Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep5_endscreen"), Hide("ep5_endscreen_updateinfo"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"))
            xpos 1760
            ypos 900

#    $ ep5_endmsg = "Thank you for playing Leap of Faith chapter 1-5. I hope you enjoyed it, and that you will come back for the continuation of the story. "
#    $ ep5_endmsg += "\n\n{color=ffff77}Found a bug or need help?\nJoin my discord and check the channels #bug-reports or #lof-help-spoilers.{/color}"
#    $ ep5_endmsg += "\n\nBest regards\n// Drifty"

#    vpgrid:
#        xalign 0.965
#        ypos 0.092
#        xmaximum 250
#        xminimum 250
#        spacing 4
#        cols 1
#        xfill True
#        yfill True
#        vbox spacing 8:
#            hbox spacing 20:
#                vbox spacing 8:
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 250
#                        xminimum 250
#                        textbutton "{size=18}{color=77ff77}[ep5_endmsg]{/color}{/size}" text_style "task_general_notify"

    vpgrid:
        xalign 0.758
        ypos 0.56
        xmaximum 600
        xminimum 600
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Scènes Bonus débloquées: [ep5_bonusscene]/5" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep5_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep5_opportunity] (this playthrough)[ep5_op_none]" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Niveau de Séduction: [meFlirtyName]\nNiveau de Romantisme: [meRomanticName]\nNiveau Athlétique: [meSportyName]" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Le jeu est constitué de [totalDia] écrans. Vous en avez vu [seenDia]." text_style "task_general_notify"

screen ep5_endscreen_updateinfo:
    tag ep5_endscreen_updateinfo
    $ ep5_end_update = "Si vous avez téléchargé le Chapitre 6 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep5_end_update += "\n\nFichier Patch introuvable. "
    $ ep5_end_update += "\nSi vous avez déjà téléchargé le Chapitre 6 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_update]" text_style "task_general_notify"

screen ep5_endscreen_cece:
    tag ep5_endscreen_cece
    add "emptyendscreen"
    if ep4NightChoose == 1:
        add "ep4_es_cece_happy"
    else:
        add "ep4_es_cece_smile"

    $ ep5_end_cece = "Cece est rentrée chez elle avec les autres pendant que tu restais à Los Angeles avec Lexi et Holly. "
    if ep4NightChoose == 1:
        $ ep5_end_cece = "\n\nTu lui as manqué. "
    $ ep5_end_cece += "\n\nTu viens de rentrer chez toi et tu l'as rejoint. Elle semblait très heureuse de te voir."

    $ ep5_opportunity_ce = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_cece]\n\nOptions manquées pour Cece : [ep5_opportunity_ce]" text_style "task_general_notify"

screen ep5_endscreen_kira:
    tag ep5_endscreen_kira
    add "emptyendscreen"
    if ep4NightChoose == 3:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 4:
        add "ep4_es_kira_suspicious"
    else:
        add "ep4_es_kira_smile"

    $ ep5_end_kira = "Kira est rentrée chez elle avec les autres. Elle t'a dit qu'elle te considérait comme une bon ami et espérait que tu t'arrêterais un jour chez MaKenzie."
    if ep4NightChoose == 3:
        $ ep5_end_kira = "\n\nRobin t'évite. Kira a dit qu'elle lui parlerait. "
    elif ep4NightChoose == 4:
        $ ep5_end_kira = "\n\nRobin agit bizarrement. Probablement à cause de toute la situation. Mais tu devrais aller lui parler du silence radio. "
    elif ep4NightChoose == 5:
        $ ep5_end_kira = "\n\nRobin agit bizarrement. C'est peut-être à cause de toute la situation. Mais vous devriez probablement aller lui parler du silence radio - ou des deux. "

    $ ep5_opportunity_ki = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_kira]\n\nOptions manquées pour Kira : [ep5_opportunity_ki]" text_style "task_general_notify"

screen ep5_endscreen_lexi:
    tag ep5_endscreen_lexi
    add "emptyendscreen"
    if ep4NightChoose == 2:
        add "ep4_es_lexi_happy"
    else:
        add "ep4_es_lexi_smile"

    if Impact_Steph:
        $ ep5_end_lexi = "Après avoir reçu l'appel de ton père, tu es resté à Los Angeles avec Lexi et Holly pendant que Steph se rendait à l'appartement de Holly. Les autres sont rentrés chez eux. "
    else:
        $ ep5_end_lexi = "Après avoir reçu l'appel de ton père, tu es restée à Los Angeles avec Lexi et Holly. Les autres sont rentrés chez eux. "

    $ ep5_end_lexi += "\n\nElles t'ont accompagné quand tu es allé voir ton père, mais tu l'as rencontré seul. "
    $ ep5_end_lexi += "\n\nLe soir, vous vous êtes retrouvés sur les quais, où tu as fait un tour sur le yacht de Lexi. "

    if ep4NightChoose == 2:
        $ ep5_end_lexi += "\n\nTu as surpris Lexi et Holly en train de s'embrasser. Lexi s'est excusé de l'avoir fait. "
        if ep5KissOK == 1:
            $ ep5_end_lexi += "Tu lui as dit qu'il n'y avait pas de quoi s'excuser, c'était plus 'mignon' qu'autre chose. "
        elif ep5KissOK == 2:
            $ ep5_end_lexi += "Tu as accepté les excuses, mais lui as dit d'arrêter de le faire à l'avenir. "
        elif ep5KissOK == 3:
            $ ep5_end_lexi += "Tu as accepté les excuses et lui as confié qu'un plan à trois ne te dérangerait pas. "
        if ep5HollyComplete == 1:
            $ ep5_end_lexi += "\n\nTard dans la nuit pendant que tu baisais Lexi, tu as inclus Holly et vous avez fait un vrai plan à trois. "
            $ ep5_end_lexi += "Ça s'est terminé avec Holly éjaculant sur Lexi, et toi sur Holly. Ou était-ce dans Holly ? "
        elif ep5HollyComplete == 2:
            $ ep5_end_lexi += "\n\nTard dans la nuit pendant que tu baisais Lexi, tu as inclus Holly et vous avez fait un vrai plan à trois. "
            $ ep5_end_lexi += "Ça s'est terminé avec Holly éjaculant sur toi, et toi sur Lexi. Ou était-ce dans Lexi? "
        else:
            $ ep5_end_lexi += "\n\nPlus tard dans la nuit, tu as baisé Lexi. "
    if ep5BoughtCigarettes == 1:
        $ ep5_end_lexi += "\n\nTu as acheté des cigarettes pour Holly, mais pas la bonne marque. "
    elif ep5BoughtCigarettes == 2:
        $ ep5_end_lexi += "\n\nTu as acheté des cigarettes pour Holly. C'était même la bonne marque. "
    else:
        $ ep5_end_lexi += "\n\nTu n'as pas acheté de cigarettes pour Holly."

    $ ep5_opportunity_le = 0

    if ep5KissOK == 3:
        $ ep5_opportunity_le += 1
    if ep5HollyComplete > 0:
        $ ep5_opportunity_le += 1
    if ep5BoughtCigarettes == 0:
        $ ep5_opportunity_le += 1


    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_lexi]\n\nOptions manquées pour Lexi : [ep5_opportunity_le]" text_style "task_general_notify"

screen ep5_endscreen_robin:
    tag ep5_endscreen_robin
    add "emptyendscreen"
    if ep4NightChoose == 4:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 3:
        add "ep4_es_robin_sad"
    else:
        add "ep4_es_robin_smile"

    $ ep5_end_robin = "Robin est rentrée chez elle avec les autres. "
    if ep4NightChoose == 3:
        $ ep5_end_robin += "\n\nElle semblait t'éviter avant de rentrer chez elle. Kira a dit qu'elle lui parlerait. "
    elif ep4NightChoose == 4:
        $ ep5_end_robin += "\n\nElle semblait t'éviter avant de rentrer chez elle. Tu voudras peut-être lui parler maintenant que tu es à la maison. "
    elif ep4NightChoose == 5:
        $ ep5_end_robin += "\n\nElle agit bizarrement. C'est peut-être à cause de toute la situation. "

    if ep4SetupChrisWith == 3:
        if ep4NightChoose == 3:
            $ ep5_end_robin += "\n\nElle semble s'entendre avec Chris. "
        else:
            $ ep5_end_robin += "\n\nElle semble s'entendre avec Chris. À moins que ce ne soit purement des amis avec avantages. "

    $ ep5_opportunity_ro = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_robin]\n\nOptions manquées pour Robin : [ep5_opportunity_ro]" text_style "task_general_notify"

screen ep5_endscreen_stephanie:
    tag ep5_endscreen_stephanie
    add "emptyendscreen"
    if Impact_Steph:
        if ep4NightChoose == 7:
            add "ep4_es_steph_happy"
        else:
            add "ep4_es_steph_smile"
    else:
        add "ep4_es_steph_sad"


    $ ep5_end_stephanie = "Steph est allée tôt à l'appartement d'Holly, pour se préparer à une réunion avec son ancien travail et son père. "

    if ep4NightChoose == 7:
        $ ep5_end_stephanie += "Elle ne savait pas que tu es resté à LA. "
        $ ep5_end_stephanie += "\n\nTu es allé la surprendre après avoir vu ton père. "
        if ep5StephGameTrait == 1 and not ep5NoTrait:
            $ ep5_end_stephanie += "\n\nEn te faufilant jusqu'à elle, tu as actigé ton 'cheat mode séducteur super secret'. "
        elif ep5StephGameTrait == 2:
            $ ep5_end_stephanie += "\n\nEn te faufilant jusqu'à elle, tu as actigé ton 'cheat mode sportif athlétique super secret'. "
        elif ep5StephGameTrait == 3:
            $ ep5_end_stephanie += "\n\nEn te faufilant jusqu'à elle, tu as actigé ton 'cheat mode romantique super secret'. "
        else:
            $ ep5_end_stephanie += "\n\nEn te faufilant jusqu'à elle, tu as réalisé que tu avais raté de nombreuses opportunités qui t'auraient permises d'activer un de tes cheat mode. "
        if ep5PhoneMuted:
            $ ep5_end_stephanie += "\n\nGrâce à tes efforts, tes qualités et ta préparation, tu as le jeu Steph - en te faufilant avec succès jusqu'à elle. "
            $ ep5_end_stephanie += "Ensuite tu as pris une très bonne douche et un bon bain. "
        else:
            if ep5StephGameHorny:
                $ ep5_end_stephanie += "\n\nTu as décidé de lui envoyer des sextos pour l'occuper pendant que tu te faufilais, mais tu n'as toujours pas pu éviter le game over. "
            else:
                $ ep5_end_stephanie += "\n\nTu as décidé de lui envoyer des messages romatiques pour l'occuper pendant que tu te faufilais, mais tu n'as toujours pas pu éviter le game over. "
            $ ep5_end_stephanie += "Tu as quand même été récompensé par un bon moment après. "
    else:
        $ ep5_end_stephanie += "Elle ne savait pas que tu étais resté à Los Angeles, et tu n'as pas pu aller la voir. "

    if ep5StephForgive:
        if ep4NightChoose == 7:
            $ ep5_end_stephanie += "\n\nPlus tard dans la journée, Steph t'a déposé sur les quais et est allé voir son père. Tu ne peux pas t'empêcher de te demander comment cela s'est passé. "
        else:
            $ ep5_end_stephanie += "\n\nPlus tard dans la journée, Steph est allée voir son père. Tu ne peux pas t'empêcher de te demander comment cela s'est passé. "
        $ ep5_end_stephanie += "\n\nTu lui as dit que tu lui avais pardonné le passé et son départ. Elle va vivre à LA cependant, pendant que tu rentres chez toi. "
    else:
        if ep4NightChoose == 7:
            $ ep5_end_stephanie += "\n\nPlus tard dans la journée, Steph t'aa déposé sur les quais et est allé voir son père. "
        else:
            $ ep5_end_stephanie += "\n\nPlus tard dans la journée, Steph est allée voir son père. "
        $ ep5_end_stephanie += "\n\nÀ la fin, tu lui as dit que tu ne pouvais pas lui pardonner votre passé et son départ. Elle est prête à vivre à LA, tandis que tu rentres chez toi. "

    $ ep5_opportunity_st = 0

    if ep5NoTrait:
        $ ep5_opportunity_st += 1
    if ep5PhoneMuted:
        $ ep5_opportunity_st += 1

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_stephanie]\n\nOptions manquées pour Stephanie : [ep5_opportunity_st]" text_style "task_general_notify"

screen ep5_endscreen_linda:
    tag ep5_endscreen_linda
    add "emptyendscreen"
    if ep4NightChoose == 6:
        add "ep4_es_linda_happy"
    else:
        add "ep4_es_linda_smile"

    $ ep5_end_linda = "Linda est rentrée à la maison avec les autres. "

    $ ep5_end_linda += "\n\nElle a promis de ne pas voir Matt avant ton retour à la maison, mais n'était pas à la maison quand tu es arrivé. "

    if ep4NightChoose == 6:
        $ ep5_end_linda += "\n\nCette bague semble importante pour elle. Tu dois l'aider à la récupérer d'une manière ou d'une autre. "
    else:
        $ ep5_end_linda += "\n\nCette bague semble importante pour elle. Tu devrais l'aider à la récupérer d'une manière ou d'une autre. "

    $ ep5_opportunity_li = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_linda]\n\nOptions manquées pour Linda : [ep5_opportunity_li]" text_style "task_general_notify"

if credit_show:
    $ credits_show = False
    jump credits

screen endscreen_credits:
    tag endscreen_credits
    modal True
    imagebutton:
        focus_mask True
        idle Transform("credits")
        hover Transform("credits")
        action Hide("endscreen_credits")
        xpos 0
        ypos 0

init:
    transform credits_scroll:
        subpixel True align(0.15,-1.10)
        linear 70.0 align(0.15,5.0)
        Null()

label credits:
    show text [
"{size=40}{color=#4ec4d9}Leap of Faith is written,\nrendered, animated and scripted by{/color}{/size}",
"{size=30}\n\n",
"{color=#ffb0d0}Drifty{/color}",
"\n\n\n{/size}",
"{size=40}{color=#4ec4d9}Discord Team and Beta Testers{/color}{/size}",
"{size=30}\n\n",
"Rob 'The Panty Sniffer' Johnson\n",
"Pial\n",
"Cursen\n",
"Eerie Entity\n",
"Steele\n",
"Dawe\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Guest appearances{/size}",
"{size=30}\n\n",
"Jaye Campbell appears courtesy of\nStone Fox Studios\n\n",
"The 'Last Call' logo is a trademark of\nThunderline Studios\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Top Tier Patreon Supporters{/color}{/size}",
"{size=30}\n\n",
"The-Exotic-Titan\n",
"Smolpenus\n",
"Kytronix\n",
"Xor\n",
"Wolvy\n",
"Touhara\n",
"\n",
"Andrew Rider\n",
"aob86\n",
"Balvenie41\n",
"Darkness65\n",
"Derrek\n",
"Dudemandavid23\n",
"Lee Sullivan\n",
"Luftguran\n",
"MasterSav\n",
"ODX\n",
"RødTop\n",
"scalvi\n",
"TsunamiKata\n",
"Yukinohki\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Thank you to{/color}{/size}",
"{size=30}\n\n",
"Wibble\n",
"for the 3d conversion of the Drifty logo\n\n",
"All my patreon supporters,\n",
"for helping me realize this project.\n",
"You help me create a better game,\n",
"and it wouldn't be possible without you.\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}A special thank you to{/color}{/size}",
"{size=30}\n\n",
"{color=#9f91f9}C.{/color}\n",
"for inspiring me to make this.\n\n\n",
"'{i}To be continued...{/i}'{/size}"
] at credits_scroll
    $ renpy.pause(1, hard=True)
    return
