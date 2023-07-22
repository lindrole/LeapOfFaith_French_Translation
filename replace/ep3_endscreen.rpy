screen ep3_endscreen:

    if steambuild:
        if ach_nuke_it:
            if not achievement.has("NUKE_IT"):
                $ achievement.grant("NUKE_IT")
#                init:
#                    $ achievement.register("NUKE_IT")
#                    $ achievement.sync()
                $ achievement.sync()
        if ach_social_butterfly:
            if not achievement.has("SOCIAL_BUTTERFLY"):
                $ achievement.grant("SOCIAL_BUTTERFLY")
#                init:
#                    $ achievement.register("SOCIAL_BUTTERFLY")
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

    tag ep3_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep3_bonusscene = 0
    if persistent.scene01:
        $ ep3_bonusscene += 1
    if persistent.scene02:
        $ ep3_bonusscene += 1
    if persistent.scene03:
        $ ep3_bonusscene += 1
    else:
        if ep3RespondedLexiEyes:
            $ persistent.scene03 = True
            $ ep3_bonusscene += 1

    $ ep3_opportunity = 0 #non
    $ ep3_op_none = "."
    if not ep3PlaneParty:
        $ ep3_opportunity += 1
        $ ep3_op_none = "\nVous n'avez pas amené la fête dans le jet de Lexi."

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
        action (ToggleScreen("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep3_endscreen_kira"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep3_endscreen_lexi"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep3_endscreen_robin"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep3_endscreen_stephanie"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_linda")
        hover Transform("endscreen_linda_on")
        action (ToggleScreen("ep3_endscreen_linda"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_updateinfo"))
        xpos 1400
        ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_updateinfo"), Jump("credits7"))
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

    if renpy.loadable("script04.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep3_endscreen"), Hide("ep3_endscreen_updateinfo"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Jump("ch4Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep3_endscreen"), Hide("ep3_endscreen_updateinfo"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"))
            xpos 1760
            ypos 900

#    $ ep3_endmsg = "Thank you for playing Leap of Faith, Chapter 1-3. I hope you enjoyed it, and to see you again for the continuation of the story. "
#    $ ep3_endmsg += "\n\nRemember to save your game at this screen, to avoid replaying everything when Chapter 4 is out."
#    $ ep3_endmsg += "\n\n{color=ffff77}Found a bug?\nJoin the discord and post it in the #bug-report channel please (link below).{/color}"
#    $ ep3_endmsg += "\n\nBest regards\n// Drifty"

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
#                        textbutton "{size=18}{color=77ff77}[ep3_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Scènes Bonus débloquées: [ep3_bonusscene]/3" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep3_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep3_opportunity] (this playthrough)[ep3_op_none]" text_style "task_general_notify"
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

screen ep3_endscreen_updateinfo:
    tag ep3_endscreen_updateinfo
    $ ep3_end_update = "Si vous avez téléchargé le Chapitre 4 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep3_end_update += "\n\nFichier Patch introuvable. "
    $ ep3_end_update += "\nSi vous avez déjà téléchargé le Chapitre 4 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "

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
                        textbutton "[ep3_end_update]" text_style "task_general_notify"

screen ep3_endscreen_cece:
    tag ep3_endscreen_cece
    add "ep3_epilogue_cece_blank"
    $ ep3_end_cece = "Elle a commencé le chapitre en dormant. "
    if ep3RejectedKira:
        $ ep3_end_cece += "\n\nPlus tard, lorsque tu es rentré chez toi, tu l'as surprise en train de se sécher après une douche. Elle n'avait pas l'air de s'en soucier. "
        $ ep3_end_cece += "\n\nEnsuite, vous avez partagé un moment. "
    $ ep3_end_cece += "\n\nDans l'avion, vous avez convenu d'essayer d'obtenir un autographe de Nite Dawg - d'une manière ou d'une autre. "
    if ep3CeceDrinkMojito:
        $ ep3_end_cece += "\n\nVous avez réussi à trouver la boisson qui lui convenait le mieux. "
    if not ep3PlaneParty:
        $ ep3_end_cece += "\n\nVous n'avez pas réussi à transformer le vol en fête. "
    $ ep3_end_cece += "\n\nLe soir, Chris lui a raconté toute l'histoire à propos de Stephanie, ce qui l'a fait réfléchir. "
    $ ep3_end_cece += "\n\nElle semble aller mieux. "

    $ ep3_opportunity_ce = 0
    if not ep3RejectedKira:
        $ ep3_opportunity_ce += 1
    if not ep3CeceDrinkMojito:
        $ ep3_opportunity_ce += 1
    if ep3ToldChrisWhoMcLike <> 2:
        $ ep3_opportunity_ce += 1
    if not ep3PlaneParty:
        $ ep3_opportunity_ce += 1

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
                        textbutton "[ep3_end_cece]\n\nOptions manquées pour Cece : [ep3_opportunity_ce]" text_style "task_general_notify"

screen ep3_endscreen_kira:
    tag ep3_endscreen_kira
    add "ep3_epilogue_kira_blank"
    $ ep3_end_kira = "Elle t'a donné une explication sur pourquoi elle avait agi de manière étrange hier. Elle t'a vu dans l'appartement de Robin et apparemment, elles sont en couple. "

    if ep3KiraSexTalk == 1:
        $ ep3_end_kira += "\n\nTu lui as honnêtement dit qu'il ne s'était rien passé. "
    elif ep3KiraSexTalk == 2:
        $ ep3_end_kira += "\n\nAvec un sourire, tu lui as demandé d'aller chercher l'histoire directement auprès de Robin, sachant très bien qu'il ne s'était rien passé. "
    elif ep3KiraSexTalk == 3:
        $ ep3_end_kira += "\n\nTu as admis avoir eu des relations sexuelles avec Robin en attendant de recevoir une gifle. Stupéfait, tu as réalisé qu'elle n'allait pas te gifler et qu'elle ne s'en souciait pas du tout. "
    elif ep3KiraSexTalk == 4:
        $ ep3_end_kira += "\n\nTu n'avais pas envie de lui parler de tes aventures sexuelles avec Robin et tu lui as demandé d'aller chercher l'histoire directement auprès de Robin. Elle l'a fait un peu plus tard et... cela ne l'a pas du tout dérangée. "

    if Impact_KiraRobin:
        $ ep3_end_kira += "\n\nTu as dit à Kira que tu étais OK quant à sa relation avec Robin. "
    else:
        $ ep3_end_kira += "\n\nTu as dit à Kira que tu n'aimais pas qu'elle ait une relation avec Robin. "

    if ep3RejectedKira:
        $ ep3_end_kira += "\n\nÉtant la personne directe qu'elle est, elle t'a invité chez elle pour 'baiser comme des lapins'. Tu as décidé de rentrer chez toi à la place. "
    else:
        $ ep3_end_kira += "\n\nÉtant la personne directe qu'elle est, elle t'a invité chez elle pour 'baiser comme des lapins'. Bien sûr, tu n'as pas pu refuser une telle offre. "
    if ep3KiraEndGame == 0:
        $ ep3_end_kira += "\n\nKira n'a pas eu l'occasion de ressentir ton 'tourbillon', de te convaincre par la soumission, ou de t'apprendre à dompter un cheval sauvage. "
    elif ep3KiraEndGame == 1:
        $ ep3_end_kira += "\n\nTu as convaincu Kira par la soumission après le premier round, et elle est joyeusement passée à un autre round. "
    elif ep3KiraEndGame == 2:
        $ ep3_end_kira += "\n\nTu lui as montré le 'tourbillon' et elle est joyeusement passée à un autre round. "
    elif ep3KiraEndGame == 3:
        $ ep3_end_kira += "\n\nTu lui as montré comment apprivoiser un cheval sauvage, et elle est joyeusement passée à un autre round. "

    $ ep3_opportunity_ki = 0
    if ep3RejectedKira:
        $ ep3_opportunity_ki += 1
    if ep3KiraEndGame == 0:
        $ ep3_opportunity_ki += 1
    if ep3ToldChrisWhoMcLike <> 3 and ep3ToldChrisWhoMcLike <> 7:
        $ ep3_opportunity_ki += 1

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
                        textbutton "[ep3_end_kira]\n\nOptions manquées pour Kira : [ep3_opportunity_ki]" text_style "task_general_notify"

screen ep3_endscreen_lexi:
    tag ep3_endscreen_lexi
    add "ep3_epilogue_lexi_blank"
    $ ep3_end_lexi = "Elle t'a appelé pendant que tu étais au café avec Kira et t'a invité, ainsi que tes amis, chez elle à Los Angeles. "
    if ep3SawLexiTopless:
        $ ep3_end_lexi += "\n\nDans l'avion, tu l'as vue seins nus. Tu es allé la voir un peu trop tôt. Tu n'as pas pu prendre de photo d'elle. "
    if ep3SawLexiDress:
        $ ep3_end_lexi += "\n\nDans l'avion, elle t'a montré sa nouvelle robe. Tu as le sentiment qu'elle voulait vraiment te montrer les parties non couvertes par la robe. "
        if ep3LexiPhoto:
            $ ep3_end_lexi += "\n\nTu as pu prendre une photo d'elle dans cette robe, à sa demande. "
    if ep3SaidHiToKevin:
        $ ep3_end_lexi += "\n\nElle a absolument adoré que tu dises salut à son chauffeur, Kevin, avant d'entrer dans la limousine. "
    else:
        $ ep3_end_lexi += "\n\nTu ne semblais pas avoir remarqué son chauffeur, Kevin. "
    if "ep3_leximsg1" in cam_gallery:
        $ ep3_end_lexi += "\n\nElle a eu une très bonne impression de toi lors de vos échanges de messages la veille du départ. "
    if "ep3_leximsg2" in cam_gallery:
        $ ep3_end_lexi += "\n\nElle a pris plaisir à échanger des messages avec toi la veille du départ. "
    if not ep3PlaneParty:
        $ ep3_end_lexi += "\n\nTu n'as pas réussi à transformer le vol en fête. "


    $ ep3_opportunity_le = 0
    if not ep3SaidHiToKevin:
        $ ep3_opportunity_le += 1
    if ep3TimePassed >= 2:
        $ ep3_opportunity_le += 1
    if not ep3LexiPhoto:
        $ ep3_opportunity_le += 1
    if ep3ToldChrisWhoMcLike <> 1:
        $ ep3_opportunity_le += 1
    if not ep3RespondedLexiExtended:
        $ ep3_opportunity_le += 1
    if not ep3PlaneParty:
        $ ep3_opportunity_le += 1

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
                        textbutton "[ep3_end_lexi]\n\nOptions manquées pour Lexi : [ep3_opportunity_le]" text_style "task_general_notify"

screen ep3_endscreen_robin:
    tag ep3_endscreen_robin
    add "ep3_epilogue_robin_blank"
    $ ep3_end_robin = "Tu es allé au café avec Kira et tu l'y as rencontrée. "
    if Impact_KiraRobin:
        $ ep3_end_robin += "\n\nTu as dit à Kira que tu étais OK avec leur relation. "
    else:
        $ ep3_end_robin += "\n\nTu as dit à Kira que tu n'aimais pas qu'elles soient en couple. "

    $ ep3_opportunity_ro = 0
    if ep3ToldChrisWhoMcLike <> 4 and ep3ToldChrisWhoMcLike <> 7:
        $ ep3_opportunity_ro += 1

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
                        textbutton "[ep3_end_robin]\n\nOptions manquées pour Robin : [ep3_opportunity_ro]" text_style "task_general_notify"

screen ep3_endscreen_stephanie:
    tag ep3_endscreen_stephanie
    add "ep3_epilogue_steph_blank"
    $ ep3_end_stephanie = "Il semblerait qu'elle t'ait effectivement dit qu'elle partait, mais pas de manière évidente, pas en te regardant directement dans les yeux. "
    $ ep3_end_stephanie += "\n\nTu devrais l'écouter lorsque tu auras l'occasion de le faire. Pour le clap de fin ou pour pardonner. "
    $ ep3_end_stephanie += "Après tout, tu ne peux pas vraiment avancer tant que tu n'as pas enterré le passé. "
    if ep3ToldChrisWhoMcLike == 6:
        $ ep3_end_stephanie += "\n\nTu as dit à Chris que tu l'aimes."

    $ ep3_opportunity_st = 0
    if ep3ToldChrisWhoMcLike <> 6:
        $ ep3_opportunity_st += 1

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
                        textbutton "[ep3_end_stephanie]\n\nOptions manquées pour Stephanie : [ep3_opportunity_st]" text_style "task_general_notify"

screen ep3_endscreen_linda:
    tag ep3_endscreen_linda
    add "ep3_epilogue_linda_blank"
    $ ep3_end_linda = "Linda a été très occupée, à chercher un job ? "
    $ ep3_end_linda += "\n\nTu n'as toujours pas eu l'occasion de t'asseoir et de parler avec elle correctement."
    if Impact_KiraRobin:
        if ep3LindaWatchRK:
            $ ep3_end_linda += "\n\nElle semblait excitée en regardant Kira et Robin s'adonner à des activités intimes dans l'avion."
    if not ep3PlaneParty:
        $ ep3_end_linda += "\n\nTu n'as pas réussi à transformer le vol en fête. "
    if ep3LimoLindaPic:
        $ ep3_end_linda += "\n\nLe fait de prendre sa photo dans la limousine, lui a fait grandement plaisir."

    $ ep3_opportunity_li = 0
    if not ep3LookedLinda:
        $ ep3_opportunity_li += 1
    if ep3ToldChrisWhoMcLike <> 5:
        $ ep3_opportunity_li += 1
    if not ep3LimoLindaPic:
        $ ep3_opportunity_li += 1
    if not ep3PlaneParty:
        $ ep3_opportunity_li += 1

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
                        textbutton "[ep3_end_linda]\n\nOptions manquées pour Linda : [ep3_opportunity_li]" text_style "task_general_notify"

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
