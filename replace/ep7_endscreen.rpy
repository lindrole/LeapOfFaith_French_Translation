$ credits_show = True

screen ep7_endscreen:

    if steambuild:
        $ ach_experienced_length = len(ach_experienced)

        if ach_experienced_length <= 1:
            if not achievement.has("ONLY_ONE"):
                $ achievement.grant("ONLY_ONE")
#                init:
#                    $ achievement.register("ONLY_ONE")
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

    tag endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep7_bonusscene = 0
    if persistent.scene01:
        $ ep7_bonusscene += 1
    if persistent.scene02:
        $ ep7_bonusscene += 1
    if persistent.scene03:
        $ ep7_bonusscene += 1
    if persistent.scene04:
        $ ep7_bonusscene += 1
    if persistent.scene05:
        $ ep7_bonusscene += 1
    $ persistent.scene06 = True

    $ ep7_opportunity = 0 #non
    $ ep7_op_none = "."

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
        action (ToggleScreen("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_linda"), Hide("ep7_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep7_endscreen_kira"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_linda"), Hide("ep7_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep7_endscreen_lexi"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_linda"), Hide("ep7_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep7_endscreen_robin"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_linda"), Hide("ep7_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    if Impact_Steph:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_stephanie")
            hover Transform("endscreen_stephanie_on")
            action (ToggleScreen("ep7_endscreen_stephanie"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_linda"), Hide("ep7_endscreen_updateinfo"))
            xpos 1200
            ypos 350

        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep7_endscreen_linda"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_updateinfo"))
            xpos 1400
            ypos 350
    else:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep7_endscreen_linda"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_updateinfo"))
            xpos 1200
            ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep7_endscreen_linda"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_updateinfo"), Call("credits7"))
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

    if renpy.loadable("script08.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep7_endscreen"), Hide("ep7_endscreen_updateinfo"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_linda"), Jump("ch8Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep7_endscreen"), Hide("ep7_endscreen_updateinfo"), Hide("ep7_endscreen_cece"), Hide("ep7_endscreen_kira"), Hide("ep7_endscreen_lexi"), Hide("ep7_endscreen_robin"), Hide("ep7_endscreen_stephanie"), Hide("ep7_endscreen_linda"))
            xpos 1760
            ypos 900

#    $ ep7_endmsg = "Thank you for playing Leap of Faith chapter 1-7. I hope you enjoyed it, and that you will come back for the conclusion of the story. "
#    $ ep7_endmsg += "\n\n{color=ffff77}Found a bug or need help?\nJoin my discord and check the channels #bug-reports or #lof-help-spoilers.{/color}"
#    $ ep7_endmsg += "\n\nTake care.\n// Drifty"

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
#                        textbutton "{size=18}{color=77ff77}[ep7_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Scènes Bonus débloquées: [ep7_bonusscene]/5" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep7_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep7_opportunity] (this playthrough)[ep7_op_none]" text_style "task_general_notify"
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

screen ep7_endscreen_updateinfo:
    tag ep7_endscreen_updateinfo
    $ ep7_end_update = "Si vous avez téléchargé le Chapitre 6 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep7_end_update += "\n\nFichier Patch introuvable. "
    $ ep7_end_update += "\nSi vous avez déjà téléchargé le Chapitre 6 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "

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
                        textbutton "[ep7_end_update]" text_style "task_general_notify"

screen ep7_endscreen_cece:
    tag ep7_endscreen_cece
    add "emptyendscreen"
    if ep4NightChoose == 1:
        add "ep4_es_cece_happy"
    else:
        add "ep4_es_cece_smile"

    $ ep7_end_cece = "Tu étais là pour Cece lorsqu'elle était à l'hôpital et tu l'as soutenue tout au long de son rétablissement."
    if ep7CeceCalm >= 12:
        $ ep7_end_cece += "\n\nTu as obtenu {} points en essayant de l'aider à se souvenir, ce qui est suffisant pour qu'elle retrouve la plupart de ses souvenirs et sa confiance en toi.".format(ep7CeceCalm)
    elif ep7CeceCalm <= 7:
        $ ep7_end_cece += "\n\nTu as obtenu {} points en essayant de l'aider à se souvenir. Tu aurais pu faire mieux.".format(ep7CeceCalm)
    else:
        $ ep7_end_cece += "\n\nTu as obtenu {} points en essayant de l'aider à se souvenir. Il y a encore quelques zones d'ombre.".format(ep7CeceCalm)

    if ep4NightChoose == 1:
        $ ep7_end_cece += "\n\nElle retrouve lentement mais sûrement ses sentiments pour toi. Il reste encore du chemin à parcourir, mais tu as fait tout ce que tu pouvais."
    else:
        $ ep7_end_cece += "\n\nElle est heureuse que tu aies été là pour elle. À un moment donné, elle devra trouver son propre bonheur, mais tu as fait tout ce que tu pouvais."

    $ ep7_opportunity_ce = 0

    if ep7CeceCalm <= 9:
        $ ep7_opportunity_ce += 1

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
#                        textbutton "[ep7_end_cece]" text_style "task_general_notify"
                        textbutton "[ep7_end_cece]\n\nOptions manquées pour Cece : [ep7_opportunity_ce]" text_style "task_general_notify"

screen ep7_endscreen_kira:
    tag ep7_endscreen_kira
    add "emptyendscreen"
    if ep4NightChoose == 3:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 4:
        add "ep4_es_kira_suspicious"
    else:
        add "ep4_es_kira_smile"

    $ ep7_end_kira = "Kira rentre chez ses parents et va essayer de se réconcilier avec eux."

    if ep4NightChoose == 3:
        $ ep7_end_kira += "\n\nTu as toujours des sentiments pour elle. Elle est incertaine de ses propres sentiments."
    elif ep4NightChoose == 4:
        $ ep7_end_kira += "\n\nKira pense qu'elle retient Robin loin de toi."
    elif ep4NightChoose == 5:
        $ ep7_end_kira += "\n\nTu as toujours des sentiments pour elle et Robin. Elle se sent bien dans une relation avec Robin, mais veut plus."
    else:
        $ ep7_end_kira += "\n\nTu lui as dit que tu resterais en contact même si elle déménageait définitivement."

    $ ep7_opportunity_ki = 0

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
#                        textbutton "[ep7_end_kira]" text_style "task_general_notify"
                        textbutton "[ep7_end_kira]\n\nOptions manquées pour Kira : [ep7_opportunity_ki]" text_style "task_general_notify"

screen ep7_endscreen_lexi:
    tag ep7_endscreen_lexi
    add "emptyendscreen"
    if ep4NightChoose == 2:
        if ep7HollyEndingStart:
            add "ep4_es_lexi_smile"
        else:
            add "ep4_es_lexi_happy"
    else:
        add "ep4_es_lexi_smile"

    $ ep7_end_lexi = "Lexi est en retard sur son planning de tournée après avoir passé plusieurs semaines à l'hôpital avec vous tous."
    if ep4NightChoose == 2:
        if ep7HollyEndingStart:
            if ep7LoveBoth:
                $ ep7_end_lexi += "\n\nTu lui as parlé de ta romance avec Holly. De plus, tu lui as dit que tu ne pouvais pas choisir entre elles deux. Elle a dit qu'elle réfléchirait, mais que cela pourrait prendre du temps."
                $ ep7_end_lexi += "\n\nTu ne sais pas quand ou si tu la reverras un jour."
            else:
                $ ep7_end_lexi += "\n\nTu lui as parlé de ta romance avec Holly. De plus, tu lui as dit que tu étais tombé amoureux de Holly. Elle était déçue, mais a dit qu'elle finirait par s'en remettre. 'Elle le fait toujours'."
                $ ep7_end_lexi += "\n\nTu ne sais pas si tu la reverras un jour."
        else:
            $ ep7_end_lexi += "\n\nVous avez pratiquement consolidé votre relation. Maintenant, si seulement vous pouviez surmonter vos différences évidentes."
            $ ep7_end_lexi += "\n\nTu ne sais pas quand tu la reverras."

    $ ep7_opportunity_le = 0

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
#                        textbutton "[ep7_end_lexi]" text_style "task_general_notify"
                        textbutton "[ep7_end_lexi]\n\nOptions manquées pour Lexi : [ep7_opportunity_le]" text_style "task_general_notify"

screen ep7_endscreen_robin:
    tag ep7_endscreen_robin
    add "emptyendscreen"
    if ep4NightChoose == 4:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 3:
        add "ep4_es_robin_sad"
    else:
        add "ep4_es_robin_smile"

    $ ep7_end_robin = "Robin accompagne Kira chez ses parents et tentera de se réconcilier avec eux."

    if ep4NightChoose == 4:
        $ ep7_end_robin += "\n\nTu as toujours des sentiments pour elle. Elle est incertaine de ses propres sentiments."
    elif ep4NightChoose == 3:
        $ ep7_end_robin += "\n\nKira sent qu'elle retient Robin loin de toi."
    elif ep4NightChoose == 5:
        $ ep7_end_robin += "\n\nTu as toujours des sentiments pour elle et Kira. Elle se sent à l'aise dans une relation avec Kira, mais en veut plus."
    else:
        $ ep7_end_robin += "\n\nTu lui as dit que vous resteriez en contact même si elle partait définitivement."

    $ ep7_opportunity_ro = 0

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
#                        textbutton "[ep7_end_robin]" text_style "task_general_notify"
                        textbutton "[ep7_end_robin]\n\nOptions manquées pour Robin : [ep7_opportunity_ro]" text_style "task_general_notify"

screen ep7_endscreen_stephanie:
    tag ep7_endscreen_stephanie
    add "emptyendscreen"
    if Impact_Steph:
        if ep4NightChoose == 7:
            add "ep4_es_steph_happy"
        else:
            add "ep4_es_steph_smile"
    else:
        add "ep4_es_steph_sad"

    if ep4NightChoose == 7:
        $ ep7_end_stephanie = "Toi et Stephanie êtes de nouveau ensemble, et les mauvais moments sont derrière vous."
        $ ep7_end_stephanie += "\n\nIl est temps de recommencer à vivre ta vie... en faisant la même chose encore et encore..."
    else:
        $ ep7_end_stephanie = "Stephanie essaie de remettre sa vie sur les rails. Elle est retournée chez son ancien employeur pour récupérer son poste."
        $ ep7_end_stephanie += "\n\nElle se sent bien en étant amie avec toi."

    $ ep7_opportunity_st = 0

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
#                        textbutton "[ep7_end_stephanie]" text_style "task_general_notify"
                        textbutton "[ep7_end_stephanie]\n\nOptions manquées pour Stephanie : [ep7_opportunity_st]" text_style "task_general_notify"

screen ep7_endscreen_linda:
    tag ep7_endscreen_linda
    add "emptyendscreen"
    if ep4NightChoose == 6:
        add "ep4_es_linda_happy"
    else:
        add "ep4_es_linda_smile"

    $ ep7_end_linda = "Linda a un petit secret, et elle ne va pas le révéler. Pas tout de suite."
    if ep4NightChoose == 6:
        $ ep7_end_linda += "\n\nVous avez passé un peu de temps ensemble, juste tous les deux, et elle est tout à fait d'accord avec ça."
        $ ep7_end_linda += "\n\nTu as été un peu con à l'hôpital quand elle a essayé de te montrer quelque chose, et il est temps de te rattraper."
    else:
        $ ep7_end_linda += "\n\nVous avez passé un peu de temps ensemble à l'hôpital, mais maintenant elle fait ses propres choses."

    $ ep7_opportunity_li = 0

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
                        textbutton "[ep7_end_linda]" text_style "task_general_notify"
#                        textbutton "[ep7_end_linda]\n\nOptions manquées pour Linda : [ep7_opportunity_li]" text_style "task_general_notify"

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
        subpixel True align(0.15,-0.65)
        linear 150.0 align(0.15,5.0)
        Null()

label credits7:
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
"Wibble\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Guest appearances{/size}{size=15}\n(in order of appearance){/size}",
"{size=30}\n\n",
"The 'Last Call' logo is a trademark of\nThunderline Studios\nfrom the game\n{color=#7777ff}Last Call{/color}\n\n",
"'Jaye Campbell' appears courtesy of\nStone Fox Studios\nfrom the game\n{color=#7777ff}Chasing Sunsets{/color}\n\n",
"'Dj Kink' appears courtesy of\nDigi B.\n from the game\n{color=#7777ff}Artemis{/color}\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Top Tier Patreon Supporters{/color}{/size}",
"{size=30}\n\n",
"The-Exotic-Titan\n",
"Smolpenus\n",
"Kytronix\n",
"Xor\n",
"Wolvy\n",
"Touhara\n",
"Gus Chiggins\n",
"\n",
"Aeonton\n",
"Andrew Rider\n",
"aob86\n",
"Balvenie41\n",
"Bedywyr\n",
"beosol\n",
"Cobbie916\n",
"Creyczak\n",
"Darkness65\n",
"Derrek\n",
"Dreadlocdj\n",
"Dudemandavid23\n",
"dylan44\n",
"Englen\n",
"Hank Rockwell\n",
"Harry Potter\n",
"Houseofcards87\n",
"HUN\n",
"Igbokay\n",
"Jim Fullerton\n",
"Kevin Allan\n",
"Kris\n",
"Lancastle\n",
"Lee Sullivan\n",
"Luftguran\n",
"MasterSav\n",
"Michael Johnson\n",
"Moony\n",
"Moratyr\n",
"Musclerock\n",
"ODX\n",
"OnniLaava\n",
"Pink Duck\n",
"RødTop\n",
"Samuel M. A.\n",
"scalvi\n",
"Shia Fall\n",
"Travis Moloney\n",
"TsunamiKata\n",
"ujikonapiro\n",
"UnequalSym\n",
"Valr Kerran\n",
"VkRely\n",
"Wilson Wonka\n",
"wulftattu\n",
"Yukinohki\n",
"\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Thank you to{/color}{/size}",
"{size=30}\n\n",
"Wibble\n",
"for the 3d conversion of the Drifty logo\n",
"and the fantastic concert arena.\n\n",
"All my patreon supporters,\n",
"for helping me realize this project.\n",
"You help me create a better game,\n",
"and it wouldn't be possible without you.\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}A special thank you to{/color}{/size}",
"{size=30}\n\n",
"{color=#9f91f9}C.{/color}\n",
"for inspiring me to make this.\n\n\n",
"'{i}To be concluded...{/i}'{/size}"
] at credits_scroll
    $ renpy.pause(1, hard=True)
    return

$ renpy.pause()
