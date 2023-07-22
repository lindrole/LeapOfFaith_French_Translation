$ credits_show = True

screen ep6_endscreen:

    if steambuild:
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

    tag ep6_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep6_bonusscene = 0
    if persistent.scene01:
        $ ep6_bonusscene += 1
    if persistent.scene02:
        $ ep6_bonusscene += 1
    if persistent.scene03:
        $ ep6_bonusscene += 1
    if persistent.scene04:
        $ ep6_bonusscene += 1
    if persistent.scene05:
        $ ep6_bonusscene += 1
    $ persistent.scene06 = True

    $ ep6_opportunity = 0 #non
    $ ep6_op_none = "."

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
        action (ToggleScreen("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep6_endscreen_kira"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep6_endscreen_lexi"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep6_endscreen_robin"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    if Impact_Steph:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_stephanie")
            hover Transform("endscreen_stephanie_on")
            action (ToggleScreen("ep6_endscreen_stephanie"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_updateinfo"))
            xpos 1200
            ypos 350

        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep6_endscreen_linda"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_updateinfo"))
            xpos 1400
            ypos 350
    else:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep6_endscreen_linda"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_updateinfo"))
            xpos 1200
            ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_updateinfo"), Jump("credits7"))
#        action (Hide("ep6_endscreen_linda"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_updateinfo"), Jump("credits7"))
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

    if renpy.loadable("script07.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep6_endscreen"), Hide("ep6_endscreen_updateinfo"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_linda"), Jump("ch7Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep6_endscreen"), Hide("ep6_endscreen_updateinfo"), Hide("ep6_endscreen_cece"), Hide("ep6_endscreen_kira"), Hide("ep6_endscreen_lexi"), Hide("ep6_endscreen_robin"), Hide("ep6_endscreen_stephanie"), Hide("ep6_endscreen_linda"))
            xpos 1760
            ypos 900

#    $ ep6_endmsg = "Thank you for playing Leap of Faith chapter 1-6. I hope you enjoyed it, and that you will come back for the continuation of the story. "
#    $ ep6_endmsg += "\n\n{color=ffff77}Found a bug or need help?\nJoin my discord and check the channels #bug-reports or #lof-help-spoilers.{/color}"
#    $ ep6_endmsg += "\n\nTake care.\n// Drifty"

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
#                        textbutton "{size=18}{color=77ff77}[ep6_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Scènes Bonus débloquées: [ep6_bonusscene]/5" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep6_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep6_opportunity] (this playthrough)[ep6_op_none]" text_style "task_general_notify"
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

screen ep6_endscreen_updateinfo:
    tag ep6_endscreen_updateinfo
    $ ep6_end_update = "Si vous avez téléchargé le Chapitre 6 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep6_end_update += "\n\nFichier Patch introuvable. "
    $ ep6_end_update += "\nSi vous avez déjà téléchargé le Chapitre 6 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "

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
                        textbutton "[ep6_end_update]" text_style "task_general_notify"

screen ep6_endscreen_cece:
    tag ep6_endscreen_cece
    add "emptyendscreen"
#    if ep4NightChoose == 1:
#        add "ep4_es_cece_happy"
#    else:
#        add "ep4_es_cece_smile"

    $ ep6_end_cece = "Parfois, il se passe des choses sur lesquelles vous n'avez aucun contrôle. L'important n'est pas qu'elles se soient produites, mais comment vous y faites face."

    $ ep6_opportunity_ce = 0

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
                        textbutton "[ep6_end_cece]" text_style "task_general_notify"
#                        textbutton "[ep6_end_cece]\n\nOptions manquées pour Cece : [ep6_opportunity_ce]" text_style "task_general_notify"

screen ep6_endscreen_kira:
    tag ep6_endscreen_kira
    add "emptyendscreen"
#    if ep4NightChoose == 3:
#        add "ep4_es_kira_happy"
#    elif ep4NightChoose == 5:
#        add "ep4_es_kira_happy"
#    elif ep4NightChoose == 4:
#        add "ep4_es_kira_suspicious"
#    else:
#        add "ep4_es_kira_smile"

    $ ep6_end_kira = "Tu as passé du temps avec Kira tout en l'aidant dans son travail."
    if ep4NightChoose == 3:
        if ep6HadSexWithKira:
            $ ep6_end_kira += "\n\nMais même si tout va bien entre vous et que vous avez eu des relations sexuelles, il semblait juste de la remettre avec Robin au bal de promo."
            if ep6HadSexWithRobin:
                $ ep6_end_kira += "\n\nTu as aussi couché avec Robin, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_kira += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."
        else:
            $ ep6_end_kira += "\n\nMais même si tout va bien entre vous, c'était bien de la remettre avec Robin au bal de promo."
            if ep6HadSexWithRobin:
                $ ep6_end_kira += "\n\nTu as aussi couché avec Robin, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_kira += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."
    if ep4NightChoose == 5:
        if ep6HadSexWithKira:
            $ ep6_end_kira += "\n\nMais même si tout va bien entre vous et que vous avez eu des relations sexuelles, il semblait juste de la remettre avec Robin au bal de promo."
            if ep6HadSexWithRobin:
                $ ep6_end_kira += "\n\nTu as aussi couché avec Robin, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_kira += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."
        else:
            $ ep6_end_kira += "\n\nMais même si tout va bien entre vous, c'était bien de la remettre avec Robin au bal de promo."
            if ep6HadSexWithRobin:
                $ ep6_end_kira += "\n\nTu as aussi couché avec Robin, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_kira += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."

    $ ep6_opportunity_ki = 0
    if not ep6HadSexWithKira:
        $ ep6_opportunity_ki += 1

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
                        textbutton "[ep6_end_kira]" text_style "task_general_notify"
#                        textbutton "[ep6_end_kira]\n\nOptions manquées pour Kira : [ep6_opportunity_ki]" text_style "task_general_notify"

screen ep6_endscreen_lexi:
    tag ep6_endscreen_lexi
    add "emptyendscreen"
#    if ep4NightChoose == 2:
#        add "ep4_es_lexi_happy"
#    else:
#        add "ep4_es_lexi_smile"

    $ ep6_end_lexi = "Tu as passé du temps avec Lexi de manière inattendue lors du bal de promo que Cece a aidé à organiser."
    if ep4NightChoose == 2:
        $ ep6_end_lexi += "\n\nPour la première fois de sa vie, elle ne voulait pas partir en tournée, car cela signifierait passer moins de temps avec toi."
        $ ep6_end_lexi += "\n\nMais maintenant, ironiquement, sa tournée est la dernière chose à laquelle elle pense."

    $ ep6_opportunity_le = 0

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
                        textbutton "[ep6_end_lexi]" text_style "task_general_notify"
#                        textbutton "[ep6_end_lexi]\n\nOptions manquées pour Lexi : [ep6_opportunity_le]" text_style "task_general_notify"

screen ep6_endscreen_robin:
    tag ep6_endscreen_robin
    add "emptyendscreen"
#    if ep4NightChoose == 4:
#        add "ep4_es_robin_happy"
#    elif ep4NightChoose == 5:
#        add "ep4_es_robin_happy"
#    elif ep4NightChoose == 3:
#        add "ep4_es_robin_sad"
#    else:
#        add "ep4_es_robin_smile"

    $ ep6_end_robin = "Tu as passé du temps avec Robin tout en l'aidant à remettre le bowling sur les rails."
    if ep4NightChoose == 3:
        if ep6HadSexWithRobin:
            $ ep6_end_robin += "\n\nMais même si tout va bien entre vous et que vous avez eu des relations sexuelles, il semblait juste de la remettre avec Kira au bal de promo."
            if ep6HadSexWithKira:
                $ ep6_end_robin += "\n\nTu as aussi couché avec Kira, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_robin += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."
        else:
            $ ep6_end_robin += "\n\nMais même si tout va bien entre vous, c'était bien de la remettre avec Kira au bal de promo."
            if ep6HadSexWithKira:
                $ ep6_end_robin += "\n\nTu as aussi couché avec Kira, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_robin += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."
    if ep4NightChoose == 5:
        if ep6HadSexWithRobin:
            $ ep6_end_robin += "\n\nMais même si tout va bien entre vous et que vous avez eu des relations sexuelles, il semblait juste de la remettre avec Kira au bal de promo."
            if ep6HadSexWithKira:
                $ ep6_end_robin += "\n\nTu as aussi couché avec Kira, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_robin += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."
        else:
            $ ep6_end_robin += "\n\nMais même si tout va bien entre vous, c'était bien de la remettre avec Kira au bal de promo."
            if ep6HadSexWithKira:
                $ ep6_end_robin += "\n\nTu as aussi couché avec Kira, sachant qu'aucune d'elles ne s'en soucie."
            $ ep6_end_robin += "\n\nLes choses sont hors de tes mains pour l'instant, mais on ne sait jamais."


    $ ep6_opportunity_ro = 0
    if not ep6HadSexWithRobin:
        $ ep6_opportunity_ro += 1

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
                        textbutton "[ep6_end_robin]" text_style "task_general_notify"
#                        textbutton "[ep6_end_robin]\n\nOptions manquées pour Robin : [ep6_opportunity_ro]" text_style "task_general_notify"

screen ep6_endscreen_stephanie:
    tag ep6_endscreen_stephanie
    add "emptyendscreen"
#    if Impact_Steph:
#        if ep4NightChoose == 7:
#            add "ep4_es_steph_happy"
#        else:
#            add "ep4_es_steph_smile"
#    else:
#        add "ep4_es_steph_sad"


    $ ep6_end_stephanie = "Tu as passé du temps avec Stephanie lors du bal de promo que Cece a aidé à organiser."
    $ ep6_end_stephanie += "\n\nIl semblerait qu'elle n'ait pas eu la chance pour se réconcilier avec son père."

    $ ep6_opportunity_st = 0

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
                        textbutton "[ep6_end_stephanie]" text_style "task_general_notify"
#                        textbutton "[ep6_end_stephanie]\n\nStephanie Options manquées pour : [ep6_opportunity_st]" text_style "task_general_notify"

screen ep6_endscreen_linda:
    tag ep6_endscreen_linda
    add "emptyendscreen"
#    if ep4NightChoose == 6:
#        add "ep4_es_linda_happy"
#    else:
#        add "ep4_es_linda_smile"

    $ ep6_end_linda = "Linda s'est jointe à toi un jour après ton retour à la maison."
    $ ep6_end_linda += "\n\nElle n'a pas partagé la raison de son absence, mais tu as eu l'impression que c'était quelque chose d'important. Du moins pour elle."

    $ ep6_opportunity_li = 0

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
                        textbutton "[ep6_end_linda]" text_style "task_general_notify"
#                        textbutton "[ep6_end_linda]\n\nOptions manquées pour Linda : [ep6_opportunity_li]" text_style "task_general_notify"

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

label credits6:
    show text [""] at credits_scroll
    $ renpy.pause(1, hard=True)
    return
