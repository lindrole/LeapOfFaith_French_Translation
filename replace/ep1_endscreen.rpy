image endscreen_cece_on = Movie(channel="main", play="images/common/es_cece.webm")
image endscreen_kira_on = Movie(channel="main", play="images/common/es_kira.webm")
image endscreen_lexi_on = Movie(channel="main", play="images/common/es_lexi.webm")
image endscreen_robin_on = Movie(channel="main", play="images/common/es_robin.webm")
image endscreen_stephanie_on = Movie(channel="main", play="images/common/es_steph.webm")

default ep1_bonusscene_total = 3
default ep1_opportunity = 0
default ep1_opportunity_ce = 0
default ep1_opportunity_ki = 0
default ep1_opportunity_le = 0
default ep1_opportunity_li = 0
default ep1_opportunity_ro = 0
default ep1_opportunity_st = 0

screen ep1_endscreen:

    tag ep1_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep1_bonusscene = 0
    if persistent.scene01:
        $ ep1_bonusscene += 1
    else:
        if d1_responded_kira_thinkingof == 1:
            $ persistent.scene01 = True
            $ ep1_bonusscene += 1

#    $ ep1_gallery = 0
#    if wentBowlingKira:
#        $ persistent.gallery01 = True
#        $ ep1_gallery += 1

    $ ep1_opportunity = 0 #non
    if d1_responded_chris == 0:
        $ ep1_opportunity += 1

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
        action (ToggleScreen("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep1_endscreen_kira"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep1_endscreen_lexi"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep1_endscreen_robin"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep1_endscreen_stephanie"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_uk")
        hover Transform("endscreen_uk_on")
        action (ToggleScreen("ep1_endscreen_uk"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_updateinfo"))
        xpos 1400
        ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_updateinfo"), Jump("credits7"))
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

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_continue")
        hover Transform("ph_ic_continue_h")
        action (Hide("ep1_endscreen"), Hide("ep1_endscreen_updateinfo"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Jump("ch2Update"))
        xpos 1760
        ypos 900

#    $ ep1_endmsg = "Thank you for playing Leap of Faith, Chapter 1. I hope you enjoyed it, and hope to see you again for the continuation of the story. "
#    $ ep1_endmsg += "\n\nRemember to save your game at this screen, to avoid replaying Chapter 1 when Chapter 2 is out."
#    $ ep1_endmsg += "\n\nBest regards\n// Drifty"

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
#                        textbutton "{size=18}{color=77ff77}[ep1_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Scènes Bonus débloquées: [ep1_bonusscene]/[ep1_bonusscene_total]" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep1_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep1_opportunity] (durant cette partie de jeu)\n{size=18}{color=ffff00}(Les options sont des choix qui auront, d'une manière ou d'une autre, un impact sur les chapitres futurs. Consultez les fiches des personnages individuels pour plus d'informations.){/color}{/size}" text_style "task_general_notify"
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

screen ep1_endscreen_updateinfo:
    tag ep1_endscreen_updateinfo
    $ ep1_end_update = "Si vous avez téléchargé le Chapitre 2 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep1_end_update += "\n\nFichier Patch introuvable. "
    $ ep1_end_update += "\nSi vous avez déjà téléchargé le Chapitre 2 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "
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
                        textbutton "[ep1_end_update]" text_style "task_general_notify"

screen ep1_endscreen_cece:
    tag ep1_endscreen_cece
    $ ep1_end_cece = "Vous avez sauvé la vie de Cece. Pour elle, vous êtes une deuxième chance dans la vie. "
    $ ep1_end_cece += "\n\nElle est actuellement hospitalisée. Vous êtes là avec elle. "

    $ ep1_opportunity_ce = 0
    if ep1OfferedCeceStay:
        $ ep1_opportunity_ce += 1

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
                        textbutton "[ep1_end_cece]\n\nOptions manquées pour Cece: [ep1_opportunity_ce]" text_style "task_general_notify"

screen ep1_endscreen_kira:
    tag ep1_endscreen_kira
    $ ep1_end_kira = "Vous avez rencontré Kira à MaKenzie lors d'un déjeuner. "
    if d1_responded_kira != 0:
        $ ep1_end_kira += "\n\nVous avez obtenu son numéro de téléphone et lui avez envoyé un message en retour. "
        if wentBowlingKira:
            if ep1KiraWalkHome:
                $ ep1_end_kira += "\n\nVous êtes allés jouer au bowling tous les deux, et après l'avoir ramenée chez elle, elle vous a invité à entrer. "
                if ep1RejectedKira:
                    $ ep1_end_kira += "Vous avez décliné ses avances. "
                else:
                    $ ep1_end_kira += "Vous avez accepté, mais elle a changé d'avis. "
            else:
                $ ep1_end_kira += "\n\nVous êtes allés jouer au bowling tous les deux, mais vous ne l'avez pas raccompagnée chez elle. "
            if d1_responded_kira_thinkingof == 1:
                $ ep1_end_kira += "\n\nVous lui avez dit dans un message que vous penseriez à elle pendant que vous seriez dans le métro. "
        else:
            $ ep1_end_kira += "\n\nVous avez refusé d'aller jouer au bowling avec elle. "
    else:
        $ ep1_end_kira += "\n\nVous avez obtenu son numéro de téléphone, mais vous ne lui avez pas répondu envoyé de message. "

    $ ep1_opportunity_ki = 0
    if not wentBowlingKira:
        $ ep1_opportunity_ki += 2

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
                        textbutton "[ep1_end_kira]\n\nOptions manquées pour Kira : [ep1_opportunity_ki]" text_style "task_general_notify"

screen ep1_endscreen_lexi:
    tag ep1_endscreen_lexi
    $ ep1_end_lexi = "Vous avez rencontré Lexi au Metronome entre ses performances, où elle a pris quelques verres de vin avec vous. "
    if saidLexiWasBeautiful:
        $ ep1_end_lexi += "\n\nElle a pensé à vous plus tard dans la soirée. "
    else:
        $ ep1_end_lexi += "\n\nElle vous a trouvé mignon. "

    $ ep1_opportunity_le = 0
    if saidLexiWasBeautiful:
        $ ep1_opportunity_le += 1

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
                        textbutton "[ep1_end_lexi]\n\nOptions manquées pour Lexi : [ep1_opportunity_le]" text_style "task_general_notify"

screen ep1_endscreen_robin:
    tag ep1_endscreen_robin
    if wentBowlingKira:
        $ ep1_end_robin = "Vous avez rencontré Robin en allant jouer au bowling avec Kira. Elle est la propriétaire de la salle de bowling. "
        $ ep1_end_robin += "Elle vous a dit de ne pas accepter les avances de Kira si elle se proposait à vous pendant la soirée. "
        if ep1SaidLikedRobin:
            $ ep1_end_robin += "\n\nVous lui avez dit que vous l'aimiez bien. "
    else:
        $ ep1_end_robin = "Vous n'avez pas encore rencontré Robin. "

    $ ep1_opportunity_ro = 0
    if not ep1SaidLikedRobin:
        $ ep1_opportunity_ro += 1

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
                        textbutton "[ep1_end_robin]\n\nOptions manquées pour Robin : [ep1_opportunity_ro]" text_style "task_general_notify"

screen ep1_endscreen_stephanie:
    tag ep1_endscreen_stephanie
    $ ep1_end_stephanie = "Vous avez rêvé de Stephanie, ce qui vous a fait penser à elle à nouveau. "
    $ ep1_end_stephanie += "\n\nVous vous êtes croisés tard dans la nuit au Metronome, où elle vous a intimé de la suivre chez elle."
    if stephRejected:
        $ ep1_end_stephanie += "\n\nVous avez refusé ses avances et demandé des explications. Elle n'en avait aucune."
    else:
        $ ep1_end_stephanie += "\n\nTu l'as baisé idiot. Puis son mari est rentré à la maison et vous avez dû abandonner le navire."
        if ep1StephOrg:
            $ ep1_end_stephanie += "\n\nElle a eu un orgasme - pas toi."

    $ ep1_opportunity_st = 0
    if not ep1StephOrg:
        $ ep1_opportunity_st += 1
    if d1_responded_stephanie == 0:
        $ ep1_opportunity_st += 1

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
                        textbutton "[ep1_end_stephanie]\n\nOptions manquées pour Stéphanie : [ep1_opportunity_st]" text_style "task_general_notify"

screen ep1_endscreen_uk:
    tag ep1_endscreen_uk
    $ ep1_end_uk = "Le dernier des personnages avec qui une romance est possible. Vous la rencontrerez dans le chapitre 2. "

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
                        textbutton "[ep1_end_uk]" text_style "task_general_notify"
