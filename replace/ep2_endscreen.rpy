image endscreen_linda_on = Movie(channel="main", play="images/common/es_linda.webm")

default ep2_bonusscene_total = 1
default  ep2_opportunity = 0
default  ep2_opportunity_ce = 0
default  ep2_opportunity_ki = 0
default  ep2_opportunity_le = 0
default  ep2_opportunity_li = 0
default  ep2_opportunity_ro = 0
default  ep2_opportunity_st = 0

screen ep2_endscreen:

    if steambuild:
        if ep2LexiReply:
            if not achievement.has("NUMBER"):
                $ achievement.grant("NUMBER")
#                init:
#                    $ achievement.register("NUMBER")
#                    $ achievement.sync()
                $ achievement.sync()
            if not achievement.has("SOCIAL_BUTTERFLY"):
                $ achievement.grant("SOCIAL_BUTTERFLY")
#                init:
#                    $ achievement.register("SOCIAL_BUTTERFLY")
#                    $ achievement.sync()
                $ achievement.sync()
        if ach_social_butterfly:
            if not achievement.has("SOCIAL_BUTTERFLY"):
                $ achievement.grant("SOCIAL_BUTTERFLY")
#                init:
#                    $ achievement.register("SOCIAL_BUTTERFLY")
#                    $ achievement.sync()
                $ achievement.sync()

    tag ep2_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep2_bonusscene = 0
    if persistent.scene02:
        $ ep2_bonusscene += 1
    else:
        if ep2RespondedRobin == 2:
            $ persistent.scene02 = True
            $ ep2_bonusscene += 1
    $ ep2_bonusscene += 1

    $ ep2_opportunity_sum = ep1_opportunity
    $ ep2_opportunity = 0 #non
    if ep2ChrisShopConv == 4:
        $ ep2_opportunity += 1
        $ ep2_opportunity_sum += 1
    if not ep2BunnyPicFlex:
        $ ep2_opportunity += 1
        $ ep2_opportunity_sum += 1

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
        action (ToggleScreen("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep2_endscreen_kira"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep2_endscreen_lexi"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep2_endscreen_robin"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep2_endscreen_stephanie"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_linda")
        hover Transform("endscreen_linda_on")
        action (ToggleScreen("ep2_endscreen_linda"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_updateinfo"))
        xpos 1400
        ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_updateinfo"), Jump("credits7"))
#        action (Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_updateinfo"), Jump("credits6"))
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

    if renpy.loadable("script03.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep2_endscreen"), Hide("ep2_endscreen_updateinfo"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Jump("ch3Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep2_endscreen"), Hide("ep2_endscreen_updateinfo"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"))
            xpos 1760
            ypos 900

#    $ ep2_endmsg = "Thank you for playing Leap of Faith, Chapter 2. I hope you enjoyed it, and to see you again for the continuation of the story. "
#    $ ep2_endmsg += "\n\nRemember to save your game at this screen, to avoid replaying everything when Chapter 3 is out."
#    $ ep2_endmsg += "\n\n{color=ffff77}Found a bug?\nJoin the discord and post it in the #bug-report channel please (link below).{/color}"
#    $ ep2_endmsg += "\n\nBest regards\n// Drifty"

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
#                        textbutton "{size=18}{color=77ff77}[ep2_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Scènes Bonus débloquées: [ep2_bonusscene]/3" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep2_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep2_opportunity] (this playthrough)\n{size=18}{color=ffff00}(Options are choices that in some way will impact future chapters. See individual characters for more.){/color}{/size}" text_style "task_general_notify"
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

screen ep2_endscreen_updateinfo:
    tag ep2_endscreen_updateinfo
    $ ep2_end_update = "Si vous avez téléchargé le Chapitre 3 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep2_end_update += "\n\nFichier Patch introuvable. "
    $ ep2_end_update += "\nSi vous avez déjà téléchargé le Chapitre 3 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "

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
                        textbutton "[ep2_end_update]" text_style "task_general_notify"

screen ep2_endscreen_cece:
    tag ep2_endscreen_cece
    $ ep2_end_cece = "Elle vit actuellement dans votre appartement. Il y a quelque chose chez elle. "
    $ ep2_end_cece += "\n\nVous n'avez pas pu résoudre ses problèmes ou passer beaucoup de temps seul. Mais elle a semblé s'ouvrir un peu à la fin. "

    $ ep2_opportunity_ce_total = ep1_opportunity_ce
    $ ep2_opportunity_ce = 0
    if ep2Eyecontact <> 1:
        $ ep2_opportunity_ce += 1
        $ ep2_opportunity_ce_total += 1
    if ep2ToldChrisAboutCece:
        $ ep2_opportunity_ce += 1
        $ ep2_opportunity_ce_total += 1

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
                        textbutton "[ep2_end_cece]\n\nOptions manquées pour Cece : [ep2_opportunity_ce]" text_style "task_general_notify"

screen ep2_endscreen_kira:
    tag ep2_endscreen_kira
    $ ep2_end_kira = "Tu n'as pas passé de temps avec Kira dans ce chapitre. "
    if ep2KiraReply:
        $ ep2_end_kira += "\n\nElle t'a envoyé un message et tu as répondu. "
        if ep2KiraReplyTwo:
            $ ep2_end_kira += "\n\nLe lendemain, elle t'a envoyé un nouveau message, où elle a agi de manière un peu étrange. "
        else:
            $ ep2_end_kira += "\n\nLe lendemain, elle t'a envoyé un nouveau message auquel tu n'as pas répondu. "
    else:
        $ ep2_end_kira += "\n\nElle t'a envoyé un message. Tu n'as pas répondu. "
    if not ep2RobinCrosseyed:
        $ ep2_end_kira += "\n\nOh, et il semble que tu partages un petit secret avec Kira à propos de Robin quand elle est ivre. "

    $ ep2_opportunity_ki_total = ep1_opportunity_ki
    $ ep2_opportunity_ki = 0
    if not ep2KiraReply:
        $ ep2_opportunity_ki += 1
        $ ep2_opportunity_ki_total += 1
    if not ep2KiraReplyTwo:
        $ ep2_opportunity_ki += 1
        $ ep2_opportunity_ki_total += 1
    if ep2RobinCrosseyed:
        $ ep2_opportunity_ki += 1
        $ ep2_opportunity_ki_total += 1

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
                        textbutton "[ep2_end_kira]\n\nOptions manquées pour Kira : [ep2_opportunity_ki]" text_style "task_general_notify"

screen ep2_endscreen_lexi:
    tag ep2_endscreen_lexi
    $ ep2_end_lexi = "Chris t'a dit qu'il avait parlé à Lexi après que tu ais quitté le Metro ; où elle t'avait demandé. Cependant, il a oublié de lui donner ton numéro de téléphone. "
    if ep2LexiReply:
        $ ep2_end_lexi += "\n\nTu as cependant réussi à trouver un moyen de lui donner ton numéro de téléphone. "
    else:
        $ ep2_end_lexi += "\n\nTu n'as pas réussi à trouver un moyen de lui donner ton numéro de téléphone. "

    $ ep2_opportunity_le_total = ep1_opportunity_le
    $ ep2_opportunity_le = 0
    if not ep2LexiReply:
        $ ep2_opportunity_le += 1
        $ ep2_opportunity_le_total += 1
    if not ep2LexiSlippers:
        $ ep2_opportunity_le += 1
        $ ep2_opportunity_le_total += 1
    if not ep2NukeDance:
        $ ep2_opportunity_le += 1
        $ ep2_opportunity_le_total += 1

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
                        textbutton "[ep2_end_lexi]\n\nOptions manquées pour Lexi : [ep2_opportunity_le]" text_style "task_general_notify"

screen ep2_endscreen_robin:
    tag ep2_endscreen_robin
    if ep2WentToRobin:
        $ ep2_end_robin = "Tu es allé au Plaza Bowling pour aider Robin lors de sa soirée d'ouverture. "
        $ ep2_end_robin += "Malheureusement, elle avait connu une série de malchances et avait décidé de fermer plus tôt et de rentrer chez elle. Tu l'as accompagnée. "
        if ep2SaidLikedRobin:
            $ ep2_end_robin += "\n\nTu lui as dit que tu l'aimais bien. "
    else:
        $ ep2_end_robin = "Tu n'es pas allé au Plaza Bowling pour aider Robin lors de sa soirée d'ouverture. "
    if ep2RejectedRobin:
        $ ep2_end_robin += "\n\nElle a essayé de t'avoir pour la nuit, mais tu as décliné. "
    else:
        $ ep2_end_robin += "\n\nVous avez eu des relations sexuelles avec elle. Elle a laissé entendre une relation d'amis avec avantages, mais qui sait. Peut-être que c'était l'alcool qui parlait. "

    $ ep2_opportunity_ro_total = ep1_opportunity_ro
    $ ep2_opportunity_ro = 0
    if not ep2WentToRobin:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if not ep2SaidLikedRobin:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if ep2RejectedRobin:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if not ep2RobinCrosseyed:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if not ep2RobinCommandoAbuse:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if ep2RespondedRobin == 0:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1

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
                        textbutton "[ep2_end_robin]\n\nOptions manquées pour Robin : [ep2_opportunity_ro]" text_style "task_general_notify"

screen ep2_endscreen_stephanie:
    tag ep2_endscreen_stephanie
    $ ep2_end_stephanie = "Tu n'as pas revu Stephanie depuis cette nuit après le Metro. "
    $ ep2_end_stephanie += "\n\nAprès avoir ajouté Nüke à ton téléphone, tu as remarqué qu'elle y était aussi."

    $ ep2_opportunity_st_total = ep1_opportunity_st
    $ ep2_opportunity_st = 0
    if ep2ChrisConvOverSteph == 1:
        $ ep2_opportunity_st += 1
        $ ep2_opportunity_st_total += 1

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
                        textbutton "[ep2_end_stephanie]\n\nOptions manquées pour Stephanie : [ep2_opportunity_st]" text_style "task_general_notify"

screen ep2_endscreen_linda:
    tag ep2_endscreen_linda
    $ ep2_end_linda = "Il semblerait que le monde soit petit. La meilleure amie de Cece n'est autre que ton amie d'enfance, Linda. "
    $ ep2_end_linda += "\n\nTu n'as pas encore eu l'occasion de t'asseoir et de discuter avec elle correctement."
    if ep2LindaDressingFlirt:
        $ ep2_end_linda += "\n\nLes choses ont pris une tournure assez torride dans la salle d'habillage chez Ashley."

    $ ep2_opportunity_li_total = ep1_opportunity_li
    $ ep2_opportunity_li = 0
    if ep2Eyecontact <> 2:
        $ ep2_opportunity_li += 1
        $ ep2_opportunity_li_total += 1
    if not ep2LindaDressingFlirt:
        $ ep2_opportunity_li += 1
        $ ep2_opportunity_li_total += 1

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
                        textbutton "[ep2_end_linda]\n\nOptions manquées pour Linda : [ep2_opportunity_li]" text_style "task_general_notify"

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
