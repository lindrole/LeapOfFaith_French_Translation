screen ep4_endscreen:

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

    tag ep4_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep4_bonusscene = 0
    if persistent.scene01:
        $ ep4_bonusscene += 1
    if persistent.scene02:
        $ ep4_bonusscene += 1
    if persistent.scene03:
        $ ep4_bonusscene += 1
    if persistent.scene04:
        $ ep4_bonusscene += 1
    else:
        $ persistent.scene04 = True
        $ ep4_bonusscene += 1

    $ ep4_opportunity = 0 #non
    $ ep4_op_none = "."
    if ep4ChrisStatus <> 1:
        $ ep4_opportunity += 1
        $ ep4_op_none = "\nTu n'as pas essayé de caser Chris avec quelqu'un."

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
        action (ToggleScreen("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep4_endscreen_kira"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep4_endscreen_lexi"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep4_endscreen_robin"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep4_endscreen_stephanie"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_linda")
        hover Transform("endscreen_linda_on")
        action (ToggleScreen("ep4_endscreen_linda"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_updateinfo"))
        xpos 1400
        ypos 350

#    imagebutton:
#        focus_mask True
#        idle Transform("ph_ic_ty")
#        hover Transform("ph_ic_ty_h")
#        action Show("endscreen_credits")
#        action Show("credits")
#        action (Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_updateinfo"), Jump("credits7"))
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

    if renpy.loadable("script05.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep4_endscreen"), Hide("ep4_endscreen_updateinfo"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Jump("ch5Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep4_endscreen"), Hide("ep4_endscreen_updateinfo"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"))
            xpos 1760
            ypos 900

#    $ ep4_endmsg = "Thank you for playing Leap of Faith chapter 1-4. I hope you enjoyed it, and that you will come back for the continuation of the story. "
#    $ ep4_endmsg += "\n\n{color=ffff77}Found a bug?\nJoin my discord and post it in the #bug-reports channel please (link below) and it will be fixed quickly.{/color}"
#    $ ep4_endmsg += "\n\nBest regards\n// Drifty"

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
#                        textbutton "{size=18}{color=77ff77}[ep4_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Scènes Bonus débloquées: [ep4_bonusscene]/4" text_style "task_general_notify"
#                    frame:
#                        background Frame("taskop_general",10,10)
#                        xmaximum 550
#                        xminimum 550
#                        textbutton "Gallery unlocked: [ep4_gallery]/1" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Options manquées hors romances: [ep4_opportunity] (this playthrough)[ep4_op_none]" text_style "task_general_notify"
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

screen ep4_endscreen_updateinfo:
    tag ep4_endscreen_updateinfo
    $ ep4_end_update = "Si vous avez téléchargé le Chapitre 5 sous forme de patch, vous pouvez l'installer à partir d'ici (au cas où la mise à jour automatique ne se serait pas effectuée). "
    $ ep4_end_update += "\n\nFichier Patch introuvable. "
    $ ep4_end_update += "\nSi vous avez déjà téléchargé le Chapitre 4 sous forme de Patch, assurez-vous de décompresser le Patch et de placer son contenu dans le dossier du jeu (game/). "

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
                        textbutton "[ep4_end_update]" text_style "task_general_notify"

screen ep4_endscreen_cece:
    tag ep4_endscreen_cece
    if ep4NightChoose == 1:
        add "ep4_es_cece_happy"
    else:
        add "ep4_es_cece_smile"

    if ep4NightChoose == 1:
        $ ep4_end_cece = "Tu es allé te promener la nuit près de la piscine du rez-de-chaussée avec Cece. "
        $ ep4_end_cece += "La situation est devenue plutôt intéressante. "
        if ep4CeceSexTalk == 0:
            $ ep4_end_cece += "\n\nQuand elle t'a demandé si tu avais été avec beaucoup de femmes, tu as répondu sincèrement que tu n'avais été avec personne d'autre depuis Steph. "
        elif ep4CeceSexTalk == 1:
            $ ep4_end_cece += "\n\nQuand elle t'a demandé si tu avais été avec beaucoup de femmes, tu lui as menti en disant que tu n'avais été avec personne d'autre depuis Steph. "
        elif ep4CeceSexTalk == 2:
            $ ep4_end_cece += "\n\nQuand elle t'a demandé si tu avais été avec beaucoup de femmes, tu as répondu oui. "
    else:
        $ ep4_end_cece = "Tu n'es pas allé te promener la nuit avec Cece. "
    if ep4GotCoffee:
        $ ep4_end_cece += "\n\nLe matin, tu lui as apporté du café. "
    else:
        $ ep4_end_cece += "\n\nLe matin, tu ne lui as pas apporté de café. "
    if not ep3RejectedKira:
        $ ep4_end_cece += "\n\nElle a découvert que toi et Kira aviez eu des relations sexuelles la veille. "
        if ep4NightChoose == 1:
            if ep4CeceSexTalk == 1:
                $ ep4_end_cece += "\nElle n'a pas aimé ça. "
            else:
                $ ep4_end_cece += "\nCela ne semblait pas lui importuner tant que ça. "
    $ ep4_end_cece += "\n\nAprès avoir parlé avec Steph, elle t'a conseillé de l'emmener avec toi. "
    if Impact_Steph:
        $ ep4_end_cece += "\nTu as accepté. "
    else:
        $ ep4_end_cece += "\nTu as refusé. "

    if ep4GotRobinsPin:
        $ ep4_end_cece += "\n\nCece a pu jouer à un petit jeu... avec Robin. "
    else:
        $ ep4_end_cece += "\n\nCece n'a pas pu jouer à un petit jeu... avec Robin. "

    if ep4AskedForDawgAutograph:
        $ ep4_end_cece += "\n\nTu as pu obtenir l'autographe de Nite Dawg pour Cece, mais pas la scène bonus. "
#        $ ep4_end_cece += "\n{a=jump:ep4Dawg}Click here{/a} for a preview. "
    else:
        if ep4Dawgs:
            $ ep4_end_cece += "\n\nTu as pu obtenir à la fois l'autographe de Nite Dawg pour Cece et la scène bonus. "
#            $ ep4_end_cece += "\n{a=jump:ep4Dawg}Click here{/a} for a preview. "
        else:
            $ ep4_end_cece += "\n\nTu n'as pas pu obtenir l'autographe de Nite Dawg pour Cece, ni la scène bonus. "
    if ep4CeceBummed:
        $ ep4_end_cece += "\n\nLorsque Cece était déprimée et ne parlait pas, tu n'as pas réussi à la réconforter. "
    else:
        $ ep4_end_cece += "\n\nLorsque Cece était déprimée et ne parlait pas, tu as réussi à la réconforter. "
    if ep4NightChoose == 1:
        $ ep4_end_cece += "Tu as passé la dernière nuit avec Cece. Elle a beaucoup apprécié cela. "

    $ ep4_opportunity_ce = 0
    if ep4NightChoose <> 1:
        $ ep4_opportunity_ce += 1
    else:
        if ep4CeceSexTalk == 1:
            $ ep4_opportunity_ce += 1
    if not ep4GotCoffee:
        $ ep4_opportunity_ce += 1
    if not ep4GotRobinsPin:
        $ ep4_opportunity_ce += 1
    if not ep4Dawgs:
        $ ep4_opportunity_ce += 1
    if ep4CeceBummed:
        $ ep4_opportunity_ce += 1
    if ep4AssgamePink <> "Cece":
        $ ep4_opportunity_ce += 1

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
                        textbutton "[ep4_end_cece]\n\nOptions manquées pour Cece : [ep4_opportunity_ce]" text_style "task_general_notify"

screen ep4_endscreen_kira:
    tag ep4_endscreen_kira
    if ep4NightChoose == 3:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 4:
        add "ep4_es_kira_suspicious"
    else:
        add "ep4_es_kira_smile"

    if ep4NightChoose == 3:
        $ ep4_end_kira = "Tu es allé voir Kira et Robin lors de la première nuit pour discuter de la situation. "
        $ ep4_end_kira += "\n\nAu fond de toi, tu sais que tu n'aimes que Kira et non les deux. "
        $ ep4_end_kira += "\n\nAprès ton voyage, Robin a proposé de se retirer de la relation et de te laisser essayer les choses avec Kira. "
    elif ep4NightChoose == 4:
        $ ep4_end_kira = "Tu es allé voir Kira et Robin lors de la première nuit pour discuter de la situation. "
        $ ep4_end_kira += "\n\nAu fond de toi, tu sais que tu n'aimes que Robin et pas toutes les deux. "
        $ ep4_end_kira += "\n\nAprès ton voyage, Kira a proposé de se retirer de la relation et de te laisser essayer avec Robin. "
    elif ep4NightChoose == 5:
        $ ep4_end_kira = "Tu es allé voir Kira et Robin lors de la première nuit pour discuter de la situation. "
        $ ep4_end_kira += "\n\nTu les apprécies toutes les deux énormément et tu as accepté d'essayer une relation à trois. "
    else:
        $ ep4_end_kira = "Tu n'es pas allé voir Kira et Robin lors de la première nuit. En fait, tu es totalement passé à autre chose. Elles sont tout à fait d'accord pour rester simplement amies."

    $ ep4_opportunity_ki = 0
    if Impact_KiraRobin:
        if ep4NightChoose <> 5:
            $ ep4_opportunity_ki += 1
    else:
        if ep4NightChoose <> 3:
            $ ep4_opportunity_ki += 1
    if ep4AssgameOrange <> "Kira":
        $ ep4_opportunity_ki += 1

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
                        textbutton "[ep4_end_kira]\n\nOptions manquées pour Kira : [ep4_opportunity_ki]" text_style "task_general_notify"

screen ep4_endscreen_lexi:
    tag ep4_endscreen_lexi
    if ep4NightChoose == 2:
        add "ep4_es_lexi_happy"
    else:
        add "ep4_es_lexi_smile"

    if ep4NightChoose == 2:
        $ ep4_end_lexi = "Tu as passé la première nuit avec Lexi dans son studio d'enregistrement. "
        $ ep4_end_lexi += "\n\nAvant d'aller écouter Stephanie, tu l'as rassurée en lui disant que tu n'avais aucun intérêt pour ton ex-petite amie. "
        $ ep4_end_lexi += "\n\nTu as passé une agréable soirée dans les rues de Los Angeles, mangé des sushis, des cupcakes et écouté une sonate en ré majeur en privé. "
        $ ep4_end_lexi += "\n\nLexi a surmonté ses problèmes intimes grâce à toi. "
    else:
        $ ep4_end_lexi = "Tu n'es pas allé avec Lexi la première nuit chez elle. "
    if ep4ToldHollyLike <> 1:
        $ ep4_end_lexi += "\n\nQuand son amie Holly t'a demandé des informations sur Lexi et tes intentions, tu n'as pas été clair dans ta réponse. "
        if ep4ChrisStatus == 1:
            if ep4SetupChrisWith == 4:
                $ ep4_end_lexi += "\n\nTu as essayé de caser Holly avec Chris. "
                if ep4SetupChrisHolly:
                    $ ep4_end_lexi += "\nPeut-être que ça marchera. "
                else:
                    $ ep4_end_lexi += "\nTu a échoué. "
    else:
        $ ep4_end_lexi += "\n\nTu as clairement indiqué tes intentions lorsque son amie, Holly, t'a posé des questions sur Lexi. Tu lui as dit que tu n'avais d'yeux que pour Lexi. "
    if ep4ToldHollyLike == 3:
        if ep4NightChoose == 2:
            $ ep4_end_lexi += "\n\nTu as dit à Holly qu'elle te plaisait. Elle ne savait pas quoi répondre à cela. "
        else:
            $ ep4_end_lexi += "\n\nTu as dit à Holly qu'elle te plaisait. Elle n'y a pas trop pensé au début, mais tu étais dans ses pensées plus tard. "

    $ ep4_opportunity_le = 0
    if ep4NightChoose <> 2:
        $ ep4_opportunity_le += 1
    if ep4ToldHollyLike <> 1:
        $ ep4_opportunity_le += 1
    if not photoop_ep4LexiSushiPic:
        $ ep4_opportunity_le += 1
        if "21;Toi;ep4p2_lexidate47;La plus belle fille du monde." not in nukeStories or "21;Toi;ep4p2_lexidate47;Profiter d'un bon dîner avec Lexi." not in nukeStories:
            $ ep4_opportunity_le += 1
    if ep4AssgameYellow <> "Lexi":
        $ ep4_opportunity_le += 1

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
                        textbutton "[ep4_end_lexi]\n\nOptions manquées pour Lexi : [ep4_opportunity_le]" text_style "task_general_notify"

screen ep4_endscreen_robin:
    tag ep4_endscreen_robin
    if ep4NightChoose == 4:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 3:
        add "ep4_es_robin_sad"
    else:
        add "ep4_es_robin_smile"

    $ ep4_end_robinChris = False
    if ep4NightChoose == 3:
        $ ep4_end_robinChris = True
        $ ep4_end_robin = "Tu es allé voir Kira et Robin lors de la première nuit pour discuter de la situation. "
        $ ep4_end_robin += "\n\nAu fond de toi, tu sais que tu n'aimes que Kira et non les deux. "
        $ ep4_end_robin += "\n\nAprès ton voyage, Robin a proposé de se retirer de la relation et de te laisser essayer les choses avec Kira. "
    elif ep4NightChoose == 4:
        $ ep4_end_robin = "Tu es allé voir Kira et Robin lors de la première nuit pour discuter de la situation. "
        $ ep4_end_robin += "\n\nAu fond de toi, tu sais que tu n'aimes que Robin et pas toutes les deux. "
        $ ep4_end_robin += "\n\nAprès ton voyage, Kira a proposé de se retirer de la relation et de te laisser essayer avec Robin. "
    elif ep4NightChoose == 5:
        $ ep4_end_robin = "Tu es allé voir Kira et Robin lors de la première nuit pour discuter de la situation. "
        $ ep4_end_robin += "\n\nTu les apprécies toutes les deux énormément et tu as accepté d'essayer une relation à trois. "
    else:
        $ ep4_end_robinChris = True
        $ ep4_end_robin = "Tu n'es pas allé voir Kira et Robin lors de la première nuit. En fait, tu es totalement passé à autre chose. Elles sont tout à fait d'accord pour rester simplement amies."

    if ep4_end_robinChris:
        if ep4ChrisStatus == 1:
            if ep4SetupChrisWith == 3:
                $ ep4_end_robin += "\n\nVoyant que Robin ne t'intéresse pas pour toi-même, tu as essayé de caser Chris avec elle. "
                if ep4SetupChrisRobin:
                    $ ep4_end_robin += "\nPeut-être que ça marchera. "
                else:
                    $ ep4_end_robin += "\nTu as échoué. "
            if ep4SetupChrisWith == 2:
                $ ep4_end_robin += "\n\nVoyant que Robin ne t'intéresse pas pour toi-même, tu as essayé de caser Chris avec elle. "
                $ ep4_end_robin += "\nTu as échoué. "

    if ep4GotRobinsPin:
        $ ep4_end_robin += "\n\nTu as réussi à obtenir le code PIN de Robin, et à te venger du fait qu'elle ait battu ton meilleur score. "
    else:
        $ ep4_end_robin += "\n\nTu n'as pas pu obtenir le code PIN de Robin, et te venger du fait qu'elle ait battu ton meilleur score.  "

    $ ep4_opportunity_ro = 0
    if Impact_KiraRobin:
        if ep4NightChoose <> 5:
            $ ep4_opportunity_ro += 1
    else:
        if ep4NightChoose <> 4:
            $ ep4_opportunity_ro += 1
    if not ep4GotRobinsPin:
        $ ep4_opportunity_ro += 1
    if ep4_end_robinChris:
        if ep4ChrisStatus == 1:
            if ep4SetupChrisWith == 1:
                if not ep4SetupChrisRobin:
                    $ ep4_opportunity_ro += 1
    if ep4AssgameGreen <> "Robin":
        $ ep4_opportunity_ro += 1

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
                        textbutton "[ep4_end_robin]\n\nOptions manquées pour Robin : [ep4_opportunity_ro]" text_style "task_general_notify"

screen ep4_endscreen_stephanie:
    tag ep4_endscreen_stephanie
    if Impact_Steph:
        if ep4NightChoose == 7:
            add "ep4_es_steph_happy"
        else:
            add "ep4_es_steph_smile"
    else:
        add "ep4_es_steph_sad"
    if ep4NightChoose == 7:
        $ ep4_end_stephanie = "Tu as décidé de lui envoyer un message dans la nuit pour essayer de vous revoir. "
    else:
        $ ep4_end_stephanie = "Tu ne lui as pas envoyé de message dans la nuit pour essayer de vous revoir. "

    $ ep4_end_stephanie += "\n\nQuand tu as réalisé qu'elle était déjà à Los Angeles, tu es allé la voir. "

    $ ep4_end_stephanie += "\n\nEn la voyant, vous étiez initialement "
    if ep4StephConfrontationMood == 0:
        $ ep4_end_stephanie += "amical"
    elif ep4StephConfrontationMood == 1:
        $ ep4_end_stephanie += "neutre"
    elif ep4StephConfrontationMood == 2:
        $ ep4_end_stephanie += "en colère"
    $ ep4_end_stephanie += ". When she was done talking, you were "
    if ep4StephLeaveMode == 0:
        $ ep4_end_stephanie += "amical"
    elif ep4StephLeaveMode == 1:
        $ ep4_end_stephanie += "neutre"
    elif ep4StephLeaveMode == 2:
        $ ep4_end_stephanie += "en colère"
    $ ep4_end_stephanie += "."

    if ep4StephLeaveMode == 2:
        if Impact_Steph:
            $ ep4_end_stephanie += "\n\nTu as quand même décidé de l'emmener pour le reste du voyage."
        else:
            $ ep4_end_stephanie += "\n\nTu as décidé de ne pas l'emmener pour le reste du voyage."
    else:
        if Impact_Steph:
            $ ep4_end_stephanie += "\n\nTu as quand même décidé de l'emmener pour le reste du voyage."
        else:
            $ ep4_end_stephanie += "\n\nTu as décidé de ne pas l'emmener pour le reste du voyage."

    if not ep4TNDSteph:
        $ ep4_end_stephanie += "\n\nTu ne voulais pas entendre ce qu'elle avait à dire à Action ou Vérité, mini-vérités."

    if ep4NightChoose == 7:
        $ ep4_end_stephanie += "\n\nAprès deux ans de séparation, vous vous êtes enfin remis ensemble. C'était incroyable."
    else:
        if ep4NightChoose == 1:
            if Impact_Steph:
                if ep4StephSunsetChoose:
                    $ ep4_end_stephanie += "\n\nVous étiez nostalgique d'être assis au coucher du soleil avec elle et vous lui avez dit que vous pouviez réparer votre relation avec elle. "
                    $ ep4_end_stephanie += "\nElle a refusé. "
                else:
                    $ ep4_end_stephanie += "\n\nTu as partagé le coucher de soleil avec elle. "

    $ ep4_opportunity_st = 0
    if ep4NightChoose <> 7:
        $ ep4_opportunity_st += 1
    if not Impact_Steph:
        $ ep4_opportunity_st += 1
    else:
        if ep4AssgameBlue <> "Steph":
            $ ep4_opportunity_st += 1
    if not ep4TNDSteph:
        $ ep4_opportunity_st += 1

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
                        textbutton "[ep4_end_stephanie]\n\nOptions manquées pour Stephanie : [ep4_opportunity_st]" text_style "task_general_notify"

screen ep4_endscreen_linda:
    tag ep4_endscreen_linda
    if ep4NightChoose == 6:
        add "ep4_es_linda_happy"
    else:
        add "ep4_es_linda_smile"

    if ep4NightChoose == 6:
        $ ep4_end_linda = "Tu as passé toute la première nuit chez Lexi à vous remémorer et à renouer avec Linda. "
    else:
        $ ep4_end_linda = "Tu n'as pas passé beaucoup de temps avec Linda la première nuit chez Lexi. "
        if ep4ChrisStatus == 1:
            if ep4SetupChrisWith == 1:
                $ ep4_end_linda += "\n\nVoyant que Linda ne t'intéresse pas pour toi-même, tu as essayé de caser Chris avec elle. "
                if ep4SetupChrisLinda:
                    $ ep4_end_linda += "Peut-être que ça marchera. "
                else:
                    $ ep4_end_linda += "Tu as échoué. "

    if ep4SpentNightWithLindaAndChris:
        $ ep4_end_linda += "\n\nLorsque tu as remarqué que Chris était debout, tu l'as inclus dans votre conversation avec Linda. "
    else:
        $ ep4_end_linda += "\n\nTu n'as pas inclus Chris lorsque tu as parlé à Linda. "

    $ ep4_opportunity_li = 0
    if ep4NightChoose <> 6:
        $ ep4_opportunity_li += 1
    else:
        if ep4ChrisStatus == 1:
            if ep4SetupChrisWith == 1:
                if not ep4SetupChrisLinda:
                    $ ep4_opportunity_li += 1

    if not ep4SpentNightWithLindaAndChris:
        $ ep4_opportunity_li += 1
    if ep4AssgamePurple <> "Linda":
        $ ep4_opportunity_li += 1

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
                        textbutton "[ep4_end_linda]\n\nOptions manquées pour Linda : [ep4_opportunity_li]" text_style "task_general_notify"

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
