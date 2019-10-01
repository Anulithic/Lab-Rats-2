﻿## This file holds all of the descriptions for the crises that can (and will) arise during play.
## They are instances of the Action class and hold:
## 1) A name and/or short description. Unlikely to ever be publically shown for these events
## 2) A requirement function. Used to determine if the crisis is possible.
## 3) An effect label. Points towards a label that will run the actual event, compute final effects, and take input from the player.


## Potential new crises ##
# Lily is going on a date. Forbid her, help her dress, fuck her first, etc.
# Girl is seen not wearing uniform - Leads to potential for punishment (level of punishment might depeond on other corporate policies)
# Catch someone sneaking into work late.
# Catch someone slacking.
# Catch someone sneaking serum doses out of the lab! (Test it on them as punishment).
# Expand the existing crises with more options and levels, ect. (Tax option is top priority)
# Bulk order demand for a large number of a single type of serum comes in (10 + 2*diff) due in 7 days.
# Walk past one of your girls bending over. Quick check to see if you just pass by, slap her ass, or pull down her pants and fuck her.
# You're horny at work and can't get anything done. Jerk off or call someone in to help you.
#


#We want to add more at home morning crises so that we don't have the same ones triggering over and over
#We want more crises that deal with other characters in the game
#We want to figure out how we're going to do "one off" on enter crises, like walking in on a girl masturbating.


## Potential Policies ##
# Optional in house serum testing - Gives the ability to give girls serum, for a cash reward.
# Business size policies - Increase the total number of employees you can have working for you at once.
# Efficency policies - Lets you increase the general efficency of your company, making HR even more useful.
# R&D connections - Unlocks certain key traits for R&D (ie. game is gated behind earning money).
# Discount suppliers - Decreases price paid for serum supplies.



### LIST OF CURRENT CRISES IN EXISTANCE ###
# Broken AC
# Free drink sneak
# Girl out of uniform
# Office flirt
# Special Training Opportunity
# Lab exposure incident
# production exposure incident
# Water Spill on shirt
# home fuck/visit
# Cat fight
# Investment Opportunity
# Mastery Boost
# Random trait for side effect
# Mom changing
# Lily new underwear
# Mom selfies
# Daughter introduction

#todo: teach lily hoqw to deepthroat/ role to teach her how to fuck
#todo: girl who loves you sends you sexy selfies
#todo: Lily invites you to a university party as her +1.


### SPECIAL CRISES ###
# New serum creation
# Girl quitting
# No research reminder

### MORNING CRISES ###
# Mom morning suprise
# Lily morning encounter
# Family Breakfast


## Crises are stored in a weighted list, to be polled each turn to see if something triggers (and if so, what).


######################
## BUSSINESS CRISES ##
######################
init 1 python:
    crisis_list = [] #To be filled with tuples of [Action, weight]. Weights are relative to other entries in the list.
    morning_crisis_list = [] #Morning crises are called when a new day starts. They are for events that take place after the MC has been able to rest and is at home.

    def in_research_with_other(): #A common requirement check, the PC is in the office (not nessesarily the lab), during work hours, with at least one other person.
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            if mc.is_at_work(): #Check to see if the main character is at work
                if len(mc.business.research_team) > 0: #Check to see if there's at least one person in the research team team at work and that something is being researched.
                        return True
        return False

    def in_production_with_other():
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            if mc.is_at_work(): #Check to see if the main character is at work
                if len(mc.business.production_team) > 0: #Check to see if there's at least one person in the research team team at work and that something is being researched.
                        return True
        return False

    def anyone_else_in_office(): #Returns true if there is anyone else at work with the mc.
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if mc.business.get_employee_count() > 0:
                    return True
        return False

    def mc_asleep(): #Returns true if the main character is at home and in bed.
        if time_of_day == 4: #It has to be after work, right when you've gone to bed.
            if mc.location == bedroom:
                return True
        return False

    def mc_at_home(): #Returns true if the main character is inside their house, anywhere.
        if mc.location == hall or mc.location == bedroom or mc.location == lily_bedroom or mc.location == mom_bedroom or mc.location == kitchen:
            return True
        return False

    #Defining the requirement to be tested.
    def broken_AC_crisis_requirement():
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            if mc.is_at_work(): #Check to see if the main character is at work
                if len(mc.business.production_team) > 0: #Check to see if there's at least one person in the production team at work.
                    return True
        return False

    broken_AC_crisis = Action("Crisis Test",broken_AC_crisis_requirement,"broken_AC_crisis_label")
    crisis_list.append([broken_AC_crisis,5])


label broken_AC_crisis_label:
    $ temp_sluttiness_increase = 20 #This is a bonus to sluttiness when stripping down because of the heat.

    "There is a sudden bang in the office, followed by a strange silence. A quick check reveals the air conditioning has died!"
    "The machines running at full speed in the production department kick out a significant amount of heat. Without air condition the temperature quickly rises to uncomfortable levels."
    $ mc.business.p_div.show_background()
    #We're going to use the most slutty girl of the group lead the pack. She'll be the one we pay attention to.
    python:
        the_person = None
        for girl in mc.business.production_team:
            if not the_person:
                the_person = girl
            else:
                if girl.sluttiness > the_person.sluttiness:
                    the_person = girl
    $ the_person.draw_person()
    if len(mc.business.production_team) == 0:
        $ sole_worker = mc.business.production_team[0].name
        "The air conditioner was under warranty, and a quick call has one of their repair men over in a couple of hours. Until then [sole_worker] wants to know what to do."
    else:
        "The air conditioner was under warranty, and a quick call has one of their repair men over in a couple of hours. Until then, the production staff want to know what to do."

    menu:
        "Take a break.":
            "You tell everyone in the production lab to take a break for a few hours while the air conditioning is repaired."
            "The unexpected break raises moral and makes the production staff feel more independent."
            python:
                for person in mc.business.production_team:
                    person.change_happiness(5)
                    person.change_obedience(-2)
            "The repair man shows up early and it turns out to be an easy fix. The lab is soon back up and running."

        "It's not that hot, get back to work!":
            "Nobody's happy working in the heat, but exercising your authority will make your production staff more likely to obey in the future."
            python:
                for person in mc.business.production_team:
                    person.change_happiness(-5)
                    person.change_obedience(2)
            "The repair man shows up early and it turns out to be an easy fix. The lab is soon back up and running."

        "Tell everyone to strip down and keep working." if casual_uniform_policy.is_owned():
            if len(mc.business.production_team) > 1: #We have more than one person, do a group strip scene.
                mc.name "I know it's uncomfortable in here right now, but we're just going to have to make due."
                mc.name "If anyone feels the need to take something off to get comfortable, I'm lifting the dress code until the air conditioning is fixed."

                if the_person.sluttiness < 20: #TODO: Link this to personalities somehow.
                    the_person.char "He's got a point girls. Come on, we're all adults here."
                elif the_person.sluttiness < 60:
                    the_person.char "He's got a point girls. I'm sure we've all shown a little bit of skin before anyways, right?"
                else:
                    the_person.char "Let's do it girls! I can't be the only one who loves an excuse to flash her tits, right?"

            else: #There's just one person here, have them strip down.
                $ the_person = mc.business.production_team[0] #Get the one person, the crisis requires we have at least 1 person in here so this should always be true.
                $ the_person.draw_person()
                mc.name "[the_person.title], I know it's uncomfortable in here right now, but we're going to have to make due."
                mc.name "If you feel like it would help to take something off, I'm lifting the dress code until the air condition is fixed."
                if the_person.sluttiness < 20:
                    the_person.char "Taking some of this off would be a lot more comfortable..."
                else:
                    the_person.char "I might as well, a little skin never hurt anyone, right?"

            #First, we'll get a copy of the lead girls outfit to use as a tester.
            $ test_outfit = the_person.outfit.get_copy()
            $ removed_something = False

            $ the_clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True) #Remove something from our test outfit.
            while the_clothing and the_person.judge_outfit(test_outfit, temp_sluttiness_increase): #This will loop over and over until she is out of things to remove OR nolonger can strip something that is appropriate.
                #Note: there can be some variation in this event depending on if the upper or lower was randomly checked first.
                $ the_person.draw_animated_removal(the_clothing) #Draw the item being removed from our current outfit
                $ the_person.outfit = test_outfit.get_copy() #Swap our current outfit out for the test outfit.
                $ random_strip_descrip = renpy.random.randint(0,4)
                if random_strip_descrip == 0 or not removed_something:
                    "[the_person.title] pulls off her [the_clothing.name] and puts it aside." #Always called first.
                elif random_strip_descrip == 1:
                    "[the_person.title] takes off her [the_clothing.name] and adds it to the pile of clothing."
                elif random_strip_descrip == 2:
                    "[the_person.title] strips off her [the_clothing.name] and tosses it to the side."
                elif random_strip_descrip == 3:
                    "[the_person.title] removes her [the_clothing.name] and tosses it with the rest of her stuff."
                else: # random_strip_descrip == 4:
                    "[the_person.title] quickly slides off her [the_clothing.name] and leaves it on the ground."
                $ removed_something = True
                $ the_clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)

            if removed_something:
                if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible():
                    "Once she's done stripping [the_person.possessive_title] is practically naked."
                elif the_person.outfit.tits_visible():
                    "Once she's done stripping [the_person.possessive_title] has her nice [the_person.tits] tits out on display."
                elif the_person.outfit.vagina_visible():
                    "Once she's done stripping [the_person.possessive_title] has her pretty little pussy out on display for everyone."
                else:
                    "[the_person.possessive_title] finishes stripping and looks back at you."
                the_person.char "Ahh, that's a lot better."
            else:
                "[the_person.possessive_title] fiddles with some of her clothing, then shrugs."
                the_person.char "I'm not sure I'm comfortable taking any of this off... I'm sure I'll be fine in the heat for a little bit."

            if len(mc.business.production_team) > 1:
                if removed_something:
                    "The rest of the department follows the lead of [the_person.title], stripping off various amounts of clothing."
                        #Gives you the chance to watch one of the other girls in the department strip.
                    $ list_of_other_girls = list(mc.business.production_team)
                    $ list_of_other_girls.remove(the_person) #We already watched her strip.
                    call screen person_choice(list_of_other_girls, person_prefix = "Watch", person_suffix = "Strip.")
                    $ girl_choice = _return

                        # strip_watch_list = format_person_list(list_of_other_girls)
                        # for a_choice in strip_watch_list:
                        #     a_choice[0] = "Watch " + a_choice[0] + " Strip."
                        # girl_choice = renpy.display_menu(strip_watch_list)
                        # girl_choice.draw_person()
                    "You pay special attention to [girl_choice.title] as she follows the lead of [the_person.possessive_title]."
                    $ test_outfit = girl_choice.outfit.get_copy()
                    $ removed_something = False

                    $ the_clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True) #Remove something from our test outfit.
                    while the_clothing and girl_choice.judge_outfit(test_outfit, temp_sluttiness_increase): #This will loop over and over until she is out of things to remove OR nolonger can strip something that is appropriate.
                        #Note: there can be some variation in this event depending on if the upper or lower was randomly checked first.
                        $ girl_choice.draw_animated_removal(the_clothing) #Animate the removal.
                        $ girl_choice.outfit = test_outfit.get_copy() #Swap outfits so we can keep updating
                        $ random_strip_descrip = renpy.random.randint(0,4)
                        if random_strip_descrip == 0 or not removed_something:
                            "[girl_choice.title] pulls off her [the_clothing.name] and puts it aside." #Always called first.
                        elif random_strip_descrip == 1:
                            "[girl_choice.title] takes off her [the_clothing.name] and adds it to the pile of clothing."
                        elif random_strip_descrip == 2:
                            "[girl_choice.title] strips off her [the_clothing.name] and tosses it to the side."
                        elif random_strip_descrip == 3:
                            "[girl_choice.title] removes her [the_clothing.name] and tosses it with the rest of her stuff."
                        else: # random_strip_descrip == 4:
                            "[girl_choice.title] quickly slides off her [the_clothing.name] and leaves it on the ground."
                        $ removed_something = True
                        $ the_clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)

                    if removed_something:
                        if girl_choice.outfit.tits_visible() and girl_choice.outfit.vagina_visible():
                            "Once she's done stripping [girl_choice.possessive_title] is practically naked."
                        elif girl_choice.outfit.tits_visible():
                            "Once she's done stripping [girl_choice.possessive_title] has her nice [girl_choice.tits] tits out on display."
                        elif girl_choice.outfit.vagina_visible():
                            "Once she's done stripping [girl_choice.possessive_title] has her pretty little pussy out on display for everyone."
                        else:
                            "[girl_choice.possessive_title] finishes stripping and looks at [the_person.title]."
                        girl_choice.char "Ahh, that's a lot better."
                        $ slut_report = girl_choice.change_slut_temp(10)
                        if girl_choice.sluttiness < 40:
                            "[girl_choice.title] definitely saw you watching her as she stripped. She looks at you and blushes slightly and avoids making eye contact."
                        else:
                            $ girl_choice.change_love(2)
                            "[girl_choice.title] definitely saw you watching her as she stripped. She looks at you and gives a quick wink before turning back to [the_person.title]."
                    else:
                        "[girl_choice.title] fiddles with some of her clothing, then shrugs meekly."
                        girl_choice.char "I'm not sure I'm comfortable taking any of this off... I'm sure I'll be fine in the heat for a little bit."



                    "The girls laugh and tease each other as they strip down, and they all seem to be more comfortable with the heat once they are less clothed."
                    "For a while all of the girls work in various states of undress while under your watchful eye."
                    "The repair man shows up early, and you lead him directly to the the AC unit. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."
                else:
                    "The other girls exchange glances, and everyone seems decides it's best not to take this too far."
                    "They get back to work fully dressed, and soon the repair man has shown up. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."
            else:
                if removed_something:
                    "[the_person.title] gets back to work. Working in her stripped down attire seems to make her more comfortable with the idea in general."
                    "The repair man shows up early, and you lead him directly to the AC unit. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."
                else:
                    "[the_person.title] gets back to work, still fully clothed."
                    "The repair man shows up early, and you lead him directly to the the AC unit. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."

            if removed_something:
                python:
                    for person in mc.business.production_team:
                        person.change_slut_temp(10, add_to_log = False)
                $ mc.log_event("All Production Staff: +10 Sluttiness","float_text_pink")

        "Tell everyone to strip down and keep working.\n{size=22}Requires: [casual_uniform_policy.name] (disabled)" if not casual_uniform_policy.is_owned():
            pass
    $renpy.scene("Active")
    return

init 1 python:
    def get_drink_crisis_requirement():
        if anyone_else_in_office():
            if len(mc.location.people) > 0: #We want this to trigger when the mc is at work and there's someone else in the room.
                return True
        return False

    get_drink_crisis = Action("Getting a Drink", get_drink_crisis_requirement, "get_drink_crisis_label")
    crisis_list.append([get_drink_crisis,5])


label get_drink_crisis_label():
    if not get_drink_crisis_requirement():
        return #Return if we don't still meet the same requirements, because something must have changed because of a different event.

    #Lets get the girl of interest.
    $ the_person = get_random_from_list(mc.location.people)

    "After working for a few minutes you decide to take a five minute break and get a drink. You stand up to go and find some coffee."
    $ the_person.draw_person()
    the_person.char "Stretching your legs?"
    mc.name "Yeah, I was going to get some coffee. Do you want anything?"
    $ coffee = get_random_coffee_style()
    the_person.char "Sure. [coffee], please."
    $ renpy.scene("Active")
    "You nod and head to the little break room in the office. It doesn't take you long to have both of your drinks made up."
    menu:
        "Add a dose of serum to [the_person.title]'s drink.":
            call give_serum(the_person) from _call_give_serum_1
            $ the_person.draw_person(emotion = "happy")
            "Once you're finished making your drinks you head back to the office. You put [the_person.title]'s coffee down in front of her."
            the_person.char "Thanks [the_person.mc_title]."
            mc.name "No problem at all."
            $ renpy.scene("Active")


        "Leave her drink alone.":
            "You decide not to test a dose of serum out on [the_person.title] and take the drinks back."


    return

init 1 python:
    def no_uniform_punishment_requirement():
        if mc.business.get_employee_count() > 0:
            if mc.business.is_open_for_business() and mc.is_at_work():
                for person in mc.business.get_employee_list():
                    if person.obedience < 110: #Only triggers on disobedient characters, so make sure we have some.
                        if mc.business.get_uniform_wardrobe(mc.business.get_employee_title(person)).get_count()>0: #Make sure that person has a uniform assigned for their department
                            return True
        return False

    no_uniform_punishment_crisis = Action("Not In Uniform Crisis", no_uniform_punishment_requirement, "no_uniform_punishment_label")
    crisis_list.append([no_uniform_punishment_crisis,5])

label no_uniform_punishment_label():
    if mc.business.get_employee_count() <= 0:
        return #We must have fired someone in another crisis, so don't run this because there might not be anyone.

    python:
        disobedient_people = []
        for person in mc.business.get_employee_list():
            if person.obedience < 110:
                if mc.business.get_uniform_wardrobe(mc.business.get_employee_title(person)).get_count()>0: #Make sure we're getting only people who should be wearing a uniform.
                    disobedient_people.append(person)
        the_person = get_random_from_list(disobedient_people)


    if the_person is None:
        "Test"
        return #We must have fixed up any obedience problems, they'll all be in uniform.
    else:
        $ the_person.outfit = the_person.planned_outfit.get_copy() #Put them in their non-work outfit.

    "You decide to take a break and stretch your legs. You start walking around the office, peeking in on your different divisions. You turn a corner and run into [the_person.title]."
    $ the_person.draw_person()
    the_person.char "Oh, hey [the_person.mc_title]. I was just getting back to work."
    mc.name "Shouldn't you be in your uniform [the_person.title]?"
    $ random_excuse = renpy.random.randint(0,2) #Get a random excuse for why she's not wearing her uniform.
    if random_excuse == 0:
        the_person.char "I'm sorry, I just had to step out for a moment to pick something up. I was assuming that wouldn't be a problem."
    elif random_excuse == 1:
        the_person.char "It's just so impractical though, I was hoping I could just wear this for a few hours and try and get some real work done."
    else: # random_excuse == 2:
        the_person.char "I mean, that uniform policy was just a suggestion, right? There's no way you expect us to actually wear it all the time."

    $ pay_percent = int(the_person.salary*0.1)
    menu:
        "Let it go.":
            mc.name "The uniform policy isn't just a suggestion, if you're on the clock you need to be dressed appropriately. Go get changed."
            "She nods and starts to walk off."
            $ the_person.change_obedience(-2)
            the_person.char "I'll take care of it boss, it won't happen again."

        "Punish her.":
            mc.name "The uniform policy isn't just a suggesiton. When you're on the clock you're the face of this company, which means I expect you to be in uniform."
            menu:
                "Lecture her.":
                    "You shake your head, disappointed."
                    mc.name "You should know better than this [the_person.title], I honestly thought you were smarter."
                    the_person.char "I'll make sure it doesn't happen again."
                    mc.name "Make sure you do. If you aren't able to fit into the corporate culture here I'll have to find someone to replace you."
                    $ the_person.draw_person(emotion="sad")
                    the_person.char "Understood. I'm sorry."
                    $ the_person.change_obedience(1)
                    $ the_person.change_happiness(-2)
                    "[the_person.title] walks off."

                "Reduce her pay. -$[pay_percent]/day":
                    mc.name "This is honestly unacceptable [the_person.title]. You knew what the uniform policy was and chose to violate it anyway."
                    the_person.char "It won't happen again, I'll go get changed right now."
                    mc.name "I'm sorry, but that's not good enough. I'm going to have to reduce your pay until your behaviour improves."
                    $ the_person.draw_person(emotion="angry")
                    $ the_person.change_obedience(5)
                    $ the_person.change_happiness(-10)
                    $ the_person.salary += -pay_percent
                    $ mc.log_event("[the_person.title] -$[pay_percent]/day Salary","float_text_green")
                    the_person.char "What? Come on [the_person.mc_title], that's bullshit!"
                    mc.name "I can't be making rules exceptions just for you. Go get changed and get back to work, we can talk about this later."
                    "[the_person.title] huffs and walks off."

                "Tell her to work naked instead." if the_person.sluttiness > 40 and reduced_coverage_uniform_policy.is_owned():
                    "You shake your head, disappointed."
                    mc.name "Well if you don't want to wear your uniform, I guess you're just going to be wearing nothing at all."
                    if the_person.sluttiness > 70 - (10 * the_person.get_opinion_score("not wearing anything")): #triggers easier if the person likes getting naked.
                        the_person.char "Ugh, fine."
                        if the_person.outfit.slut_requirement < 40:
                            "[the_person.title] starts to strip down right in front of you, pulling off one piece of clothing at a time."
                        else:
                            "[the_person.title] starts to pull off what little clothing she was wearing."

                        python:
                            for clothing in the_person.outfit.get_upper_ordered():
                                the_person.draw_animated_removal(clothing)
                                renpy.say("","") #Make the player click through as she strips
                            for clothing in the_person.outfit.get_lower_ordered():
                                the_person.draw_animated_removal(clothing)
                                renpy.say("","")

                        the_person.char "There, can I get back to work now?"
                        mc.name "Yes. Maybe you'll think next time before you violate company policy."
                        $ the_person.change_obedience(5)
                        $ the_person.change_happiness(-5)
                        $ slut_report = the_person.change_slut_temp(3)

                    else:
                        the_person.char "Very funny [the_person.mc_title]. I promise I'll get changed as soon as I can."
                        mc.name "I'm not joking [the_person.title]. You can put your uniform back on in a few hours; until then you'll be working naked."
                        if the_person.get_opinion_score("not wearing anything") > 0:
                            the_person.char "What? Are you really going to make me do that?"
                            mc.name "I am. You're welcome to check your contract - the latest uniform changes, which you signed off on by the way, made it official company policy."
                            "[the_person.possessive_title] is flustered for a moment."
                            the_person.char "I... If you say I have to."
                            "She turns and heads to the washroom. You follow and wait outside until she's changed out of her clothing."
                        else:
                            $ the_person.draw_person(emotion = "angry")
                            the_person.char "You can't make me do that!"
                            mc.name "Actually I can. You're welcome to check your contract - the latest uniform changes everyone signed off on made it offical company policy."
                            "[the_person.possessive_title] stammers for a moment."
                            the_person.char "Ugh! Fine!"
                            $ renpy.scene("Active")
                            "She storms off to the washroom. You wait outside until she's changed."
                            the_person.char "This is humiliating."
                        python:
                            for clothing in the_person.outfit.get_upper_ordered():
                                the_person.outfit.remove_clothing(clothing)
                            for clothing in the_person.outfit.get_lower_ordered():
                                the_person.outfit.remove_clothing(clothing)
                        $ the_person.draw_person(emotion = "angry")
                        "She steps out into the hallway again, completely naked."
                        mc.name "Well maybe you'll think next time before you violate company policy."

                        if the_person.get_opinion_score("not wearing anything") <= 0:
                            "[the_person.possessive_title] glares at you."
                            $ the_person.change_happiness(-10)

                        else:
                            "[the_person.possessive_title] seems embarrassed and looks away from you."
                        the_person.char "Can I get back to work now?"
                        mc.name "Get going."

                        $ the_person.change_obedience(10)
                        $ slut_report = the_person.change_slut_temp(5)

                    $ the_person.change_love(the_person.get_opinion_score("not wearing anything"))
                    $ the_person.discover_opinion("not wearing anything")
                    "You watch [the_person.title] as she walks away completely naked, then get back to work yourself."

                "Deny her an orgasm." if the_person.sluttiness > 60 and mc.current_stamina > 0:
                    mc.name "I'm starting to think there's only one thing that will actually teach you a lesson though..."
                    "You step close to [the_person.title] and reach a hand around, grabbing onto her ass and squeezing it hard."
                    the_person.char "Ah... What are you doing?"
                    mc.name "Showing a disobedient slut why she should follow the rules."
                    "The closer you can bring [the_person.possessive_title] to orgasm without allowing her to the more effective this will be."
                    $ mc.current_stamina += -1
                    call fuck_person(the_person) from _call_fuck_person_6
                    if the_person.arousal > 100:
                        #You made her cum, she gets even more disobedient
                        the_person.char "Oh wow... I need to ignore this uniform thing more often. That felt amazing."
                        mc.name "Please, I need you to at least try and follow the rules [the_person.title]."
                        the_person.char "Yeah... Sure..."
                        $ obedience_change = -5
                        $ the_person.change_love(2)

                    elif the_person.arousal > 80:
                        #You got her close but didn't push her over the edge. Full gain.
                        the_person.char "Ah... damn it [the_person.mc_title], I was so close!"
                        mc.name "If you were in uniform I would have let you cum, but I can't reward you unless you're following the rules. Understood?"
                        "[the_person.title] bites her lip and nods. Her face is flush and she's still breathing deeply."
                        $obedience_change = 10

                    else:
                        #You probably just got a blowjob or something. partial gain.
                        the_person.char "Wait, that's it?"
                        mc.name "If you were in uniform maybe we could have had some more fun, but I can't reward you unless you're following the rules. Understood?"
                        "[the_person.title] sighs and pouts."
                        the_person.char "Yes sir."
                        $obedience_change = 5

                    $ the_person.change_obedience(obedience_change)
                    $ the_person.reset_arousal()
                    $ the_person.review_outfit()
                    "You leave [the_person.title] to get cleaned up and get back to work."

                "Deny her an orgasm.\n{size=22}Requires Stamina{/size} (disabled)" if the_person.sluttiness > 60 and mc.current_stamina == 0:
                        pass

    $renpy.scene("Active")
    return


init 1 python:
    def office_flirt_requirement():
        if anyone_else_in_office():
            if len(mc.location.people) > 0: # Requires you to be in the office during work hours and for other people to be with you.
                return True
        return False

    office_flirt_crisis = Action("Office Flirt Crisis", office_flirt_requirement,"office_flirt_label")
    crisis_list.append([office_flirt_crisis,5])

label office_flirt_label():
    if not len(mc.location.people) > 0:
        return #Someone must have quit or moved, so we no longer have anyone to flirt with

    $ the_person = get_random_from_list(mc.location.people)
    $ the_person.draw_person(position = "walking_away")
    if mc.location == mc.business.m_div: #Note: This won't actually work properly because the locations for production and marketing are the same. TODO: Fix that.
        "[the_person.title] walks by you while you're recording shipping addresses for the next batch of serum."

    elif mc.location == mc.business.p_div:
        "[the_person.title] walks by you while you're preparing your next production batch of serum."

    elif mc.location == mc.business.r_div:
        "[the_person.title] walks by you while you're putting together notes for the last serum test you ran."

    elif mc.location == mc.business.s_div:
        "[the_person.title] walks by you while you're assembling a list of low-cost material suppliers."

    else: # == h_div
        "[the_person.title] walks by you while you're preparing the payroll for last week."

    if the_person.outfit.slut_requirement < 10:
        # It's a relatively conservative outfit.
        "You turn to watch her go past. Her outfit doesn't show it off, but you enjoy the way her ass looks as she walks."

    elif the_person.outfit.slut_requirement < 30:
        # It's a risque outfit
        "You turn to watch her go past. Her outfit does a good job of showing off her ass as she walks."

    elif the_person.outfit.slut_requirement < 60:
        # It's a very revealing outfit.
        if the_person.outfit.vagina_visible(): #We use vagina as a proxy for ass too.
            "You turn to watch her go past. Her ass looks particularly good with nothing blocking your view of it."
        else:
            $ what_we_see = the_person.outfit.get_lower_visible()
            $ top_item = what_we_see[0]
            "You turn to watch her go past. Her ass looks particularly good, barely hidden underneath her [top_item.name]."
    else:
        # She's practically (or literally) naked.
        if the_person.outfit.vagina_visible(): #We use vagina as a proxy for ass too.
            "You turn to watch her go past. Her ass looks particularly good with nothing blocking your view of it."
        else:
            $ what_we_see = the_person.outfit.get_lower_visible()
            $ top_item = what_we_see[0]
            "You turn to watch her go past. Her ass looks particularly good, barely hidden underneath her [top_item.name]."

    "She stops at a shelf and runs her finger along a row of binders, obviously looking for something. After a moment she moves down a shelf and checks there."
    "You watch as [the_person.title] searches row after row, going lower and lower each time. Soon she's bent over with her ass high in the air."

    menu:
        "Get back to work.":
            "You take one last glance, then get back to your work. A moment later [the_person.possessive_title] walks past you again as she heads back to her work station."

        "Take a moment and enjoy the view.":
            #We should have a random chance of her noticing you.
            "You sit back in your chair and take a moment to enjoy [the_person.possessive_title]'s ass wiggling at you."
            if renpy.random.randint(0,100) < 50: #50/50 chance
                the_person.char "[the_person.mc_title], can you help me find something?"
                "[the_person.title] looks over her shoulder at you before you can look away."
                $ the_person.draw_person(position = "back_peek") #Draw her standing up properly in her normal pose.
                if the_person.sluttiness > 30:
                    the_person.char "Getting a good view?"
                    $ change_amount = 5
                    $ slut_report = the_person.change_slut_temp(change_amount)
                    "[the_person.possessive_title] shakes her butt for you a little and laughs."
                    the_person.char "Seriously though, could you come give me a hand?"
                    mc.name "Sure, what are you looking for?"
                    "You get up and help [the_person.title] find the right binder."
                    the_person.char "Thank you [the_person.mc_title], don't be scared of watching me leave either."
                    "She winks at you and walks away, putting in extra effort to make her butt swing side to side as she goes."
                else:
                    $ the_person.draw_person(emotion="angry")
                    the_person.char "Were staring at my ass this whole time?"
                    $ the_person.draw_person()
                    mc.name "No, I was... waiting to see if you needed any help. What were you looking for?"
                    if mc.charisma > 4:
                        "[the_person.possessive_title] hesitates for a moment, then turns to the shelf again."
                        $ the_person.draw_person(position = "walking_away")
                        the_person.char "There's a binder here with a procedure I wrote out, I think it's been moved. Did you see it?"
                        "It looks like you've managed to convince her. You help [the_person.title] find the binder she was looking for, then you both go back to your work stations."
                    else:
                        $ the_person.change_happiness(-5)
                        $ the_person.change_obedience(-1)
                        $ the_person.change_love(-2)
                        the_person.char "Don't give me that, I know what I saw. Ugh, men are all the same."
                        "[the_person.possessive_title] glares at you and storms off. When you see her later in the day she's calmed down, but she's still not happy with you."
            else:
                "It takes her a few minutes, but she finally pulls one of the binders out and stands up."
                $ the_person.draw_person(position = "walking_away")
                "You turn your attention back to your work as she walks back to her work station."

        "Let her know you're watching.":
            # A slutty person shows off
            mc.name "Keep looking [the_person.title], I'm sure it's down there somewhere!"
            if the_person.sluttiness < 20:
                #They aren't very slutty, this is offensive.
                $ the_person.draw_person(position = "back_peek")
                "[the_person.possessive_title] looks over her shoulder at you."
                the_person.char "What? I..."
                "She realises that she's got her ass pointed right at you. She stands up quickly."
                $ the_person.draw_person(emotion="angry")
                the_person.char "Oh my god, have you been watching me this whole time?!"
                mc.name "No, I was just... waiting to see if you needed any help. What where you looking for?"
                $ the_person.change_happiness(-10)
                $ the_person.change_obedience(-2)
                $ the_person.change_love(-2)
                the_person.char "Ugh, yeah right. You're a fucking pig, you know that?"
                $ the_person.draw_person(position = "walking_away")
                "[the_person.title] glares at you and storms off. When you see her later in the day she's calmed down, but she's still not happy with you."
            elif the_person.sluttiness < 60:
                # They're slutty enough to like being watched, but not enough to ask for a quick fuck.
                $ the_person.draw_person(position = "back_peek")
                "[the_person.title] looks over her shoulder at you."
                the_person.char "What? I... Oh."
                $ the_person.draw_person(position = "back_peek", emotion="happy")
                "She realises that she's got her ass pointed right at you. She smiles and wiggles her butt a little."
                the_person.char "Do you like what you see? I didn't mean to put on a show, but if I'm already here..."
                $ the_person.draw_person(position="walking_away")
                "[the_person.possessive_title] spreads her legs and bends her knees, waving her ass side to side and up and down for you."
                #if she's wearing something on the bottom and the outfit isn't too slutty, take off her bottom bit.
                if len(the_person.outfit.get_lower_ordered()) > 0: #ie. she's wearing something to take off
                    $ test_outfit = copy.deepcopy(the_person.outfit)
                    $ the_item = test_outfit.get_lower_ordered()[-1] #Get the top layer item
                    $ test_outfit.remove_clothing(the_item)
                    if the_person.judge_outfit(test_outfit):
                        the_person.char "I'm sure you'd like a better look, lets get this out of the way first."
                        "[the_person.title] stands up and pulls off her [the_item.name], dropping to the floor."
                        $ the_person.draw_animated_removal(the_item, position = "back_peek", emotion = "happy")
                        mc.name "Mmm, looking good [the_person.title]."
                        $ the_person.draw_person(position="walking_away")
                        "She smiles and turns back to the shelf, planting two hands on one of the beams and bending over again. She works her ass back and forth, up and down, while you watch from your desk."
                        $ the_person.draw_person(emotion = "happy")
                        "After a minute of teasing you she stops, stands up, and turns towards you."
                        $ the_person.change_happiness(5)
                        $ the_person.change_obedience(1)
                        $ change_amount = 10
                        $ slut_report = the_person.change_slut_temp(change_amount)
                        the_person.char "Hope you had a good time, I should really be getting back to work though. Feel free to watch me leave."
                        $ the_person.draw_person(position = "walking_away")
                        "[the_person.possessive_title] grabs her [the_item.name], turns back to the shelf, and finally finds the binder she was looking for. She takes it and walks past you, making sure to shake her ass as you watch."

                    else:
                        the_person.char "I bet you wish you could get a look under this, right?"
                        mc.name "Mmm, maybe I will soon."
                        "She keeps wiggling her ass, working it up and down, left and right, while you watch from your desk."
                        $ the_person.draw_person(emotion="happy")
                        "After a minute of teasing you she stops, stands up, and turns towards you."
                        $ the_person.change_happiness(5)
                        $ the_person.change_obedience(1)
                        $ change_amount = 10
                        $ slut_report = the_person.change_slut_temp(change_amount)
                        the_person.char "Hope you had a good time, I should really be getting back to work though. Feel free to watch me leave."
                        $ the_person.draw_person(position="walking_away")
                        "[the_person.title] winks at you, then turns back to the shelf and resumes her search. When she finds it she walks back past you, making sure to shake her ass as you watch."

                else:
                    "With nothing covering her up you're able to get a great look of [the_person.title]'s shapely butt. She works it around for a minute or two while you watch from your desk."
                    the_person.char "Oh, here it is..."
                    $ the_person.draw_person(emotion="happy")
                    "[the_person.possessive_title] slides a binder out from the shelf and stands back up."
                    the_person.char "Sorry to end the show, but I've got what I need. Feel free to watch me leave though."
                    $ the_person.change_happiness(5)
                    $ the_person.change_obedience(1)
                    $ change_amount = 10
                    $ slut_report = the_person.change_slut_temp(change_amount)
                    $ the_person.draw_person(position="walking_away")
                    "She winks and walks past your desk, making sure to shake her ass as you watch."

            else:
                #She's very slutty already.
                $ the_person.draw_person(position = "back_peek")
                "[the_person.title] looks over her shoulder and winks at you."
                the_person.char "I'm glad you're enjoying the show, I'd hate to bend over like this and not have anyone notice."
                "She reaches back and runs a hand over her ass, then spanks it lightly."
                the_person.char "Could you come over and help me look for something, please? I promise I'll repay the favour."
                menu:
                    "Help her find what she's looking for.":
                        $ the_person.draw_person(emotion = "happy")
                        "You get up from your desk and join [the_person.title] at the shelf. As soon as you get there she slides one of the binders out and holds it up."
                        the_person.char "Oh, it looks like I found it. Oh well, I still promised to pay you back..."
                        "She runs a finger down the front of your chest, then down to your crotch. She bites her lip and looks at you."
                        the_person.char "Come on, lets slip into the supply closet for a moment. Being watched like that gets me so worked up, I'll let you do whatever dirty things you want to me."
                        menu:
                            "Have sex with [the_person.title]." if mc.current_stamina > 0:
                                "You take [the_person.title]'s hand and pull her into the supply closet."
                                $ the_person.add_situational_slut("situation",10, "Showing off got me horny.")
                                $ the_person.sluttiness += 10
                                $ mc.current_stamina += -1
                                call fuck_person(the_person) from _call_fuck_person_7
                                $ change_amount = __builtin__.int(the_person.arousal/10)
                                $ slut_report = the_person.change_slut_temp(change_amount)
                                $ the_person.clear_situational_slut("situation")
                                "Once you've gotten yourself dressed you slip out of the closet again and head back to your desk. [the_person.possessive_title] comes out after, walking past your desk with the binder she was looking for held close."

                            "Have sex with [the_person.title].\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                                pass

                            "Get back to work.":
                                mc.name "Sorry [the_person.title], but I've got stuff to get done right now. You'll have to take care of that yourself."
                                $ the_person.change_obedience(5)
                                $ change_amount = 2
                                $ slut_report = the_person.change_slut_temp(change_amount)
                                if the_person.obedience > 110:
                                    "She nods and holds the binder close. She looks you up and down one last time, then walks back to her work station. You watch her from behind as she goes."
                                else:
                                    the_person.char "Aww, you're the worst. Fine, but don't tease me like too often, okay? A girl can only take so much."
                                    $ the_person.draw_person(position = "walking_away")
                                    "She holds the binder close and turns around. You watch her from behind as she walks back to her work station."


                    "Stay at your desk.":
                        mc.name "I think I like the view from here, actually. Take your time, I really don't mind."
                        the_person.char "Mmm, looking for a show instead?"
                        $ the_person.draw_person(position = "walking_away")
                        "She smiles and turns back to the shelf, planting two hands on one of the beams and bending over again. She works her ass back and forth, up and down, while you watch from your desk."
                        the_person.char "Oh, here it is..."
                        "[the_person.title] slides a binder out from the shelf and stands back up."
                        $ the_person.draw_person(emotion = "happy")
                        the_person.char "Sorry to finish so soon, but I've got what I need. Feel free to watch me leave though."
                        $ the_person.change_happiness(5)
                        $ the_person.change_obedience(2)
                        $ change_amount = 10
                        $ slut_report = the_person.change_slut_temp(change_amount)
                        "She winks and walks past your desk, making sure to shake her ass as you watch."
    $ renpy.scene("Active")
    return


init 1 python:
    def special_training_requirement():
        if mc.business.get_employee_count() > 0: #As long as you have at least one person working for you.
            if mc.business.is_open_for_business(): # Only triggers during the day when people are working.
                return True
        return False

    special_training_crisis = Action("Special Training Crisis",special_training_requirement,"special_training_crisis_label")
    crisis_list.append([special_training_crisis,5])

label special_training_crisis_label():
    if not mc.business.get_employee_count() > 0:
        return #We must have had someone quit or be fired, so we no longer can get a random person.

    $ the_person = get_random_from_list(mc.business.get_employee_list())
    "You get a text  from [the_person.title]."
    the_person.char "[the_person.mc_title], I've just gotten word about a training seminar going on right now a few blocks away. I would love to take a trip over and see if there is anything I could learn."
    the_person.char "There's a sign up fee of $500. If you can cover that, I'll head over right away."
    menu:
        "Send [the_person.title] to the Seminar. -$500" if mc.business.funds >= 500:
            $ mc.business.funds += -500
            "You type up a response."
            mc.name "That sounds like a great idea. I'll call and sort out the fee, you start heading over."
            the_person.char "Understood, thank you sir! What would you like me to focus on?"
            menu:
                "Improve HR Skill (Current [the_person.hr_skill])":
                    $ the_person.hr_skill += 2
                    $ mc.log_event("[the_person.title]: +2 HR Skill", "float_text_grey")
                    "[the_person.title] leaves work for a few hours to attend the training seminar. When she comes back she has learned several useful business structuring techniques."

                "Improve Marketing Skill (Current [the_person.market_skill])":
                    $ the_person.market_skill += 2
                    $ mc.log_event("[the_person.title]: +2 Marketing Skill", "float_text_grey")
                    "[the_person.title] leaves work for a few hours to attend the training seminar. When she comes back she is far more familiar with local market demands."

                "Improve Researching Skill (Current [the_person.research_skill])":
                    $ the_person.research_skill += 2
                    $ mc.log_event("[the_person.title]: +2 Researching Skill", "float_text_grey")
                    "[the_person.title] leaves work for a few hours to attend the training seminar. When she comes back she has several interesting new researching technqiues to test."

                "Improve Production Skill (Current [the_person.production_skill])":
                    $ the_person.production_skill += 2
                    $ mc.log_event("[the_person.title]: +2 Production Skill", "float_text_grey")
                    "[the_person.title] leaves work for a few hours to attend the training seminar. When she comes back she has a few new ideas for streamlining production."

                "Improve Supply Skill (Current [the_person.supply_skill])":
                    $ the_person.supply_skill += 2
                    $ mc.log_event("[the_person.title]: +2 Supply Skill", "float_text_grey")
                    "[the_person.title] leaves work for a few hours to attend the training seminar. When she comes back she is far more familiar with local suppliers and their goods."


        "Tell her to stay at work.":
            "You type up a response."
            mc.name "I'm sorry [the_person.title], but there aren't any extra funds in the budget right now."
            the_person.char "Noted, maybe some other time then."

    return

init 1 python:
    def lab_accident_requirement():
        if in_research_with_other():
            if mc.business.active_research_design and type(mc.business.active_research_design) is SerumDesign:
                return True
        return False

    lab_accident_crisis = Action("Lab Accident Crisis",lab_accident_requirement,"lab_accident_crisis_label")
    crisis_list.append([lab_accident_crisis,5])

label lab_accident_crisis_label():
    ## Some quick checks to make sure the crisis is still valid (for example, a serum being finished before this event can trigger)
    if not mc.business.active_research_design:
        return
    if not type(mc.business.active_research_design) is SerumDesign:
        return

    $ the_serum = mc.business.active_research_design
    $ the_person = get_random_from_list(mc.business.research_team)
    $ the_place = mc.business.r_div

    if mc.location == mc.business.r_div:
        $ the_place.show_background()
        "There's a sudden crash and sharp yell of suprise as you're working in the lab."
        $the_person.call_dialogue("suprised_exclaim")
        the_person.char "[the_person.mc_title], I think I need you for a moment."


    else:
        "Your phone buzzes - it's a text from [the_person.title] on your research team."
        the_person.char "There's been a small accident, can I see you in the lab?"
        "You hurry over to your research and development lab to see what the problem is."
        $ the_place.show_background()


    $ the_person.draw_person(emotion = "sad")
    "You get to [the_person.title]'s lab bench. There's a shattered test tube still on it and a pool of coloured liquid."
    mc.name "What happened?"
    $ techno = get_random_from_list(technobabble_list)
    the_person.char "I was trying to [techno] and went to move the sample. It slipped out of my hand and when I tried to grab it..."
    "She turns her palm up to you. It's covered in the same coloured liquid, and there's a small cut."
    the_person.char "I'm not sure what the uptake is like with this new design. I think everything will be fine, but would you mind hanging around for a few minutes?"
    $the_person.give_serum(copy.copy(the_serum))
    "It doesn't seem like [the_person.possessive_title] is having any unexpected affects from the dose of serum, so you return to your work."
    return

init 1 python:
    def production_accident_requirement():
        if in_production_with_other():
            if len(mc.business.serum_production_array) > 0: #Check to see if there's at least one person in the production department and that we're serum right now.
                return True
        return False

    production_accident_crisis = Action("Production Accident Crisis",production_accident_requirement,"production_accident_crisis_label")
    crisis_list.append([production_accident_crisis,5])


label production_accident_crisis_label():

    $ the_serum = mc.business.get_random_weighed_production_serum()
    if the_serum is None:
        return #We aren't actually producing anything. Abort crisis.
    $ the_person = get_random_from_list(mc.business.production_team)
    $ the_place = mc.business.p_div

    if mc.location == mc.business.p_div:
        $ the_place.show_background()
        "There's a sudden crash and sharp yell of suprise as you're working in the lab."
        $the_person.call_dialogue("suprised_exclaim")
        the_person.char "[the_person.mc_title], I think I need you for a moment."


    else:
        "Your phone buzzes - it's a text from [the_person.title] on your production team."
        the_person.char "There's been a small accident, can I see you in the lab?"
        "You hurry over to the production lab to see what the problem is."
        $ the_place.show_background()


    $ the_person.draw_person(emotion = "sad")
    "You get to [the_person.title]'s lab bench. There's a collection of shattered test tubes still on it and a pool of coloured liquid."
    mc.name "What happened?"
    $ techno = get_random_from_list(technobabble_list)
    the_person.char "I was trying to [techno] like I normally do and went to move the batch. It slipped out of my hand and when I tried to grab it..."
    "She turns her palm up to you. It's covered in the same coloured liquid, and there's a small cut."
    the_person.char "I'm not sure what the uptake is like with this new design. I think everything will be fine, but would you mind hanging around for a few minutes?."
    $the_person.give_serum(copy.copy(the_serum))
    "It doesn't seem like [the_person.possessive_title] is having any unexpected affects from the dose of serum, so you return to your work."
    return

init 1 python:
    def water_spill_crisis_requirement():
        return anyone_else_in_office()

    water_spill_crisis = Action("Water Spill Crisis",water_spill_crisis_requirement,"water_spill_crisis_label")
    crisis_list.append([water_spill_crisis,5])

label extra_mastery_crisis_label():
    $ the_person = mc.business.head_researcher
    if the_person is None:
        return

    $ the_research = mc.business.active_research_design
    if the_research is None:
        return

    $ the_trait = None
    if type(the_research) is SerumTrait:
        $ the_trait = mc.business.active_research_design
    elif type(the_research) is SerumDesign:
        $ the_trait = get_random_from_list(the_research.traits)

    if the_person in mc.location.people:
        #She's in the same room as you.
        the_person.char "[the_person.mc_title], I have something interesting to show you."
        $ the_person.draw_person()
    else:
        #She comes to meet you,
        "Your work is interrupted when [the_person.title] comes into the room."
        $ the_person.draw_person()
        the_person.char "[the_person.mc_title], there has been an interesting breakthrough in my research."
    "She places a file in front of you and keeps talking."
    $ techno_string = "I've discovered that I can " + get_random_from_list(technobabble_list) + " and the chance for a side effect should drop significantly when working with " + the_trait.name + "."
    the_person.char "[techno_string]"
    the_person.char "I would like to do some more experimentation, but the equipment I need is quite expensive."
    $ cost = __builtin__.int(the_trait.mastery_level * 50) #The cost is 100 * mastery level,
    "You look through the file [the_person.title] gave you. It would cost $[cost] to raise the mastery level of [the_trait.name] by 2."
    menu:
        "Purchase the equipment. -$[cost] (tooltip)Raises the mastery level of [the_trait.name] by 2. The higher your mastery of a serum trait the less likely it is to produce a side effect." if mc.business.funds >= cost:

            "You hand the file back to [the_person.title]."
            mc.name "This is a terrific idea, I want you to purchase whatever equipment you need and get to work immediately."
            $ the_person.draw_person(emotion = "happy")
            the_person.char "Understood!"
            $ mc.business.funds += -cost
            $ the_trait.add_mastery(2)
            $ mc.log_event("Mastery of " + the_trait.name + " increased by 2.", "float_text_blue")

        "Purchase the equipment. -$[cost] (disabled)" if mc.business.funds < cost:
            pass

        "Do not purchase the equipment.":
            "You hand the file back to [the_person.title]."
            mc.name "We don't have the budget for this right now, you will have to make due with the current lab equipment."
            "She takes the file back and nods."
            the_person.char "Understood, sorry to have bothered you."


    $ renpy.scene("Active")
    return

init 1 python:
    def extra_mastery_crisis_requirement():
        if not mc.business.is_open_for_business():
            return False
        if not mc.is_at_work():
            return False
        if mc.business.head_researcher is None:
            return False
        if mc.business.active_research_design is None:
            return False
        if type(mc.business.active_research_design) is SerumTrait and not mc.business.active_research_design.researched:
            return False #This event only triggers when making new serum designs (which use existing traits) or when working on mastering an existing trait.
        return True

    extra_mastery_crisis = Action("Mastery Boost",extra_mastery_crisis_requirement,"extra_mastery_crisis_label")
    crisis_list.append([extra_mastery_crisis,5])

init 1 python:
    def trait_for_side_effect_requirement():
        if not mc.business.is_open_for_business():
            return False
        if not mc.is_at_work():
            return False
        if mc.business.head_researcher is None:
            return False
        if mc.business.active_research_design is None:
            return False
        if type(mc.business.active_research_design) is not SerumDesign:
            return False #This event only triggers when making new serum designs (which use existing traits) or when working on mastering an existing trait.
        return True

    trait_for_side_effect_crisis = Action("Trait for Side Effect Crisis", trait_for_side_effect_requirement, "trait_for_side_effect_label")
    crisis_list.append([trait_for_side_effect_crisis,5])

label trait_for_side_effect_label():
    #TODO: Test this
    $ the_person = mc.business.head_researcher
    $ the_design = mc.business.active_research_design

    $ list_of_valid_traits = []
    python:
        for trait in list_of_traits:
            if trait.researched and trait not in the_design.traits:
                list_of_valid_traits.append(trait)

    $ the_trait = get_random_from_list(list_of_valid_traits) #Note that this can generate normally impossible designs!
    $ the_side_effect = get_random_from_list(list_of_side_effects)

    if the_trait is None or the_side_effect is None: #If it turns out this event is impossible just flub out.
        return

    if the_person in mc.location.people:
        the_person.char "[the_person.mc_title], do you have a moment?"
        $ the_person.draw_person()
        "Your head researcher [the_person.title] gets your attention and leads you over to her lab bench."
    else:
        "You get a call from your head researcher [the_person.title]."
        the_person.char "[the_person.mc_title], if you can come down to the research lab I think I've discovered something interesting."
        $mc.change_location(mc.business.r_div)
        "You head to your R&D lab and meet [the_person.title]. She leads you over to her lab bench."

    the_person.char "I've been working on the design you set out for [the_design.name] and one of the test batches developed some very interesting side effects."
    "You look over the notes [the_person.possessive_title] has taken. The varient she has created includes an extra serum trait as well as a negative side effect."
    "It doesn't seem like there will be any way to detangle the effects."
    #TODO: Make sure these actually display the traits properly.
    show screen trait_list_tooltip([the_trait, the_side_effect])
    menu:
        "Add [the_trait.name] and [the_side_effect.name] to [the_design.name].":
            hide screen trait_list_tooltip
            mc.name "I think this is a lucky breakthrough. Keep working with this design now."
            $ the_design.add_trait(the_trait)
            $ the_design.add_trait(the_side_effect, is_side_effect = True)

        "Leave the design as it is.":
            hide screen trait_list_tooltip
            mc.name "I don't think the side effects are acceptable. Revert back to a more stable version and keep going from there."

    the_person.char "Understood sir, I'll make the changes to all of the documentation."
    $ renpy.scene("Active")

    return

label water_spill_crisis_label():
    $ the_person = get_random_from_list(mc.business.get_employee_list())
    $ the_place = mc.business.get_employee_workstation(the_person)
    $ ordered_top = the_person.outfit.get_upper_ordered()
    if len(ordered_top) == 0:
        return #She's not wearing a top, we can't exactly spill water on nothing!
    else:
        $ the_clothing = the_person.outfit.get_upper_ordered()[-1] #Get the very top item of clothing.


    "You're hard at work when [the_person.title] comes up to you. She's got her phone clutched in one hand, a water bottle in the other."
    $ the_person.draw_person()
    $ the_person.call_dialogue("greetings")
    mc.name "Hey [the_person.title], how can I help you?"
    the_person.char "I had a few questions about how my taxes were going to be calculated this year, and I was hoping you could answer some of them."
    "You listen as [the_person.possessive_title] dives into her tax situation."
    "You aren't paying a terrible amount of attention until she goes to take a drink from her water bottle and dumps it down her front!"
    $ dry_colour = the_clothing.colour
    $ wet_colour = copy.copy(dry_colour)

    $ wet_colour[3] = 0.85 * wet_colour[3]
    $ the_clothing.colour = wet_colour
    $ the_person.draw_person(emotion="angry")
    $ the_person.call_dialogue("suprised_exclaim")
    "She tries to wipe the water off, but not before it's soaked through the front of her [the_clothing.name]."
    $ test_outfit = copy.deepcopy(the_person.outfit) #Make a copy, we'll try removing the wet item and reevaluating.
    $ test_outfit.remove_clothing(the_clothing)
    $ thinks_appropriate = the_person.judge_outfit(test_outfit,10) #Does she think it's appropriate to strip off her top when it's wet?
    if not thinks_appropriate:
        the_person.char "I'm so sorry about this [the_person.mc_title], I just... I just need to go and dry this off!"
        $ renpy.scene("Active")
        "[the_person.title] runs off towards the bathroom."
        $ the_clothing.colour = dry_colour
        "After a few minutes she's back, with her [the_clothing.name] dried off and no longer transparent."
        $ the_person.draw_person()
        $ slut_report = the_person.change_slut_temp(1)
        the_person.char "Ugh, that was so embarrasing. Lets just forget about that, okay?"
        mc.name "Of course, back to your taxes then, right?"
        "You help [the_person.possessive_title] sort out her tax issues, then get back to work."
    else:
        $ thinks_appropriate = the_person.judge_outfit(test_outfit) #Does she think it's appropriate to just strip it off all of the time?
        if thinks_appropriate:
            the_person.char "I'm so sorry about this [the_person.mc_title]. Let me just take this off, you keep talking."
            $ the_person.draw_animated_removal(the_clothing)
            if the_person.outfit.tits_visible():
                "[the_person.title] strips off her [the_clothing.name], letting you get a nice good look at her [the_person.tits] sized tits."
            else:
                "[the_person.title] strips off her [the_clothing.name] and puts it to the side, then turns her attention back to you."
            menu:
                "Right, your taxes...":
                    the_person.char "I hope I'm not distracting you. I can dry my shirt off if you'd prefer."
                    mc.name "No, that's fine. Just remind me again what we were talking about."
                    $ slut_report = the_person.change_slut_temp(1)
                    "You help [the_person.possessive_title] with her tax questions while she stands topless beside your desk."

                "Keep going..." if minimal_coverage_uniform_policy.is_owned():
                    mc.name "You might as well keep going. All this tax talk is boring and I'd appreciate somthing pleasant to look at while I help you."
                    if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible():
                        mc.name "Not that there's much I can't see already..."
                    elif the_person.outfit.tits_visible():
                        mc.name "You already have your tits out for me, what's a little more skin?"
                    elif the_person.outfit.vagina_visible():
                        mc.name "I mean, I can already see your cunt. What's a little more skin at that point?"

                    if the_person.judge_outfit(the_person.outfit, -25): #How comfortable are they with their current outfit? If they have an extra 20 sluttiness start stripping!
                        "[the_person.title] smiles mischievously and starts to strip down some more."
                        the_person.char "You have been very helpful to me. It's the least I could do."

                    elif the_person.obedience > 140:
                        "[the_person.title] nods and starts to strip down some more."
                        the_person.char "I'll do whatever you would like me to do, sir."

                    else:
                        the_person.char "I mean... isn't this enough skin already? I guess you set the uniforms though..."
                        "[the_person.possessive_title] starts to strip down some more."

                    python:
                        next_piece = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        while (next_piece and the_person.judge_outfit(the_person.outfit, the_person.obedience-100+10)):
                            the_person.draw_animated_removal(next_piece)
                            renpy.say("",the_person.title + " takes off her " + next_piece.name + " and leave it on the ground.")
                            next_piece = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)

                    the_person.char "There, I hope that's good enough."
                    mc.name "Much better. Now, back to those taxes."
                    $ slut_report = the_person.change_slut_temp(5)
                    $ the_person.change_obedience(5)
                    if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible():
                        "You help [the_person.possessive_title] with her tax questions while she stands next to your desk, her body completely on display."
                    else:
                        "You help [the_person.possessive_title] with her tax questions while she stands next to your desk, still partially undressed."


                "Keep going... \n{size=22}Requires: Minimal Coverage Corporate Uniforms{/size} (disabled)" if not minimal_coverage_uniform_policy.is_owned():
                    pass

            $ the_person.review_outfit()

        else:
            the_person.char "I'm so sorry about this [the_person.mc_title], should I go dry this off first?"
            menu:
                "Dry it off now.":
                    mc.name "You go dry it off, I'll wait here for you."
                    the_person.char "I'll be back as soon as I can."
                    $ renpy.scene("Active")
                    "[the_person.title] runs off towards the bathroom."
                    $ the_clothing.colour = dry_colour
                    "After a few minutes she's back, with her [the_clothing.name] dried off and no longer transparent."
                    $ the_person.draw_person()
                    $ slut_report = the_person.change_slut_temp(1)
                    the_person.char "Ugh, that was so embarrasing. Lets just forget about that, okay?"
                    mc.name "Of course, back to your taxes then, right?"
                    "You help [the_person.possessive_title] sort out her tax issues, then get back to work."

                "Leave it alone.":
                    mc.name "I'd like to get back to work as quickly as possible, just leave it for now and you can dry it off later."
                    if test_outfit.tits_visible():
                        "[the_person.title] looks down at her transparent top, then nods and continues on about her taxes. Getting a good look at her tits makes the boring topic much more interesting."
                    else:
                        "[the_person.title] looks down at her top, then nods and continues. At least the transparent clothing helps make the boring topic more interesting."
                    $ the_person.change_obedience(1)
                    $ slut_report = the_person.change_slut_temp(1)
                    "After a few minutes you've answered all of [the_person.possessive_title]'s questions, and she heads off to dry her [the_clothing.name] off."
                    $ the_clothing.colour = dry_colour

                "Take it off.":
                    mc.name "I'm really quite busy right now, just take it off now and you can dry it off later."
                    the_person.char "I... Okay, fine. I really need your help on this."
                    $ the_person.draw_animated_removal(the_clothing)
                    $ the_person.change_happiness(-5)
                    $ slut_report = the_person.change_slut_temp(2)
                    $ the_person.change_obedience(2)
                    "[the_person.title] clearly isn't happy, but she takes off her [the_clothing.name] and resumes talking about her taxes."
                    if test_outfit.tits_visible():
                        "Getting a good look at her tits makes the boring topic much more interesting. After a few minutes you've sorted out her problems. She goes to dry her top while you get back to work."
                    else:
                        "You spend a few minutes and sort out all of her problems. When you're done she goes off to dry her top while you get back to work."
                    $ the_clothing.colour = dry_colour
                    $ the_person.outfit.add_upper(the_clothing)

    $ renpy.scene("Active")
    return

init 1 python:
    def home_fuck_crisis_requirement():
        if mc_asleep():
            if mc.business.get_max_employee_slut()>=15: #We need them to start with at least sluttiness 15 so a bonus and some foreplay will get you up to sex range.
                return True
        return False

    home_fuck_crisis = Action("Home Fuck Crisis",home_fuck_crisis_requirement,"home_fuck_crisis_label")
    crisis_list.append([home_fuck_crisis,3])

label home_fuck_crisis_label():
    ## A horny employee comes to your house at night and wants you to fuck them. They're drunk, with bonus sluttiness, and will tkae a pay cut if you make them cum.
    $ meets_sluttiness_list = []
    python:
        for person in mc.business.get_employee_list():
            if person.sluttiness >= 15 and (person.relationship == "Single" or person.get_opinion_score("cheating on men") > 0):
                meets_sluttiness_list.append(person)
    $ the_person = get_random_from_list(meets_sluttiness_list)
    if the_person is None:
        return

    "Some time late in the night, you're awoken by the buzz of your phone getting a text. You roll over and ignore it."
    "A few minutes later it buzzes again, then again. You're forced to wake up and see what is the matter."
    "[the_person.title] has been texting you. She's sent you several messages, with the last ending:"
    the_person.char "I'm here... Should I just knock on the door?"
    "You drag yourself out of bed and stumble out to the front hall. You move to a window and peek out at your front door."
    $ the_person.draw_person(emotion = "happy") #TODO: Create a set of late night outfits that she can be wearing.
    $ the_person.add_situational_slut("drunk", 20, "More than a little tipsy.")
    "You see [the_person.title] standing outside. You open the door before she goes to knock."
    mc.name "[the_person.title], what are you doing here? It's the middle of the night."
    "[the_person.possessive_title] takes a step towards you, running a hand down your chest. You guide her outside so she won't wake up your mother or sister."
    the_person.char "Oh [the_person.mc_title], I just had the worst night and I need you to help me!"
    "You can smell alcohol on her breath."
    the_person.char "I was out with some friends, and I got talking with this guy..."
    if the_person.relationship != "Single":
        $ SO_title = SO_relationship_to_title(the_person.relationship)
        mc.name "Wait, don't you have a [SO_title]?"
        the_person.char "So? He doesn't need to know about everything I do. So there I was with this guy..."
    the_person.char "We were getting along so well, so I went home with him. We get to his place and make out in his car for a while..."
    "You stay silent, listening to [the_person.title]'s rambling story."
    $ the_person.draw_person(emotion = "angry")
    the_person.char "Then he tells me, suprise, he's married and his wife is home."
    if the_person.get_opinion_score("cheating on men") < 0:
        the_person.char "I don't want to be a home wrecker, so I got out of there as fast as I could. I'm here because I'm still a little horny, and you're the first guy I thought of."
    elif the_person.get_opinion_score("cheating on men") > 0:
        $ the_person.discover_opinion("cheating on men")
        the_person.char "That just got me more turned on, but before I get some his wife called. He got spooked and called it off."
        the_person.char "I took a cab here because I'm still horny and you're the first guy I thought of."
    elif the_person.sluttiness > 50:
        the_person.char "Well I wasn't going to let that stop me, so I say we should fuck in his car."
        the_person.char "We're just getting warmed up when his wife calls, then he gets spooked and says that it's a bad idea..."
        the_person.char "So I took a cab here, because I'm still horny and I want {i}someone{/i} to fuck me tonight."
    else:
        the_person.char "He wanted to have sex in his car, but I'm not that easy. I told him I knew someone with a bed who would love to have me..."
        the_person.char "So I got a taxi and came here, because you're the first guy I thought of."

    "[the_person.possessive_title] takes a not very subtle look at your crotch."
    $ the_person.draw_person(emotion = "happy")

    the_person.char "Can you help me? I need you to make me cum so fucking badly right now..."
    "She places her hands on your hips and steps close."
    menu:
        "Help her cum. (tooltip)She would love to climax right now, but seems like she would be very disappointed if you can't get here there." if mc.current_stamina > 0:
            "You take [the_person.title]'s hands and lead her through your house to your room."
            mc.name "You'll need to be quiet, there are other people in the house."
            the_person.char "That's fine, as long as none of them are your wife!"
            $ mc.current_stamina += -1
            call fuck_person(the_person) from _call_fuck_person_4
            #Now that you've had sex, we calculate the change to her stats and move on.
            if the_person.arousal > 100:
                $ the_person.change_obedience(3)
                $ the_person.change_love(5)
                $ the_person.change_happiness(5)
                the_person.char "Mmm, that was just what I needed [the_person.mc_title]. Ah..."
                "You and [the_person.title] lounge around for a few minutes until she has completely recovered."
                the_person.char "I had a great time [the_person.mc_title], but I should be getting home. Could you call me a cab?"

            else:
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(-5)
                the_person.char "Ugh, fuck! This is worse than it was before! Screw it, I'll take care of this at home. Call me a cab, please."

            $ the_person.reset_arousal()
            $ renpy.scene("Active")
            "A few minutes later [the_person.title] is gone, and you're able to get back to bed."

        "Help her cum.\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
            pass

        "Ask her to leave. (tooltip)She would love to climax, but seems like she would be very disappointed if you can't get here there.":
            mc.name "[the_person.title], you're drunk and not thinking straight. I'll call you a cab to get you home, in the morning this will all seem like a bad idea."
            $ the_person.draw_person(emotion = "sad")
            the_person.char "Really? Oh come on, I need you so badly though..."
            "You place your hands on [the_person.title]'s shoulders and keep her at arms length."
            mc.name "Trust me, it's for the best."
            $ the_person.change_obedience(1)
            $ the_person.change_love(1)
            "You call a cab for [the_person.title] and get her sent home. She might not thank you for it, but she'll be more likely to listen to you from now on."

    $ the_person.clear_situational_slut("drunk")
    return

init 1 python:
    def quiting_crisis_requirement(): #We are only going to look at quitting actions if it is in the middle of the day when people are at work.
        if time_of_day == 1 or time_of_day == 2 or time_of_day==3:
            return True
        else:
            return False

label quitting_crisis_label(the_person): #The person tries to quit, you have a chance to keep her around for a hefty raise (Or by fucking her, if her sluttiness is high enough).
    if mc.business.get_employee_workstation(the_person) is None:
        return #They're already not employed now, just return and go about your business.

    if the_person.get_job_happiness_score() >= 0:
        return #They've become happy with their job, so just clear this from the list and move on. They don't actually quit.

    "Your phone buzzes, grabbing your attention. It's an email from [the_person.title], marked \"Urgent, need to talk\"."
    "You open up the email and read through the body."
    the_person.char "[the_person.mc_title], there's something important I need to talk to you about. When can we have a meeting?"
    $ the_place = mc.business.h_div
    if mc.location == mc.business.h_div: #If you're arleady in your office just kick back and relax.
        $ the_place.show_background()
        "You type up a response."
        mc.name "I'm in my office right now, come over whenever you would like."
        "You organize the papers on your desk while you wait for [the_person.title]. After a few minutes she comes in and closes the door behind her."
    else:
        "You type up a response."
        mc.name "I'm out of the office right now, but if it's important I can be back in a few minutes."
        the_person.char "It is. See you at your office."
        $ the_place.show_background()
        "You travel back to your office. You're just in the door when [the_person.title] comes in and closes the door behind her."

    $the_person.draw_person()
    the_person.char "Thank you for meeting with me on such short notice. I thought about sending you an email but I think this should be said in person."
    "[the_person.title] takes a deep breath then continues."
    if the_person.happiness < 100:
        the_person.char "I've been doing my best to keep my head up lately, but honestly I just have been hating working here. I've decided that today is going to be my last day."
    elif the_person.salary < the_person.calculate_base_salary():
        the_person.char "I've been looking into other positions, and the pay I'm recieving here just isn't high enough. I've decided to accept another offer; today will be my last day."
    else:
        the_person.char "I've been looking for a change in my life, and I feel like this job is holding me back. I've decided that today is going to be my last day."

    menu:
        "Offer a raise.":
            mc.name "I'm very sorry to hear that [the_person.title], I understand that your job can be difficult at times."
            "You pull out [the_person.title]'s employee records and look them over."
            mc.name "Looking at this I can understand why you would be looking for greener pastures. How much of a raise would it take to convince you to stay?"

            $ deficit = -the_person.get_job_happiness_score()
            $ deficit += 5 #She needs a little extra to make it worth her while.
            "[the_person.possessive_title] takes a long moment before responding."
            the_person.char "I think I would need an extra $[deficit] a day in wages. That would keep me here."
            menu:
                "Accept. (+$[deficit]/day)":
                    $ the_person.salary += deficit
                    $ raise_string = the_person.title +": +$" +str(deficit) + "/day Salary"
                    $ mc.log_event(raise_string,"float_text_green")
                    mc.name "That sounds completely reasonable. I'll mark that down right now and you should see your raise in your next paycheck."
                    the_person.char "Thank you sir, I'm glad we were able to come to an agreement."

                "Refuse.":
                    mc.name "That's going to be very tough to do [the_person.title], it just isn't in the budget right now."
                    the_person.char "I understand. I suppose I will start clearing out my desk, I'll be gone by the end of the day."
                    "[the_person.title] lets herself out of your office. You take a moment to complete the required paperwork and get back to what you were doing."
                    $ mc.business.remove_employee(the_person)


        "Make her cum to convince her to stay." if the_person.effective_sluttiness() > 60 and mc.current_stamina > 0:
            "You stand up from your desk and walk over to [the_person.title]."
            mc.name "[the_person.title], you've always been a good employee of mine."
            if the_person.outfit.vagina_available():
                "You reach a hand down between [the_person.title]'s legs and run a finger over her pussy."
            elif the_person.outfit.tits_available():
                "You cup one of [the_person.title]'s breasts and squeeze it lightly."
            else:
                "You reach around and grab [the_person.title]'s ass with one hand, squeezing it gently."
            mc.name "Let me show you the perks of working around here, if you still want to quit after then I won't stop you."
            "[the_person.possessive_title] thinks for a moment, then nods."
            $ mc.current_stamina += -1
            call fuck_person(the_person) from _call_fuck_person_5
            if the_person.arousal > 100: #If you made them cum, they'll stay on for a little while.
                the_person.char "Ah... Ah..."
                mc.name "Well [the_person.title], are you still thinking of leaving?"
                "[the_person.title] pants slowly and shakes her head."
                the_person.char "I don't think I will be, sir. Sorry to have wasted your time."
                mc.name "It was my pleasure."
                "[the_person.possessive_title] takes a moment to put herself back together, then steps out of your office."

            else: #If you fail to make them cum first they quit and leave.
                the_person.char "I'm sorry [the_person.mc_title], but I haven't changed my mind. I'll clear out my desk and be gone by the end of the day."
                "[the_person.possessive_title] takes a moment to put herself back together, then steps out of your office."
                $ mc.business.remove_employee(the_person)
            $ the_person.reset_arousal()

        "Make her cum to convince her to stay.\n{size=22}Requires Stamina{/size} (disabled)" if the_person.effective_sluttiness() > 60 and mc.current_stamina == 0:
            pass

        "Let her go.":
            mc.name "I'm sorry to hear that [the_person.title], but if that's the way you feel then it's probably for the best."
            the_person.char "I'm glad you understand. I'll clear out my desk and be gone by the end of the day."
            "[the_person.possessive_title] leaves, and you return to what you were doing."
            $ mc.business.remove_employee(the_person)

    $renpy.scene("Active")
    return

init 1 python:
    def invest_opportunity_crisis_requirement():
        #Be at work during work hours with at least two other peopel with relatively low obedience
        if mc.business.research_tier > 0 and mc.business.is_open_for_business() and not invest_opportunity_crisis in mc.business.mandatory_crises_list:
            if mc.is_at_work():
                return True
        return False

    invest_opportunity_crisis = Action("Investment Opportunity",invest_opportunity_crisis_requirement,"invest_opportunity_crisis_label")
    crisis_list.append([invest_opportunity_crisis,2])

    def invest_rep_visit_requirement(trigger_day):
        if day == trigger_day:
            if mc.is_at_work():
                return True
            elif time_of_day == 3: #End of day, return True only so the event fires and you get an angry phonecall.
                return True
        return False

label invest_opportunity_crisis_label():
    #You receive a call asking for a tour of your facilities. Once there the investvestment agent can be "persuaded" to impress them.
    "Your phone rings while you're busy working. You lean back in your chair and answer it."
    mc.name "[mc.business.name] here, [mc.name] speaking."
    $ rep_name = get_random_male_name()
    rep_name "Ah, [mc.name], I'm glad I was able to get ahold of you. My name is [rep_name]."
    rep_name "I am the local representative of a rather large mutual fund. It is my responsibility to evaluate local businesses and see if they would be worthwhile investments."
    rep_name "My research turned up your company, and we might be interested in making an investment. I was hoping I could set up a tour with you to take a look around and ask you some questions."
    menu:
        "Offer [rep_name] a tour.":
            mc.name "That sounds like a wonderful idea. Would you be available this coming Monday?"
            rep_name "Monday will be fine. Thank you for your time [mc.name], we will be in touch again soon."
            "[rep_name] hangs up the phone. You make a note on your calander for next Monday, leaving a reminder to be in the office during working hours."
            $ invest_rep_visit = Action("Investment Representative Visit",invest_rep_visit_requirement,"invest_rep_visit_label", args = rep_name, requirement_args = [day + 7 - (day%7)]) #Set the trigger day for the next monday. Monday is day%7 == 0
            $ mc.business.mandatory_crises_list.append(invest_rep_visit) #Add the event here so that it pops when the requirements are met.

        "Turn [rep_name] away.":
            mc.name "I'm flattered to hear you're interested, but we are not open to the public."
            rep_name "We could be talking about a significant investment here, are you sure you don't want to reconsider?"
            mc.name "As I said, we are not open to the public. Thank you for your time."
            "You hang up the phone and get back to your work."

    return

label invest_rep_visit_label(rep_name):
    #There are two possible ways this event is triggered. First we will handle if the player is late to the meeting (aka not at work on the day in question). They get an angry phonecall and the event ends.
    if time_of_day == 3:
        "Your phone rings. When you check it you recognise the name [rep_name], the representative of a mutual fund that you had promised a tour. You answer your phone."
        mc.name "[rep_name], I'm so sorry to have kept you waiting, I..."
        rep_name "Don't bother, I've been waiting here all day but if you can't be bothered to show up to your own office for a planned tour I want nothing to do with your business. Good day."
        "[rep_name] hangs up. You doubt he will be interested in rescheduling."
    else:
        #The event was triggered properly, aka the MC was at their office during the next Monday, so they meet rep_name and give them a tour of the facilities.
        "Your phone rings. When you check it you recognise the name [rep_name], the represntative of a mutual fund that you had promised a tour. You answer your phone."
        mc.name "[rep_name], good to hear from you. How are you doing?"
        rep_name "I'm doing well. I'm just pulling into your parking lot now, do I need to check in at security?"
        mc.name "Don't worry about it, I'll come out and meet you and we can start the tour."
        "You hurry out to the parking lot and spot a man you assume to be [rep_name] getting out his car. He's middle aged, not particularly handsome, and dressed conservatively in a suit and tie."
        rep_name "Good to finaly meet you in person."
        "He reaches out his hand and you shake it."
        rep_name "Before we get started I wanted to ask you some questions about what you do here."
        mc.name "I'll answer whatever I can."
        rep_name "Your business licence says you're working in commercial pharmaceuticals. What, exactly, does that mean?"
        $ lobby.show_background()
        "You lead [rep_name] into the office lobby."
        mc.name "We have a number of different products that we produce, but they're all based on the same fundamental principle."
        mc.name "Our products remove personal inhibitions, limitations, fears. All of those mental roadblocks that stop us from achieving what we want to in life."
        "[rep_name] nods as if he understands."
        "You decide it would be a good idea to call up someone to help you convince [rep_name] of the value of your product."
        if mc.business.get_employee_count() == 0:
            "Unfortunately, you're the only employee of your own business, so you have nobody to show off to [rep_name]."
            "Instead you show him around the various empty departments. It becomes clear with time that he is less than impressed."
            rep_name "Thank you for taking time out of your day and showing me around, but I don't think I could suggest we invest anything in a one man operation like this."
            rep_name "I'll keep an eye on you though, if you grow your business a little bit maybe I'll call you up and we can reevaluate."
            mc.name "I understand completely. I'll walk you out."
            "You walk [rep_name] back to his car and watch as he drives away."
        else:
            mc.name "Actually, how about I call down one of my employees and have them give you a tour around. They've all had much more experience with our product than I have."
            rep_name "That sounds like an excellent idea, I would like to talk to someone who is involved with the day to day operations around here."
            call screen employee_overview(person_select = True)
            $ helper = _return
            "You send [helper.title] a text to meet you. You and [rep_name] grab chairs and wait in the lobby until she arrives."
            $ helper.draw_person()
            if helper.outfit.slut_requirement > 60:
                "[rep_name]'s goes slack-jawed when he sees [helper.title] wearing not much at all."
            elif helper.outfit.slut_requirement > 20:
                "Your idle conversation with [rep_name] trails off when [helper.title] comes into the room. You see his eyes run up and down her before he regains his composure."
            else:
                "[rep_name] smiles and nods at [helper.title] as she comes into the room."

            helper.char "How can I help [helper.mc_title]?"
            "You take [helper.possessive_title] to the side and tell her what you want her to do."
            $ success_chance = 10
            $ flirt_requires_string = "Flirt with " + rep_name + ".\n{size=22}Requires: Obedience 110, " + get_red_heart(10) + "{/size}"
            $ seduce_requires_string = "Seduce " + rep_name + ".\n{size=22}Requires: Obedience 130, " + get_red_heart(60) + "{/size}" #TODO: check to make sure that the sluttiness requirement is being shown.

            menu:
                "Impress [rep_name].": #Simplest option, just positive talk about the company.
                    mc.name "[rep_name] here is interested in learning more about the company; I would like you to give him a full tour."
                    "[helper.title] nods and turns to [rep_name]."
                    helper.char "[rep_name], I'll be your tour guide today. If you just follow me, there is plenty to see."
                    mc.name "I'll be in my office taking care of some paperwork, bring [rep_name] to me when you're done with the tour."
                    "[rep_name] stands and follows [helper.possessive_title] out of the lobby. You return to your office to kill some time and avoid getting in the way."
                    $ success_chance += 5*(helper.charisma + helper.market_skill)
                    $ success_chance += helper.outfit.slut_requirement/5 #Our success chance is based on the impressing persons charisma and marketing, with a small bonus based on their outfit's sluttiness.

                "Flirt with [rep_name]." if helper.sluttiness >= 20 and helper.obedience >= 110: #Requires some sluttiness, more effective than impress.
                    mc.name "[rep_name] here is interested in learning more about the company; I would like you to give him a full tour."
                    helper.char "I can take care of that."
                    mc.name "One more thing: I doubt he spends much time around someone as beautiful as you. Lay the charm on thick for him."
                    "[helper.title] smiles and nods, then turns to [rep_name]."
                    helper.char "[rep_name], it's a pleasure to meet you. I will be your tour guide today, so if you just follow me we have plenty to see."
                    "[rep_name] stands up and follows [helper.possessive_title] out of the lobby. While they're walking away [helper.title] places a hand on his arm."
                    $ helper.draw_person(position = "walking_away")
                    helper.char "This is a wonderful suit by the way, it fits you fantastically. Where do you shop?"
                    "The sound of their conversation trails off as they leave the room. You retreat to your office to kill some time and avoid getting in the way."
                    $ success_chance += 7*(helper.charisma + helper.market_skill)
                    $ success_chance += helper.outfit.slut_requirement/4 #Same basic calculations as above but both outfit sluttiness and charisma/skill are more effective.

                "[flirt_requires_string] (disabled)" if not (helper.sluttiness >= 20 and helper.obedience >= 110):
                    pass

                "Seduce [rep_name]." if helper.sluttiness >= 60 and helper.obedience >= 130: #Take rep_name off screen and "convince" him to invest in your company. Highest effectiveness but requires high levels of sluttiness and obedience.
                    mc.name "[rep_name] here is interested in learning more about the company. I need you to give him a complete tour and show him our operations."
                    helper.char "I can take care of that sir."
                    mc.name "Good. Now this is important so once the tour is done I want you to pull him into one of the meeting rooms and make sure he has a very pleasant visit."
                    "[helper.title] looks past you at [rep_name] and smiles mischievously."
                    helper.char "That I can certainly do. Excuse me, [rep_name]? I will be your tour guide today. If you follow me we can begin."
                    $ helper.draw_person(position = "walking_away")
                    "[rep_name] stands up and follows [helper.possessive_title] out of the lobby. [helper.title] seems to swing her hips a little more purposefully as she walks in front of [rep_name]."
                    "You retreat to your office to kill some time and avoid getting in the way of the tour."
                    $ success_chance += 4*(helper.charisma + helper.market_skill) # Lower stat contribution but...
                    $ success_chance += helper.outfit.slut_requirement/3 # Higher outfit contribution and...
                    python:
                        for skill in helper.sex_skills:
                            success_chance += helper.sex_skills[skill] #And all sex skills contribute, an average of +4 resulting in a higher average score.

                "[seduce_requires_string] (disabled)" if not (helper.sluttiness >= 60 and helper.obedience >= 130):
                    pass

            $ renpy.scene("Active")
            $ office.show_background()
            "Half an hour later there is a knock on your office door."
            mc.name "Come in."
            $ helper.draw_person()
            helper.char "All done with the tour. Let me know if you need anything else."
            "[rep_name] steps into your office and [helper.title] closes the door behind him. [rep_name] sits down in the chair on the opposite side of your desk."
            $ renpy.scene("Active")
            $ random_roll = renpy.random.randint(0,100)
            if random_roll < success_chance:
                rep_name "I won't waste any more of your time [mc.name], I can say with certainty that my investors are going to be interested in investing in your business."
                mc.name "I'm glad to hear it."
                rep_name "I would like to offer you $5000 to help you expand your business. In exchange we would like to be kept informed of your scientific progress."
                menu:
                    "Accept $5000.":
                        "You reach your hand across the table to shake [rep_name]'s hand."
                        mc.name "I think we have a deal. Lets sort out the paperwork."
                        $ mc.business.funds += 5000
                        "Within an hour $5000 has been moved into your companies bank account. [rep_name] leaves with a report detailing your current research progress."


                    "Reject the offer.":
                        mc.name "That's a very tempting offer, but we keep a tight grip on all of our research material."
                        "[rep_name] nods and stands up."
                        rep_name "I understand. Maybe in the future you will reconsider. Thank you for your time and the tour."
                        "You walk [rep_name] back to his car and watch as he drives away."

            else:
                rep_name "I won't waste any more of your time [mc.name]. What you're doing here is certainly, ah, interesting, but I don't think I can recommend it as a sound investment at the moment."
                rep_name "In the future I might visit again to reevaluate though."
                mc.name "I understand. Thank you for your time, I'll see you out."
                "You walk [rep_name] back to his car and watch as he drives away."
    return

init 1 python:
    def work_relationship_change_crisis_requirement():
        if mc.business.is_open_for_business():
            if mc.business.get_employee_count >= 2: #Quick check to avoid doing a full array check on a starting company
                if town_relationships.get_business_relationships(types = "Acquaintance"):
                    return True
        return False
    work_relationship_change_crisis = Action("Work Relationship Change Crisis", work_relationship_change_crisis_requirement, "work_relationship_change_label")
    crisis_list.append([work_relationship_change_crisis,12])

label work_relationship_change_label():
    $ the_relationship = get_random_from_list(town_relationships.get_business_relationships())
    if the_relationship is None:
        return

    if renpy.random.randint(0,1) == 0:
        $ person_one = the_relationship.person_a
        $ person_two = the_relationship.person_b
    else:
        $ person_one = the_relationship.person_b
        $ person_two = the_relationship.person_a

    $ friend_chance = 50
    python:
        for an_opinion in person_one.opinions:
            if person_one.get_opinion_score(an_opinion) == person_two.get_opinion_score(an_opinion):
                friend_chance += 10
            elif (person_one.get_opinion_score(an_opinion) > 0 and person_two.get_opinion_score(an_opinion) < 0) or (person_two.get_opinion_score(an_opinion) > 0 and person_one.get_opinion_score(an_opinion) < 0):
                friend_chance += -10

        friend_chance += (person_one.get_opinion_score("small talk")*5) + (person_two.get_opinion_score("small talk")*5)


    if renpy.random.randint(0,100) < friend_chance:
        #Their relationship improves
        $ town_relationships.improve_relationship(person_one, person_two)
        if mc.is_at_work():
            "While working you notice [person_one.title] and [person_two.title] are spending more time together. They seem to have become friends!"
    else:
        #Their relationship worsens
        $ town_relationships.worsen_relationship(person_one, person_two)
        if mc.is_at_work():
            "While working you notice [person_one.title] and [person_two.title] aren't getting along with each other. They seem to have developed an unfriendly rivalry."

    return

init 1 python:
    def work_chat_crisis_requirement():
        if mc.business.is_open_for_business() and mc.is_at_work():
            if len(mc.location.people) > 0: #If we're open for business and there are people in the same location as us
                return True
        return False

    work_chat_crisis = Action("Work Chat Crisis", work_chat_crisis_requirement, "work_chat_crisis_label")
    crisis_list.append([work_chat_crisis,12])

label work_chat_crisis_label:
    if not mc.business.is_open_for_business() or not mc.is_at_work():
        return

    $ possible_people = []
    python:
        for person in mc.location.people:
            if mc.business.get_employee_title(person) != "None" and not person.get_opinion_score("small talk") < 0:
                possible_people.append(person)
    $ the_person = get_random_from_list(possible_people)
    if the_person is None:
        return #Everyone here must hate small talk. Oh well.

    #She stikes up a conversation while you're working. "So what have you been up to"/"Do anything fun recently?"/"It's nice to have some company (only if only person in room)", etc.
    #If low sluttiness you just have a nice chat. Add options to flirt, nothing major. Maybe talk about opinion stuff.
    #If moderate sluttiness she may flash you, bend over provocatively, touch herself, etc. Maybe asks to see your cock if nobody else is around.
    #If high sluttiness and low/moderate obedience she will ask you to fuck her. If high obedience she will ask if you need any "stress relief". Other people around act accordingly.

    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits beside you while you're working."
    if len(mc.location.people) <= 1: #it's just you and her.
        the_person.char "It's nice to have some company, glad you're here [the_person.mc_title]."
    else:
        the_person.char "Glad to have you helping out [the_person.mc_title]."
    "[the_person.title] makes small talk with you for a few minutes while you work."
    if the_person.sluttiness < 30: #Just chat
        menu:
            "Talk about work.":
                mc.name "So, any interesting office stories that I might not have heard?"
                the_person.char "Well, nothing about anyone I work with now, but at my last job..."
                "[the_person.possessive_title] dives into a long story. You listen and nod, keeping most of your attention on your own work until she finishes."
                the_person.char "...Of course, I'd never dream of doing something like that here."
                $ the_person.change_obedience(5)
                mc.name "Glad to hear it."

            "Talk about her hobbies.":
                mc.name "So, anything you're looking forward to soon?"
                if the_person.get_opinion_score("sports") > 0:
                    the_person.char "Well, there's a big football game coming in a couple days that I'm excited for. The tournament so far has been..."
                    $ the_person.discover_opinion("sports")
                    "[the_person.possessive_title] gives a passionate story about her favourite teams recent success. You listen and nod, keeping most of your attention on your own work."
                    the_person.char "...But we'll see if all of that pays off."

                elif the_person.get_opinion_score("hiking") > 0:
                    the_person.char "Well, I'm planning a big hiking trip for next summer. I've got my route all planned out..."
                    $ the_person.discover_opinion("hiking")
                    "[the_person.possessive_title] gives an interesting story about her last hiking trip. You listen and nod, keeping most of your attention on your own work."
                    the_person.char "...So we'll have to see if the tent holds up this time."

                else:
                    the_person.char "Soon? Let me think... I'm going to go see a movie with a friend in a few days. She's been off..."
                    "[the_person.possessive_title] talks about some of her plans for the weekend. You listen and nod, keeping most of your attention on your own work until she's finished."
                    the_person.char "...Other than that, I think I'm just going to be taking it easy."
                $ the_person.change_happiness(5)
                the_person.char "Anyways, I'll stop talking your ear off and let you get back to work. Thanks for chatting!"

            "Talk about her body.":
                mc.name "Hey, I wanted to tell you that you're looking really good. You must really take care of yourself."
                if len(mc.location.people) <= 1:
                    the_person.char "Oh, well thank you. Should we really be talking about that though?"
                    "She looks away, a little embarrassed."
                    mc.name "There's nobody else around; I don't think there's anything wrong with appreciating the work someone puts into making sure they look good."
                    if the_person.get_opinion_score("showing her tits") > 0:
                        the_person.char "I... I guess you're right. Do you think I look good?"
                        "[the_person.title] turns in her chair to look at you."
                        mc.name "Of course, you look fabulous!"
                        if not the_person.outfit.tits_visible():
                            if the_person.has_large_tits():
                                the_person.char "What do you think about my... breasts? I've always thought they're one of my best features."
                                "She presses her arms together, accentuating her nice big tits."
                                the_person.char "Oh my god, what am I saying. I'm sorry [the_person.mc_title], I shouldn't..."
                                mc.name "No, it's fine. You're right, they look great."
                                "[the_person.possessive_title] breathes out slowly. She's blushing hard and is avoiding making eye contact."
                                the_person.char "Thank you. We should... we should be focusing on our work."
                            else:
                                the_person.char "What do you think about my... breasts? I've always liked them, but I know most guys like them bigger."
                                "She moves her arms to the side so you can get a better look at her chest. She's not big breasted, but you enjoy the view either way."
                                the_person.char "Oh my god, what am I saying. I'm sorry [the_person.mc_title], I shouldn't..."
                                mc.name "No, it's fine. I like them a little on the small side. I'd need a better look to be sure, but I'd bet they look fantastic."
                                "[the_person.possessive_title] breathes out slowly. She's blushing hard and is avoiding making eye contact."
                                the_person.char "Thank you. We should... we should be focusing on our work."
                        else:
                            the_person.char "What do you think of my... breasts? I mean, I know you can already see them, but do you like them too?"
                            if the_person.has_large_tits():
                                "[the_person.possessive_title] stops trying to hide her big, naked tits and lets you get a good look. She blushes intensely."
                            else:
                                "[the_person.possessive_title] stops trying to hide her cute little tits and lets you get a good look. She looks off to the side and blushes."
                            mc.name "I think they're one of your best features."
                            the_person.char "Thank you. We should... we should probably be focusing on our work."
                        $ the_person.change_slut_temp(6*the_person.get_opinion_score("showing her tits"))
                        "You and [the_person.title] finish talking and get back to work."

                    elif the_person.get_opinion_score("showing her ass") > 0:
                        the_person.char "I... I guess you're right. There isn't anything wrong with that. What do you think of my butt? I've always been kind of proud of it."
                        $ the_person.draw_person(position = "back_peek")
                        "[the_person.title] stands up and turns around for you."
                        mc.name "It's cute, I like it."
                        $ top_clothing = None
                        if the_person.outfit.get_lower_ordered():
                            $top_clothing = the_person.outfit.get_lower_ordered()[-1]

                        if top_clothing:
                            "[the_person.possessive_title] pulls at her [top_clothing.name], sliding it down a little bit as if she's about to remove it."
                            the_person.char "What am I doing... I'm sorry, I got a little carried away."
                            $the_person.draw_person()
                            mc.name "It's fine, don't worry about it."
                        else:
                            "[the_person.possessive_title] wiggles her butt at you."
                            the_person.char "I guess everyone's already had a good look at my ass anyways..."
                            $the_person.draw_person()
                            "[the_person.anme] stands up suddenly and turns back towards you."
                            the_person.char "I'm sorry, I don't know what came over me [the_person.mc_title]. I'll just... I'll just sit down again."

                        $the_person.draw_person(position="sitting")
                        "[the_person.possessive_title] sits down and takes a deep breath. She's blushing and avoiding making eye contact with you."
                        $ the_person.change_slut_temp(6*the_person.get_opinion_score("showing her ass"))
                        the_person.char "I think we should be focusing on our work, don't you agree?"

                    else:
                        the_person.char "I... think you're right, there's nothing wrong with it. I guess that means I can tell you that you're a pretty good looking guy."
                        mc.name "Well I'm not going to turn down the compliment."
                        "[the_person.title] looks your body up and down. Her eyes linger at your crotch, so you take a moment to reposition your cock in your pants."
                        "After a few seconds [the_person.possessive_title] shakes her head clear and turns her attention back to her work."
                        $ the_person.change_slut_temp(5)
                        the_person.char "Sorry, I'm getting us both distracted when we've got work to do."

                else:
                    the_person.char "Oh, thank you! I do my best to work out, watch what I eat. All of that good stuff."
                    mc.name "Well it certainly pays off. You've got a nice butt, cute breasts, the whole package."
                    "[the_person.title] blushes and glances around the room at her co-workers."
                    the_person.char "Oh my god, stop [the_person.mc_title]! Could you imagine if someone heard you talking like that?"
                    "She bites her lip and smiles. You catch her eyes flick down to your crotch for a split second."
                    $ the_person.change_slut_temp(5)
                    the_person.char "But thank you, I like hearing it. Now don't you have work you're suppose to be doing?"

    elif the_person.sluttiness < 60: #Moderate sluttiness
        "After a minute or two [the_person.title] stands up and stretches."
        $ the_person.draw_person()
        the_person.char "Don't mind me, I just a minute to relax before I get back to work."
        mc.name "No problem, take your time."
        $ the_person.draw_person(position = "back_peek")
        if the_person.has_large_tits():
            if the_person.outfit.tits_visible():
                "[the_person.possessive_title] bends over and stretches against the desk you're working at. Her large tits hang below her, swinging back and forth."
            else:
                "[the_person.possessive_title] bends over and stretches against the desk you're working at. Her large tits strain against her clothing."
        else:
            "[the_person.possessive_title] bends over and stretches against the wall beside you. She glances over her shoulder and wiggles her butt."
        the_person.char "It's nice having you here as a distraction [the_person.mc_title]. Sitting at a desk all day drives me a little stir crazy."
        $ the_person.draw_person(position="sitting")

        if len(mc.location.people) <= 1:
            if not the_person.get_opinion_score("public sex") < 0:
                "She sits back down beside you. You work together for a few more minutes before she sighs and puts her pen down again."
                if the_person.obedience < 110:
                    the_person.char "Sorry, I just still can't focus. I'm going to take my five minute break, I hope you don't mind."
                else:
                    the_person.char "Sorry sir, I just can't focus. Would you mind if I took a five minute break?"
                    mc.name "If that's what you need to do, just don't take too long."

                if the_person.outfit.vagina_available():
                    "[the_person.title] slides her chair back from the desk and runs her finger along her pussy. She bites her lip and moans quietly to herself."
                else:
                    if the_person.outfit.get_lower_ordered(): #Purely a safety check to avoid crashes.
                        $ top_layer = the_person.outfit.get_lower_ordered()[-1]
                        "[the_person.title] rolls her chair back from the desk and slides a hand inside of her [top_layer.name]. She bites her lip and moans quietly to herself."

                the_person.char "Ah... I really needed this. If you need to do the same I understand."
                "She sighs and leans back in her office chair, legs spread while she touches herself."
                menu:
                    "Masturbate with [the_person.title]." if mc.current_stamina>0:
                        mc.name "You know, I think that's a good idea."
                        "You slide your own chair away from the desk and unzip your pants. [the_person.possessive_title] watches as you pull your cock free."
                        if the_person.get_opinion_score("masturbating") > 0:
                            the_person.char "Ah... I love being able to touch myself like this. There's nothing better than being in control of your own pleasure, right?"

                        elif the_person.get_opinion_score("masturbating") == 0:
                            the_person.char "Mmm, it's nice to get myself off like this sometimes. I really breaks up the monotony of the day."

                        else:
                            the_person.char "I don't normally like doing this, but I guess it's the only way I'll be able to focus today."

                        $ the_person.discover_opinion("masturbating")
                        "You start to stroke yourself off while [the_person.title] fingers herself in front of you. Her eyes are fixed on your hard shaft."
                        "You're both quiet for a few minutes while you get yourselves off. [the_person.title]'s breathing gets faster and her movements more frantic."
                        $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                        the_person.char "Oh god... here I come!"
                        "She gasps and grabs at the office chair arm with her free hand. Her body stiffens for a second, then relaxes all at once."
                        "The sight of [the_person.title] making herself cum drives you even closer to your own orgasm."
                        $ the_person.draw_person(position = "sitting")
                        the_person.char "Are you almost there?"
                        "You moan and nod."
                        if the_person.get_opinion_score("drinking cum") > 0:
                            "[the_person.possessive_title] gets up from her chair and kneels down between your legs."
                            $ the_person.draw_person(position="blowjob")
                            the_person.char "Do you you want to cum in my mouth?"
                            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                            "You're right on the edge. You nod and she opens her mouth and sticks out her tongue."
                            $ the_person.cum_in_mouth()
                            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                            "You stroke your cock faster and push yourself over the edge, pumping your cum into [the_person.title]'s waiting mouth. She closes her eyes and sighs happily with each spurt."
                            $ the_person.change_slut_temp(the_person.get_opinion_score("drinking cum"))
                            $ the_person.discover_opinion("drinking cum")
                            "You slump back when you're done, feeling tired and content. [the_person.title] closes her mouth and swallows, wiping the last few drops from her lips with her hand."
                            $ the_person.draw_person(position = "sitting")
                            "She stands up and goes back to her chair."

                        elif the_person.get_opinion_score("cum facials") > 0 or the_person.get_opinion_score("being covered in cum") > 0:
                            "[the_person.possessive_title] gets up from her chair and kneels down between your legs."
                            $ the_person.draw_person(position="blowjob")
                            the_person.char "Do you you want to cum on my face?"
                            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                            "You're right on the edge. You nod and she closes her eyes and tilts her head back."
                            $ the_person.cum_on_face()
                            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                            "You stroke your cock faster and push yourself over the edge, firing your cum onto [the_person.title]'s waiting face. She stays still until you're completely finished."
                            $ the_person.change_slut_temp(the_person.get_opinion_score("cum facials")+the_person.get_opinion_score("being covered in cum"))
                            $ the_person.discover_opinion("being covered in cum")
                            $ the_person.discover_opinion("cum facials")
                            the_person.char "Mmm, that feels nice..."
                            "She sits on her knees for a few seconds, then and goes back to her chair."
                            $ the_person.draw_person(position = "sitting")
                            "She looks around the desk for something to get cleaned up with."

                        else:
                            the_person.char "Do it, I want to watch you cum!"
                            "You grunt and push yourself over the edge. You pump your cum out in spurts onto the floor."
                            the_person.char "Well done, I'll make sure to clean that up in a little bit for you."
                            "You slump back in your chair and take a deep breath."
                        the_person.char "That was really nice [the_person.mc_title], I feel like I can finally focus."
                        "She spins her chair back to her desk and gets back to work, as if nothing out of the ordinary happened."
                        "You zip your pants up and do the same."
                        $ mc.current_stamina += -1

                    "Masturbate with [the_person.title].\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                        pass

                    "Focus on your work.":
                        mc.name "Thanks, but I think I'll just enjoy the show."
                        "She nods and turns her attention to herself. You listen as [the_person.title] touches her own pussy and brings herself closer and closer to masturbating."
                        if the_person.get_opinion_score("public sex")>0:
                            the_person.char "[the_person.mc_title]... I'm going to cum soon. I want you to... I want you to watch me cum."
                            $ the_person.discover_opinion("public sex")
                            $ the_person.change_obedience(the_person.get_opinion_score("public sex"))
                            "You turn your chair and watch [the_person.possessive_title]. Being watched seems to turn her on even more."
                            "It doesn't take long before she's moaning and panting. You watch as she drives herself to climax."
                        else:
                            the_person.char "Oh god... there it is..."
                            "You hear [the_person.title] gasp. You glance over and watch as she climaxes."
                        $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                        "[the_person.possessive_title]'s breath catches in her throat as she cums. Her free hand grasps at the arm of her office chair. She holds still for a few seconds, then lets out a long sigh."
                        $ the_person.change_slut_temp(5+the_person.get_opinion_score("masturbating"))
                        the_person.char "Oh that's so much better... Whew."
                        "[the_person.title] pulls her chair back to her desk and gets back to work, as if nothing out of the ordinary happened."

            else:
                #TODO: She doesn't like the idea of masturbating in front of people. You get back to work.
                the_person.char "I could really use an orgasm right now to help me relax. It'll have to wait until I get home though."
                $ the_person.discover_opinion("public sex")


        else:
            #There are other people. She wants to talk about sex and stuff and other people might comment
            "She sits back down beside you and you both get back to work."
            if not the_person.get_opinion_score("public sex") < 0:
                "A few minutes later you glance over at [the_person.title] and notice some movement below her desk."
                if the_person.outfit.vagina_available():
                    "[the_person.possessive_title] has her legs spread and is gently stroking her pussy below the desk, out of sight of everyone else in the room."
                else:
                    if the_person.outfit.get_lower_ordered():
                        $ top_layer = the_person.outfit.get_lower_ordered()[-1]
                        "[the_person.possessive_title] has a hand down her [top_layer.name]. You can see one of her fingers making little movements under the fabric as she touches herself."

                "You lean over and whisper to her."
                mc.name "Having fun?"
                the_person.char "Oh! I'm sorry I just..."
                "She keeps moving her hand, fingering herself below the desk."
                if len(mc.location.people) > 2:
                    the_person.char "I can't focus and need to do relax. Keep your voice down, I don't want everyone to know."
                else:
                    $ other_people = []
                    python:
                        for person in mc.location.people:
                            if person is not the_person:
                                other_people.append(person)
                    $ other_person = get_random_from_list(other_people)
                    the_person.char "I can't focus and need to do this to relax. Keep your voice down, I don't want [other_person.name] to know."
                "She bites her lip and moans softly."
                if the_person.get_opinion_score("giving handjobs") > 0:
                    the_person.char "Can I... touch your cock? I'm so close and I want to feel it."
                    menu:
                        "Let [the_person.title] touch you.":
                            "You turn your chair to face [the_person.title] and spread your legs. She reaches over with her free hand and plants it on your crotch."
                            $ the_person.change_obedience(the_person.get_opinion_score("giving handjobs"))
                            the_person.char "Oh god, it's so nice and big..."
                            "She rubs your dick with her hand, feeling it's outline through your pants."
                            "You're thinking about pulling your cock out for [the_person.title] when she takes her hand off of you and sits back in her office chair."

                        "Say no.":
                            mc.name "Not when there are other people around."
                            "[the_person.title] pouts for a second, but she's quickly distracted by her own fingers. Her breathing gets faster and louder."
                else:
                    the_person.char "Just... give me a second and I'll be done."
                    "[the_person.title]'s breathing gets faster as she touches herself."

                if the_person.has_large_tits():
                    if the_person.outfit.tits_available():
                        "[the_person.title] grabs one of her exposed tits and squeezes it hard. She takes a deep breath in and holds it."
                    else:
                        "[the_person.title] slides a hand under her clothing and grabs one of her big tits. She squeezes it hard and gasps."
                else:
                    "[the_person.title] grabs at the arm of her chair and squeezes it hard. She takes a deep breath in and holds it for a second."
                "You watch as [the_person.title]'s whole body shivers from her orgasm. She holds still for a second, then breathes out and relaxes completely."
                $ the_person.change_slut_temp(5+the_person.get_opinion_score("public sex") + the_person.get_opinion_score("masturbating"))
                the_person.char "Oh... Oh that's so much better..."
                mc.name "Well thanks for letting me be part of the show."
                "She sits up in her chair and smiles."
                the_person.char "Any time. Now, I really do have work I need to get done."
                "[the_person.possessive_title] grabs a pen and gets back to work as if nothing out of the ordinary happened."


            else:
                pass #She doesn't like the idea of public sex so she doesn't do anything.

    else: #High sluttiness
        if the_person.obedience < 125:
            "You're getting some good work done when [the_person.title] reaches over and plants her hand on your crotch."
            the_person.char "Fuck, I'm feeling so horny right now [the_person.mc_title], I don't think I can concentrate right now..."
            "She finds your zipper and slides it down, letting her get at your already hardening cock."
            the_person.char "Think you can help me?"
            menu:
                "Fuck [the_person.title].\n{size=22}Modifiers: +10 Sluttiness, -5 Obedience{/size}" if mc.current_stamina > 0:
                    the_person.char "I think I can."
                    $ the_person.add_situational_slut("seduction_approach",10,"You promised to focus on me.")
                    $ the_person.add_situational_obedience("seduction_approach",-5,"You promised to focus on me.")
                    $ the_person.change_arousal(10+5*the_person.get_opinion_score("taking control"))
                    $ the_person.discover_opinion("taking control")
                    $ mc.current_stamina += -1
                    call fuck_person(the_person,private = False) from _call_fuck_person_9
                    if the_person.arousal >= 100:
                        the_person.char "Ah... I think I'll actually be able to focus after that. Thanks [the_person.mc_title]."
                    else:
                        the_person.char "Fuck... I don't think that's made the situation any better. All I can think about is getting off..."
                    $ the_person.reset_arousal()
                    $ the_person.review_outfit()
                    #Tidy up our situational modifiers, if any.
                    $ the_person.clear_situational_slut("seduction_approach")
                    $ the_person.clear_situational_obedience("seduction_approach")
                    "Once [the_person.title] gets herself tidied up she sits down at her desk and goes back to work, as if nothing out of the ordinary happened."

                "Fuck [the_person.title].\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                    pass

                "Focus on your work.":
                    mc.name "I don't think so [the_person.title], we've both got work to do right now."
                    $ the_person.change_obedience(5)
                    $ the_person.change_happiness(-5)
                    "[the_person.possessive_title] takes her hand off of your dick and pouts a little, but does eventually focus on her work."

        else:
            "You're getting some good work done when [the_person.title] slides her chair next to yours and runs her hands along your thighs."
            the_person.char "You know if you need anything I'm here for you to use, sir. I know how stressful your job can be..."
            "Her hands move higher, rubbing at your crotch."
            menu:
                "Fuck [the_person.title].\n{size=22}Modifiers: +15 Obedience{/size}" if mc.current_stamina > 0:
                    the_person.char "I think I can."
                    $ the_person.add_situational_obedience("seduction_approach",+15)
                    $ the_person.change_arousal(10+5*the_person.get_opinion_score("being submissive"))
                    $ the_person.discover_opinion("being submissive")
                    $ mc.current_stamina += -1
                    call fuck_person(the_person,private = False) from _call_fuck_person_10
                    the_person.char "Ah... Thank you sir, I hope that helps you focus on all your hard, hard work."
                    $ the_person.reset_arousal()
                    $ the_person.review_outfit()
                    #Tidy up our situational modifiers, if any.
                    $ the_person.clear_situational_slut("seduction_approach")
                    $ the_person.clear_situational_obedience("seduction_approach")
                    "Once [the_person.title] gets herself tidied up she sits down at her desk and goes back to work, as if nothing out of the ordinary happened."

                "Fuck [the_person.title].\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                    pass

                "Focus on your work.":
                    mc.name "I'm fine right now, thank you though. If I need you I'll make sure to let you know."
                    the_person.char "Of course, sir."
                    $ the_person.change_obedience(5)
                    $ the_person.change_happiness(-5)
                    "She looks a little disappointed, but goes back to her work immediately."
    $ renpy.scene("Active")
    return

init 1 python:
    def cat_fight_crisis_requirement():
        #Be at work during work hours with at least two other people who have a poor relationship
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if town_relationships.get_business_relationships(["Rival","Nemesis"]): #If we have at least one Rival or Nemesis relationship in the company this event can trigger.

                #if len(mc.business.get_requirement_employee_list(obedience_max = 130)) >= 2: #We have at least two people around with low obedience. Old, now relaced by

                    return True
        return False

    cat_fight_crisis = Action("Cat Fight Crisis",cat_fight_crisis_requirement,"cat_fight_crisis_label")
    crisis_list.append([cat_fight_crisis,3])

label cat_fight_crisis_label():
    #Two girls have an argument. Side with one over the other or neither (for about break even cost). At higher sluttiness have them kiss and make up.
    if not cat_fight_crisis_requirement(): #If something has changed since we added this crisis as a valid one just return. Should not happen often.
        return

    $ the_relationship = get_random_from_list(own_relationships.get_business_relationships(["Rival","Nemesis"])) #Get a random rival or nemesis relationship within the company
    if the_relationship is None:
        return #Just in case something goes wrong getting a relationship we'll exit gracefully.
    if renpy.random.randint(0,1) == 1: #Randomize the order so that repeated events with the same people alternate who is person_one and two.
        $ person_one = the_relationship.person_a
        $ person_two = the_relationship.perosn_b
    else:
        $ person_one = the_relationship.person_b
        $ person_two = the_relationship.perosn_a


    person_one.char "Excuse me, [person_one.mc_title]?"
    $ person_one.draw_person(emotion = "angry")
    "You feel a tap on your back while you're working. [person_one.title] and [person_two.title] are glaring at each other while they wait to get your attention."
    person_one.char "I was just in the break room and saw [person_two.title] digging around in the fridge looking for other people's lunches."
    $ person_two.draw_person(emotion = "angry") #TODO: Build in better support for multi character drawing.
    person_two.char "That's a lie and you know it! I was looking for my own lunch and you're just trying to get me in trouble!"
    "[person_two.title] looks at you and pleads."
    person_two.char "You have to believe me, [person_one.title] is making all of this up! That's just the kind of thing she would do, too."
    if person_two.sluttiness > 50:
        $ person_one.draw_person(emotion = "angry")
        person_one.char "Jesus, why don't you just suck his cock and get it over with. That's how you normally convince people, right?"
    else:
        $ person_one.draw_person(emotion = "angry")
        person_one.char "Oh boo hoo, you got caught and now you're going to get in trouble. Jesus, is this what you're always like?"
    "[person_two.title] spins to glare at [person_one.title]."
    $ person_two.draw_person(emotion = "angry")
    if person_one.sluttiness > 50:
        person_two.char "At least I'm not slave to some guys dick like you are. You're such a worthless slut."
    else:
        person_two.char "Oh fuck you. You're just a stuck up bitch, you know that?"

    menu:
        "Side with [person_one.title].":
            #Obedience and happiness boost to p1, reduction for p2
            call cat_fight_pick_winner(person_one,person_two) from _call_cat_fight_pick_winner


        "Side with [person_two.title].":
            #Obedience and happiness boost to p2, reductio n for p1
            call cat_fight_pick_winner(person_two,person_one) from _call_cat_fight_pick_winner_1


        "Stop the argument, side with no one.":
            #Obedience boost to both, happinss drop to both. At high sluttiness have them "kiss and make up"
            mc.name "Enough! I can't be the arbitrator for every single conflict we have in this office. You two are going to have to figure this out between yourselves."
            $ person_one.draw_person(emotion = "sad")
            person_one.char "But sir..."
            if person_one.sluttiness > 50 and person_two.sluttiness > 50:
                mc.name "I said nough. Clearly you need help sorting this out."
                "You stand up and take [person_one.title]'s hand in your right hand, then take [person_two.title]'s hand in your left."
                mc.name "The two of you are part of a larger team. I need you to work together."
                "You bring the girls hands together and wrap yours around both of theirs."
                person_one.char "Sorry sir, you're right."
                $ person_two.draw_person(emotion = "sad")
                person_two.char "You're right, I'm sorry sir. And I'm sorry [person_one.title]."
                "You bring your hands back, leaving [person_one.title] and [person_two.title] holding hands. They look away from each other sheepishly."
                mc.name "Good to hear. Now kiss and make up, then you can get back to work."
                "The girls glance at you, then at each other. After a moment of hesitation [person_two.title] leans forward and kisses [person_one.title] on the lips."
                "You watch for a moment as your two employees kiss next to your desk. What starts out as a gentle peck turns into a deep, heavy kiss."
                $ person_two.draw_person()
                "[person_one.title] breaks the kiss and steps back, blushing and panting softly."
                $ person_one.change_obedience(5)
                $ slut_report = person_one.change_slut_temp(10)
                person_one.name "I should... I should get back to work. Sorry for causing any trouble."
                $ person_two.draw_person(position = "walking_away")
                "[person_two.title] watches [person_one.title] leave, eyes lingering on her ass as she walks away."
                mc.name "Go on, you should get back to work too."
                $ person_one.draw_person()
                $ person_two.change_obedience(5)
                $ slut_report = person_two.change_slut_temp(10)
                "You give [person_two.title] a light slap on the butt to pull her attention back to you. She nods quickly and heads the other way."
                $ town_relationships.improve_relationship(person_one, person_two)
                $ renpy.scene("Active")

            else:
                mc.name "I said enough. Now do you need my help talking this out?"
                $ person_one.change_happiness(-5)
                $ person_one.change_obedience(+5)
                person_one.char "No sir, I think we will be alright."
                $ person_two.draw_person(emotion = "sad")
                $ person_two.change_happiness(-5)
                $ person_two.change_obedience(+5)
                person_two.char "Understood sir, there won't be any more problems."
                mc.name "Good to hear. Now get back to work."
                $ renpy.scene("Active")


        "Stay silent and let them fight it out.":
            "Both of the girls look at you, waiting to see who's side you take."
            mc.name "This isn't my fight. You two are going to have to sort this out yourselves."
            $ town_relationships.worsen_relationship(person_one, person_two)
            if renpy.random.randint(0,1) == 0: #Establish a winner and loser for the fight, random here so that the earlieer section of the event doesn't suggest which one it is.
                $ winner = person_one
                $ loser = person_two
            else:
                $ winner = person_two
                $ loser = person_one

            if person_one.sluttiness < 40 or person_two.sluttiness < 40:
                #Catfight starts! Neither is particularly slutty, fight ends once one has their clothing damaged (if they're wearing some clothing, make sure to account for that).
                #Random piece of clothing is lost from a random member of the fight, after which time they run off to get things organised again.
                $ winner.draw_person(emotion = "angry")
                winner.char "Hear that? We're going to have to sort this out, right here. Right now."
                "[winner.title] takes a step towards [loser.title], invading her personal space."
                $ loser.draw_person(emotion = "angry")
                loser.char "What, is that suppose to scare me. Back up."
                "[loser.title] plants a hand on [winner.title]'s chest and shoves her backwards. [winner.title] stumbles a step and bumps into a desk behind her."
                $ winner.draw_person(emotion = "angry")
                winner.char "Oh that's fucking IT! COME HERE BITCH!"
                "[winner.title] throws herself at [loser.title]. Before you can say anything else they're grabbing at each others hair, yelling and screaming as they bounce around the office."
                $ the_clothing = loser.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                if the_clothing:
                    "While they fight [winner.title] gets a hold of [loser.title]'s [the_clothing.name]. She tugs on it hard while she swings [loser.title] around and there's a loud rip."
                    $ loser.draw_animated_removal(the_clothing, emotion = "angry")
                    loser.char "Ugh, look what you've done! Give that back!"
                    "[winner.title] throws the torn garment to [loser.title] and smiles in victory."
                    $ winner.draw_person(emotion = "happy")
                    winner.char "I hope that teaches you a lesson."
                    $ loser.draw_person(emotion = "sad")
                    $ loser.change_obedience(-5)
                    $ loser.change_happiness(-5)
                    $ slut_report = loser.change_slut_temp(5)
                    loser.char "Fuck you. Bitch."
                    $ loser.draw_person(position = "walking_away")
                    "[loser.title] grabs her [the_clothing.name] and hurries off to find somewhere private."
                    $ winner.draw_person(emotion = "happy")
                    $ winner.change_obedience(-5)
                    $ winner.change_happiness(5)
                    "[winner.title] looks at you, out of breath but obviously a little smug."
                    winner.char "Sorry sir, I won't let her get out of line like that again."
                    "She smooths her hair back and gets back to work. You decide to do the same."
                else:
                    "After a minute of fighting [winner.title] gets her hands on [loser.title]'s hair and yanks on it hard. [loser.title] yells and struggles, but it's clear she's lost."
                    $ loser.draw_person(emotion = "angry")
                    loser.char "Fine! Fine, you win!"
                    $ winner.draw_person(emotion = "happy")
                    "[winner.title] pushes [loser.title] away from her and smiles in victory."
                    winner.char "I hope that teaches you a lesson."
                    $ loser.draw_person(emotion = "sad")
                    $ loser.change_obedience(-5)
                    $ loser.change_happiness(-5)
                    $ slut_report = loser.change_slut_temp(5)
                    loser.char "Fuck you. Bitch."
                    $ loser.draw_person(position = "walking_away")
                    $ loser.draw_person(position = "walking_away")
                    "[loser.title] storms off to find somewhere private to nurse her wounds."
                    $ winner.draw_person(emotion = "happy")
                    $ winner.change_obedience(-5)
                    $ winner.change_happiness(5)
                    "[winner.title] looks at you, out of breath but obviously a little smug."
                    winner.char "Sorry sir, I won't let her get out of line like that again."
                    "She smooths her hair back and gets back to work. You decide to do the same."

            else: #both >= 40
                #Girls start pulling clothing off of eachother on purpose until one is naked enough to be very embarassed, then they give up.
                $ winner.draw_person(emotion = "angry")
                winner.char "Hear that? We're going to have to sort this out, right here. Right now."
                "[winner.title] takes a step towards [loser.title], invading her personal space."
                $ loser.draw_person(emotion = "angry")
                loser.char "What, is that suppose to scare me. Back up."
                "[loser.title] plants a hand on [winner.title]'s chest and shoves her backwards. [winner.title] stumbles a step and bumps into a desk behind her."
                $ winner.draw_person(emotion = "angry")
                winner.char "Oh that's fucking IT! COME HERE BITCH!"
                "[winner.title] throws herself at [loser.title]. Before you can say anything else they're grabbing at each others hair, yelling and screaming as they bounce around the office."
                $ the_clothing = loser.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                while the_clothing and loser.outfit.slut_requirement < 80:
                    $ rand_fight = renpy.random.randint(0,3)
                    if rand_fight == 0:
                        "[winner.title] grabs [loser.title] by the [the_clothing.name] and yanks her around. There's a loud rip and the piece of clothing comes free."
                        $ loser.draw_animated_removal(the_clothing, emotion = "angry")
                        loser.char "You bitch!"
                    elif rand_fight == 1:
                        "[loser.title] circles around [winner.title], then runs forward yelling and screaming. [winner.title] pushes her to the side, then grabs her by the [the_clothing.name] and tries to pull her to the ground."
                        "The girls struggle until [loser.title]'s [the_clothing.name] comes free and they seperate. [winner.title] drops it to the ground."
                        $ loser.draw_animated_removal(the_clothing, emotion = "angry")
                        loser.char "You'll pay for that, slut!"
                    elif rand_fight == 2:
                        "[winner.title] and [loser.title] collide, screaming profanities at each other."
                        "You aren't sure exactly what happens, but when they seperate [winner.title] is holding a piece of fabric that use to be [loser.title]'s [the_clothing.name]."
                        $ loser.draw_animated_removal(the_clothing, emotion = "angry")
                        loser.char "Is that all you've got?"
                    else: #rand_fight == 3
                        "[loser.title] gets an arm around [winner.title]'s waist and pushes her against a desk. The two grapple for a moment, then [winner.title] grabs [loser.title] by the [the_clothing.name] and pulls until the piece of clothing rips off."
                        $ loser.draw_animated_removal(the_clothing, emotion = "angry")
                        loser.char "Fuck, you're going to pay for that!"

                    $ returns_favour = renpy.random.randint(0,2)
                    if returns_favour == 0: #Doesn't actually return the favour, because she's the loser she only does it %66 of the time.
                        $ winner.draw_person(emotion = "angry")
                        "[winner.title] laughs and crouches low."
                        winner.char "Come on! Come and get it, you cocksucking whore!"
                    elif returns_favour == 1:
                        $ winner.draw_person(emotion = "angry")
                        winner.char "Do you think I'm afraid of you? Come on!"
                        $ other_clothing = winner.outfit.remove_random_any(top_layer_first = True, exclude_feet = True)
                        if other_clothing:
                            "[winner.title] rushes forward and grabs at [loser.title]. [loser.title] manages to get the upper hand, grabbing onto [winner.title]'s [other_clothing.name] and whipping her around. With a sharp rip it comes free."
                            $ winner.draw_animated_removal(other_clothing, emotion = "angry")
                            winner.char "Get over here!"

                    elif returns_favour == 2:
                        $ other_clothing = winner.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        $ winner.draw_animated_removal(other_clothing, emotion = "angry")
                        if other_clothing:
                            "[winner.title] screams loudly and tries to grab [loser.title] by the waist. [loser.title] is fast enough to get to the side. She grabs [loser.title]'s [other_clothing.name] and yanks on it hard."
                            "[winner.title] struggles for a moment, then manages to slip free of the garment and steps back. [loser.title] drops it to the ground and they square off again."
                        else:
                            "[winner.title] screams loudly and tries to grab [loser.title] by the waist. [loser.title] is fast enough to get out of the way, and they square off again as the fight continues."

                    $ the_clothing = loser.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)

                $ loser.draw_person(emotion = "sad")
                "[loser.title] looks down at herself. She seems to realise for the first time how little she's wearing now."
                loser.char "Look what you've done! Oh god, I need to... I need to go!"
                if loser.sluttiness > 80 and winner.sluttiness > 80:
                    "[loser.title] turns to hurry away, but [winner.title] swoops in and grabs her from behind."
                    loser.char "Hey!"
                    $ winner.draw_person(emotion = "happy")
                    winner.char "You're not going anywhere, not yet!"
                    "[winner.title] reaches a hand down between [loser.title]'s legs, running her finger over her coworkers pussy."
                    $ loser.change_arousal(5) #The girls arousal gain is the base gain + 10% per the characters skill in that category.
                    $ loser.draw_person()
                    loser.char "Hey... that's not fair! I... ah..."
                    "[loser.title] stops fighting almost immediately, leaning against [winner.title] and breathing heavily. You've got a front row seat as [winner.title] starts to finger [loser.title]."
                    $ loser.change_arousal(15)
                    $ loser.draw_person()
                    loser.char "Oh god... [winner.title], just... Ah!"
                    "[winner.title] isn't going easy on [loser.title]. She shivers and bucks against [winner.title]."
                    $ loser.change_arousal(25)
                    $ loser.draw_person()
                    "[winner.title] speeds up, pumping her fingers in and out of [loser.title]'s exposded cunt. She moans loudly and rolls her hips against [winner.title]'s."
                    $ loser.change_arousal(25)
                    $ winner.draw_person()
                    winner.char "You thought you could get away easy, huh? Well now I'm going to make you cum right here, you dirty little slut!"
                    $ loser.change_arousal(25)
                    $ loser.draw_person()
                    "[loser.title] looks right into your eyes. She doesn't look embarrassed - in fact it looks like she's turned on by you watching her get finger banged right in the middle of the office."
                    loser.char "I'm goint to... I'm going to... AH!"
                    $ loser.change_arousal(25)
                    $ loser.draw_person(emotion = "orgasm")
                    winner.char "That's it, cum for me slut!"
                    "[loser.title] screams loudly and shivers wildly. She only stays on her feet because [winner.title] is holding her in place."
                    $ loser.change_slut_core(10)
                    $ slut_report = loser.change_slut_temp (25)
                    $ loser.change_happiness(10)
                    $ loser.change_obedience(-5)
                    "[winner.title] holds [loser.title] up a little longer, then lets her go. [loser.title] stumbles forward on wobbly legs until she finds a chair to collapse into. She pants loudly."
                    $ winner.draw_person(emotion = "happy")
                    $ winner.change_slut_core(5)
                    $ slut_report = winner.change_slut_temp(15)
                    $ winner.change_obedience(-5)
                    winner.char "There we go, that should have sorted her out. I'm sorry about that sir."
                    mc.name "You did what you had to, I understand."
                    "[winner.title] smiles proudly and walks off. It takes a few more minutes before [loser.title] is any state to go anywhere. When she's able to she gathers her things and head off to get cleaned up."

                else:
                    $ slut_report = loser.change_slut_temp(10)
                    $ loser.change_obedience(-10)
                    $ loser.change_happiness(-10)
                    $ loser.draw_person(position = "walking_away")
                    "[loser.title] gathers up what clothes she can from the ground, then hurries away to find somewhere private."
                    $ winner.draw_person(emotion = "happy")
                    "[winner.title] watches [loser.title] leave, panting heavily."
                    $ slut_report = loser.change_slut_temp(5)
                    $ winner.change_obedience(-10)
                    $ winner.change_happiness(10)
                    winner.char "Hah... I knew I had that..."
                    "[winner.title] takes a look down at herself."
                    winner.char "I should probably go get cleaned up too. Sorry about all of this sir."
                    "[winner.title] leaves and you get back to work."


    $ renpy.scene("Active")
    return

label cat_fight_pick_winner(winner, loser):
    $ loser.draw_person(emotion = "angry")
    $ loser.change_happiness(-5)
    $ loser.change_obedience(-5)
    mc.name "Enough! [loser.title], I don't want to hear anything about this from you again. Consider this a formal warning."
    loser.char "Wait, but I..."
    mc.name "That's the end of it, now I want both of you to get back to work. Thank you for bringing this to my attention [winner.title]."
    $ winner.draw_person(emotion = "happy")
    $ winner.change_happiness(5)
    $ winner.change_obedience(5)
    winner.char "My pleasure sir, just trying to keep things orderly around here."
    "[winner.title] shoots a smug look at [loser.title] then turns around and walks away. [loser.title] shakes her head and storms off in the other direction."
    $ renpy.scene("Active")
    return

init 1 python:
    def research_reminder_crisis_requirement():
        if anyone_else_in_office() and not mc.business.head_researcher is None:
            if mc.business.active_research_design is None:
                for trait in list_of_traits:
                    if not trait.researched:
                        return True
        return False


    research_reminder_crisis = Action("Research Reminder Crisis", research_reminder_crisis_requirement,"research_reminder_crisis_label")
    crisis_list.append([research_reminder_crisis,20])

label research_reminder_crisis_label():
    if not research_reminder_crisis_requirement(): #something strange happened to make this no longer a valid crisis. Skip it.
        return

    $ the_person = mc.business.head_researcher

    "While you're working you recieve an email from your head researcher [the_person.title]. It reads:"

    $ researched_all_at_level = True
    python:
        for trait in list_of_traits:
            if not trait.researched and trait.tier == mc.business.research_tier:
                researched_all_at_level = False
                break

    if researched_all_at_level:
        the_person.char "[the_person.mc_title], I appreciate all the free time you're giving me here in the lab, but I think my talents would be better used if you put me to work."
        the_person.char "I've followed up on all the immediate research leads we had. I think we should start thinking about some more dramatic options."
        the_person.char "Come to the lab when you have some free time and we can talk about what comes next."
    else: #We have more to research at this level. Let them just keep chugging along.
        the_person.char "[the_person.mc_title], I appreciate all the free time you're giving me here in the lab, but I think my talents would be better used if you put me to work."
        the_person.char "I've got some promising leads, stop by when you have a chance and let me know what you want me to work on."
    return


init 1 python:
    def serum_creation_crisis_requirement():
        return True #Always true, this will always happen right after a serum is created, regardless of the time.

label serum_creation_crisis_label(the_serum): # Called every time a new serum is created, test it on a R&D member.
    if mc.business.head_researcher:
        $ rd_staff = mc.business.head_researcher
    else:
        $ rd_staff = get_random_from_list(mc.business.r_div.people) #Get a random researcher from the R&D department. TODO: Repalce this with the head researcher position.

    if rd_staff is not None and not mc.business.is_weekend():
        if mc.location == mc.business.r_div: # The MC is in the lab, just physically get them.
            $ the_place = mc.business.r_div
            $ the_place.show_background()
            "There's a tap on your shoulder. You turn and see [rd_staff.title], looking obviously excited."
            $ rd_staff.draw_person(emotion="happy")
            rd_staff.title "[rd_staff.mc_title], I'm sorry to bother you but I've had a breakthrough! The first test dose of serum \"[the_serum.name]\" is coming out right now!"
            rd_staff.title "What would you like me to do?"
            menu:
                "Insist on a final test of [the_serum.name].":
                    mc.name "Excellent, show me what you've done."
                    #Fall through to the next section.

                "Finalize the design of [the_serum.name].":
                    mc.name "Thank you for letting me know [rd_staff.title]. Make sure you all of the safety documentation written up and send the design along. I trust you can take care of that."
                    $ rd_staff.change_happiness(5)
                    $ change_amount = 5
                    $ rd_staff.change_obedience(change_amount)
                    rd_staff.title "Of course. If nothing else comes up we will send the design to production. You can have the production line changed over whenever you wish."
                    $renpy.scene("Active")
                    return

        else: # The MC is somewhere else, bring them to the lab for this.
            "Your phone buzzes, grabbing your attention. It's a call from the R&D section of your buisness."
            "As soon as you answer you hear the voice of [rd_staff.title]."
            show screen person_info_ui(rd_staff)
            rd_staff.title "[rd_staff.mc_title], I've had a breakthrough! The first test dose of serum \"[the_serum.name]\" is coming out right now!"
            rd_staff.title "What would you like me to do?"
            menu:
                "Insist on a final test of [the_serum.name].":
                    mc.name "Excellent, I'll be down in a moment to take a look."
                    "You hang up and travel over to the lab. You're greeted by [rd_staff.title] as soon as you're in the door."
                    $ the_place = mc.business.r_div
                    $ the_place.show_background()
                    $ rd_staff.draw_person(emotion="happy")
                    $ rd_staff.call_dialogue("greetings")
                    mc.name "We're set up over here. come this way."
                    #Fall through to the next section.

                "Finalize the design of [the_serum.name].":
                    mc.name "Thank you for letting me know [rd_staff.title]. Make sure all of the safety documentation is written up and send the design along. I trust you can take care of that."
                    $ rd_staff.change_happiness(5)
                    $ change_amount = 5
                    $ rd_staff.change_obedience(change_amount)
                    rd_staff.title "Of course. If nothing else comes up we will send the design to production. You can have the production line changed over whenever you wish."
                    "[rd_staff.title] hangs up."
                    $renpy.scene("Active")
                    return

        ## Test the serum out on someone.
        "[rd_staff.title] brings you to her work bench. A centrifuge is finished a cycle and spinning down."
        $ technobabble = get_random_from_list(technobabble_list)
        rd_staff.title "Perfect, it's just finishing now. I had this flash of inspiration and realised all I needed to do was [technobabble]."
        "[rd_staff.possessive_title] opens the centrifuge lid and takes out a small glass vial. She holds it up to the light and nods approvingly, then hands it to you."
        menu:
            "Give the serum back for final testing.":
                mc.name "It seems like you have everything under control here [rd_staff.title], I'm going to leave that testing your capable hands."
                $ rd_staff.change_happiness(5)
                $ change_amount = 5
                $ rd_staff.change_obedience(change_amount)

                rd_staff.title "I'll do my best sir, thank you!"
                if rd_staff.sluttiness < 10:
                    mc.name "I'm sure you will. Keep up the good work."
                elif rd_staff.sluttiness < 30:
                    "You give [rd_staff.title] a pat on the back."
                    mc.name "I'm sure you will. Keep up the good work."
                elif rd_staff.sluttiness < 80:
                    "You give [rd_staff.title] a quick slap on the ass. She gasps softly in suprise."
                    mc.name "I'm sure you will. Keep up the good work."
                else:
                    "You grab [rd_staff.title]'s ass and squeeze it hard. She gasps in suprise, then moans softly."
                    mc.name "I'm sure you will. Keep up the good work."

                "You leave [rd_staff.title] to to her work in the lab and return to what you were doing."
                $renpy.scene("Active")
                return

            "Test the [the_serum.name] on someone.":
                mc.name "If we are going to be releasing this to the public we need to be should be absolutely sure there are no adverse effects. I'd like to run one final test."
                "You think for a moment about who to in your R&D team to test the serum on."
                call screen employee_overview(white_list = mc.business.research_team, person_select = True)
                $ selected_person = _return
                if not selected_person == rd_staff:
                    mc.name "[rd_staff.title], fetch me [selected_person.name]."
                    $ renpy.scene("Active")
                    "She nods and heads off. Soon after [selected_person.name] is standing in front of you."
                    $ selected_person.draw_person()
                    selected_person.char "You wanted me sir?"
                    $ rd_staff = selected_person

                mc.name "How confident in your work are you [rd_staff.title]? Before we send this along to production I think we should put it through one final test."
                if rd_staff.obedience < 80:
                    $ rd_staff.draw_person(emotion="angry")
                    $ rd_staff.change_happiness(-10)
                    $ rd_staff.change_obedience(-5)
                    rd_staff.char "Really? I'm just suppose to take a completely untested drug because it might make you more money? That's fucking ridiculous and we both know it."
                    "[rd_staff.possessive_title] puts the serum down on the lab bench and crosses her arms."
                    rd_staff.char "Just get out of here and I'll finish the initial testing in a safe enviroment."
                    mc.name "Fine, just make sure you get it done."
                    rd_staff.char "That's what I'm paid for, isn't it?"
                    "You leave [rd_staff.title] to her to work in the lab and return to what you were doing."
                    $renpy.scene("Active")
                    return

                elif rd_staff.obedience < 120:
                    "[rd_staff.title] pauses for a moment before responding."
                    rd_staff.char "That's a big risk you know. If I'm going to do something like that, I think I deserve a raise."
                    $ raise_amount = int(rd_staff.salary*0.1)
                    menu:
                        "Give [rd_staff.title] a 10%% raise. (+$[raise_amount]/day)":
                            $ mc.log_event("[rd_staff.title]: +$[raise_amount]/day Salary", "float_text_green")
                            mc.name "Alright, you've got yourself a deal. I'll have the books updated by the end of the day."
                            $ rd_staff.salary += raise_amount
                            rd_staff.char "Good to hear it. Let's get right to it then."
                            $ rd_staff.give_serum(copy.copy(the_serum))

                        "Refuse.":
                            mc.name "I'm sorry but that just isn't in the budget right now."
                            rd_staff.char "Fine, then I'll just have to put this new design through the normal safety tests. I'll have the results for you as soon as possible."
                            mc.name "Fine, just make sure you get it done."
                            "[rd_staff.possessive_title] nods. You leave her to work in the lab and return to what you were doing."
                            $renpy.scene("Active")
                            return

                else:
                    "[rd_staff.title] pauses for a moment, then nods."
                    rd_staff.char "Okay sir, if you think it will help the business."
                    $ rd_staff.give_serum(copy.copy(the_serum))


        "[rd_staff.title] drinks down the contents of the vial and places it to the side."
        rd_staff.char "Okay, I guess we just wait to see if there are any effects..."
        "You spend time a few minutes with [rd_staff.possessive_title] to make sure there are no acute effects. The time passes uneventfully."
        rd_staff.char "From a safety perspective everything seems fine. I don't see any problem sending this design to production."
        mc.name "Thank you for the help [rd_staff.title]."
        "You leave her to get back to her work and return to what you were doing."
        $ change_amount = 5
        $ rd_staff.change_obedience(change_amount)
        $renpy.scene("Active")
        return

    else: #There's nobody else in the lab, guess you've done all the hard work yourself!
        "You finish work on your new serum design, dubbing it \"[the_serum.name]\". The lab is empty, so you celebrate by yourself."
        return
    return #We should always have returned by this point anyways, but just in case we'll catch it here.



init 1 python:
    def daughter_work_crisis_requirement():
        # Requres you to have an employee over a certain age, with at least one kid, who hasn't been introduced to the game yet.
        # Requires you and her to be at work.
        # Requries you to have a free slot in the company
        if mc.business.is_open_for_business() and mc.is_at_work() and mc.business.get_employee_count() < mc.business.max_employee_count:
            for person in mc.business.get_employee_list():
                if person.kids != 0 and person.age >= 34 and person.kids > town_relationships.get_existing_child_count(person): #At least one person fits the criteria we need to select a mother, the crisis is valid.
                    return True
        return False

        daughter_work_crisis = Action("Daughter Work Crisis", daughter_work_crisis_requirement,"daughter_work_crisis_label")
        crisis_list.append([daughter_work_crisis,2])


label daughter_work_crisis_label():
    if mc.business.get_employee_count() >= mc.business.max_employee_count:
        return #The business is full due to some other crisis triggering this time chunk.

    python:
        valid_people_list = []
        for person in mc.business.get_employee_list():
            if person.kids != 0 and person.age >= 34 and person.kids > town_relationships.get_existing_child_count(person): #They have undiscovered kids we can add in.
                valid_people_list.append(person)

    $ the_person = get_random_from_list(valid_people_list) #Pick someone appropriate from the company.
    if the_person is None:
        return #We couldn't find anyone to be a parent, so the event fails.


    $ the_daughter = the_person.generate_daughter() #Produces a person who has a high chance to share characteristics with her mother.


    $ the_person.draw_person()
    the_person.char "[the_person.mc_title], could I talk to you for a moment in your office?"
    mc.name "Of course. What's up?"
    "You and [the_person.possessive_title] step into your office. You sit down at your desk while she closes the door."
    $ reason = renpy.random.randint(0,2)
    if reason == 0: #TODO: Make this based on her stats?
        the_person.char "I wanted to ask you... My daughter is living at home and I think it's time she got a job."
        the_person.char "I promise she would be a very hard worker, and I'd keep a close eye on her."

    elif reason == 1:
        the_person.char "This is embarrassing to ask, but... my daughter was let go from her job last week."
        the_person.char "It would mean the world to me if you would look at this and at least consider it."

    else: # reason == 2
        the_person.char "I wanted to ask you... Well, my daughter just finished school and has been looking for a job." #TOOD: Add other excuses, like 'needs to pay rent somehow' or 'can't keep out of trouble.'
        the_person.char "I was thinking that she might be a good fit for the company. I can tell you she's very smart."
    $ promised_sex = False
    if the_person.sluttiness > 70:
        "[the_person.title] hands over a printed out resume and leans forward onto your desk, bringing her breasts closer to you."
        the_person.char "If you did hire her, I would be so very thankful. I'm sure we could find some way for me to show you how thankful."
        $ promised_sex = True

    else:
        "[the_person.title] hands over a printed out resume waits nervously for you to look it over."

    menu:
        "Look at the resume for [the_person.name]'s daughter.":
            pass

        "Tell her you aren't hiring.":
            "You hand the resume back."
            mc.name "I'm sorry, but I'm not looking to hire anyone right now."
            if the_person.sluttiness > 50 and not promised_sex:
                the_person.char "Wait, please [the_person.mc_title], at least take a look. Maybe I could... convince you to consider her?"
                the_person.char "She means the world to me, and I would do anything to give her a better chance. Anything at all."
                "She puts her arms behind her back and puffs out her chest in a clear attempt to show off her tits."
                menu:
                    "Look at the resume for [the_person.name]'s daughter.":
                        "Convinced, you start to read through the resume."
                        $ promised_sex = True

                    "Tell her you aren't hiring.":
                        if the_person.love < 10:
                            mc.name "If I want to fuck you I wouldn't need to hire your daughter to do it. Give it up, you look desparate"
                            $ the_person.change_obedience(3)
                            "She steps back and looks away."
                            the_person.char "Uh, right. Sorry for taking up your time."
                            "[the_person.possessive_title] hurries out of your office."
                        else:
                            mc.name "I'm not hiring right now, and that's final. Now I'm sure you have work to do."
                            $ the_prson.change_obedience(1)
                            "She takes the resume back and steps away from your desk, defeated."
                            the_person.char "Right, of course. Sorry for wasting up your time."
                        $ renpy.scene("Active")
                        return
            elif promised_sex:
                the_person.char "There's nothing I could do? Nothing at all?"
                "She moves to run a hand down your shirt, but you shove the resume back into her hand."
                if the_person.love < 10:
                    mc.name "If I want to fuck you I wouldn't need to hire your daughter to do it. Give it up, you look desparate"
                    $ the_person.change_obedience(3)
                    "She steps back and looks away."
                    the_person.char "Uh, right. Sorry for taking up your time."
                    "[the_person.possessive_title] hurries out of your office."
                else:
                    mc.name "I'm not hiring right now, and that's final. Now I'm sure you have work to do."
                    $ the_prson.change_obedience(1)
                    "She takes the resume back and steps away from your desk, defeated."
                    the_person.char "Right, of course. Sorry for wasting up your time."
                $ renpy.scene("Active")
                return

            else:
                $ the_person.draw_person(emotion = "sad")
                $ the_person.change_happiness(-3)
                the_person.char "I understand. Sorry for taking up your time."
                "She collects the resume and leaves your office."
                $ renpy.scene("Active")
                return

    call screen interview_ui([the_daugther]) #Hire her or reject her.

    if _return == the_daughter: #You've chosen to hire her.
        if promised_sex:
            mc.name "Alright, I'll admit this looks promising, but I need some convincing."
            the_person.char "Of course, [the_person.mc_title]."
            "She steps around your desk and comes closer to you."
            $ the_person.add_situational_obedience("bribe", 30, "It's for my daughter and her future!")
            call fuck_person(the_person) from _call_fuck_person_27
            $ the_person.draw_person()
            $ the_person.reset_arousal()
            $ mc.current_stamina += -1
            $ the_person.clear_situational_obedience("bribe")
            $ the_person.change_obedience(2)
            $ the_person.review_outfit()
            the_person.char "Are we all done then?"
            mc.name "For now. You can call your daughter and give her the good news. I won't give her any preferential treatment from here on out though."
            the_person.char "Of course. Thank you."
            call hire_someone(the_daughter) from _call_hire_someone_1
        else:
            mc.name "Alright [the_person.title], this looks promising. I can't give her any preferential treatment, but I'll give her a try."
            $ the_person.change_happiness(5)
            $ the_person.change_love(2)
            the_person.char "Thank you so much!"
            call hire_someone(the_daughter) from _call_hire_someone_2
    else: #is "None
        if promised_sex: #You promised to do it for sex but don't want to hire her, mom is dissapointed.
            mc.name "I'm sorry but her credentials just aren't what they need to be. I could never justify hiring your daughter."
            $ the_person.change_happiness(-5)
            $ the_person.change_love(-1)
            $ the_person.draw_person(emotion = "sad")
            "[the_person.possessive_title] seems to deflate. She nods sadly."
            the_person.char "I understand. Thank you for the time."


        else:
            mc.name "I'm sorry but I don't think her skills are where I would need them to be."
            $ the_person.change_obedience(1)
            the_person.char "I understand, thank you for at least taking a look for me."

    $ renpy.scene("Active")
    return




    #TODO: Work crisis where you get horny and have to "resolve" it somehow.

#################
## HOME CRISES ##
#################

init 1 python:
    def mom_outfit_help_requirement():
        if mc_at_home() and time_of_day==4 and (day%7==6 or day%7==0 or day%7==1 or day%7==2 or day%7==3): #It has to be a day before a weekday, so she has work in the morning.
            return True
        return False

    mom_outfit_help_crisis = Action("Mom Outfit Help Crisis ",mom_outfit_help_requirement,"mom_outfit_help_crisis_label")
    crisis_list.append([mom_outfit_help_crisis,5])

label mom_outfit_help_crisis_label():
    $ the_person = mom
    # Your mom asks for help planning an outfit for the next day. As a bonus you get to watch her strip down between outfits (peek/don't peek decision given, she doesn't care at high sluttiness)
    if not mom in mc.location.people:
        #She's in a different room, shh calls you in.
        the_person.char "[the_person.mc_title], can you help me with something for a moment?"
        "You hear [the_person.possessive_title] call for you from her bedroom."
        menu:
            "Help [the_person.possessive_title].":
                mc.name "Sure thing, I'll be right there."
                $ mom_bedroom.show_background()
                $ the_person.draw_person()
                "You step into [the_person.possessive_title]. She's standing at the foot of her bed and laying out a few sets of clothing."
                mc.name "Hey Mom, what's up?"

            "Say you're busy.":
                mc.name "Sorry [the_person.title], I'm a little busy at the moment."
                the_person.char "Okay, I'll ask your sister."
                $ renpy.scene("Active")
                return
    else:
        #She's in the room with you right now (how? no clue, but maybe it'll happen one day!)
        $ the_person.draw_person()
        the_person.char "[the_person.mc_title], could you help me with something for a moment?"
        menu:
            "Help [the_person.possessive_title].":
                mc.name "Sure thing, what's up?"
                "[the_person.possessive_title] goes over to her closet and pulls out a few sets of clothing. She starts to lay them out."

            "Say you're busy.":
                mc.name "Sorry Mom, I should really be getting to bed."
                the_person.char "That's okay [the_person.mc_title], I'll ask your sister then."
                $ renpy.scene("Active")
                return

    the_person.char "I've got a meeting with an important client tomorrow and I don't know what I should wear."
    the_person.char "Could you give me your opinion?"
    mc.name "Of course, lets take a look!"
    $ first_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness) # A normal outfit for her, made from her wardrobe.
    $ second_outfit = None # Changes her goals based on how you respond to the first one (ie. she tones it down, makes it sluttier, or keeps it the way it is)
    $ third_outfit = None # She asks you to put something together from her wardrobe. If it's reasonable for her she'll add it to her wardrobe.
    $ caught = False #Did you get cuaght watching her strip

    if the_person.sluttiness + the_person.love < 35: #She really doesn't want you to see anything
        the_person.char "Okay, I'll need a moment to get changed."
        mc.name "I can just turn around, if that would be faster."
        the_person.char "I'll just be a second. Go on, out."
        $ renpy.scene("Active")
        "[the_person.possessive_title] shoos you out of her bedroom. You lean against her door and wait."
        the_person.char "Okay, all done. Come on in!"

    elif the_person.sluttiness + the_person.love < 60: #She just asks you to turn your back, so you can peek if you want.
        the_person.char "Okay, I'll need a moment to get changed. Could you just turn around for a second?"
        $ renpy.scene("Active")
        "You nod and turn your back to [the_person.possessive_title]. You hear her moving behind you as she starts to get undressed."
        menu:
            "Try and peek.":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."

                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice is not None and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person.char "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_happiness(-5)
                        $ the_person.change_slut_temp(1+the_person.get_opinion_score("not wearing anything"))
                        the_person.char "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person.char "Could you wait outside, please?"
                        $ renpy.scene("Active")
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person.char "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching.":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking.":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ renpy.scene("Active")
                                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person.char "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done.":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person.char "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person.char "Just give me one second to get dressed [the_person.mc_title]."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        while strip_choice is not None:
            $ the_person.draw_animated_removal(strip_choice)
            "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        "Once she's stripped naked she grabs her new outfit and starts to put it on."

    $ the_person.outfit = first_outfit
    $ the_person.draw_person()
    the_person.char "Well, what do you think?"
    "You take a moment to think before responding."
    menu:
        "Say it's too revealing.":
            mc.name "I don't think it's very appropriate for work Mom. Maybe you should try something a little less... revealing."
            $ the_person.change_slut_temp(-2)
            the_person.char "Maybe you're right. Okay, I'll try something a little more conservative for this next outfit."
            $ second_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness-10, 0) #Note that if we have impossible values for this function it'll keep exanding the threshold until it's possible

        "Say she looks beautiful in it.":
            mc.name "You look beautiful Mom, I think it would be perfect."
            $ the_person.change_happiness(5)
            $ the_person.change_love(1)
            "She smiles and blushes."
            the_person.char "You aren't just saying that, are you? I want your real opinion"
            mc.name "It's a great look for you."
            the_person.char "Great! I want to try another outfit before I settle on this one though, if you don't mind."
            $ second_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness, 0)

        "Say it's not revealing enough.":
            mc.name "I don't know Mom, it's a little stuffy, isn't it? Maybe you should pick something that's a little more modern and fun."
            $ the_person.change_slut_temp(1+the_person.get_opinion_score("skimpy uniforms"))
            $ the_person.discover_opinion("skimpy uniforms")
            if the_person.get_opinion_score("skimpy uniforms") >= 0:
                the_person.char "Do you think so? Maybe it is a little too conservative."
                "She nods and turns towards her closet."
                the_person.char "Okay, I'll give something else a try then."
            else:
                the_person.char "Oh no, I hate having to dress in those skimpy little outfits everyone wants their secretary in these days."
                "She sighs and shrugs."
                the_person.char "Well, if that's what you think I'll give something else a try."
            $ second_outfit = the_person.wardrobe.decide_on_outfit(the_person.sluttiness+10, 10)


    #Strip choices for the second peek section
    if the_person.sluttiness + the_person.love < 35 or caught: #She really doesn't want you to see anything
        the_person.char "Okay, I just need to get changed again."
        $ renpy.scene("Active")
        "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
        the_person.char "Okay, come in!"

    elif the_person.sluttiness  + the_person.love < 60: #She just asks you to turn your back, so you can peek if you want.
        the_person.char "I'm going to need to get changed again."
        $ renpy.scene("Active")
        "You turn around to give her some privacy."
        menu:
            "Try and peek.":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                $ caught = False
                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice is not None and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person.char "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_happiness(-5)
                        $ the_person.change_slut_temp(1+the_person.get_opinion_score("not wearing anything"))
                        the_person.char "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person.char "Could you wait outside, please?"
                        $ renpy.scene("Active")
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person.char "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching.":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking.":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ renpy.scene("Active")
                                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person.char "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done.":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person.char "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person.char "It'll just take me a second to get changed."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        while strip_choice is not None:
            $ the_person.draw_animated_removal(strip_choice)
            "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
        "Once she's stripped naked she grabs another outfit and starts to put it on."

    $ the_person.outfit = second_outfit
    $ the_person.draw_person()

    the_person.char "Alright, there we go! Now, do you think this is better or worse than what I was just wearing?"
    $ the_person.draw_person(position = "back_peek")
    "She gives you a few turns, letting you get a look at the full outfit."
    $ the_person.draw_person()
    menu:
        "Suggest the first outfit.":
            mc.name "I think you looked best in the first outfit, you should wear that."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            the_person.char "I think you're right, I'll put it away for tomorrow."

        "Suggest the second outfit.":
            mc.name "I think this one suits you better, you should wear it tomorrow."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            the_person.char "I think you're right, it does look good on me."

        "Suggest your own outfit.":
            mc.name "They both look good, but I think I have another idea for something you could wear..."
            "You go to [the_person.possessive_title]'s closet and start to put together an outfit of your own for her."
            $ renpy.scene("Active")
            call screen outfit_select_manager(slut_limit = the_person.sluttiness + 10)
            $ third_outfit = _return
            $ the_person.draw_person()

            if third_outfit == "No Return":
                "You try a few different combinations, but you can't come up with anything you think Mom will like."
                mc.name "Sorry Mom, I thought I had an idea but I guess I was wrong."
                the_person.char "That's fine [the_person.mc_title]. I think I'm going to go with the first one anyway."
                $ the_person.change_happiness(5)
            else:
                "You lay the outfit out for [the_person.possessive_title]. She looks it over and nods."
                the_person.char "I'll try it on, but I think I like it!"

                if the_person.sluttiness + the_person.love < 35 or caught: #She really doesn't want you to see anything
                    $ renpy.scene("Active")
                    "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
                    the_person.char "Okay, come back!"

                elif the_person.sluttiness + the_person.love < 60: #She just asks you to turn your back, so you can peek if you want.
                    the_person.char "I'm just going to get changed one last time, if you could turn around for a second."
                    $ renpy.scene("Active")
                    "You turn around to give her some privacy."
                    menu:
                        "Try and peek.":
                            # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                            $ the_person.draw_person()
                            "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                            $ caught = False
                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                            while strip_choice is not None and not caught:
                                $ the_person.draw_animated_removal(strip_choice)
                                "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
                                if renpy.random.randint(0,100) < 10: #you got caught
                                    the_person.char "I'll be done in just a second [the_person.mc_title]..."
                                    "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                                    $ the_person.draw_person(emotion = "angry")
                                    $ the_person.change_happiness(-5)
                                    $ the_person.change_slut_temp(1+the_person.get_opinion_score("not wearing anything"))
                                    the_person.char "[the_person.mc_title], are you watching me change!"
                                    mc.name "No, I... The mirror was just sort of there."
                                    "She covers herself with her hands and motions for the door."
                                    the_person.char "Could you wait outside, please?"
                                    $ renpy.scene("Active")
                                    "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                                    the_person.char "Okay, you can come back in."
                                    $ caught = True
                                else:
                                    menu:
                                        "Keep watching.":
                                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                                        "Stop peeking.":
                                            "You pull your eyes away from the mirror and do your best not to peek."
                                            $ renpy.scene("Active")
                                            $ strip_choice = None

                            if not caught:
                                "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                                the_person.char "Okay [the_person.mc_title], you can look."

                        "Wait until she's done.":
                            "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                            the_person.char "Okay, all done. You can look."

                else: #She's slutty enough that she doesn't care if you watch or not.
                    the_person.char "It'll just take a moment for me to slip into this."
                    "[the_person.possessive_title] starts to strip down in front of you."
                    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                    while strip_choice is not None:
                        $ the_person.draw_animated_removal(strip_choice)
                        "You watch as [the_person.possessive_title] take off her [strip_choice.name]."
                        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                    "Once she's stripped naked she grabs another outfit and starts to put it on."

                $ the_person.outfit = third_outfit
                $ the_person.draw_person()
                $ the_person.change_happiness(5)
                $ the_person.change_obedience(5)
                $ the_person.change_love(1)
                the_person.char "I think you have great fashion sense [the_person.mc_title]! It's settled, I'll wear this tomorrow!"
                $ the_person.add_outfit(third_outfit,"full")

    the_person.char "Thank you so much for the help [the_person.mc_title]. I don't know why but I've been feeling much more unsure about the way I dress lately."
    mc.name "Any time, I'm just glad to help."
    "You leave [the_person.possessive_title] in her room as she starts to pack her clothes away."

    $ renpy.scene("Active")
    return

init 1 python:
    def mom_lingerie_surprise_requirement():
        if mc_at_home() and time_of_day==4 and not mc.location.has_person(mom): #Make sure we aren't already in the same room because we were sleeping together.
            if mom.sluttiness > 40 and mom.love > 40:
                return True
        return False

    mom_lingerie_surprise_crisis = Action("Mom Lingerie Surprise Crisis", mom_lingerie_surprise_requirement, "mom_lingerie_surprise_label")
    crisis_list.append([mom_lingerie_surprise_crisis,3])

label mom_lingerie_surprise_label():
    #In which your Mom comes to your room at night in some sexy lingerie and fools around with you. Triggers at high sluttiness and love.
    $ the_person = mom
    "You are woken up in the middle of the night by the sound of your bedroom door closing."
    "You sit up and turn on the lamp beside your bed."
    $ the_person.outfit = lingerie_wardrobe.pick_random_outfit()
    $ the_person.draw_person(position = "stand4")
    the_person.char "I'm sorry to wake you up [the_person.mc_title], but I wanted to ask you something."
    "[the_person.possessive_title] is standing by the door, wearing some very revealing lingerie. She walks over to your bed and sits down beside you."
    $ the_person.draw_person(position = "sitting")
    mc.name "What did you want to ask?"
    the_person.char "I know you've been busy with work, and I'm very pround, but sometimes I worry you're not having your needs met."
    "She places a hand on your arm and slides it up to your chest, caressing you with her soft fingers."
    the_person.char "Your physical needs, I mean. I know I'm your mother, but I thought I could dress up and you could pretend I was someone else. Someone not related to you."
    menu:
        "Ask for her help.(tootlip) Ask your mother to help satisfy your phsyical desires." if mc.current_stamina > 0:
            mc.name "That would be amazing Mom, I could really use your help."
            $ the_person.change_slut_temp(2)
            "[the_person.possessive_title] smiles and bounces slightly on your bed."
            if the_person.sluttiness < 60:
                the_person.char "Excellent! Now you just pretend that I'm... your highschool sweetheart, and that we aren't related. Okay?"

            elif the_person.sluttiness < 80:
                the_person.char "Excellent! Don't think of me as your mother, just think of me as a sexy mom from down the street. A real milf, right?"

            else:
                the_person.char "Excellent! Now don't think of me as your mom, just think of me as your private, slutty milf. I'll do wahtever your cock wants me to do, okay?"
            "You nod and she slides closer to you on the bed."

            $ the_person.add_situational_obedience("crisis_stuff", 25, "I'm doing it for my family.")
            call fuck_person(the_person) from _call_fuck_person_14
            if the_person.arousal >= 100:
                "[the_person.possessive_title] needs a few minutes to lie down when you're finished. Bit by bit her breathing slows down."
                $ the_person.change_love(5)
                the_person.char "Oh [the_person.mc_title], that was magical. I've never felt so close to you before..."

            else:
                "When you're finished [the_person.possessive_title] gives you a kiss on your forehead and stands up to leave."
                $ the_person.change_love(3)
                $ the_person.draw_person(position = "back_peek")
                the_person.char "Sweet dreams."

            $ the_person.reset_arousal()
            $ the_person.clear_situational_obedience("crisis_stuff")
            $ mc.current_stamina += -1

        "Ask for her help. \nRequires: Stamina (disabled)" if mc.current_stamina == 0:
            pass

        "Not tonight.":
            mc.name "That's very sweet of you Mom, and you look very nice, but I really just need a good nights sleep."
            "You see a split second of disappointment on [the_person.possessive_title]'s face, then it's gone and she blushes and turns away."
            the_person.char "Of course, I'm so sorry to have bothered you. I mean, it would be strange if we did anything like that, right?"
            $ the_person.draw_person(position = "walking_away")
            "She stands up and leaves your room. You're asleep within minutes."

    $ renpy.scene("Active")
    return

init 1 python:
    def mom_selfie_requirement():
        if not mc_at_home() and not (time_of_day == 0 or time_of_day == 4): #She always sents you text while you're not at home for the middle part of the day
            if not mom in mc.location.people: #Obviously don't do it if she's right there with you.
                if mom.love >= 30:
                    return True
        return False

    mom_selfie_crisis = Action("Mom Selfie Crisis", mom_selfie_requirement, "mom_selfie_label")
    crisis_list.append([mom_selfie_crisis,7])

label mom_selfie_label():
    #TODO: have a way of saving and reviewing selfies in the future.
    #TODO: Have a proper weekday/weekend schedule for people and use that to determine when Mom is at home, at work, or out on the town.
    $ the_person = mom
    $ lowest_stat = mom.sluttiness
    if the_person.love < lowest_stat:
        $ lowest_stat = mom.love

    "While you're going about your day you get a text from your mother."
    if lowest_stat >= 100:
        #Both love and sluttiness are very high, she sends you super slutty selfies and says she can't wait till you come home, fuck her, and make her your woman.
        $ ran_num = renpy.random.randint(0,2) #Used to determine which varient we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            if mc.business.is_weekend():
                $ the_person.outfit = lingerie_wardrobe.pick_random_outfit()
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "Her first message is a selfie of herself lying down on your bed in lingerie."
                the_person.char "I can't wait until you come home and make love to me. I wish I could spend every minute of every day worshiping your cock like a good mother should."
            else:
                the_person.char "It's so hard not to talk about you at work. The other women are gossiping and I just want to tell them how good it feels when you try and breed me..."
                the_person.char "My pussy full of your warm cum, knowing that I can take care of you the way only a mother could."
                the_person.char "I think I'm going to go touch myself in the bathroom. I hope you are having a great day too [the_person.mc_title]!"

        elif ran_num == 1:
            python:
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)
            the_person.char "Hi [the_person.mc_title], I hope I'm not interrupting your busy work day. This is just a quick reminder..."
            $ the_person.draw_person(emotion = "happy")
            "You get a selfie from [the_person.possessive_title] naked in front of her bedroom mirror."
            the_person.char "...that your Mom wants to feel you inside her tonight. Don't stay out too late!"

        elif ran_num == 2:
            #Blowjob pose, she tells you to face fuck her, as is her duty
            pass

    elif lowest_stat >= 80:
        #Both are high. Sends you slutty selfies and talks about how she wants to fuck you. Sends them from work, etc.
        $ ran_num = renpy.random.randint(0,1) #Used to determine which varient we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            if mc.business.is_weekend():
                the_person.char "I'm here at home and wishing it was you could help me take these pictures..."
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.possessive_title] sends you a selfie her bedroom naked and bent over her bed."
            else:
                the_person.char "I'm stuck here at work and all I can think about is you. Wish you were here..."
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.possessive_title] sends you a selfie of herself in the office bathroom, naked and bending over the sink."

        elif ran_num == 1:
            if mc.business.is_weekend():
                the_person.char "I know it shouldn't, but thinking about you gets me so wet. You've made me a new woman [the_person.mc_title]."
            else:
                the_person.char "I'm at work and stuck at my desk but I can't get you out of my head. I'm so wet, I wonder if anyone would notice if I touched myself..."

    elif lowest_stat >= 60:
        #Sends you nudes and talks about how she'll help you blow off steam later.
        $ ran_num = renpy.random.randint(0,3) #Used to determine which varient we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            if mc.business.is_weekend():
                the_person.char "I was just about to get in the shower and I thought you might like a peek. Love you [the_person.mc_title]!"
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        if the_person.outfit.panties_covered(): #If we get down to her panties keep them on, because that's sexier.
                            the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "[the_person.possessive_title] sends you a picture of herself stripped down in front of her bedroom mirror."

            else:
                the_person.char "I thought you might be stressed so I snuck away from work to take this for you."
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        if the_person.outfit.panties_covered():
                            the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "[the_person.possessive_title] sends you a picture of herself stripped down in the office bathroom."
                the_person.char "I've got to get back to work. I hope nobody noticed me gone!"

        elif ran_num == 1:
            the_person.char "I thought you might enjoy this ;)"
            python:
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)
            $ the_person.draw_person(emotion = "happy")
            "Mom sends you a picture of herself stripped naked in front of her bathroom mirror."
        elif ran_num == 2:
            the_person.char "I've been trying on underwear all day. Would you like a peek?"

            "[the_person.possessive_title] doesn't wait for a reply and starts sending selfies."
            python:
                for i in range(3):
                    the_person.outfit = the_person.wardrobe.get_random_appropriate_underwear(the_person.sluttiness, guarantee_output = True)
                    the_person.draw_person(emotion = "happy")
                    renpy.say("","")
            the_person.char "I hope you think your mommy looks sexy in her underwear ;)"
        elif ran_num == 3:
            python:
                while not the_person.outfit.tits_visible():
                    the_person.outfit.remove_random_upper(top_layer_first = True)

            if mc.business.is_weekend():
                the_person.char "I'm so glad it's the weekend, I can finally let these girls out..."
                $ the_person.draw_person(emotion = "happy")
                "She sends you a selfie fron the kitchen with her top off."
                the_person.char "I hope your day is going well, love you!"

            else:
                the_person.char "I think I'd be much more popular here at work if I was allowed to dress like this..."
                $ the_person.draw_person(emotion = "happy")
                "She sends you a selfie from her office bathroom with her top off."
                the_person.char "Oh well, at least I know you appreciate it. I need to get back to work, see you at dinner!"

    elif lowest_stat >= 40:
        #Sends you teasing pictures (ie. no shirt or something) and talks about how much she loves you.
        $ ran_num = renpy.random.randint(0,2) #Used to determine which varient we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            the_person.char "You're such a hard worker [the_person.mc_title]. Here's a little gift from the woman who loves you most in the world!"
            $ the_person.outfit.remove_random_upper(top_layer_first = True)
            $ the_person.draw_person(emotion = "happy")
            if mc.business.is_weekend():
                "[the_person.possessive_title] sends you a selfie without her shirt on. The background looks like her bedroom."
            else:
                "[the_person.possessive_title] sends you a sends you a selfie without her shirt on. It looks like it was taken in the bathroom of her office."

        elif ran_num == 1:
            if mc.business.is_weekend():
                the_person.char "I wish you were here spending time with me. Maybe this will convince you your mom is a cool person to hang out with!"
                $ the_person.outfit.remove_random_upper(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "Mom sends you a selfie from her bedroom without her shirt on."

            else:
                the_person.char "I'm busy here at work but I really wish I could be spending time with you instead. Do you think I'm pretty enough to spend time with ;)"
                $ the_person.outfit.remove_random_upper(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "Mom sends you a selfie without her shirt on. It looks like she's taken in the bathroom of her office."

        elif ran_num == 2:
            $ the_clothing = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
            if the_clothing:
                $ the_clothing.colour[3] = the_clothing.colour[3]*0.9 #It's translucent.
                the_person.char "It looks like my [the_clothing.name] didn't like being in the wash, it's gone all see-through."
                $ the_person.draw_person(emotion = "happy")
                if the_clothing.underwear:
                    "You get a selfie from [the_person.possessive_title] wearing a slightly transparent bra."
                else:
                    "You get a selfie from [the_person.possessive_title] wearing a slightly transparent top."
                the_person.char "Oh well, I can still wear it when I'm doing chores around the house. Hope your day is going better, love you!"
            else:
                the_person.char "I've looked everywhere, but I just can't find my favourite bra!"
                $ the_person.draw_person(emotion = "default")
                "[the_person.possessive_title] sends you a short video of herself walking around your home. Her bare tits bounce with each step."
                the_person.char "You don't happen to know where it is, do you? I'm wandering around looking for it and it's getting chilly!"

    elif lowest_stat >= 20:
        #Sends you normal texts but talks about wanting to get away to talk to you instead
        $ ran_num = renpy.random.randint(0,4) #Used to determine which varient we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            the_person.char "I hope I'm not interrupting, I just wanted to say hi and check in. I'm stuck here at work but wish I could spend more time with you."
            the_person.char "Have a great day, see you later tonight. Love, Mom."

        elif ran_num == 1:
            the_person.char "I hope you are having a great day [the_person.mc_title]! Imagining you out there working so hard makes me prouder than you can imagine!"
            the_person.char "I'm looking forward to seeing you at home tonight. Love, Mom."

        elif ran_num == 2:
            the_person.char "I hope you aren't busy, I was thinking about you and just wanted to say hi!"
            $ the_person.draw_person(emotion = "happy")
            if mc.business.is_weekend():
                "[the_person.possessive_title] sends you a selfie she took in the living room of your house."
            else:
                "[the_person.possessive_title] sends you a selfie she took from her office at work."
        elif ran_num == 3:
            the_person.char "Kids these days are always sending selfies to each other, right? I hope I'm doing this right!"
            $ the_person.draw_person(emotion = "happy")
            if mc.business.is_weekend():
                "[the_person.possessive_title] sends you a selfie she took in the living room of your house."
            else:
                "[the_person.possessive_title] sends you a selfie she took from her office at work."
        elif ran_num == 4:
            the_person.char "All your hard work has inspired me [the_person.mc_title], I'm going out for a walk to stay in shape!"
            $ the_person.draw_person(emotion = "happy")
            "[the_person.possessive_title] sends you a short video she took of herself outside. She's keeping up a brisk walk and seems slightly out of breath."
            if not the_person.outfit.wearing_bra() and the_person.has_large_tits():
                "She doesn't seem to realise it but it's very obvious [the_person.possessive_title] isn't wearing a bra under her shirt. Her sizeable breasts heave up and down with each step."

    else:
        #Sends you normal motherly texts.
        $ ran_num = renpy.random.randint(0,2) #Used to determine which varient we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            the_person.char "I hope I'm not interrupting your busy day [the_person.mc_title]. I just wanted to let you know that I'm proud of you and you're doing great work."
            the_person.char "Keep it up! Dinner will be at the normal time."

        elif ran_num == 1:
            the_person.char "Remember that your mother loves you no matter what! Have a great day!"

        elif ran_num == 2:
            the_person.char "Hi [the_person.mc_title], I'm just checking in to make sure you're doing okay. I hope you don't mind your "

    "It's so sweet of her to think of you."
    $ the_person.outfit = the_person.planned_outfit.get_copy() #Make sure to reset their outfits so they're dressed properly.
    $renpy.scene("Active")
    return

init 1 python:
    def mom_morning_surprise_requirement():
        if mc_at_home() and time_of_day==0 and mc.business.is_work_day(): #It is the end of the day. TODO: Make this trigger as a morning crisis instead.
            if mom.love >= 45:
                return True
        return False

    mom_morning_surprise_crisis = Action("Mom Morning Surprise", mom_morning_surprise_requirement, "mom_morning_surprise_label")
    morning_crisis_list.append([mom_morning_surprise_crisis, 5])

label mom_morning_surprise_label():
    #TODO: Finish all of the side functionalit this event requires to be implemented.
    $ the_person = mom
    if the_person.sluttiness < 50:
        the_person.char "[the_person.mc_title], it's time to wake up."
        "You're woken up by the gentle voice of your mother. You struggle to open your eyes and find her sitting on the edge of your bed."
        $ the_person.draw_person(position="sitting")
        mc.name "Uh... Huh?"
        the_person.char "You're normally up by now, but I didn't hear an alarm and I was worried you were going to be late."
        "You roll over and check your phone. It looks like you forgot to set an alarm and you've overslept."
        mc.name "Thanks Mom, you really saved me here."
        $ the_person.change_happiness(3)
        "She smiles and stands up."
        $ the_person.draw_person()
        the_person.char "There's some breakfast in the kitchen, make sure to grab some before you go flying out the door."
        "You sit up on the side of the bed and stretch, letting out a long yawn."
        if the_person.sluttiness < 20:
            the_person.char "Oh... I should... Uh..."
            "[the_person.possessive_title] blushes and turns around suddenly. It takes you a moment to realise why: your morning wood pitching an impressive tent with your underwear."
            mc.name "Sorry Mom, I didn't..."
            the_person.char "No, it's perfectly natural. I'll give you some privacy."
            $ the_person.change_slut_temp(2)
            "She takes one last glance at you then hurries from the room."
            $ renpy.scene("Active")
            "You get up and ready, hurrying a little to make up for lost time."
        else:
            the_person.char "Oh, and you might want to take care of that before you go out [the_person.mc_title]."
            "She nods towards your crotch and you realise you're pitching an impressive tent."
            mc.name "Oh, sorry about that."
            the_person.char "No, it's perfectly natural and nothing to be embarrassed about."
            $ the_person.change_slut_temp(3)
            "She stares at it for a short moment before pulling her eyes back up to meet yours."
            #TODO: She offers to pick out an outfit for you while you jerk off "To avoid bothering anyone at work".
            the_person.char "Certainly nothing to be embarrassed, but I think you should take care of it before you leave."
            "[the_person.possessive_title] turns around and starts rifling through your closet."
            $ the_person.draw_person(position = "walking_away")
            the_person.char "I'll find you a nice outfit to wear to save you some time. Go ahead [the_person.mc_title], pretend I'm not even here. It's nothing I haven't seen before."
            menu:
                "Masturbate.":
                    "You pull your underwear down, grab your hard cock, and start to stroke it."
                    mc.name "Thanks Mom, you're really helping me out this morning."
                    the_person.char "Anything to help you succeed."
                    $ the_person.draw_person(position = "back_peek")
                    "She wiggles her butt, then turns her attention back to putting together an outfit for you."
                    "You keep jerking yourself off, pulling yourself closer and closer to orgasm."
                    "You're getting close when [the_person.possessive_title] turns around and walks back towards your bed with a handful of clothes."
                    the_person.char "I think you'll look really cute in this. Are you almost done [the_person.mc_title]?"
                    menu:
                        "Order her to get on her knees." if the_person.obedience >= 130:
                            mc.name "I'm so close. Get on your knees Mom."
                            the_person.char "If... if that's what you need to finish."
                            $ the_person.draw_person(position = "blowjob")
                            menu:
                                "Order her to open her mouth." if the_person.obedience >= 140:
                                    mc.name "Open your mouth Mom."
                                    the_person.char "[the_person.mc_title], I don't think..."
                                    mc.name "I'm so close Mom, open your mouth!"
                                    "She hesitates for a split second, then closes her eyes and opens her mouth."
                                    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
                                    "Seeing [the_person.possessive_title] presenting herself for you pushes you past the point of no return."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
                                    "You slide forward a little, place the tip of your cock on her bottom lip, and start to fire your load into her mouth."
                                    "[the_person.possessive_title] stays perfectly still while you cum. When you're done you sit back and sigh."
                                    "[the_person.title] turns away and spits your cum out into her hand. She takes a long while to say anything."
                                    the_person.char "I don't... That wasn't what we should do [the_person.mc_title]."
                                    mc.name "You were just being a loving mother and doing what I asked. That was amazing."
                                    $ the_person.change_obedience(5)
                                    $ the_person.change_slut_temp(5)
                                    "I... I don't know. Just don't tell anyone, okay?"
                                    mc.name "Of course, I promise Mom."
                                    $ the_person.draw_person()
                                    "She stands up and heads for the door."
                                    the_person.char "Well hurry up at least and get dressed, I don't want you to be late after all that!"

                                "Order her to open her mouth.\nRequires: 140 Obedience (disabled)" if the_person.obedience < 140:
                                    pass

                                "Order her to hold up her tits." if the_person.has_large_tits():
                                    mc.name "Hold up your tits, I'm going to cum!"
                                    "[the_person.possessive_title] mumbles something but does as she's told. She cups her large breasts in her hands and presents them in front of you."
                                    "You grunt and climax, firing your load out and right onto [the_person.possessive_title]'s chest."
                                    $ the_person.cum_on_tits()
                                    #TODO: have more clothing aware stuff here
                                    the_person.char "I... Oh [the_person.mc_title], I don't think I should have let you do that."
                                    $ the_person.draw_person()
                                    mc.name "It's okay Mom, you were just being a loving mother and doing what I asked."
                                    $ the_person.change_obedience(3)
                                    $ the_person.change_slut_temp(5)
                                    the_person.char "Maybe you're right... Now hurry up and get dressed before you're late!"
                                    # TODO: She should seem a little shocked, but otherwise okay with how things turned out

                        "Order her to get on her kness.\nRequires: 130 Obedience (disabled)" if the_person.obedience < 130:
                            pass

                        "Climax.":
                            "Knowing that [the_person.possessive_title] is just a step away watching you stroke your cock and waiting for you to cum pushes you over the edge."
                            "You grunt and climax, firing your load out in an arc. [the_person.title] gasps softly and watches it fly, looks away."
                            the_person.char "Well done. I'll make sure to clean that up while you're out today."
                            "She leans over and kisses you on the forehead."
                            the_person.char "Now get dressed or you'll be late for work."
                            $ renpy.scene("Active")
                            "[the_person.possessive_title] leaves and you get dressed as quickly as you can manage."

                "Ask her to leave.":
                    mc.name "I think it will take care of itself Mom. Thanks for hte offer but I can pick out my own outfit."
                    the_person.char "Oh, okay [the_person.mc_title]. Just make sure don't give any of those nice girls you work with a shock when you walk in."
                    $ the_person.draw_person()
                    "She turns back to you and gives you a hug and a kiss. Her eyes continue to linger on your crotch."
                    $ renpy.scene("Active")
                    "When she leaves you get dressed as quickly as you can, rushing to make up for lost time."


    elif the_person.sluttiness < 70:
        "You're slowly awoken by a strange, pleasant sensation. When you open your eyes it takes a moment to realise you aren't still dreaming."
        $ the_person.draw_person(position = "blowjob") #TODO: We need a handjob pose.
        "[the_person.possessive_title] is sitting on the side of your bed. The covers have been pulled down and she has your morning wood in her hand. She strokes it slowly as she speaks."
        the_person.char "Good morning [the_person.mc_title]. You forgot to set an alarm and overslept. I came in to wake you up and saw this..."
        "She speeds up her strokes."
        the_person.char "I thought that this would be a much nicer way to wake up, and I can't let you leave the house in this condition."
        mc.name "Right, of course. Thanks Mom."
        "You lie back, relax, and enjoy the feeling of your mothers hand caressing your hard shaft."
        the_person.char "Anything for you [the_person.mc_title], I just want to make sure you're happy and successful."
        "After a few minutes you can feel your orgasm starting to build. Mom rubs your precum over your shaft and keeps stroking."
        menu:
            "Order her to take your cum in her mouth." if the_person.obedience >= 130:
                mc.name "I'm almost there Mom, I need to cum in your mouth."
                $ the_person.change_obedience(5)
                "She nods and leans over, stroking your cock faster and faster as she places the tip just inside her mouth."
                "The soft touch of her lips pushes you over the edge. You gasp and climax, shooting your hot load into [the_person.possessive_title]'s waiting mouth."
                $ the_person.cum_in_mouth()
                "[the_person.title] pulls back off your cock slowly. She spits your cum out into her hand and straightens up."

            "Order her to take your cum in her mouth.\nRequires: 130 Obedience (disabled)" if the_person.obedience<130:
                pass
            "Climax":
                mc.name "I'm almost there Mom, keep going!"
                "She nods and strokes your dick as fast as she can manage, pusing you over the edge."
                "You grunt and fire your hot load into up into the air. It falls back down onto your stomach and [the_person.possessive_title]'s hand."
                "Mom strokes you slowly for a few seconds, then lets go and places her hand on her lap while you take a second to recover."

        the_person.char "Whew, that was a lot. I hope that leaves you feeling relaxed for the rest of the day."
        "She leans forward and kisses you on the forehead."
        mc.name "Thanks Mom, you're the best."
        $ the_person.change_love(2)
        $ the_person.change_slut_temp(5)
        $ the_person.change_happiness(5)
        $ the_person.draw_person(position = "back_peek")
        "She smiles and gets up. She pauses before she leaves your room."
        the_person.char "You better get ready now or you're going to be late!"


    elif the_person.sluttiness < 90:
        #TODO: image a lying down blowjob pose
        "You're slowly awoken by a strange, pleasant sensation. When you open your eyes it takes a moment to realise you aren't still dreaming."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.possessive_title] is lying face down between your legs, gently sucking off your morning wood."
        "She notices you waking up and pulls off of your cock to speak."
        the_person.char "Good morning [the_person.mc_title]. I noticed your alarm hadn't gone off and came in to wake you up..."
        "She licks your shaft absentmindedly."
        the_person.char "And saw this. I thought this would be a much nicer way of waking you up."
        mc.name "That feels great Mom."
        $ the_person.change_happiness(5)
        "She smiles up at you, then lifts her head and slides your hard dick back into her mouth."
        "You lie back and enjoy the feeling of [the_person.possessive_title] sucking you off."
        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
        "For several minutes the room is quiet save for a soft slurping sound each time [the_person.title] slides herself down your shaft."
        "You rest a hand on the back of her head as you feel your orgasm start to build, encouraging her to go faster and deeper."
        mc.name "I'm almost there Mom, keep going!"
        "She mumbles out an unintelligible response and keeps sucking your cock."
        "You arch your back and grunt as you climax, firing a shot of cum into [the_person.possessive_title]'s mouth."
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "blowjob")
        "She pulls back until the tip of your cock is just inside her lips and holds there, collecting each new spurt of semem until you're completely spent."
        "When you're done she pulls up and off, keeping her lips tight to avoid spilling any onto you."
        menu:
            "Order her to swallow." if the_person.obedience >= 130:
                mc.name "That was great Mom, now I want you to swallow."
                "She looks at you and hesitates for a split second, then you see her throat bob as she sucks down your cum."
                $ the_person.change_obedience(5)
                "[the_person.possessive_title] takes a second gulp to make sure it's all gone, then opens her mouth and takes a deep breath."


            "Order her to swallow.\nRequires: 130 Obedience (disabled)" if the_person.obedience < 130:
                pass

            "Let her spit it out.":
                $ the_person.draw_person(position = "sitting")
                "You watch as she slides her legs off the side of your bed, holds out a hand, and spits your cum out into it."

        the_person.char "Whew, I'm glad I was able to help with that [the_person.mc_title]. That was a lot more than I was expecting."
        mc.name "Thanks Mom, you're the best."
        $ the_person.change_love(2)
        $ the_person.change_slut_temp(5)
        "She smiles and leans over to give you a kiss on the forehead."
        the_person.char "My pleasure, now you should be getting up or you'll be late for work!"
        $renpy.scene("Active")
        "[the_person.possessive_title] gets up and leaves you alone to get dressed and ready for the day. You rush a little to make up for lost time."

    else:
        #TODO: We need a girl_on_top position. Missionary images until then.
        # First we need to take her and remove enough clothing that we can get to her vagina, otherwise none of this stuff makes sense.
        # We do that by getting her lowest level pieces of bottom clothing and removing it, then working our way up until we can use her vagina.
        # This makes sure skirts are kept on (because this is suppose to be a quicky).
        $ bottom_list = the_person.outfit.get_lower_ordered()
        $ removed_something = False
        $ the_index = 0
        while not the_person.outfit.vagina_available and the_index < __builtin__.len(bottom_list):
            $ the_person.outfit.remove(bottom_list[index])
            $ removed_something = True
            $ the_index += 1
        "You're woken up by your bed shifting under you and a sudden weight around your waist."
        $ the_person.draw_person(position = "cowgirl", emotion = "happy")
        "[the_person.possessive_title] has pulled down your sheets and underwear and is straddling you. The tip of your morning wood is brushing against her pussy."
        the_person.char "Good morning [the_person.mc_title]. I didn't hear your alarm go off and when I came to check on you I noticed this..."
        "She grinds her hips back and forth, rubbing your shaft along the lips of her cunt."
        the_person.char "Would you like me to take care of this for you?"
        menu:
            "Let Mom fuck you." if mc.current_stamina > 0:
                mc.name "That would be great Mom."
                $ the_person.change_happiness(5)
                $ the_person.change_love(2)
                "You lie back relax as [the_person.possessive_title] lowers herself down onto your hard cock."
                call fuck_person(the_person, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, girl_in_charge = True) from _call_fuck_person_15
                $ mc.current_stamina += -1
                if the_person.arousal >= 100:
                    $ the_person.change_love(5)
                    the_person.char "That was amazing [the_person.mc_title], you know how to make me feel like women again!"
                    "She rolls over and kisses you, then rests her head on your chest."
                    "After a minute she sighs and starts to get up."
                    the_person.char "I shouldn't be keeping you from your work, I don't want to make you any more late!"
                    "She reaches down to help you up. She smiles at you longingly, eyes lingering on your crotch, and leaves you alone in your room."
                else:
                    the_person.char "I'm glad I could help [the_person.mc_title]. Now you should hurry up before you're late!"
                    "[the_person.possessive_title kisses you on the forehead and stands up to leave."
                    "You get yourself put together and rush to make up for lost time."
                $ the_person.reset_arousal()
                $ the_person.review_outfit()

            "Let Mom fuck you.\nRequires: 1 Stamina (disabled)" if mc.current_stamina <= 0:
                pass

            "Ask her to get off.":
                mc.name "Sorry Mom, but I need to save my energy for later today."
                $ the_person.change_happiness(-3)
                $ the_person.change_obedience(5)
                "She frowns but nods. She swings her leg back over you and stands up."
                $ the_person.draw_person()
                the_person.char "Of course [the_person.mc_title], if you need me for anything just let me know. I hope you aren't running too late!"
                if removed_something:
                    "[the_person.title] collects some of her discarded from your floor and heads for the door."
                else:
                    "[the_person.title] gives you a kiss on the forehead and heads for the door."
                $ renpy.scene("Active")
                "You get up and rush to get ready to make up for lost time."

    $ renpy.scene("Active")
    return

init 1 python:
    def lily_new_underwear_requirement():
        if mc_at_home() and time_of_day==4: #It is the end of the day.
            if lily.sluttiness >= 15 and lily.love >= 0: #She's slutty enough to show you her new underwear, but not so slutty that she thinks underwear is unnesesary.
                return True
        return False
    lily_new_underwear_crisis = Action("Lily New Underwear Crisis", lily_new_underwear_requirement, "lily_new_underwear_crisis_label")
    crisis_list.append([lily_new_underwear_crisis, 5])

label lily_new_underwear_crisis_label():
    # Lily has some new underwear she wants to demo for you.
    # We base the underwear sluttiness on Lily's sluttiness and use Love+Sluttiness to see if she'll show you as a "full outfit".
    $ the_person = lily #Just so we can keep
    $ valid_underwear_options = []
    $ the_underwear = None
    python:
        for underwear in default_wardrobe.get_underwear_sets_list():
            #She picks underwear that is in the top 20 sluttiness of what she considers slutty underwear AND that she would feel comfortable wearing in front of her (hopefully loving) brother.
            if underwear.get_underwear_slut_score() <= the_person.sluttiness and underwear.get_underwear_slut_score() >= the_person.sluttiness-20 and the_person.judge_outfit(underwear, the_person.love+30):
                valid_underwear_options.append(underwear)

        the_underwear = get_random_from_list(valid_underwear_options)
    if the_underwear is None:
        return #Lily doesn't have any skimpy underwear to show us :(

    $ bedroom.show_background()
    $ mc.change_location(bedroom) #Make sure we're in our bedroom.
    if the_person.obedience >= 95:
        "There's a knock at your door."
        the_person.char "[the_person.mc_title], can I talk to you for a sec?"
        mc.name "Uh, sure. Come in."
        "Your bedroom door opens and [the_person.possessive_title] steps in. She's carrying a shopping bag in one hand."
    else:
        "There's a single knock at your bedroom door before it's opened up. [the_person.possessive_title] steps in, carrying a shopping bag in one hand."
    $ the_person.draw_person(emotion = "happy")
    if the_underwear.get_underwear_slut_score() < 10:
        the_person.char "This is a little awkward, but I picked up some new underwear at the mall today but I don't know if I like the way it looks."
        the_person.char "Would you take a look and let me know what you think?"
    elif the_underwear.get_underwear_slut_score() < 20:
        the_person.char "I was at the mall today and picked up some new underwear. I know Mom would say it's too skimpy, but I wanted a guys opinion."
        the_person.char "Would you let me try it on and tell me what you think?"
    else:
        the_person.char "I was at the mall today and picked up some lingerie. I was hoping you'd let me model it for you and tell me what you think."

    menu:
        "Take a look at [the_person.title]'s new underwear.":
            "You sit up from your bed and give [the_person.possessive_title] your full attention."
            mc.name "Sure thing, is it in there?"
            "You nod your head towards the bag she is holding."
            the_person.char "Yeah, I'll go put it on and be back in a second. Don't move!"
            #TODO: Have an option where she puts it on right in front of you."
            $ renpy.scene("Active")
            "[the_person.title] skips out of your room, closing the door behind her."
            $ the_person.outfit = the_underwear.get_copy()
            "You're left waiting for a few minutes. Finally, your door cracks open and [the_person.title] slips inside."
            $ the_person.draw_person(emotion="happy")
            the_person.char "Here we go. What do you think?"
            $ the_person.draw_person(emotion="happy", position = "back_peek")
            "She turns around to give you a good look from behind."
            menu:
                "She looks beautiful.": #Raises love
                    mc.name "You look beautiful [the_person.title]. You're a heartstopper."
                    $ the_person.change_love(2)
                    the_person.char "Aww, you really think so?"

                "She looks sexy.": #Raises sluttiness
                    mc.name "You look damn sexy in it [the_person.title]. Like you're just waiting to pounce someone."
                    $ the_person.change_slut_temp(3)
                    the_person.char "Ooh, I like being sexy. Rawr!"

                "She looks elegant.": #Raises obedience
                    mc.name "It makes you look very elegent, [the_person.title]. Like a proper lady."
                    $ the_person.change_obedience(2)
                    the_person.char "It's not too uptight, is it? Do you think Mom would wear something like this?"

                "You don't like it.": #Raises nothing.
                    mc.name "I'm not sure it's a good look on you [the_person.title]."
                    $ the_person.change_happiness(-2)
                    the_person.char "No? Darn, it was starting to grow on me..."

            "[the_person.title] stands in front of your mirror and poses."
            $ the_person.draw_person(emotion = "happy")
            the_person.char "Do you think I should keep it? I'm on the fence."
            menu:
                "Keep it.":
                    $ the_person.wardrobe.add_underwear_set(the_underwear)
                    mc.name "You should absolutely keep it. It looks fantastic on you."
                    $ the_person.change_happiness(3)
                    "[the_person.title] grins and nods."
                    the_person.char "You're right, of course you're right. Thank you [the_person.mc_title], you're the best!"


                "Return it.":
                    mc.name "I think you have other stuff that looks better."
                    $ the_person.change_obedience(2)
                    the_person.char "I think you're right, I should save my money and get something better. Thank you [the_person.mc_title], you're the best!"

            $ the_person.change_love(3)
            "[the_person.possessive_title] walks over to you and gives you a hug."
            the_person.char "Okay, it's getting cold. I'm going to go put some clothes on!"
            $ renpy.scene("Active")
            "[the_person.title] slips out into the hall, leaving you alone in your room."


        "Send her away.":
            mc.name "Sorry [the_person.title], but I'm busy right now. You'll have to figure out if you like it by yourself."
            the_person.char "Right, no problem. Have a good night!"
            $ renpy.scene("Active")
            "She leaves and closes your door behind her."

    $ renpy.scene("Active")
    return

init 1 python:
    def lily_morning_encounter_requirement():
        if mc_at_home() and time_of_day == 0:
            return True
        return False

    lily_morning_encounter_crisis = Action("Lily Morning Encounter", lily_morning_encounter_requirement, "lily_morning_encounter_label")
    morning_crisis_list.append([lily_morning_encounter_crisis, 5])

label lily_morning_encounter_label():
    # You run into Lily early in the morning as she's going to get some fresh laundry. At low sluttiness she is embarassed, at high she is completely naked.
    $ the_person = lily
    if the_person.sluttiness >= 60:
        $ the_person.outfit = default_wardrobe.get_outfit_with_name("Nude 1") #If sh's very slutty she doesn't mind being naked.
    else:
        $ the_person.outfit = the_person.wardrobe.get_random_appropriate_underwear(the_person.sluttiness, guarantee_output = True) # Otherwise get an underwear set she would wear.

    "You wake up in the morning to your alarm. You get dressed and leave your room to get some breakfast."
    $ the_person.draw_person()
    if the_person.outfit.wearing_panties():
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, completeley naked."
    else:
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing nothing but her underwear."

    if the_person.sluttiness < 20:
        #She's startled and embarassed.
        "[the_person.title] closes her door behind her, then notices you. She gives a startled yell."
        the_person.char "Ah! [the_person.mc_title], what are you doing here?"
        "She tries to cover herself with her hands and fumbles with her door handle."
        mc.name "I'm just going to get some breakfast. What are you doing?"
        "[the_person.title] gets her door open and hurries back inside. She leans out so all you can see is her head."
        the_person.char "I was going to get some laundry and thought you were still asleep. Could you, uh, move along?"
        $ the_person.change_slut_temp(2)
        "You shrug and continue on your way."

    elif the_person.sluttiness < 60:
        #She doesn't mind but doesn't think to tease you further
        "[the_person.title] closes her door behind her, then notices you. She turns and smiles."
        the_person.char "Morning [the_person.mc_title], I didn't think you'd be up yet."
        mc.name "Yep, early start today. What are you up to?"
        if the_person.outfit.wearing_panties():
            "She starts to walk alongside you and doesn't seem to mind being in her underwear."
        else:
            "She starts to walk alongside you and doesn't seem to mind being naked."
        the_person.char "I'm just up to get some laundry. I put some in last night."
        "You let [the_person.title] get a step ahead of you so you can look at her ass."
        $ the_person.draw_person(position = "walking_away")
        menu:
            "Compliment her.":
                #Bonus love and happiness
                mc.name "Well, I'm glad I ran into you. Seing you is a pretty good way to start my day."
                $ the_person.change_love(2)
                $ the_person.change_happiness(5)
                the_person.char "You're just saying that because you get to see me naked, you perv."
                $ the_person.draw_person(position = "back_peek")
                "She peeks back at you and winks."

            "Slap her ass.":
                #Bonus sluttiness and obedience
                mc.name "Did you know you look really cute without any clothes on?"
                "You give her a quick slap on the ass from behind. She yelps and jumps forward a step."
                the_person.char "Ah! Hey, I'm not dressed like this for you, this is my house too you know."
                "She reaches back and rubs her butt where you spanked it."
                the_person.char "And ew. I'm your sister, you shouldn't be gawking at me."
                mc.name "I'll stop gawking when you stop shaking that ass."
                $ the_person.draw_person(position = "back_peek")
                the_person.char "You wish this ass was for you."
                "She spanks herself lightly and winks at you."
                $ the_person.change_slut_temp(4)
                $ the_person.change_obedience(2)

        $ the_person.draw_person(position = "walking_away")
        "You reach the door to the kitchen and split up. You wait a second and enjoy the view as your [the_person.possessive_title] walks away."

    else: #sluttiness >= 50
        #She likes being watched and teases you a little while you walk together.
        "[the_person.title] closes her door behing her, then notices you."
        the_person.char "Morning [the_person.mc_title], I was wondering if you were going to be up now."
        mc.name "Yep, early start today. What are you up to?"
        the_person.char "I was just going to get some laundry out of the machine."
        if the_person.outfit.wearing_panties():
            "[the_person.possessive_title] thumbs her underwear playfully."
        else:
            "[the_person.possessive_title] absentmindedly runs her hands over her hips."
        the_person.char "I know you like it when I walk around naked but Mom doesn't. At least when I'm doing laundry I have an excuse."
        "You join her as she starts to walk down the hall."
        $ the_person.draw_person(position = "walking_away")
        menu:
            "Grope her as you walk.":
                "You reach behind [the_person.title] and grab her ass while she's walking. She moans softly and leans against you."
                the_person.char "[the_person.mc_title], what are you doing? We can't doing anything here..."
                mc.name "I know, I'm just having a feel. You've got a great ass."
                "You spank her butt and she moans again. You work your hand down between her legs from behind and run a finger along her slit."
                the_person.char "Fuck, please don't get me too wet. I don't want to have to explain that to Mom if she finds us."
                "You flick your finger over [the_person.possessive_title]'s clit, then slide your hand back and kneed her ass some more."
                $ the_person.change_slut_temp(5)
                $ the_person.change_love(2)
                "When you reach the kitchen [the_person.title] reluctantly pulls away from you."


            "Put her hand on your cock as you walk.":
                "You take [the_person.title]'s left hand and push it against your crotch."
                the_person.char "What are you doing?"
                mc.name "Look at what you do to me when you walk around like this. You're driving me crazy [the_person.title]."
                "You let go of her hand but it stays planted on your bulge as you walk."
                the_person.char "You're such a pervert, you know that? I can't believe you'd even think about me like that..."
                "Her hand slides up to your waist, then down under your underwear. She wraps her hand around your shaft and rubs it gently."
                mc.name "Don't pretend like you don't like it. You're just as horny as I am."
                the_person.char "Hey, I'm just doing this for you, okay?"
                mc.name "Sure thing sis. Keep going."
                $ the_person.change_slut_temp(3)
                $ the_person.change_obedience(3)
                "The two of you walk slowly towards the kitchen as [the_person.possessive_title] fondles your dick."
                "When you reach the door to the kitchen she reluctantly pulls her hand out of your pants."

        mc.name "Maybe we'll follow up on this later."
        "[the_person.possessive_title]'s face is flush. She nods and heads towards the laundry room. You get to watch her ass as she goes."

    $ the_person.outfit = the_person.planned_outfit.get_copy() #Make sure to reset their outfits for the day.
    $ renpy.scene("Active")
    return

init 1 python:
    def family_weekend_breakfast_requirement():
        if mc_at_home() and time_of_day == 0 and mc.business.is_weekend() and mom.love > 20:
            return True
        return False

    family_morning_breakfast_crisis = Action("Family Morning Breakfast", family_weekend_breakfast_requirement, "family_morning_breakfast_label")
    morning_crisis_list.append([family_morning_breakfast_crisis,15])

label family_morning_breakfast_label():
    $ the_mom = mom
    $ the_sister = lily
    if the_mom is None or the_sister is None:
        return #If we don't have family members abort because something has gone horribly wrong!

    $ mom_slutty = False
    $ sis_slutty = False
    if the_mom.sluttiness > 40:
        $ mom_slutty = True
        $ the_mom.outfit = the_mom.wardrobe.get_random_appropriate_underwear(the_mom.sluttiness, guarantee_output = True)

    if the_sister.sluttiness > 40:
        $ sis_slutty = True
        $ the_sister.outfit = the_sister.wardrobe.get_random_appropriate_underwear(the_sister.sluttiness, guarantee_output = True)
    $ bedroom.show_background()
    "You're woken up in the morning by a knock at your door."
    mc.name "Uh, come in."
    "You groan to yourself and sit up in bed."
    if the_mom.love > the_sister.love:
        $ the_mom.draw_person()
        "Your mother cracks your door open and leans in."
        the_mom.char "I'm making some breakfast for you and your sister. Come on down if you'd like some."
        mc.name "Thanks Mom, I'll be down in a minute."
        $ renpy.scene("Active")
        "She flashes you a smile and closes the door."
    else:
        $ the_sister.draw_person()
        "[the_sister.possessive_title] cracks your door open and leans in. She seems just as tired as you are."
        the_sister.char "Hey, I think Mom's making a family breakfast for us."
        mc.name "Thanks for letting me know [the_sister.title], I'll be down in a minute."
        $ renpy.scene("Active")
        "She nods and closes your door as she leaves."

    "You get up, get dressed, and head for the kitchen."
    $ mc.change_location(kitchen)
    $ kitchen.show_background()
    $ the_mom.draw_person(position = "walking_away")
    if mom_slutty:
        if the_mom.outfit.wearing_panties():
            "[the_mom.possessive_title] is just in her underwear in front of the stove, humming as she scrambles a pan full of eggs."
        else:
            "[the_mom.possessive_title] is in front of the stove naked, humming as she scrambles a pan full of eggs."
    else:
        "[the_mom.possessive_title] is at the stove and humming to herself as she scrambles a pan full of eggs."
    $ the_mom.draw_person(position = "back_peek")
    the_mom.char "Good morning [the_mom.mc_title]. I'm almost ready to serve, hopefully your sister will be here soon."
    the_sister.char "I'm coming!"
    $ the_sister.draw_person()
    if sis_slutty:
        if the_sister.outfit.wearing_panties():
            "[the_sister.possessive_title] comes into the room just wearing her underwear. She gives a dramatic yawn before sitting down at the kitchen table."
        else:
            "[the_sister.possessive_title] comes into the room naked. She gives a dramatic yawn before sitting down at the kitchen table."
    else:
        "[the_sister.possessive_title] comes into the room and gives a dramatic yawn before sitting down at the kitchen table."

    if mom_slutty and sis_slutty:
        #You have breakfast with both of them stripped down like it's no big thing.
        $ the_sister.draw_person(position = "sitting")
        the_sister.char "Hope I'm not too late."
        $ the_mom.draw_person(position = "walking_away")
        "Your mother takes the pan off the stove and begins to slide the contents off onto three plates."
        the_mom.char "No, just on time."
        $ the_mom.draw_person()
        "She turns around and hands one plate to you and one plate to [the_sister.title]."
        $ the_sister.draw_person(position = "sitting")
        the_sister.char "Thanks Mom, you're the best!"
        $ the_mom.draw_person(position="sitting")
        the_mom.char "No problem, I'm just happy to spend my morning relaxing with my two favourite people!"
        "You enjoy a relaxing breakfast bonding with your mother and sister. [the_mom.possessive_title] seems particularly happy she gets to spend time with you."
        "Neither [the_sister.title] or [the_mom.possessive_title] seem to think it's strange to relax in their underwear."
        $ the_sister.change_love(3)
        $ the_sister.change_slut_temp(3)
        $ the_mom.change_love(3)
        $ the_mom.change_slut_temp(3)
        $ the_mom.change_happiness(10)
        "When you're done you help Mom put the dirty dishes away and get on with your day."



    elif mom_slutty and not sis_slutty:
        #Lily thinks her mom is embarassing and weird but Mom pulls rank.
        the_sister.char "Oh my god Mom, what are you wearing?"
        $ the_mom.draw_person(position = "back_peek")
        the_mom.char "What? It's the weekend and it's just the three of us. I didn't think anyone would mind if I was a little more casual."
        $ the_sister.draw_person(position = "sitting")
        if the_mom.outfit.vagina_visible():
            the_sister.char "Mom, I don't think you know what casual means. Could you at least put on some panties or something?"

        elif the_mom.outfit.tits_visible():
            the_sister.char "Mom, I don't think you know what casual means. I mean, couldn't you at least put a bra?"

        else:
            the_sister.char "Mom, you're prancing around the kitchen in your underwear. In front of your son and daughter. That's weird."
            "[the_sister.title] looks at you."
            the_sister.char "Right [the_sister.mc_title], that's weird?"

        if the_mom.obedience > 115:
            $ the_mom.draw_person(position = "back_peek")
            the_mom.char "What do you think [the_mom.mc_title], do you think it's \"weird\" for your mother to want to be comfortable in her own house?"
            menu:
                "Side with Mom.":
                    mc.name "I think Mom's right [the_sister.title]. It's nothing we haven't seen before, she's just trying to relax on her days off."
                    $ the_mom.change_obedience(-5)
                    $ the_sister.change_obedience(5)
                    "[the_sister.title] looks at the two of you like you're crazy then sighs dramatically."
                    the_sister.char "Fine, but this is really weird, okay?"
                    $ the_mom.draw_person(position = "sitting")
                    "[the_mom.possessive_title] dishes out three portions and sits down at the table with you. [the_sister.title] eventaully gets use to her mothers outfit and joins in on your conversation."
                    $ the_sister.change_slut_temp(5)
                    $ the_mom.change_happiness(10)


                "Side with [the_sister.title].":
                    mc.name "I actually think [the_sister.title] is right, this is a little weird. Could you go put something on, for our sakes?"
                    $ the_sister.change_obedience(-2)
                    $ the_sister.change_slut_temp(2)
                    $ the_mom.change_obedience(5)
                    $ the_mom.change_slut_temp(5)
                    the_mom.char "Oh you two, you're so silly. Fine, I'll be back in a moment. [the_sister.title], could you watch the eggs?"
                    $ the_sister.draw_person(position = "walking_away")
                    "Your mother leaves to get dressed. [the_sister.possessive_title] ends up serving out breakfast for all three of you."
                    $ the_mom.outfit = the_mom.planned_outfit.get_copy()
                    the_sister.char "She's been so weird lately. I don't know what's going on with her..."
                    $ the_mom.draw_person(position = "sitting")
                    $ the_sister.change_happiness(5)
                    $ the_mom.change_happiness(5)
                    "When [the_mom.possessive_title] gets back she sits down at the table and the three of you enjoy your breakfast together."

        else:
            #She likes what she likes
            $ the_mom.draw_person(position = "back_peek")
            the_mom.char "Well luckily I'm your mother and it doesn't matter what you think. I'm going to wear what makes me comfortable."
            "She takes the pan off the stove and slides the scrambled eggs out equally onto three plates."
            the_mom.char "Now, would you like some breakfast or not?"
            "[the_sister.title] sighs dramatically."
            the_sister.char "Fine, but this is really weird, okay?"
            $ the_sister.change_slut_temp(5)
            $ the_mom.change_happiness(10)
            $ the_mom.draw_person(position = "sitting")
            "[the_mom.possessive_title] gives everyone a plate and sits down. [the_sister.title] eventaully gets use to her mothers outfit and joins in on your conversation."
            "When you're done you help Mom put the dirty dishes away and get on with your day."


    elif sis_slutty and not mom_slutty:
        #MOm thinks lilly is way too underdressed and sends her back to get dressed.
        $ the_sister.draw_person(position = "sitting")
        "Your mother turns around and gasps."
        $ the_mom.draw_person(emotion = "angry")
        the_mom.char "[the_sister.title]! What are you wearing?"
        $ the_sister.draw_person(position = "sitting")
        the_sister.char "What do you mean? I just got up, I haven't had time to pick out an outfit yet."
        $ the_mom.draw_person(emotion = "angry")
        the_mom.char "You shouldn't be running around the house naked. Go put some clothes on young lady."
        $ the_sister.draw_person(position = "sitting", emotion = "angry")
        "[the_sister.possessive_title] scoffs and rolls her eyes."
        the_sister.char "Come on Mom, you're being ridiculous. This is my house too, I should be able to wear whatever I want!"
        "Your mother and sister lock eyes, engaged in a subtle battle of wills."
        if the_sister.obedience > the_mom.obedience:
            $ the_mom.draw_person(position = "walking_away")
            "Mom sighs loudly and turns back to the stove."
            the_mom.char "Fine! You're so stubborn [the_sister.title], I don't know how I survive around here!"
            $ the_sister.change_obedience(-2)
            $ the_sister.change_happiness(10)
            $ the_sister.change_slut_temp(3)
            $ the_mom.change_obedience(10)
            $ the_sister.draw_person(position = "sitting", emotion = "happy")
            "[the_sister.possessive_title] looks at you, obviously pleased with herself, and winks."

        else:
            "[the_sister.title] finally sighs loudly and looks away. She pushes her chair back and stands up in defeat."
            $ the_sister.draw_person(emotion = "angry")
            the_sister.char "Fine! I'll go put on some stupid clothes so my stupid mother doesn't keep worrying."
            $ the_sister.draw_person(position = "walking_away")
            "[the_sister.title] sulks out of the kitchen."
            $ the_mom.draw_person()
            the_mom.char "I don't know how I manage to survive with you two around!"
            $ the_sister.outfit = the_sister.planned_outfit.get_copy()
            $ the_sister.change_obedience(10)
            $ the_sister.change_happiness(-5)
            $ the_mom.change_obedience(-2)
            $ the_sister.draw_person(position = "sitting")
            "[the_sister.possessive_title] is back by the time Mom starts to plate breakfast. She sits down and starts to eat without saying anything."
        "When you're done you help Mom put the dirty dishes away and get on with your day."



    else:
        #Neither of them are particularly slutty, so it's just a normal breakfast.
        $ the_sister.draw_person(position = "sitting")
        the_sister.char "So what's the occasion Mom?"
        $ the_mom.draw_person()
        "[the_mom.possessive_title] takes the pan off the stove and scoops the scrambled eggs out equally onto three waiting plates."
        the_mom.char "Nothing special, I just thought we could have a nice quiet weekend breakfast together."
        "She slides one plate in front of you and one plate in front of [the_sister.title], then turns around to get her own before sitting down to join you."
        $ the_mom.draw_person(position = "sitting")
        the_mom.char "Go ahead, eat up!"
        $ the_sister.change_love(3)
        $ the_mom.change_love(3)
        $ the_mom.change_happiness(5)
        "You enjoy a relaxing breakfast bonding with your mother and sister. Your mom seems particularly happy she gets to spend time with you."
        "When you're done you help Mom put the dirty dishes away and get on with your day."

    $ renpy.scene("Active")
    return
