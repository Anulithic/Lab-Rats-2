# Holds all of the labels for command related actions.

label serum_demand_label(the_person):
    # Description called when you use a girls obedience to have her take a dose of serum for you.

    #TODO: Make this dialogue personality based.
    mc.name "[the_person.title], you're going to drink this for me."
    "You pull out a vial of serum and present it to [the_person.title]."
    the_person.char "What is it for, is it important?"
    mc.name "Of course it is, I wouldn't ask you to if it wasn't."
    "[the_person.title] hesitates for a second, then nods obediently."
    the_person.char "Okay, if that's what you need me to do."
    call give_serum(the_person) from _call_give_serum_17
    #TODO: Add a post-serum bit of dialogue as well.
    return

label wardrobe_change_label(the_person):
    menu:
        "Add an outfit.":
            mc.name "[the_person.title], I've got something I'd like you to wear for me."
            $ renpy.scene("Active")
            call screen outfit_select_manager()
            $ the_person.draw_person()
            if not _return == "No Return":
                $ new_outfit = _return
                menu:
                    "Save as a full outfit.":
                        $ outfit_type = "full"

                    "Save as an underwear set." if new_outfit.is_suitable_underwear_set():
                        $ outfit_type = "under"

                    "Save as an underwear set. (disabled)" if not new_outfit.is_suitable_underwear_set():
                        pass

                    "Save as an overwear set." if new_outfit.is_suitable_overwear_set():
                        $ outfit_type = "over"

                    "Save as an overwear set. (disabled)" if not new_outfit.is_suitable_overwear_set():
                        pass


                $ is_under = False
                $ is_over = False
                if outfit_type == "under":
                    $ is_under = True
                elif outfit_type == "over":
                    $ is_over = True

                if the_person.judge_outfit(new_outfit, as_underwear = is_under, as_overwear = is_over):
                    $ the_person.add_outfit(new_outfit,outfit_type)
                    $ the_person.call_dialogue("clothing_accept")

                else:
                    $ the_person.call_dialogue("clothing_reject")


            else:
                mc.name "On second thought, never mind."

        "Delete an outfit.":
            mc.name "[the_person.title], lets have a talk about what you've been wearing."
            $ renpy.scene("Active")
            call screen outfit_delete_manager(the_person.wardrobe)
            $ the_person.draw_person()
            #TODO: Figure out what happens when someone doesn't have anything in their wardrobe.

        "Wear an outfit right now.":
            mc.name "[the_person.title], I want you to get changed for me."
            $ renpy.scene("Active")
            call screen girl_outfit_select_manager(the_person.wardrobe)
            if _return != "None":
                $ the_person.set_outfit(_return)

            $ the_person.draw_person()
            if the_person.update_outfit_taboos():
                "[the_person.title] seems nervous wearing her new outfit in front of you, but quickly warms up to it."
            the_person.char "Is this better?"
    return

label change_titles_person(the_person):
    menu:
        "Change what you call her (tooltip)Change the title you have for her. This may just be her name, an honorific such as \"Miss.\", or a complete nickname such as \"Cocksleeve\". Different combinations of stats, roles, and personalities unlock different titles.":
            $ title_choice = new_title_menu(the_person)
            if not (title_choice == "Back" or the_person.title == the_person.create_formatted_title(title_choice)):
                "You tell [the_person.name] [the_person.last_name] that you are going to call her [title_choice] instead of [the_person.title]."
                $ the_person.set_title(title_choice)

        "Change what she calls you (tooltip)Change the title she has for you. This may just be your name, an honorific such as \"Mr.Games\", or a complete nickname such as \"Master\". Different combinations of stats, roles, and personalities unlock different titles.":
            $ title_choice = new_mc_title_menu(the_person)
            if not (title_choice == "Back" or the_person.mc_title == title_choice):
                "You tell [the_person.title] to stop calling you [the_person.mc_title] and to refer to you as [title_choice] instead."
                $ the_person.set_mc_title(title_choice)

        "Change how you refer to her (tooltip)Change your possessive title for this girl. A possessive title takes the form \"your employee\", \"your sister\", etc. It can also just be their name repeated. Different combinations of stats, roles, and personalities unlock different titles.":
            $ title_choice = new_possessive_title_menu(the_person)
            if not (title_choice == "Back" or the_person.possessive_title ==  the_person.create_formatted_title(the_person.possessive_title)):
                "You decide to start referring [the_person.name] [the_person.last_name] as [title_choice] instead of [the_person.possessive_title] when you're talking about her."
                $ the_person.set_possessive_title(title_choice)
    return

label demand_touch_label(the_person):
    #TODO: You demand she stays still and lets you touch her. Leads directly into the sex system at a standing massage
    #TODO: Think about what this means for being public/private.
    $ mc.change_energy(-10)
    $ should_be_private = True
    mc.name "All you have to do is relax and stay still. Understood?"
    if the_person.obedience > 140:
        "[the_person.possessive_title] nods obediently."
    else:
        the_person.char "I... Okay. What are you going to do?"
        mc.name "Don't worry, you'll understand soon."
        "[the_person.possessive_title] seems nervous, but follows your instructions for now."

    "You step closer to her and place your hands on her shoulders, rubbing them gently."
    "You slide your hands lower, down her sides and behind her back. You cup her ass with both hands and squeeze."
    if the_person.effective_sluttiness("touching_body") < 0:
        the_person.char "Hey, I..."
        mc.name "I said silent, didn't I?"
        if the_person.obedience > 140:
            the_person.char "I... I'm sorry."
        else:
            "[the_person.possessive_title]'s body is tense as you touch her."
        $ the_person.change_love(-1)
    else:
        "[the_person.title] places her hands in front of her and waits passively as you grope her ass."


    if the_person.has_large_tits():
        "You take your hand off her ass and walk behind her. You cup one of her heavy breasts in one hand, moving the other down between her thighs."
    else:
        "You take your hand off her ass and walk behind her. You grab one of her small tits with one hand and move the other down between her thighs."

    if mc.location.get_person_count() > 1: #We're not in private, give the option to go somewhere quiet.
        $ extra_people_count = mc.location.get_person_count() - 1
        $ the_person.discover_opinion("public sex")
        if the_person.effective_sluttiness("touching_body") < (10 - (the_person.get_opinion_score("public sex" * 5))) and the_person.obedience < 140:
            #She's very embarrassed and _demands_ to go somewhere else
            "[the_person.possessive_title] grabs your hands and glances around nervously."
            the_person.char "[the_person.mc_title], there are people around! If you want me to do this, we need to go somewhere else."
            "She has a fierce look in her eye, like this might be the limit of her obedience."
            menu:
                "Find somewhere quiet.\n{size=22}No interruptions{/size}":
                    mc.name "Alright, come with me."
                    "You take [the_person.title] by her wrist and lead her away."
                    #TODO: have each location have a unique "find someplace quiet" descriptor with a default fallback option
                    "After a couple of minutes searching you find a quiet space with just the two of you."
                    "You don't waste any time getting back to what you were doing, grabbing [the_person.possessive_title]'s tits and groping her ass."

                "Stay where you are.\n{size=22}[extra_people_count] watching{/size}":
                    mc.name "We're going to stay right here."
                    the_person.char "I... No, I'm not going to let you do this!"
                    "She pushes your hands away from her and steps back, glaring at you."
                    "After a moment [the_person.title] seems almost as shocked by her actions as you are. She glances around, then looks down at the ground, as if embarrassed."
                    $ the_person.change_happiness(-5)
                    $ the_person.change_love(-2)
                    $ the_person.change_obedience(-2)
                    the_person.char "I'm sorry, I just can't do it."
                    return

        elif the_person.effective_sluttiness("touching_body") < (30 - (the_person.get_opinion_score("public sex" * 5))):
            #She's embarrassed by it and demands to go somewhere else. If she's v
            "[the_person.possessive_title] looks around nervously."
            the_person.char "[the_person.mc_title], there are other people looking. Could we please find somewhere private?"
            menu:
                "Find somewhere quiet.\n{size=22}No interruptions{/size}":
                    mc.name "Alright, come with me."
                    "You take [the_person.title] by her wrist and lead her away."
                    #TODO: have each location have a unique "find someplace quiet" descriptor with a default fallback option
                    "After searching for a couple of minutes you find a quiet space with just the two of you."
                    "You don't waste any time getting back to what you were doing, grabbing [the_person.possessive_title]'s tits and groping her ass."

                "Stay where you are.\n{size=22}[extra_people_count] watching{/size}":
                    mc.name "We're going to stay right here."
                    the_person.char "But people are watching, and..."
                    mc.name "I don't care if they're watching."
                    $ the_person.change_arousal(5 * the_person.get_opinion_score("being submissive"))
                    $ the_person.change_love(-1 + the_person.get_opinion_score("being submissive"))
                    $ the_person.change_slut_temp(1)
                    $ should_be_private = False

        else:
            #She's fine with it, but we'll give you the option anyways.
            "There are other people around, but [the_person.possessive_title] either doesn't care or is too determined to follow your instructions exactly."
            menu:
                "Find somewhere quiet.\n{size=22}No interruptions{/size}":
                    mc.name "Come with me, I don't want to be interrupted."
                    "You take [the_person.title] by the wrist and lead her away. She follows without question."
                    "After searching for a couple of minutes you find a quiet space with just the two of you."
                    "You don't waste any time getting back to what you were doing, grabbing [the_person.possessive_title]'s tits and groping her ass."

                "Stay where you are.\n{size=22}[extra_people_count] watching{/size}":
                    $ should_be_private = False


    if the_person.has_taboo("touching_body"):
        $ the_person.call_dialogue("touching_body_taboo_break") #TODO: Have a variant when a person is being _commanded_ instead of seduced.
        $ the_person.break_taboo("touching_body")


    if prostitute_role in the_person.special_role:
        the_person.char "We can continue what you started, but it would cost you two hundred dollars."
        menu:
            "Pay her. -$200":
                $ mc.business.funds += -200
                $ the_person.change_obedience(1)
                call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_45
            "No":
                mc.name "Thanks for the offer, but no thanks."
                "She shrugs."
                the_person.char "Your loss."
    else:
        call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_44

        $ the_person.review_outfit()
    return

init -3 python:
    def demand_strip_tits_requirement(the_person):
        if the_person.outfit.tits_visible():
            return False #Can't strip if they're already visible
        elif the_person.obedience < 130:
            return "Requires: 130 Obedience"
        else:
            return True

    def demand_strip_underwear_requirement(the_person):
        if the_person.outfit.tits_visible() or the_person.outfit.vagina_visible():
            return False #Can't strip if we're already past underwear
        elif the_person.outfit.wearing_panties() and not the_person.outfit.panties_covered() and the_person.outfit.wearing_bra() and not the_person.outfit.bra_covered():
            return False #Can't strip if we can already see all of her underwear.
        elif the_person.obedience < 130:
            return "Requires: 130 Obedience"
        else:
            return True

    def demand_strip_naked_requirement(the_person):
        if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible():
            return False
        elif the_person.obedience < 160:
            return "Requires: 160 Obedience"
        else:
            return True

    def build_demand_strip_menu(the_person):
        demand_strip_tits_action = Action("Get your tits out.", demand_strip_tits_requirement, "demand_strip_tits_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Have her strip down until you can see her tits.")
        demand_strip_underwear_action = Action("Strip to your underwear.", demand_strip_underwear_requirement, "demand_strip_underwear_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Have her strip down until she's only in her underwear.")
        demand_strip_naked_action = Action("Get naked.", demand_strip_naked_requirement, "demand_strip_naked_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Have her strip until she is completely naked.")
        return ["Strip Command", demand_strip_tits_action, demand_strip_underwear_action, demand_strip_naked_action, ["Never mind", "Return"]]


label demand_strip_label(the_person):
    #TODO: Command her to "Get into your underwear", "Show me your tits", or "Get naked"
    # the_person.effective_sluttiness("bare_tits")
    # the_person.effective_sluttiness("underwear_nudity")
    # the_person.effective_sluttiness(["bare_tits", "bare_pussy"])


    call screen main_choice_display(build_menu_items([build_demand_strip_menu(the_person)]))
    if _return != "Return": #Just return, we either don't want to select any of these options, or we _can't_
        $ _return.call_action()

    return

label demand_strip_tits_label(the_person):
    #TODO: Most of this dialogue should be moved into a personality specific branch. A task for next update.
    mc.name "You're going to get your tits out for me."
    $ strip_list = the_person.outfit.get_tit_strip_list()
    $ first_item = strip_list[0]
    if the_person.effective_sluttiness("bare_tits") < (40 - (5*the_person.get_opinion_score("showing her tits"))): # She wouldn't normally show off her tits.
        $ the_person.discover_opinion("showing her tits")
        if mc.location.get_person_count() > 1: #We're in public, so she's shy.
            "[the_person.possessive_title] looks around nervously, then back at you."
            the_person.char "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private.":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're finally alone she moves to pull off her [first_item.display_name] for you."


                "Stay right here." if the_person.obedience >= 140:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to pull off her [first_item.display_name] for you."

                "Stay right here.\nRequires: 140 Obedience (disabled)" if the_person.obedience < 140:
                    pass
            call top_strip_description(the_person, strip_list) from _call_top_strip_description


        else:
            #We're in private, so she's a little more brave. If she loves you she might even do it for fun
            if the_person.effective_sluttiness("bare_tits") + the_person.love < (40 - (5*the_person.get_opinion_score("showing her tits"))):
                #Pure Obedience going on
                "[the_person.possessive_title] seems uncomfortable, but without hesitation begins to take off her [first_item.display_name]."

            else:
                #She loves you, this is just cutting to the chase.
                "[the_person.possessive_title] nods obediently and begins to take off her [first_item.display_name] while you watch."
            call top_strip_description(the_person, strip_list) from _call_top_strip_description_1

    else:
        # She doesn't have any problem showing off her tits, so she doesn't care if she's in public or not.
        $ the_person.discover_opinion("showing her tits")
        the_person.char "Oh, is that all?"
        if mc.location.get_person_count() > 1:
            "[the_person.possessive_title] doesn't seem to care about the other people around and starts to pull off her [first_item.display_name] right away."
        else:
            "[the_person.possessive_title] starts to pull off her [first_item.display_name] right away."
        call top_strip_description(the_person, strip_list) from _call_top_strip_description_2


    if the_person.update_outfit_taboos() or the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("showing her tits"))): # She's shy
        "[the_person.title] brings her hands up to cover her breasts."
        the_person.char "Are we done?"
        mc.name "I want to get a look first, and I can't see anything if you're hiding everything like this."
        "She nods and moves her hands to her side again. She blushes and looks away as you oggle her tits."
        $ the_person.change_slut_temp(1+ the_person.get_opinion_score("showing her tits"))
        $ the_person.change_happiness(-2 + the_person.get_opinion_score("showing her tits"))
        "When you've seen enough you give her an approving nod. She sighs and moves towards her clothes."
        the_person.char "Can get dressed now?"
    else: # She's into it
        $ the_person.draw_person(the_animation = blowjob_bob) #TODO Make sure this effect looks right
        "[the_person.title] places her hands behind her and bounces on her feet, jiggling her tits for your amusement."
        "When you've seen enough you nod approvingly. [the_person.possessive_title] smiles happily."
        the_person.char "So you want me to get dressed again?"

    menu:
        "Let her get dressed.":
            mc.name "Yeah, you can."
            "You watch her put her clothes back on, covering up her tits."
            $ the_person.apply_outfit(the_person.planned_outfit)
            $ the_person.draw_person()

        "Keep your tits out.":
            mc.name "I think you look good with your tits out. Stay like this for a while, okay?"
            if the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("showing her tits"))):
                the_person.char "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut_temp(1)
                $ the_person.change_happiness(-2)
            else:
                the_person.char "Okay, if that's what you want me to do [the_person.mc_title]."
    return

label top_strip_description(the_person, strip_list):
    #Helper label for demand_strip_tits
    python:
        for item_to_strip in strip_list:
            the_person.draw_animated_removal(item_to_strip)
            if item_to_strip == strip_list[-1]: #Special line for the last item.
                if the_person.has_large_tits():
                    renpy.say("","She pulls off her " + item_to_strip.display_name + ", letting her tits spill out.")
                else:
                    renpy.say("","She pulls off her " + item_to_strip.display_name + ", revealing her cute tits.")
            else:
                renpy.say ("","")
    return

label underwear_strip_description(the_person):
    python:
        the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
        while the_person.outfit.bra_covered() and the_item is not None:
            the_person.draw_animated_removal(the_item)
            the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)

        the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
        while the_person.outfit.panties_covered() and the_item is not None:
            the_person.draw_animated_removal(the_item)
            the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)

        renpy.say("",the_person.possessive_title + " strips off her " + the_item.display_name + ", leaving her wearing only her underwear.") #TODO: Generalize these kinds of strip functions.

    return

label naked_strip_description(the_person): #TODO: Generalize these
    python:
        the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
        while the_item is not None and not the_person.outfit.tits_visible():
            the_person.draw_animated_removal(the_item)
            if the_person.outfit.tits_visible():
                renpy.say("",the_person.possessive_title + " pulls her tits out from her " + the_item.display_name + ", putting them on display for you.")
            the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)



        the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
        while the_item is not None and not the_person.outfit.vagina_visible():
            the_person.draw_animated_removal(the_item)
            if the_person.outfit.vagina_visible():
                renpy.say("",the_person.possessive_title + " peels off her " + the_item.display_name + ", revealing her cute little pussy.")
            the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
    return

label demand_strip_underwear_label(the_person):
    mc.name "You're going to strip into your underwear for me."
    if not the_person.outfit.wearing_panties() or not the_person.outfit.wearing_bra():
        the_person.char "I can't do that [the_person.mc_title]."
        mc.name "Yes you can, you..."
        "She interrupts you."
        if not the_person.outfit.wearing_panties() and not the_person.outfit.wearing_bra():
            the_person.char "No, I can't show you my underwear because... I'm not wearing any."
        elif not the_person.outfit.wearing_panties():
            the_person.char "No, I can't show you my underwear because... I'm not wearing any panties."
        else:
            the_person.char "No, I can't show you my underwear because... I'm not wearing a bra in the first place."
        mc.name "Well, that's as good a reason as any."
        return

    if mc.location.get_person_count() > 1: #You aren't alone.
        if the_person.effective_sluttiness("underwear_nudity") < (40 - (5*the_person.get_opinion_score("lingerie"))): #She's shy and wants to go somewhere private
            "[the_person.possessive_title] looks around nervously, then back at you."
            the_person.char "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private.":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to pull off her clothes for you."


                "Stay right here." if the_person.obedience >= 140:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to pull off her clothes."

                "Stay right here.\nRequires: 140 Obedience (disabled)" if the_person.obedience < 140:
                    pass

        else: #She's into it
            "[the_person.possessive_title] nods obediently, seemingly unbothered by your command."


        call underwear_strip_description(the_person) from _call_underwear_strip_description


    else: #You are alone
        if the_person.effective_sluttiness("underwear_nudity") < (40 - (5*the_person.get_opinion_score("lingerie"))): #She's shy
            "[the_person.possessive_title] seems uncomfortable, but she nods obediently and starts to pull off her clothes."

        else: #She's into it.
            the_person.char "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."

        call underwear_strip_description(the_person) from _call_underwear_strip_description_1

    if the_person.update_outfit_taboos() or the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("lingerie"))): # She's shy
        the_person.char "Um... So what do we do now?"
        mc.name "Just relax and let me take a look. You look cute."
        "She nods and puts her hands behind her back. She blushes and looks away self-conciously as you oggle her."
        $ the_person.change_slut_temp( 1+ the_person.get_opinion_score("lingerie"))
        $ the_person.change_happiness(-2 + the_person.get_opinion_score("lingerie"))
        mc.name "Let me see what it looks like from behind."
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] spins around obediently."
        "You enjoy the view for a little while longer. [the_person.possessive_title] seems anxious to cover up again."
        the_person.char "Can I get dressed now?"
        $ the_person.draw_person()


    else:
        "[the_person.title] immediately puts her hands behind her back and pushes her chest forward, accentuating her tits."
        the_person.char "So, what do you think? Does my underwear look good?"
        mc.name "I does, you look cute."
        "She smiles and gives you a spin, letting you take a look at her from behind."
        $ the_person.draw_person(position = "back_peek")
        "You enjoy the view for a little while longer, then nod approvingly to [the_person.possessive_title]."
        $ the_person.draw_person()
        the_person.char "Would you like me to get dressed again?"

    menu:
        "Let her get dressed.":
            mc.name "Yeah, you can."
            "You watch her put her clothes back on."
            $ the_person.apply_outfit(the_person.planned_outfit)
            $ the_person.draw_person()

        "Stay in your underwear.":
            mc.name "Your underwear is too cute to hide it away, you should should stay in it for a while."
            if the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("lingerie"))):
                the_person.char "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut_temp(1)
                $ the_person.change_happiness(-2)
            else:
                the_person.char "Okay, if that's what you want me to do [the_person.mc_title]."
    return

label demand_strip_naked_label(the_person):
    if mc.location.get_person_count() > 1: #Other people are around
        if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) < (80 - (5*the_person.get_opinion_score("not wearing anything"))): #She's shy and wants to go somewhere private
            "[the_person.possessive_title] looks around nervously, then back at you."
            the_person.char "But... Here? I don't want to get naked in front of other people."
            menu:
                "Find somewhere private.":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to strip down immediately."


                "Stay right here." if the_person.obedience >= 170:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to strip down."

                "Stay right here.\nRequires: 140 Obedience (disabled)" if the_person.obedience < 170:
                    pass
        else:
            "[the_person.possessive_title] nods and starts to enthusiastically strip down."

    else:
        if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) < (80 - (5*the_person.get_opinion_score("not wearing anything"))): #She's shy
            "[the_person.possessive_title] seems uncomfortable, but she nods obediently and starts to pull off all her clothes."


        else:
            the_person.char "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."

    call naked_strip_description(the_person) from _call_naked_strip_description

    if the_person.update_outfit_taboos() or the_person.effective_sluttiness() < (80 - (5*the_person.get_opinion_score("not wearing anything"))): # She's shy
        the_person.char "What would you like me to do now?"
        "She instinctively puts her hands behind her back while she waits for your instructions."
        mc.name "Give me a spin, I want to see your ass."
        "She blushes, but nods and turns around."
        $ the_person.draw_person(position = "back_peek")
        "[the_person.possessive_title] waits patiently until you signal for her to turn around again."
        $ the_person.draw_person()
        the_person.char "Are we finished? Is that all?"

    else:
        "[the_person.title] puts her hands behind her back and pushes her chest forward, accentuating her tits."
        "She waits silently for you to tell her what to do. You notice her nipples harden as you watch her."
        mc.name "Do you like this?"
        #TODO: THis should probably include dialogue based on their being naked opinions.
        the_person.char "If I'm doing it for you I do."
        mc.name "Good. Turn around, I want to see your ass."
        "She nods happily and turns around, wiggling her butt for you."
        $ the_person.draw_person(position = "back_peek")
        "You enjoy the view until you're satisfied."
        mc.name "Okay, turn around again."
        $ the_person.draw_person()
        theperson.char "Is there anything else, [the_person.mc_title]?"

    menu:
        "Let her get dressed.":
            mc.name "I've seen enough. You can get dressed."
            "You watch her as she gets dressed again."
            $ the_person.apply_outfit(the_person.planned_outfit)
            $ the_person.draw_person()

        "Keep her naked.":
            mc.name "Your body is way too nice looking to hide away. Stay like this for a while."
            if the_person.effective_sluttiness() < (80 - (5*the_person.get_opinion_score("not wearing anything"))):
                the_person.char "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut_temp(1)
                $ the_person.change_happiness(-2)
            else:
                the_person.char "Okay, if that's what you want me to do [the_person.mc_title]."
                "[the_person.title] doesn't seem to mind."
    return
