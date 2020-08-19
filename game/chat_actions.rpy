init -2 python:
    def always_true_requirement():
        return True

    def small_talk_requirement(the_person):
        if mc.energy < 15:
            return "Requires: 15 Energy"
        else:
            return True

    def compliment_requirement(the_person):
        if the_person.love < 10:
            return "Requires: 10 Love"
        elif mc.energy < 15:
            return "Requires: 15 Energy"
        else:
            return True

    def flirt_requirement(the_person):
        if the_person.love < 10:
            return "Requires: 10 Love"
        elif mc.energy < 15:
            return "Requires: 15 Energy"
        else:
            return True

    def date_option_requirement(the_person):
        if the_person.love < 20:
            return "Requires: 20 Love"
        return True

    def lunch_date_requirement(the_person):
        love_requirement = 20

        if time_of_day < 2:
            return "Too early to go for lunch"
        elif time_of_day > 2:
            return "Too late to go for lunch"
        elif the_person.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        else:
            return True

    def movie_date_requirement(the_person):
        love_requirement = 30
        if the_person.relationship == "Girlfriend":
            love_requirement += 10
        elif the_person.relationship == "Fiancée":
            love_requirement += 15
        elif the_person.relationship == "Married":
            love_requirement += 20
        love_requirement += -10*the_person.get_opinion_score("cheating on men")
        if love_requirement < 30:
            love_requirement = 30

        if the_person.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        elif mc.business.event_triggers_dict.get("date_scheduled", False):
            return "You already have a date planned!"
        else:
            return True


    def dinner_date_requirement(the_person):
        love_requirement = 40
        if the_person.relationship == "Girlfriend":
            love_requirement += 20
        elif the_person.relationship == "Fiancée":
            love_requirement += 30
        elif the_person.relationship == "Married":
            love_requirement += 40
        love_requirement += -10*the_person.get_opinion_score("cheating on men")
        if love_requirement < 40:
            love_requirement = 40

        if the_person.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        elif mc.business.event_triggers_dict.get("date_scheduled", False):
            return "You already have a date planned!"
        else:
            return True

    def evening_date_trigger(day_of_week): #Used for a mandatory crisis that triggers on the next Friday in time chunk 3.
        if time_of_day == 3 and day%7 == day_of_week: #Day of week is a number from 0 to 6, where 0 is Monday.
            return True
        return False

    # TODO: Decide if this is even needed with the new serum/sex change
    def serum_give_requirement(the_person):
        #the_person parameter passed to match other actions and for future proofing.
        if mc.inventory.get_any_serum_count() <= 0:
            return "Requires: Serum in inventory"
        else:
            return True

    def seduce_requirement(the_person):
        if the_person.sluttiness < 15:
            return "Requires: {image=gui/heart/three_quarter_red_quarter_empty_heart.png}"
        else:
            return True

    def grope_requirement(the_person):
        if the_person.sluttiness < 5:
            return False #Don't show the option at all at minimal sluttiness.
        elif mc.energy < 5:
            return "Not enough {image=gui/extra_images/energy_token.png}"
        else:
            return True

    def command_requirement(the_person):
        if the_person.obedience < 105:
            return "Requires: 105 Obedience"
        elif mc.energy < 10:
            return "Not enough {image=gui/extra_images/energy_token.png}"
        else:
            return True

    def change_titles_requirement(the_person):
        if the_person.obedience < 105:
            return "Requires: 105 Obedience"
        else:
            return True

    def serum_demand_requirement(the_person):
        if employee_role in the_person.special_role:
            #It's easier to convince her if she works for you
            if the_person.obedience < 110:
                return "Requires: 110 Obedience"
            elif mc.inventory.get_any_serum_count() <= 0:
                return "Requires: Serum in inventory"
            else:
                return True

        else:
            if the_person.obedience < 120:
                return "Requires: 120 Obedience"
            elif mc.inventory.get_any_serum_count() <= 0:
                return "Requires: Serum in inventory"
            else:
                return True

    def wardrobe_change_requirment(the_person):
        if the_person.obedience < 120:
            return "Requires: 120 Obedience"
        else:
            return True

    def bc_talk_requirement(the_person):
        if persistent.pregnancy_pref == 0:
            return False
        elif the_person.effective_sluttiness() < 15 or the_person.love < 15:
            return False
        elif pregnant_role in the_person.special_role: # don't talk about bc when she is pregnant
            return False
        else:
            return True

    def demand_touch_requirement(the_person):
        if the_person.obedience < 125: #TODO: Note: This isn't based on sluttiness directly, but we should have some dialogue reference to it.
            return "Requires: 125 Obedience"
        else:
            return True

    def demand_strip_requirement(the_person):
        if demand_strip_tits_requirement(the_person) == True or demand_strip_underwear_requirement(the_person) == True or demand_strip_naked_requirement(the_person) == True:
            return True
        return False

    def demand_bc_requirement(the_person):
        if persistent.pregnancy_pref == 0: #Don't talk about pregnancy if we don't want any of it.
            return False
        elif the_person.obedience < 100:
            return False
        elif the_person.obedience < 115:
            return "Requires: 115 Obedience"
        else:
            return True

    def lunch_date_create_topics_menu(the_person):
        opinion_question_list = []

        #Generates a list with a few (usually 4, unless there's some opinion collision, but it's not important enough to filter things out more intelligently) opinions, one of which she likes
        for x in __builtin__.range(3):
            possible_opinions = get_random_opinion()
            if possible_opinions not in opinion_question_list:
                opinion_question_list.append(possible_opinions)

        key_opinion = the_person.get_random_opinion(only_positive = True)

        if key_opinion is not None and key_opinion not in opinion_question_list:
            opinion_question_list.append(key_opinion)

        renpy.random.shuffle(opinion_question_list)

        formatted_opinion_list = []
        for item in opinion_question_list:
            formatted_opinion_list.append(["Chat about " + item, item])
        return formatted_opinion_list

    def build_person_introduction_titles():
        title_tuple = []
        for title in get_player_titles(the_person):
            title_tuple.append([title,title])
        return title_tuple

    def get_date_plan_actions(the_person):
        lunch_date_action = Action("Ask her out to lunch {image=gui/heart/Time_Advance.png}", lunch_date_requirement, "lunch_date_plan_label", args=the_person, requirement_args=the_person,
            menu_tooltip = "Take her out on casual date out to lunch. Gives you the opportunity to impress her and further improve your relationship.")
        movie_date_action = Action("Ask her out to the movies", movie_date_requirement, "movie_date_plan_label", args=the_person, requirement_args=the_person,
            menu_tooltip = "Plan a more serious date to the movies. Another step to improving your relationship, and who knows what you might get up to in the dark!")
        dinner_date_action = Action("Ask her out to a romantic dinner", dinner_date_requirement, "dinner_date_plan_label", args=the_person, requirement_args=the_person,
            menu_tooltip = "Plan a romantic, expensive dinner with her. Impress her and you might find yourself in a more intimate setting.")
        return ["Select Date", lunch_date_action, movie_date_action, dinner_date_action, ["Never mind", "Return"]]

    def create_movie_date_action(the_person):
        movie_action = Action("Movie date", evening_date_trigger, "movie_date_label", args=the_person, requirement_args=1) #it happens on a tuesday.
        mc.business.mandatory_crises_list.append(movie_action)
        mc.business.event_triggers_dict["date_scheduled"] = True
        return

    def create_dinner_date_action(the_person):
        dinner_action = Action("Dinner date", evening_date_trigger, "dinner_date_label", args=the_person, requirement_args=4) #it happens on a friday, so day%7 == 4
        mc.business.mandatory_crises_list.append(dinner_action)
        mc.business.event_triggers_dict["date_scheduled"] = True
        return

    def new_title_menu(the_person):
        title_tuple = []
        title_choice = None
        for title in get_titles(the_person):
            title_tuple.append([title,title])
        title_tuple.append(["Do not change her title","Back"])
        title_choice = renpy.display_menu(title_tuple,True,"Choice")
        return title_choice

    def new_mc_title_menu(the_person):
        title_tuple = []
        title_choice = None
        for title in get_player_titles(the_person):
            title_tuple.append([title,title])
        title_tuple.append(["Do not change your title","Back"])
        title_choice = renpy.display_menu(title_tuple,True,"Choice")
        return title_choice

    def new_possessive_title_menu(the_person):
        title_tuple = []
        title_choice = None
        for title in get_possessive_titles(the_person):
            title_tuple.append([title,title])
        title_tuple.append(["Do not change your title","Back"])
        title_choice = renpy.display_menu(title_tuple,True,"Choice")
        return title_choice

    def get_two_titles_for_person(title_func, person):
        title_one = get_random_from_list(title_func(person))
        title_two = get_random_from_list(list( set(title_func(person)) - set([title_one]) ))
        return (title_one, title_two)

label person_introduction(the_person, girl_introduction = True):
    if girl_introduction:
        $ the_person.call_dialogue("introduction")

    #She's given us her name, now she asks for yours.
    $ title_choice = renpy.display_menu(build_person_introduction_titles(),True,"Choice")
    mc.name "[title_choice], it's a pleasure to meet you."
    $ the_person.set_mc_title(title_choice)
    return

label person_new_title(the_person): #She wants a new title or to give you a new title.
    if __builtin__.len(get_titles(the_person)) <= 1: #There's only the one title available to them. Don't bother asking to change
        return
    $ ran_num = the_person.obedience + renpy.random.randint(-20, 20) #Randomize their effective obedience a little so they sometimes ask, sometimes demand

    if ran_num > 120: #She just asks you for something "fresh". Her obedience is high enough that we already have control over this.
        the_person.char "[the_person.mc_title], do you think [the_person.title] is getting a little old? I think something new might be fun!"
        menu:
            "Change what you call her":
                #TODO: present the player with a list. TODO: Refactor the event above to be a generic way of presenting a list, w/ the dialogue separated.
                $ title_choice = new_title_menu(the_person)
                if not (title_choice == "Back" or the_person.create_formatted_title(title_choice) == the_person.title):
                    mc.name "I think [title_choice] would really suit you."
                    $ the_person.set_title(title_choice)
                    "[the_person.title] seems happy with her new title."
                else:
                    mc.name "On second thought, I think [the_person.title] suits you just fine."
                    the_person.char "If you think so [the_person.mc_title]."

            "Don't change her title":
                mc.name "I think [the_person.title] suits you just fine."
                the_person.char "If you think so [the_person.mc_title]."

    elif ran_num > 95: #She picks a couple of choices and asks you to decide.
        $ (title_one, title_two) = get_two_titles_for_person(get_titles, the_person)
        if the_person.title == the_person.create_formatted_title(title_one) or the_person.title == the_person.create_formatted_title(title_two):  #If we picked the one we're currently using we have a slightly different dialogue setup.
            if the_person.title == the_person.create_formatted_title(title_two):
                $ placeholder = title_two #Swap them around so title_one is always the current title she has
                $ title_two = title_one
                $ title_one = placeholder
                $ placeholder = None
            $ formatted_title_one = the_person.title
            $ formatted_title_two = the_person.create_formatted_title(title_two)
            the_person.char "Hey [the_person.mc_title], do you like calling me [formatted_title_one] or do you think [formatted_title_two] sounds better?"
            menu:
                "Keep calling her [formatted_title_one]":
                    mc.name "I think [the_person.title] suits you perfectly, you should keep using it."
                    "She nods in agreement."
                    the_person.char "Yeah, I think you're right."
                "Change her title to [formatted_title_two]":
                    mc.name "[formatted_title_two] does have a nice ring to it. You should start using that."
                    $ the_person.set_title(title_two)
                    the_person.char "I think you're right. Thanks for the input!"
        else: #Both are new!
            $ formatted_title_one = the_person.create_formatted_title(title_one)
            $ formatted_title_two = the_person.create_formatted_title(title_two)
            the_person.char "So [the_person.mc_title], I'm thinking of changing things up a bit. Do you think [formatted_title_one] or [formatted_title_two] sounds best?"
            menu:
                "Change her title to [formatted_title_one]":
                    mc.name "I think [formatted_title_one] is the best of the two."
                    $ the_person.set_title(title_one)
                    the_person.char "Yeah, I think you're right. I'm going to have people call me that from now on."

                "Change her title to [formatted_title_two]":
                    mc.name "I think [formatted_title_two] is the best of the two."
                    $ the_person.set_title(title_two)
                    the_person.char "Yeah, I think you're right. I'm going to have people call me that from now on."

                "Refuse to change her title\n{color=#ff0000}{size=18}-5 Happiness{/size}{/color}":
                    mc.name "I don't think either of those sound better than [the_person.title]. You should really just stick with that."
                    "[the_person.title] rolls her eyes."
                    $ the_person.change_happiness(-5)
                    the_person.char "Well that isn't very helpful [the_person.mc_title]. Fine, I guess [the_person.title] will do."

        $ formatted_title_one = None
        $ formatted_title_two = None
        $ title_one = None
        $ title_two = None
    else: #She doesn't listen to you, so she just picks one and demands that you use it, or becomes unhappy.
        $ new_title = get_random_from_list(get_titles(the_person))
        python:
            while the_person.create_formatted_title(new_title) == the_person.title:
                new_title = get_random_from_list(get_titles(the_person))

        $ formatted_new_title = the_person.create_formatted_title(new_title)
        the_person.char "By the way [the_person.mc_title], I want you to start referring to me as [formatted_new_title] from now on. I think it suits me better."
        menu:
            "Change her title to [formatted_new_title]":
                mc.name "I think you're right, [formatted_new_title] sounds good."
                $ the_person.set_title(new_title)

            "Refuse to change her title\n{color=#ff0000}{size=18}-10 Happiness{/size}{/color}":
                mc.name "I think that sounds silly, I'm just going to keep calling you [the_person.title]."
                "[the_person.title] scoffs and rolls her eyes."
                $ the_person.change_happiness(-10)
                the_person.char "Whatever. It's not like I can force you to do anything."

        $ new_title = None
        $ formatted_new_title = None
    return

label person_new_mc_title(the_person):
    if __builtin__.len(get_player_titles(the_person)) <= 1: #There's only the one title available to them. Don't bother asking to change
        return
    $ ran_num = the_person.obedience + renpy.random.randint(-20, 20)
    if ran_num > 120: #She just asks you for something "fresh". Her obedience is high enough that we already have control over this.
        the_person.char "I was just thinking that I've called you [the_person.mc_title] for a pretty long time. If you're getting tired of it I could call you something else."
        menu:
            "Change what she calls you":
                #TODO: present the player with a list. TODO: Refactor the event above to be a generic way of presenting a list, w/ the dialogue separated.
                $ title_choice = new_mc_title_menu(the_person)
                if not (title_choice == "Back" or title_choice == the_person.mc_title):
                    mc.name "I think you should call me [title_choice] from now on."
                    $ the_person.set_mc_title(title_choice)
                    "[the_person.title] seems happy with your new title."
                else:
                    mc.name "On second thought, I think [the_person.mc_title] is fine for now."
                    the_person.char "If you think so [the_person.mc_title]."

            "Don't change her title for you":
                mc.name "I think [the_person.mc_title] is fine for now."
                the_person.char "Okay, if you say so!"

    elif ran_num > 95: #She picks a couple of choices and asks you to decide.
        $ (title_one, title_two) = get_two_titles_for_person(get_player_titles, the_person)
        if the_person.mc_title == title_one or the_person.mc_title == title_two:  #If we picked the one we're currently using we have a slightly different dialogue setup.
            if the_person.mc_title == title_two:
                $ placeholder = title_two #Swap them around so title_one is always the current title she has
                $ title_two = title_one
                $ title_one = placeholder
                $ placeholder = None

            the_person.char "Hey [the_person.mc_title], would you rather I called you [title_two]?"
            menu:
                "Have her keep calling you [title_one]":
                    mc.name "I think I like [title_one], but thanks for asking."
                    "She shrugs."
                    the_person.char "Sure, whatever you like [the_person.mc_title]."
                "Have her call you [title_two] instead":
                    mc.name "[title_two] does have a nice ring to it. You should start using that."
                    $ the_person.set_mc_title(title_two)
                    the_person.char "Alright, you got it [the_person.mc_title]!"

        else: #Both are new!
            the_person.char "You know, I really think [title_one] or [title_two] would fit you a lot better than [the_person.mc_title]. Which one do you think is better?"
            menu:
                "Have her call you [title_one]":
                    mc.name "I think [title_one] is the best of the two."
                    $ the_person.set_mc_title(title_one)
                    the_person.char "Yeah, you're right. I think I'll start calling you that from now on."

                "Have her call you [title_two]":
                    mc.name "I think [title_two] is the best of the two."
                    $ the_person.set_mc_title(title_two)
                    the_person.char "Yeah, you're right. I think I'll start calling you that from now on."

                "Refuse to change your title\n{color=#ff0000}{size=18}-5 Happiness{/size}{/color}":
                    mc.name "I don't think either of those sound better than [the_person.mc_title]. Let's stick with that for now."
                    "[the_person.title] rolls her eyes."
                    $ the_person.change_happiness(-5)
                    the_person.char "Fine, if you don't like change I can't make you."
        $ title_one = None
        $ title_two = None
    else: #She doesn't listen to you, so she just picks one and demands that you use it, or becomes unhappy.
        $ new_title = get_random_from_list(get_player_titles(the_person))
        python:
            while new_title == the_person.mc_title:
                new_title = get_random_from_list(get_player_titles(the_person))

        the_person.char "You know, I think [new_title] fits you better than [the_person.mc_title]. I'm going to start using that."
        menu:
            "Let her call you [new_title]":
                mc.name "Alright, if you think that's better."
                $ the_person.set_mc_title(new_title)

            "Demand she keeps calling you [the_person.mc_title]\n{color=#ff0000}{size=18}-10 Happiness{/size}{/color}":
                mc.name "I think that sounds silly, I want you to keep calling me [the_person.mc_title]."
                "[the_person.title] scoffs and rolls her eyes."
                $ the_person.change_happiness(-10)
                the_person.char "Whatever. If it's so important to you then I guess I'll just do it."
        $ new_title = None
    return

label small_talk_person(the_person, apply_energy_cost = True): #Tier 0. Useful for discovering a character's opinions and the first step to building up love.
    if apply_energy_cost: # Useful if you want to reuse this event inside of other events.
        $ mc.change_energy(-15)
    $ smalltalk_opinion = the_person.get_opinion_score("small talk")
    mc.name "So [the_person.title], what's been on your mind recently?"
    $ the_person.discover_opinion("small talk")
    $ successful_smalltalk = 60 + (smalltalk_opinion * 20) + (mc.charisma * 5)
    $ ran_num = renpy.random.randint(0,100)
    # TODO: Add a chance that she wants to talk about someone she knows.
    if ran_num < successful_smalltalk:
        if smalltalk_opinion >= 0:
            $ the_person.draw_person(emotion = "happy")
            "She seems glad to have a chance to take a break and make small talk with you."

        else:
            "She seems uncomfortable with making small talk, but after a little work you manage to get her talking."

        $ casual_sex_talk = the_person.sluttiness > 50
        $ opinion_learned = the_person.get_random_opinion(include_known = True, include_sexy = casual_sex_talk)

        if not opinion_learned is None:
            $ opinion_state = the_person.get_opinion_topic(opinion_learned)
            $ opinion_string = opinion_score_to_string(opinion_state[0])

            "The two of you chat pleasantly for half an hour."
            the_person.char "So [the_person.mc_title], I'm curious what you think about about [opinion_learned]. Do you have any opinions on it?"
            $ love_gain = 4
            $ prediction = 0
            menu:
                "I love [opinion_learned]":
                    $ prediction = 2
                    mc.name "Me? I love [opinion_learned]. Absolutely love it."

                "I like [opinion_learned]":
                    $ prediction = 1
                    mc.name "I really like [opinion_learned]."

                "I don't have any opinion about [opinion_learned]":
                    $ prediction = 0
                    mc.name "I don't really have any thoughts on it, I guess I just don't think it's a big deal."

                "I don't like [opinion_learned]":
                    $ prediction = -1
                    mc.name "I'm not a fan, that's for sure."

                "I hate [opinion_learned]":
                    $ prediction = -2
                    mc.name "I'll be honest, I absolutely hate [opinion_learned]. I just can't stand it."

            $ prediction_difference = abs(prediction - opinion_state[0])
            if prediction_difference == 4: #as wrong as possible
                the_person.char "Really? Wow, we really don't agree about [opinion_learned], that's for sure."
            elif prediction_difference == 3:
                the_person.char "You really think so? Huh, I guess we'll just have to agree to disagree."
            elif prediction_difference == 2:
                the_person.char "I guess I could understand that."
            elif prediction_difference == 1:
                the_person.char "Yeah, I'm glad you get it. I feel like we're both on the same wavelength."
            else: #prediction_difference == 0
                the_person.char "Exactly! It's so rare that someone feels exactly the same way about [opinion_learned] as me!"


            if opinion_state[1]:
                "You listen while [the_person.possessive_title] talks about how she [opinion_string] [opinion_learned]."
            else:
                $ the_person.discover_opinion(opinion_learned)
                "You listen while [the_person.possessive_title] talks and discover that she [opinion_string] [opinion_learned]."

            $ the_person.change_love(love_gain - prediction_difference)

        else:
            "You and [the_person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."

        $ smalltalk_bonus = smalltalk_opinion + 1
        $ the_person.change_happiness(smalltalk_bonus)
        if smalltalk_opinion >= 0:
            the_person.char "It was nice chatting [the_person.mc_title], we should do it more often!"
        else:
            the_person.char "So uh... I guess that's all I have to say about that..."
            "[the_person.char] trails off awkwardly."
    else:
        if smalltalk_opinion < 0:
            the_person.char "Oh, not much."
            $ the_person.change_happiness(smalltalk_opinion)
            "You try and keep the conversation going, but making small talk with [the_person.title] is like talking to a wall."
        else:
            the_person.char "Oh, not much honestly. How about you?"
            $ the_person.change_happiness(smalltalk_opinion)
            "[the_person.possessive_title] seems happy to chitchat, and you spend a few minutes just hanging out."
            "You don't feel like you've learned much about her, but least she seems to have enjoyed talking."

    $ the_person.apply_serum_study()
    return

label compliment_person(the_person): #Tier 1. Raises the character's love. #TODO: just have it raise love and not sluttiness.
    $ mc.change_energy(-15)
    mc.name "Hey [the_person.title]. How are you doing today? You're looking good, that's for sure."
    the_person.char "Aww, thank you. You're too kind. I'm doing well."
    "You chat with [the_person.possessive_title] for a while and slip in a compliment when you can. She seems flattered by all the attention."
    $ the_person.change_love(5, max_modified_to = 20)
    $ the_person.change_happiness(2)
    the_person.char "It's been fun talking [the_person.mc_title], we should do this again sometime!"
    $ the_person.apply_serum_study()
    return


#    mc.name "Hey [the_person.name], I just wanted to say that you look great today. That style really suits you." #TODO: Add more context aware dialogue.
#    $ slut_difference = int(the_person.sluttiness - the_person.outfit.slut_requirement) #Negative if their outfit is sluttier than what they would normally wear.
#    # Note: The largest effect should occure when the outfit is just barely in line with her sluttiness. Too high or too low and it will have no effect.

#    $ sweet_spot_range = 10
#    if slut_difference < -sweet_spot_range : #Outfit is too slutty, she will never get use to wearing it.
#        the_person.char "Really? It's just so revealing, what do people think of me when they see me? I don't think I'll ever get use to wearing this."
#        $ the_person.draw_person(emotion = "default")

#    elif slut_difference > sweet_spot_range:  #Outfit is conservative, no increase.
#        $ the_person.draw_person(emotion = "default")
#        the_person.char "Really? I think it looks too bland, showing a little more skin would be nice."

#    else: #We are within the sweet_spot_range with the outfit.
#        $ slut_difference = math.fabs(slut_difference)
#        if slut_difference > sweet_spot_range:
#            $ slut_difference = sweet_spot_range
#        $ slut_difference = sweet_spot_range - slut_difference #invert the value so we now have 10 - 10 at both extreme ends, 10 - 0 at the middle where it will have the most effect.
#        $ change_amount = int((mc.charisma + 1 + slut_difference)/2)
#        if change_amount + the_person.sluttiness > 40:
#            $ change_amount = 40 - the_person.sluttiness
#        $ slut_report = the_person.change_slut_temp(change_amount)
#        the_person.char "Glad you think so, I was on the fence, but it's nice to know that somebody likes it!"
#    return

label flirt_person(the_person): #Tier 1. Raises a character's sluttiness up to a low cap while also raising their love by less than a compliment.
    #TODO: change this to be more appropriate for a love changing action (and maybe move the current stuff somewhere else?)
    #TODO: Vary the flirting intro and response based on sluttiness.
    $ mc.change_energy(-15)

    #TODO: varients of seduction attempts and responses, ramping up to entering the sex system immediately.

    # Idea:
    # -> This is love based, so most of it should hinge around location/privacy.
    #  |-> We can justify a higher Love requirement to enter the sex system immediately because there are date options for that
    #  |-> It is also suppose to be used in tandem with Obedience or Sluttiness to get somewhere, by itself (ie. Vanilla romance) is slow and boring.


    #Plan:
    # Have a few tiers of responses. Low love (0 to 15), mid love (16 to 35), high love (36>)
    # Low love: General appearance based compliments.

    #Ideas:
    # If in a poor location (not in private, not at home, etc.) she should mention that as a way of "seeing where things go", unless she is very slutty.
    # If slutty but in a poor location she might flash you her tits (TODO: Add a way of "flashing" tits through clothing items by hiding an area mask).

    if girlfriend_role in the_person.special_role:
        mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
        $ the_person.call_dialogue("flirt_response_girlfriend")

    elif affair_role in the_person.special_role:
        mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
        $ the_person.call_dialogue("flirt_response_affair")

    elif the_person.love <= 20:
        #Low Love
        mc.name "[the_person.title], you're looking nice today. That outfit looks good on you."
        $ the_person.call_dialogue("flirt_response_low")

    elif the_person.love <= 40: #20 to 40
        # Mid Love
        mc.name "You're looking hot today [the_person.title]. That outfit really shows off your body."
        $ the_person.call_dialogue("flirt_response_mid")

    else:
        # High Love
        mc.name "[the_person.title], your outfit is driving me crazy. What are my chances of getting you out of it?"
        $ the_person.call_dialogue("flirt_response_high")

    # mc.name "Hey [the_person.title], you're looking particularly good today. I wish I got to see a little bit more of that fabulous body."
    $ mc.listener_system.fire_event("player_flirt", the_person = the_person)
    $ change_amount = mc.charisma + 1 + the_person.get_opinion_score("flirting") #We still cap out at 20, but we get there a little faster or slower depending on if they like flirting
    if change_amount + the_person.sluttiness > 20:
        $ change_amount = 20 - the_person.sluttiness
        if change_amount < 0:
            $ change_amount = 0

    $ the_person.change_happiness(the_person.get_opinion_score("flirting"))
    $ the_person.change_slut_temp(change_amount)
    $ the_person.change_love(3, max_modified_to = 25)
    $ the_person.discover_opinion("flirting")
    $ the_person.apply_serum_study()
    # $ the_person.call_dialogue("flirt_response") #This has been divided up into flirt_response_[low,mid,high].

    return

label date_person(the_person): #You invite them out on a proper date
    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([get_date_plan_actions(the_person)]))
    else:
        call screen main_choice_display([get_date_plan_actions(the_person)])
    if _return != "Return":
        $ _return.call_action() #This is where you're asked to plan out the date, or whatever.
    return

label lunch_date_plan_label(the_person):
    # Take her out to lunch, raises love to a max of 50 if you pick the correct chat options
    if sister_role in the_person.special_role:
        mc.name "I was thinking about getting some lunch, do you want to come with me and hang out?"
        the_person.char "Hey, that sounds nice! You're always out of the house, I wish we got to spend more time together like we did when we were younger."

    elif mother_role in the_person.special_role:
        mc.name "I'm going to go out for lunch. You've been busy lately, would you like to take a break and join me?"
        the_person.char "Aww, it's so sweet that you still want to spend time with your mother. I'd love to!"

    elif aunt_role in the_person.special_role:
        mc.name "Would you like to come and have lunch with me? I haven't seen you much since I was a kid, I'm sure we have a lot to catch up on."
        the_person.char "It has been a long time, hasn't it. Lunch sounds wonderful!"

    elif cousin_role in the_person.special_role:
        mc.name "I'm going to get some lunch, would you like to come along with me?"
        the_person.char "You want me to be seen in public with you? You're really pushing it [the_person.mc_title], but sure."

    elif not (the_person.relationship == "Single" or the_person.get_opinion_score("cheating on men") > 0): #IF she likes cheating she doesn't even mention she's in a relationship
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me? Maybe just grab a coffee and hang out for a while?"
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "That sounds nice, [the_person.mc_title]."
        "She pauses and seems to consider something for a moment."
        the_person.char "Just so we're on the same page, this is just as friends, right? I have a [so_title], I don't want to get anything confused here."
        mc.name "Of course! I just want to hang out and talk, that's all."
        the_person.char "Okay, let's go then!"

    else:
        mc.name "Would you like to go get a coffee, maybe a little lunch, and just chat for a while? I feel like I want to get to know you better."
        the_person.char "That sounds nice, I think I'd like to get to know you better too."
        the_person.char "If you're ready to go right now I suppose I am too. Let's go!"

    call lunch_date_label(the_person) from _call_lunch_date_label #There's no need to schedule anything because this happens right away.
    return

label lunch_date_label(the_person): #Could technically be included in the planning phase, but broken out to fit the structure of the other events.
    the_person.char "So, where do you want to go?"
    $ the_type = get_random_from_list(["Chinese food","Thai food","Italian food","sushi","Korean barbecue","pizza","sandwiches"])
    mc.name "I know a nice place nearby. How do you like [the_type]?"
    the_person.char "No complaints, as long as it's good!"
    mc.name "Alright, let's go then!"
    "You and [the_person.title] walk together to a little lunch place nearby. You chat comfortably with each other as you walk."
    $ renpy.show("restaurant", what = restaraunt_background)
    "A bell on the door jingles as you walk in."
    mc.name "You grab a seat and I'll order for us."
    $ clear_scene()
    "You order food for yourself and [the_person.possessive_title] and wait until it's ready."
    $ mc.business.funds += -30
    $ the_person.draw_person(position = "sitting")
    "When it's ready you bring it over to [the_person.title] and sit down at the table across from her."
    if renpy.random.randint(0,100) < 40:
        the_person.char "Mmm, it looks delicious. I'm just going to wash my hands, I'll be back in a moment."
        $ clear_scene()
        "[the_person.possessive_title] stands up heads for the washroom."
        menu:
            "Add some serum to her food" if mc.inventory.get_any_serum_count() > 0:
                call give_serum(the_person) from _call_give_serum_20
                if _return:
                    "Once your sure nobody else is watching you add a dose of serum to [the_person.title]'s food."
                    "With that done you lean back and relax, waiting until she returns to start eating your own food."
                else:
                    "You think about adding a dose of serum to [the_person.title]'s food, but decide against it."
                    "Instead you lean back and relax, waiting until she returns to start eating your own food."

            "Add some serum to her food\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
                pass

            "Leave her food alone":
                "You lean back and relax, waiting until [the_person.title] returns to start eating."

        $ the_person.draw_person(position = "sitting")
        the_person.char "Thanks for waiting, now let's eat!"
    else:
        the_person.char "Mmm, it looks delicious. Or maybe I'm just really hungry. Either way, let's eat!"
    "You dig into your lunch, chatting between bites about this and that. What do you talk about?"
    $ conversation_choice = renpy.display_menu(lunch_date_create_topics_menu(the_person),True,"Choice")
    $ the_person.discover_opinion(conversation_choice)
    $ score = the_person.get_opinion_score(conversation_choice)
    $ kiss_after = False
    if score > 0:
        "You steer the conversation towards [conversation_choice] and [the_person.title] seems more interested and engaged."
        $ kiss_after = True
        $ the_person.change_love(10, max_modified_to = 50)
        $ the_person.change_happiness(5)
    elif score == 0:
        "You steer the conversation towards [conversation_choice]. [the_person.title] chats pleasantly with you, but she doesn't seem terribly interested in the topic."
        $ the_person.change_love(5, max_modified_to = 50)
    else: #Negative score
        "You steer the conversation towards [conversation_choice]. It becomes quickly apparent that [the_person.title] is not interested in talking about that at all."
        $ the_person.change_love(1, max_modified_to = 35)

    "Before you know it you've both finished your lunch and it's time to leave. You walk [the_person.title] outside and get ready to say goodbye."
    the_person.char "This was fun [the_person.mc_title], we should do it again."
    if not the_person.has_family_taboo() and (the_person.relationship == "Single" or the_person.get_opinion_score("cheating on men") > 0) and kiss_after:
        $ the_person.draw_person(position = "kissing")
        "She steps in close and kisses you. Her lips are soft and warm against yours."
        "After a brief second she steps back and smiles."
        $ the_person.draw_person()
        mc.name "Yeah, we should. I'll see you around."

    else:
        "She steps close and gives you a quick hug, then steps back."
        mc.name "Yeah, we should. I'll see you around."

    $ clear_scene()
    call advance_time() from _call_advance_time_29
    return

label movie_date_plan_label(the_person):
    # She starts to wonder if she should be telling her boyfriend, etc. about this.
    if day%7 == 1 and time_of_day < 3:
        $ is_tuesday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_tuesday = False


    if sister_role in the_person.special_role:
        mc.name "Hey, I was wondering if you'd like to see a movie with me some time? You know, spend a little more time together as brother-sister."
        the_person.char "It's been like, a year since I went to the movies with you. I think it was when my date ghosted me and you swept in and saved the night by coming with me."
        the_person.char "I can't quite remember what we saw though..."
        "She seems puzzled for a moment, then shrugs and smiles at you."
        the_person.char "Oh well, it's probably not important. Sure thing [the_person.mc_title], a movie sounds fun!"
        if is_tuesday:
            the_person.char "How about tonight? I think tickets are half price."
        else:
            the_person.char "How about Tuesday night? I tickets are half price."

    elif mother_role in the_person.special_role:
        mc.name "Hey [the_person.title], would you like to come to the movies with me? I want to spend some more time together, mother and son."
        the_person.char "Aww, you're precious [the_person.mc_title]. I would love to go to the movies with you."
        the_person.char "Remember how me and you use to watch movies together every weekend? I felt like our relationship was so close because of that."
        "She seems distracted by the memory for a moment, then snaps back to the conversation."
        if is_tuesday:
            the_person.char "Would you be free tonight?"
        else:
            the_person.char "Would you be free Tuesday night?"

    elif aunt_role in the_person.special_role:
        mc.name "[the_person.title], would you like to come see a movie with me? I think it would just be nice to spend some more time together."
        the_person.char "You know, I haven't been out much since I left my ex, so a movie sounds like a real good time."
        if is_tuesday:
            the_person.char "How about later tonight? I don't have anything going on."
        else:
            the_person.char "How about Tuesday night? I don't have anything going on then."

    elif cousin_role in the_person.special_role:
        mc.name "Hey, do you want to come see a movie with me and spend some time together?"
        the_person.char "Fine, but no telling people we're related, okay? I don't want anyone to think I might be a dweeb like you."
        "She gives you a wink."
        if is_tuesday:
            the_person.char "How about tonight? I didn't have anything going on."
        else:
            the_person.char "How about Tuesday? I don't have anything going on then."

    elif not the_person.relationship == "Single":
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        mc.name "It would give us a chance to spend time together."
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.get_opinion_score("cheating on men") > 0:
            the_person.char "Oh, a movie sounds fun!"
            "She gives you a playful smile."
            the_person.char "Just don't tell my [so_title], okay? He might not like me hanging around with a hot guy like you."
            mc.name "My lips are sealed."
            if the_person.effective_sluttiness() > 60:
                if is_tuesday:
                    the_person.char "Treat me right and mine might not be. He's normally out late with work tonight, how does that sound?"
                else:
                    the_person.char "Treat me right and mine might not be. He's normally out late with work on Tuesdays, how does that sound?"
            else:
                if is_tuesday:
                    the_person.char "He's normally out late with work on Tuesdays, so how about would tonight sound for you?"
                else:
                    the_person.char "He's normally out late with work on Tuesdays, how does that sound for you?"

        else:
            the_person.char "Oh, a movie sounds fun! But..."
            mc.name "Is there something wrong?"
            the_person.char "No, I just don't know what my [so_title] would think. He might be a little jealous of you, you know?"
            mc.name "You don't have to tell him that I'll be there, if you don't want to. There's no reason you couldn't go out by yourself if you wanted to."
            "She thinks about it for a moment, then nods and smiles."
            if is_tuesday:
                the_person.char "You're right, of course. He's normally busy with work tonight, so how does that sound for you?"
            else:
                the_person.char "You're right, of course. He's normally busy with work on Tuesdays, how does that sound for you?"

    else:
        mc.name "So [the_person.title], I was wondering if you'd like to come see a movie with me some time this week."
        mc.name "It would give us a chance to spend some time together and get to know each other better."
        if is_tuesday:
            the_person.char "Oh, a movie sounds fun! I don't have anything going on tonight, would that work for you?"
        else:
            the_person.char "Oh, a movie sounds fun! I don't have anything going on Tuesday night, would that work for you?"

    menu:
        "Plan a date for tonight" if is_tuesday:
            mc.name "Tonight would be perfect, I'll will see you later."
            the_person.char "See you!"
            $ create_movie_date_action(the_person)

        "Plan a date for Tuesday night" if not is_tuesday:
            mc.name "Tuesday would be perfect, I'm already looking forward to it."
            the_person.char "Me too!"
            $ create_movie_date_action(the_person)

        "Maybe some other time":
            mc.name "I'm busy on Tuesday unfortunately."
            the_person.char "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."

    return "Advance Time"

label movie_date_label(the_person):
    #The actual event produced when it's time to go on your date.
    $ mc.business.event_triggers_dict["date_scheduled"] = False #Deflag this event so you can schedule a date with another person for next week.
    "You have a movie date planned with [the_person.title] right now."

    menu:
        "Get ready for the date {image=gui/heart/Time_Advance.png}" if mc.business.funds >= 50:
            pass

        "Get ready for the date\n{color=#ff0000}{size=18}Requires: $50{/size}{/color} (disabled)" if mc.business.funds < 50:
            pass

        "Cancel the date (tooltip)She won't be happy with you canceling last minute.":
            "You get your phone out and text [the_person.title]."
            mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
            $ the_person.change_love(-5)
            $ the_person.change_happiness(-5)
            the_person.char "I hope everything is okay. Maybe we can do this some other time then."
            return

    #TODO: if she has a boyfriend have him sometime show up. Depending on Love and stuff you can sometimes get them to break up (and instantly be in a relationship), or ruin her love and happiness.

    "You get ready and text [the_person.title] confirming the time and place. A little while later you meet her outside the theater."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    $ the_person.draw_person()
    the_person.char "Hey, good to see you!"
    the_person.char "I'm ready to go in, what do you want to see?"
    $ renpy.show("Theater", what = theater_background)
    $ movie_type = None
    $ likes_movie = False
    menu:
        "Watch an action movie":
            $ the_choice = get_random_from_list(["The Revengers", "Raiders of the Found Ark", "Die Difficult", "Mission: Improbable", "Wonderful Woman", "John Wicked: Part 3", "The Destructonator", "Waterman"])
            $ movie_type = "action"
            if the_person.personality is wild_personality or the_person.personality.default_prefix == wild_personality.personality_type_prefix: #If it's a wild or wild derived personality type
                $ likes_movie = True
            mc.name "Yeah, I've wanted to see [the_choice] for a while. I'll go get us tickets."

        "Watch a comedic movie":
            $ the_choice = get_random_from_list(["Spooky Movie", "Aaron Powers", "Dumber and Dumberest-er", "Ghostblasters", "Shaun of the Undead"])
            $ movie_type = "comedy"
            if the_person.personality is relaxed_personality or the_person.personality.default_prefix == relaxed_personality.personality_type_prefix:
                $ likes_movie = True
            mc.name "I thought we'd both enjoy [the_choice]. I'll go get us tickets."

        "Watch a romantic movie":
            $ the_choice = get_random_from_list(["Olympic", "Britannic","The Workbook", "East Side Tale", "Pottery Poltergeist"])
            $ movie_type = "romantic"
            if the_person.personality is reserved_personality or the_person.personality.default_prefix == reserved_personality.personality_type_prefix:
                $ likes_movie = True
            mc.name "I thought [the_choice] would be a good fit for us. You just wait here, I'll go get us tickets."

        "Watch a foreign film":
            $ the_choice = get_random_from_list(["that one in French", "that one in Italian", "that one in Russian", "that one in Japanese", "that one in Mandarin", "that one that's silent"])
            $ movie_type = "foreign"
            if the_person.personality is introvert_personality or the_person.personality.default_prefix == introvert_personality.personality_type_prefix:
                $ likes_movie = True
            mc.name "I haven't heard much about it, but I think we should watch [the_choice]. It should be a really unique one."
            mc.name "I'll go get us tickets; be back in a moment."

    if the_person.personality is bimbo_personality and movie_type != "foreign":
        $ likes_movie = True # Bimbos like anything other than weird art pieces.

    #TODO: Generate a girl and assign them a uniform.
    "You walk up to the ticket booth and get tickets for yourself and [the_person.possessive_title]."
    $ mc.business.funds += -50

    "Tickets in hand, you rejoin [the_person.title] and set off to find your theater."
    the_person.char "Did you want to get us some popcorn or anything like that?"
    menu:
        "Stop at the concession stand\n{color=#ff0000}{size=18}Costs: $20{/size}{/color}" if mc.business.funds >= 20:
            mc.name "Sure, you run ahead and I'll go get us some snacks."
            $ clear_scene()
            $ mc.business.funds += -20
            "You give [the_person.possessive_title] her ticket and split up. At the concession stand you get a pair of drinks and some popcorn to share."
            menu:
                "Put a dose of serum in her drink" if mc.inventory.get_any_serum_count() > 0:
                    call give_serum(the_person) from _call_give_serum_14

                "Put a dose of serum in her drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
                    pass

                "Leave her drink alone":
                    pass

            "Snacks in hand you return to [the_person.title]. She takes a sip from her drink as you settle into your seat beside her."


        "Stop at the concession stand\n{color=#ff0000}{size=18}Requires: $20{/size}{/color} (disabled)" if mc.business.funds < 20:
            pass

        "Just go to the movie":
            mc.name "That stuff is always so overpriced, I hate giving them the satisfaction."
            $ the_person.change_happiness(-2)
            the_person.char "Right. Sure."
            "You find your theater, pick your seats, and settle down next to each other for the movie."


    $ the_person.draw_person(position = "sitting", lighting = [0.5,0.5,0.5])
    "You chat for a few minutes until the theater lights dim and the movie begins."

    if likes_movie: #She's enjoying the movie. Good for love gain, and you may be able to feel her up while she's enjoying the movie.
        "Halfway through the movie it's clear that [the_person.title] is having a great time. She's leaning forward in her seat, eyes fixed firmly on the screen."
        "As the movie approaches it's climax she reaches her hand down and finds yours to hold."
        "When it's finished you leave the theater together, still holding hands."
        $ the_person.draw_person()
        mc.name "So, did you like the movie?"
        the_person.char "It was amazing! Let's watch something like that next time."
        $ the_person.change_love(10, max_modified_to = 80)

    else: #She's bored. Bad for love gain, but good for getting her to fool around. She may start to feel you up to distract herself.
        "Halfway through the movie it's becoming clear that [the_person.title] isn't enthralled by it."
        if (the_person.sluttiness - the_person.get_opinion_score("public sex") * 5) > 50 and (the_person.relationship == "Single" or the_person.get_opinion_score("cheating on men") > 0) and not the_person.has_family_taboo():
            "While you're watching you feel her rest her hand on your thigh. She squeezes it gently and slides her hand up higher and higher while whispering into your ear."
            the_person.char "I'm bored. You don't mind if I make this a little more interesting, do you?"
            "You take a quick look around. The theater you're in is mostly empty, and nobody is in the same row as you."
            menu:
                "Go ahead":
                    mc.name "I'm certainly not going to stop you."
                    "Her hand slides up to your waist and undoes the button to your pants. You get a jolt of pleasure as her fingers slide onto your hardening cock."
                    "[the_person.title] stays sitting in her seat, eyes fixed on the movie screen as she begins to fondle your dick."
                    "As you get hard she starts to stroke you off. Her hand is warm and soft, and the risk of being caught only enhances the experience."
                    "After a few minutes [the_person.possessive_title] brings her hand to her mouth, licks it, and then goes back go jerking you off with her slick hand."

                    if (the_person.sluttiness - the_person.get_opinion_score("public sex") * 5) > 65 and (the_person.relationship == "Single" or the_person.get_opinion_score("cheating on men") > 0) and not the_person.has_family_taboo():
                        "You're enjoying the feeling of her wet hand sliding up and down your cock when she stops. You're about to say something when she slides off of her movie seat and kneels down in the isle."
                        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob", lighting = [0.5, 0.5, 0.5])
                        "Without a word she slides your hard dick into her mouth and starts to suck on it. You struggle to hold back your moans as she blows you."
                        "You rest a hand on the top of her head and keep a lookout in the theater, but nobody seems to have noticed."
                        "She comes up for air slides up your body, whispering into your ear."
                        the_person.char "Do you want to go to the bathroom and fuck me, or do you want to finish in my mouth right here?"
                        menu:
                            "Fuck her":
                                "You zip up your pants and stand up. [the_person.title] takes your hand and you rush out of the theater."
                                $ movie_bathroom = Room("theater bathroom", "Theater Bathroom", [], bathroom_background, [], [], [], False, [0,0], visible = False) #TODO: Decide if we need any objects in the bathroom
                                $ movie_bathroom.show_background()
                                $ movie_bathroom.add_object(make_wall())
                                $ movie_bathroom.add_object(make_floor())
                                $ mc.change_location(movie_bathroom)
                                $ the_person.change_arousal(20 + (the_person.get_opinion_score("public sex") * 10))
                                $ mc.change_arousal(40)
                                "You hurry into the women's bathroom and lock yourselves in an empty stall."
                                call fuck_person(the_person, private = True) from _call_fuck_person_28
                                $ the_person.review_outfit()
                                $ del movie_bathroom
                                $ renpy.show("Theater", what = theater_background)
                                "You slip out of the bathroom as quickly as possible and return to your seats with some time pleasantly passed."                           

                            "Cum right here":
                                mc.name "I want you to finish me here."
                                "She purrs in your ear and slides back down to her knees again. Her warm mouth wraps itself around your shaft and she starts to blow you again."
                                "It doesn't take long for her to bring you to the edge of your orgasm."
                                "You clutch at the movie seat arm rests and suppress a grunt as you climax, blowing your hot load into [the_person.title]'s mouth and down her throat."
                                $ the_person.cum_in_mouth()
                                "She waits until you're finished, then pulls off your cock, wipes her lips on the back of her hand, and sits down next to you."
                                $ the_person.change_slut_temp(3)
                                the_person.char "Thank you, that was fun."
                                "She takes your hand and holds it. You lean back, thoroughly spent, and zone out for the rest of the movie."

                "Tell her to knock it off":
                    mc.name "I just want to watch a movie together. Can you at least try and pay attention?"
                    $ the_person.change_obedience(2)
                    $ the_person.change_happiness(-5)
                    $ the_person.change_love(-1)
                    "She pulls her hand back and sighs."
                    the_person.char "Aw, you're no fun."

        else:
            # SHe just annoys you by asking random questions
            the_person.char "Who is that again?"
            mc.name "He's working for the bad guy."
            the_person.char "Wait, I thought he was just with the good guys though."
            mc.name "He was lying. It's hard to explain."
            "Eventually the movie is over and you leave the theater together."

        $ the_person.draw_person()
        mc.name "So, did you like the movie?"
        the_person.char "It was okay. Let's try something else next time though."
        $ the_person.change_love(5, max_modified_to = 80)

    the_person.char "There will be a next time, right?"
    mc.name "I'd love for there to be."
    $ the_person.change_happiness(10)

    if sister_role not in the_person.special_role and mother_role not in the_person.special_role: #You live at home with those two, so it would be weird to kiss them goodnight.
        "She leans towards you and you give her a long kiss before saying goodnight."

    else:
        "She leans towards you and gives you a quick kiss."
        the_person.char "Let's head home then."

    $ clear_scene()
    $ mc.change_location(bedroom) #Put them back at home after the event, so if they were in the bathroom they aren't any more.
    $ mc.location.show_background()
    return "Advance Time"


label dinner_date_plan_label(the_person):
    if day%7 == 4 and time_of_day < 3:
        $ is_friday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_friday = False

    if sister_role in the_person.special_role:
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together. Some brother sister bonding time."
        if is_friday:
            the_person.char "That sounds great [the_person.mc_title]. Would tonight work for you?"
        else:
            the_person.char "That sounds great [the_person.mc_title]. Would Friday be good?"

    elif mother_role in the_person.special_role:
        mc.name "Mom, I was wondering if I could take you out to dinner, just the two of us. I'd enjoy some mother son bonding time."
        if is_friday:
            the_person.char "Aww, that's so sweet. How about tonight, after we're both finished with work."
        else:
            the_person.char "Aww, that's so sweet. How about Friday, after we're both finished with work."

    elif aunt_role in the_person.special_role:
        mc.name "[the_person.title], would you like to go out on a dinner date with me? I think it would be a nice treat for you."
        the_person.char "That sounds like it would be amazing. It's been tough, just me and [cousin.title]. I don't get out much any more."
        "She smiles and gives you a quick hug."
        if is_friday:
            the_person.char "How about tonight?"
        else:
            the_person.char "How about Friday night?"

    elif cousin_role in the_person.special_role:
        mc.name "Hey, I want to take you out to dinner."
        the_person.char "Jesus, at least buy me dinner first. Wait a moment..."
        "She laughs at her own joke."
        if is_friday:
            the_person.char "Fine, how about tonight?"
        else:
            the_person.char "Fine, how about Friday?"

    elif not the_person.relationship == "Single":
        mc.name "[the_person.title], I'd love to spend some time together, just the two of us. Would you let me take you out for dinner?"
        $ SO_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "[the_person.mc_title], you know I've got a [SO_title], right? Well..."
        if the_person.get_opinion_score("cheating on men") > 0:
            "She doesn't take very long to make up her mind."
            if is_friday:
                the_person.char "He's out with friends tonight and what he doesn't know can't hurt him. Shall we go tonight?"
            else:
                the_person.char "He won't know about it, right? What he doesn't know can't hurt him. Are you free Friday?"
        else:
            "She thinks about it for a long moment."
            if is_friday:
                the_person.char "Just this once, and we have to make sure my [SO_title] never finds out. Shall we go tonight?"
            else:
                the_person.char "Just this once, and we have to make sure my [SO_title] never finds out. Are you free Friday?"

    else:
        mc.name "[the_person.title], I'd love to get to know you better. Would you let me take you out for dinner?"
        if is_friday:
            the_person.char "That sounds delightful [the_person.mc_title]. I'm free tonight, if you are available."
        else:
            the_person.char "That sounds delightful [the_person.mc_title]. I'm free Friday night, if you would be available."

    menu:
        "Plan a date for tonight" if is_friday:
            mc.name "It's a date. I'll see you tonight."
            the_person.char "See you!"
            $ create_dinner_date_action(the_person)

        "Plan a date for Friday night" if not is_friday:
            mc.name "It's a date. I'm already looking forward to it."
            the_person.char "Me too!"
            $ create_dinner_date_action(the_person)

        "Maybe some other time":
            mc.name "I'm busy on Friday unfortunately."
            the_person.char "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."
    return

label dinner_date_label(the_person):
    $ mc.business.event_triggers_dict["date_scheduled"] = False #Deflag this event so you can schedule a date with another person for next week.
    "You have a dinner date planned with [the_person.title]."
    menu:
        "Get ready for the date {image=gui/heart/Time_Advance.png}" if mc.business.funds >= 50:
            pass

        "Get ready for the date\n{color=#ff0000}{size=18}Requires: $30{/size}{/color} (disabled)" if mc.business.funds < 50:
            pass

        "Cancel the date (tooltip)She won't be happy with you canceling last minute.":
            "You get your phone out and text [the_person.title]."
            mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
            $ the_person.change_love(-5)
            $ the_person.change_happiness(-5)
            the_person.char "I hope everything is okay. Maybe we can do this some other time then."
            return

    $ mc.change_location(downtown)
    $ downtown.show_background()
    "You get yourself looking as presentable as possible and head downtown."
    $ the_person.draw_person(emotion = "happy")
    "You meet up with [the_person.title] on time."
    the_person.char "So, where are we going tonight [the_person.mc_title]?"
    menu:
        "A cheap restaurant\n{color=#ff0000}{size=18}Costs: $50{/size}{/color}":
            $ mc.business.funds += -50
            the_person.char "It sounds cozy. Let's go, I'm starving!"

        "A moderately priced restaurant\n{color=#ff0000}{size=18}Costs: $100{/size}{/color}" if mc.business.funds >= 100:
            $ mc.business.funds += -100
            $ the_person.change_love(5)
            $ the_person.change_happiness(5)
            the_person.char "It sounds nice. Come on, I'm starving and could use a drink."

        "An expensive restaurant\n{color=#ff0000}{size=18}Costs: $300{/size}{/color}" if mc.business.funds >= 300:
            $ mc.business.funds += -300
            $ the_person.change_love(10)
            $ the_person.change_happiness(5)
            the_person.char "Oh, it sounds fancy! Well, I'm flattered [the_person.mc_title]."

        "A moderately priced restaurant\n{color=#ff0000}{size=18}Requires: $100{/size}{/color} (disabled)" if mc.business.funds <= 100:
            pass

        "An expensive restaurant\n{color=#ff0000}{size=18}Requires: $300{/size}{/color} (disabled)" if mc.business.funds < 300:
            pass

    $ the_person.draw_person(emotion = "happy", position = "sitting")
    if sister_role in the_person.special_role or mother_role in the_person.special_role:
        if the_person.sluttiness >= 20:
            "You and [the_person.possessive_title] get to the restaurant and order your meals. She chats and flirts with you freely, as if forgetting you were related."
        else:
            "You and [the_person.possessive_title] get to the restaurant and order your meals."
            "She chats and laughs with you the whole night, but never seems to consider this more than a friendly family dinner."

    else:
        "You and [the_person.possessive_title] get to the restaurant and order your meals. You chat, flirt, and have a wonderful evening."

    if renpy.random.randint(0,100) < 40: #Chance to give her some serum.
        "After dinner you decide to order dessert. [the_person.title] asks for a piece of cheese cake, then stands up from the table."
        the_person.char "I'm going to go find the little girls room. I'll be back in a moment."
        $ clear_scene()
        "She heads off, leaving you alone at the table with her half finished glass of wine."
        menu:
            "Add a dose of serum to her drink" if mc.inventory.get_any_serum_count()>0:
                call give_serum(the_person) from _call_give_serum_21
                if _return:
                    "You pour a dose of serum into her wine and give it a quick swirl, then sit back and relax."
                    "[the_person.possessive_title] returns just as your dessert arrives."
                else:
                    "You sit back and relax, content to just enjoy the evening. [the_person.possessive_title] returns just as your dessert arrives."

            "Add a dose of serum to her drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
                pass

            "Leave her drink alone":
                "You sit back and relax, content to just enjoy the evening. [the_person.possessive_title] returns just as your dessert arrives."

        $ the_person.draw_person(position = "sitting")
        the_person.char "Ah, perfect timing!"
        "She sips her wine, then takes an eager bite of her cheesecake. She closes her eyes and moans dramatically."
        the_person.char "Mmm, so good!"
    $ the_person.change_love(mc.charisma)
    $ the_person.change_happiness(mc.charisma)
    if sister_role in the_person.special_role or mother_role in the_person.special_role:
        "At the end of the night you pay the bill and leave with [the_person.title]. The two of you travel home together."
        if renpy.random.randint(0,100) < the_person.sluttiness + the_person.love + (mc.charisma * 10): #She invites you back to her place.
            $ the_person.call_dialogue("date_seduction")
            menu:
                "Go to [the_person.title]'s room":
                    mc.name "I think I would. Lead the way."
                    $ mc.change_location(the_person.home)
                    $ mc.location.show_background()
                    "[the_person.possessive_title] leads you into her room and closes the door behind you."
                    $ the_person.add_situational_slut("Romanced",25,"What a wonderful date!")
                    call fuck_person(the_person, private = True) from _call_fuck_person_16
                    $ the_person.clear_situational_slut("Romanced")

                    #TODO: add support for spending the night somewhere other than home.
                    "When you and [the_person.possessive_title] are finished you slip back to your own bedroom just down the hall."

                "Call it a night":
                    mc.name "I think we should just call it a night now. I've got to get up early tomorrow."
                    "She lets go of your hand and looks away."
                    the_person.char "Right, of course. I wasn't saying we should... I was just... Goodnight [the_person.mc_title]."
                    "She hurries off to her room."
        else:
            the_person.char "I had a great night [the_person.mc_title]. We should get out of the house and spend time together more often."
            mc.name "I think so too. Goodnight [the_person.title]."

    else:
        "At the end of the night you pay the bill and leave with [the_person.title]. You wait with her while she calls for a taxi."
        if renpy.random.randint(0,100) < the_person.sluttiness + the_person.love + (mc.charisma * 10): #She invites you back to her place.
            $ the_person.call_dialogue("date_seduction") #She invites you back to her place to "spend some more time together". She's been seduced.
            menu:
                "Go to [the_person.title]'s place":
                    mc.name "That sounds like a great idea."
                    $ mc.change_location(the_person.home)
                    $ mc.location.show_background()
                    if not the_person.home in mc.known_home_locations + [lily_bedroom, mom_bedroom, aunt_bedroom, cousin_bedroom]:
                        $ mc.known_home_locations.append(the_person.home) #You know where she lives and can visit her.
                    "You join [the_person.possessive_title] when her taxi arrives. It's not a far ride to her house, and she invites you in."
                    "She pours you a drink and gives you a tour. When the tour ends in her bedroom you aren't surprised."

                    $ the_person.add_situational_slut("Romanced",25,"What a wonderful date!")
                    call fuck_person(the_person, private = True) from _call_fuck_person_17
                    $ the_person.clear_situational_slut("Romanced")

                    #TODO: add support for spending the night somewhere other than home.
                    "When you and [the_person.title] are finished you get dressed and say goodnight."
                    $ mc.change_location(bedroom)

                "Call it a night":
                    mc.name "I'd like to call it an early night today, but maybe I'll take you up on the offer some other time."
                    "Her taxi arrives. You give her a goodbye kiss and head home yourself."

        else: #She says goodnight to you here.
            the_person.char "I had a great night [the_person.mc_title], you're a lot of fun to be around. We should do this again."
            mc.name "It would be my pleasure."
            "[the_person.title]'s taxi arrives and she gives you a kiss goodbye. You watch her drive away, then head home yourself."

    $ clear_scene()
    return "Advance Time"

label serum_give_label(the_person):
    $ sneak_serum_chance = 70 + (mc.int*5) - (the_person.focus*5)  #% chance that you will successfully give serum to someone sneakily. Less focused people are easier to fool.
    $ ask_serum_chance = 10*mc.charisma + 5*the_person.int #The more charismatic you are and the more intellectually curious they are the better the chance of success
    $ demand_serum_chance = mc.charisma * (the_person.obedience - 90) #The more charismatic you are and the more obedient they are the more likely this is to succeed.

    if sneak_serum_chance < 0:
        $ sneak_serum_chance = 0
    elif sneak_serum_chance > 100:
        $ sneak_serum_chance = 100

    if ask_serum_chance < 0:
        $ ask_serum_chance = 0
    elif ask_serum_chance > 100:
        $ ask_serum_chance = 100

    if mc.business.get_employee_title(the_person) == "None":
        $demand_serum_chance += -35 #if she doesn't work for you there is a much lower chance she will listen to your demand (unless you are very charismatic or she is highly obedient.)
    if demand_serum_chance < 0:
        $ demand_serum_chance = 0
    elif demand_serum_chance > 100:
        $ demand_serum_chance = 100

    $ pay_serum_cost = the_person.salary * 5
    $ ran_num = renpy.random.randint(0,100)

    menu:
        "Give it to her stealthily\n{color=#ff0000}{size=18}Success Chance: [sneak_serum_chance]%%{/size}{/color}": #TODO: Have this modified by something so there are interesting gameplay decisions
            "You chat with [the_person.title] for a couple of minutes. Waiting to find a chance to deliver a dose of serum."
            if ran_num < sneak_serum_chance:
                #Success
                "You're able to distract [the_person.title] and have a chance to give her a dose of serum."
                call give_serum(the_person) from _call_give_serum

            else:
                #Caught!
                "You finally distract [the_person.title] and have a chance to give her a dose of serum."
                the_person.char "Hey, what's that?"
                "You nearly jump as [the_person.title] points down at the small vial of serum you have clutched in your hand."
                $ ran_num = renpy.random.randint(0,10)
                if ran_num < mc.charisma:
                    if mc.business.get_employee_title(the_person) == "None":
                        mc.name "This? Oh, it's just something we're working on at the lab that I thought you might be interested in."
                        "You dive into a technical description of your work, hoping to distract [the_person.title] from your real intentions."

                    else:
                        mc.name "This? Oh, it's just one of the serums I grabbed from production for quality control. I was just fidgeting with it I guess."
                        "You make small talk with [the_person.title], hoping to distract her from your real intentions."
                    "After a few minutes you've managed to avoid her suspicion, but haven't been able to deliver the dose of serum."

                else:
                    mc.name "This? Uh..."
                    $ the_person.draw_person(emotion="angry")
                    $ the_person.change_obedience(-10)
                    $ the_person.change_happiness(-10)
                    $ the_person.change_love(-5)
                    the_person.char "Were you about to put that in my drink? Oh my god [the_person.mc_title]!"
                    mc.name "Me? Never!"
                    "[the_person.title] shakes her head and storms off. You can only hope this doesn't turn into something more serious."
                    $ clear_scene()
                    return

        "Ask her to take it\n{color=#ff0000}{size=18}Success Chance: [ask_serum_chance]%%{/size}{/color}" if not mandatory_unpaid_serum_testing_policy.is_active() or mc.business.get_employee_title(the_person) == "None":
            if mc.business.get_employee_title(the_person) == "None":
                mc.name "[the_person.title], I've got a project going on at work that could really use a test subject. Would you be interested in helping me out?"

            else:
                mc.name "[the_person.title], there's a serum design that is in need of a test subject. Would you be interested in helping out with a quick field study?"

            if ran_num < ask_serum_chance:
                #Success
                if mc.business.get_employee_title(the_person) == "None":
                    if the_person.personality.personality_type_prefix == "nora":
                        the_person.char "I'd be happy to help. I've seen your work, I have complete confidence you've tested this design thoroughly."
                    else:
                        the_person.char "I'd be happy to help, as long as you promise it's not dangerous of course. I've always wanted to be a proper scientist!"
                else:
                    the_person.char "I'll admit I'm curious what it would do to me. Okay, as long as it's already passed the safety test requirements, of course."
                mc.name "It's completely safe, we just need to test what the results from it will be. Thank you."
                call give_serum(the_person) from _call_give_serum_2

            else:
                #Denies
                $ the_person.change_obedience(-2)
                the_person.char "I'm... I don't think I would be comfortable with that. Is that okay?"
                mc.name "Of course it is, that's why I'm asking in the first place."

        "Ask her to take it\n{color=#ff0000}{size=18}Success Chance: Required by Policy{/size}{/color}" if mandatory_unpaid_serum_testing_policy.is_active() and not mc.business.get_employee_title(the_person) == "None":
            #Auto success
            mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this."
            call give_serum(the_person) from _call_give_serum_3

        "Demand she takes it\n{color=#ff0000}{size=18}Success Chance: [demand_serum_chance]%%{/size}{/color}": #They must work for you to demand it.
            mc.name "[the_person.title], you're going to drink this for me."
            "You pull out a vial of serum and present it to [the_person.title]."
            the_person.char "What is it for, is it important?"
            mc.name "Of course it is, I wouldn't ask you to if it wasn't."
            if ran_num < demand_serum_chance:
                #Success
                the_person.char "Okay, if that's what you need me to do..."
                call give_serum(the_person) from _call_give_serum_4
            else:
                #Refuse
                $ the_person.draw_person(emotion = "angry")
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(-2)
                $ the_person.change_love(-2)
                the_person.char "You expect me to just drink random shit you hand to me? I'm sorry, but that's just ridiculous."

        "Pay her to take it\n{color=#ff0000}{size=18}Costs: $[pay_serum_cost]{/size}{/color}" if mandatory_paid_serum_testing_policy.is_active() and not mandatory_unpaid_serum_testing_policy.is_active() and not mc.business.get_employee_title(the_person) == "None": #This becomes redundent when they take it for free.
            #Pay cost and proceed
            $ mc.business.funds += -pay_serum_cost
            mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this, a bonus will be added onto your paycheck."
            call give_serum(the_person) from _call_give_serum_5


        "Pay her to take it\n{color=#ff0000}{size=18}Requires: Mandatory Paid Serum Testing{/size}{/color} (disabled)" if not mandatory_unpaid_serum_testing_policy.is_active() and not mandatory_paid_serum_testing_policy.is_active() and not mc.business.get_employee_title(the_person) == "None":
            pass

        "Do nothing":
            pass
    return

label grope_person(the_person):
    # Note: the descriptors of the actual stages are stored in grope_descriptions.rpy to keep things organized.
    $ mc.change_energy(-5)
    #TODO: Have arousal be more permanent than it is right now. ie. more events should impact it.
    call grope_shoulder(the_person) from _call_grope_shoulder
    if _return:
        call grope_waist(the_person) from _call_grope_waist
        if _return:
            call grope_ass(the_person) from _call_grope_ass
            if _return:
                call grope_tits(the_person) from _call_grope_tits
                if _return:
                    $ should_be_private = True
                    if mc.location.get_person_count() > 1: #We aren't alone and should ask if we want to find somewhere private
                        $ extra_people_count = mc.location.get_person_count() - 1
                        $ the_person.discover_opinion("public sex")
                        if the_person.effective_sluttiness("touching_body") < 40 or the_person.get_opinion_score("public sex") < 0:
                            # She's nervous about it and asks to go somewhere private.
                            the_person.char "Wait, wait..."
                            "[the_person.possessive_title] glances around at the people nearby."
                            the_person.char "I don't want other people to watch. Let's find someplace we can be alone."
                            menu:
                                "Find somewhere quiet\n{color=#ff0000}{size=18}No interruptions{/size}{/color}":
                                    mc.name "Alright, come with me."
                                    "You take [the_person.title] by her wrist and lead her away."
                                    #TODO: have each location have a unique "find someplace quiet" descriptor with a default fallback option
                                    "After a couple of minutes searching you find a quiet space with just the two of you."
                                    "You don't waste any time getting back to what you were doing, fondling [the_person.possessive_title]'s tits and ass."

                                "Stay where you are\n{color=#ff0000}{size=18}[extra_people_count] watching{/size}{/color}":
                                    $ should_be_private = False

                        else:
                            # She doesn't care, but you can find someplace private.
                            "[the_person.possessive_title] either doesn't notice or doesn't care, but there are other people around."
                            menu:
                                "Find somewhere quiet\n{color=#ff0000}{size=18}No interruptions{/size}{/color}":
                                    mc.name "Come with me, I don't want to be interrupted."
                                    "You take [the_person.title] by the wrist and lead her away. She follows eagerly."
                                    "After searching for a couple of minutes you find a quiet space with just the two of you."
                                    #TODO: have each location have a unique "find someplace quiet" descriptor with a default fallback option

                                "Stay where you are\n{color=#ff0000}{size=18}[extra_people_count] watching{/size}{/color}":
                                    $ should_be_private = False

                    if prostitute_role in the_person.special_role:
                        the_person.char "We can continue what you started, but it would cost you two hundred dollars."
                        menu:
                            "Pay her\n{color=#ff0000}{size=18}Costs: $200{/size}{/color}" if mc.business.funds > 200:
                                $ mc.business.funds += -200
                                $ the_person.change_obedience(1)
                                call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_grope_person_prostitute_role
                            "Pay her\n{color=#ff0000}{size=18}Requires: $200{/size}{/color} (disabled)" if mc.business.funds <= 200:
                                pass                                
                            "No":
                                mc.name "Thanks for the offer, but no thanks."
                                "She shrugs."
                                the_person.char "Your loss."
                    else:
                        call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_43 # Enter the sex system, starting from this point.
                    $ the_person.review_outfit()
    return

init -2 python:
    def build_command_person_actions_menu(the_person):
        change_titles_action = Action("Change how we refer to each other", requirement = change_titles_requirement, effect = "change_titles_person", args = the_person, requirement_args = the_person,
            menu_tooltip = "Manage how you refer to " + the_person.title + " and tell her how she should refer to you. Different combinations of stats, roles, and personalities unlock different titles.", priority = -5)

        wardrobe_change_action = Action("Change your wardrobe", requirement = wardrobe_change_requirment, effect = "wardrobe_change_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Add and remove outfits from " + the_person.title + "'s wardrobe, or ask her to put on a specific outfit.", priority = -5)

        serum_demand_action = Action("Drink a dose of serum for me", requirement = serum_demand_requirement, effect = "serum_demand_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Demand " + the_person.title + " drinks a dose of serum right now. Easier to command employees to test serum.", priority = -5)

        strip_demand_action = Action("Strip for me", requirement = demand_strip_requirement, effect = "demand_strip_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Command her to strip off some of her clothing.", priority = -5)

        touch_demand_action = Action("Let me touch you   {color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}", requirement = demand_touch_requirement, effect = "demand_touch_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Demand " + the_person.title + " stays still and lets you touch her. Going too far may damage your relationship.", priority = -5)

        bc_demand_action = Action("Talk about birth control", requirement = demand_bc_requirement, effect = "bc_demand_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Discuss " + the_person.title + "'s use of birth control.", priority = -5)

        return ["Command", change_titles_action, wardrobe_change_action, serum_demand_action, strip_demand_action, touch_demand_action, bc_demand_action, ["Never mind", "Return"]]

label command_person(the_person):
    mc.name "[the_person.title], I want you to do something for me."
    the_person.char "Yes [the_person.mc_title]?"

    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([build_command_person_actions_menu(the_person)]))
    else:
        call screen main_choice_display([build_command_person_actions_menu(the_person)])

    if _return != "Return":
        $ _return.call_action()
    return

label seduce_label(the_person):
    mc.name "[the_person.title], I've been thinking about you all day. I just can't get you out of my head."

    if prostitute_role in the_person.special_role and the_person.love < 20:
        the_person.char "I've been thinking about you too, but I've got bills to pay and I can't do this for free."
        return
    elif prostitute_role in the_person.special_role and the_person.love >= 20:
        the_person.char "I should really make you pay for this... but you're one of my favorites and I'm curious what you had in mind."
    else:
        $ the_person.call_dialogue("seduction_response")

    $ ran_num = renpy.random.randint(0,100)
    $ chance_service_her = the_person.sluttiness - 20 - (the_person.obedience - 100) + (mc.charisma * 4) + (the_person.get_opinion_score("taking control") * 4)
    $ chance_both_good = the_person.sluttiness - 10 + mc.charisma * 4
    $ chance_service_him = the_person.sluttiness - 20 + (the_person.obedience - 100) + (mc.charisma * 4) + (the_person.get_opinion_score("being submissive") * 4)

    if chance_service_her > 100:
        $ chance_service_her = 100
    elif chance_service_her < 0:
        $ chance_service_her = 0

    if chance_both_good > 100:
        $ chance_both_good = 100
    elif chance_both_good < 0:
        $ chance_both_good = 0

    if chance_service_him > 100:
        $ chance_service_him = 100
    elif chance_service_him < 0:
        $ chance_service_him = 0

    $ seduced = False #Flip to true if the approach works
    menu:
        "I want to make you feel good\n{color=#ff0000}{size=18}Success Chance: [chance_service_her]%%\nModifiers: +10 Sluttiness, -5 Obedience{/size}{/color} (tooltip)Suggest you will focus on her. She will be sluttier for the encounter, but more likely to make demands and take control. More likely to succeed with less obedient girls.": #Bonus to her sluttiness, penalty to obedience
            "You lean in close whisper what you want to do to her."
            if ran_num < chance_service_her: #Success
                $ seduced = True
                $ the_person.add_situational_slut("seduction_approach",10, "You promised to focus on me.")
                $ the_person.add_situational_obedience("seduction_approach",-5, "You promised to focus on me.")
                $ the_person.change_arousal(-5*the_person.get_opinion_score("taking control"))
                $ the_person.discover_opinion("taking control")
            else: #Failure
                pass

        "Let's have a good time\n{color=#ff0000}{size=18}Success Chance: [chance_both_good]%%\nModifiers: None{/size}{/color} (tooltip)Suggest you'll both end up satisfied. Has no extra effect on her sluttiness or obedience, but is not affected by her obedience in return.": #Standard
            "You lean in close and whisper what you want to do together."
            if ran_num < chance_both_good:
                $ seduced = True
            else:
                pass

        "I need you to get me off\n{color=#ff0000}{size=18}Success Chance: [chance_service_him]%%\nModifiers: +10 Obedience, -5 Sluttiness{/size}{/color} (tooltip)Demand that she focuses on making you cum. She will be more obedient but less slutty for the encounter. More likely to succeed with highly obedient girls.": #Bonus to obedience, penalty to sluttiness
            "You lean in close and whisper what you want her to do to you."
            if ran_num < chance_service_him:
                $ seduced = True
                $ the_person.add_situational_slut("seduction_approach",-5, "You want me to serve you.")
                $ the_person.add_situational_obedience("seduction_approach",10, "You want me to serve you.")
                $ the_person.change_arousal(5*the_person.get_opinion_score("being submissive"))
                $ the_person.discover_opinion("being submissive")
            else:
                pass



    if seduced and the_person.sexed_count < 1:

        $ extra_people_count = mc.location.get_person_count() - 1
        $ in_private = True
        if extra_people_count > 0: #We have more than one person here
            $ the_person.call_dialogue("seduction_accept_crowded")
            menu:
                "Find somewhere quiet\n{color=#ff0000}{size=18}No interruptions{/size}{/color}":
                    "You take [the_person.title] by the hand and find a quiet spot where you're unlikely to be interrupted."

                "Stay right here\n{color=#ff0000}{size=18}[extra_people_count] watching{/size}{/color}":
                    if the_person.sluttiness < 50:
                        mc.name "I think we'll be fine right here."
                        the_person.char "I... Okay, if you say so."

                    $ in_private = False
        else:
            $ the_person.call_dialogue("seduction_accept_alone")

        call fuck_person(the_person,private = in_private) from _call_fuck_person

        $ the_person.review_outfit()

        #Tidy up our situational modifiers, if any.
        $ the_person.clear_situational_slut("public_sex")
        $ the_person.clear_situational_slut("seduction_approach")
        $ the_person.clear_situational_obedience("seduction_approach")
    else:
        $ the_person.call_dialogue("seduction_refuse")
        $ the_person.clear_situational_slut("seduction_approach")
        $ the_person.clear_situational_obedience("seduction_approach")

    $ the_person.sexed_count += 1
    return

label bc_talk_label(the_person):
    # Contains the Love and Sluttiness based approaches to asking someone to stop taking birth control.
    mc.name "Can we talk about something?"
    the_person.char "Mmhm, what's that?"
    mc.name "I want to talk about your birth control."
    if girlfriend_role in the_person.special_role or affair_role in the_person.special_role:
        #She'll talk to you about it. High Love or moderate sluttiness are needed to convince her to stop taking BC. Easier to convince her to start.
        # High influence from opinion of creampies.

        $ needed_start = 30 + (15 * the_person.get_opinion_score("creampies"))
        $ needed_stop = 45 - (15 * the_person.get_opinion_score("creampies"))
        if affair_role in the_person.special_role:
            $ needed_stop += -10*the_person.get_opinion_score("cheating on men") #They think it's hot to have another man's baby

        if the_person.on_birth_control:
            if the_person.get_opinion_score("creampies") > 0: #She's not happy about it
                the_person.char "Oh, sure. I'm taking it right now, so if you get a little too excited and unload inside me..."
                "She smiles and shrugs."
                the_person.char "Well that wouldn't be the end of the world."
            else:
                the_person.char "Oh, sure. I'm taking it right now, so we shouldn't have any \"accidents\" to worry about."
        else:
            if the_person.get_opinion_score("creampies") > 0: #She's happy about not being on BC
                the_person.char "I'm not taking any right now, so..."
                "She smiles and shrugs."
                the_person.char "If you cum in me you might get me knocked up. It's kind of hot to think about that..."
            else:
                the_person.char "Oh, well... I'm not taking any right now."
        menu:
            "Start taking birth control" if not the_person.on_birth_control:
                mc.name "You should start taking some, I don't want you getting pregnant."
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start:
                    "She thinks about it for a moment, then nods."
                    if the_person.has_taboo("condomless_sex"):
                        the_person.char "It would be nice to not have to worry about a condom breaking when he have sex."
                        the_person.char "Okay, I'll talk to my doctor and start taking it as soon as possible."
                    else:
                        the_person.char "If we keep doing it raw that's a smart idea."
                        the_person.char "I'll talk to my doctor and start taking it as soon as possible."
                    the_person.char "I should be able to start tomorrow, we will still need to careful until then."
                    $ manage_bc(the_person, start = True)

                else:
                    "She shakes her head."
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "I don't care about that. I love the thrill of a hot load of cum inside my perfectly fertile pussy."
                        the_person.char "There's nothing hotter than that. You're just going to have to accept that it's a risk."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person.char "I'm sorry [the_person.mc_title], but I've tried it before and it plays hell with my hormones."
                        the_person.char "We can just use a condom, or do something else to have fun together."

            "Stop taking birth control" if the_person.on_birth_control:
                mc.name "I want you to stop taking it."
                if the_person.love >= needed_stop or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Yeah? I've wanted to stop too, I don't care if it's risky."
                        the_person.char "There's nothing that's more of a turn on than having a hot load inside of my pussy. Ah..."
                        "[the_person.possessive_title] sighs and seems lost in thought for a moment."
                        the_person.char "Sorry, I'm getting distracted."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person.char "Do you think that's a good idea? What if something happened?"
                        mc.name "We can deal with that when it happens. If we don't want you to get pregnant we can always use a condom."
                        "She thinks about it for a long moment, then nods and smiles."
                        the_person.char "Okay, I won't take my birth control in the morning. We'll just be careful, it'll be fine..."

                    $ manage_bc(the_person, start = False)

                else:
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "I don't think that's a good idea. If I'm on my birth control you don't need to wear a condom when we fuck."
                        the_person.char "I love feeling you raw inside me. I don't want to have to give that up."
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person.char "I don't think that's a good idea. What if something happened? Are we ready for that change in our lives?"
                        the_person.char "Maybe one day, but I'm not comfortable with it right now."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check on that."

    elif the_person.effective_sluttiness() > 40:
        $ needed_start = 40 + (15 * the_person.get_opinion_score("creampies"))
        $ needed_stop = 75 - (15 * the_person.get_opinion_score("creampies"))

        if the_person.on_birth_control:
            if the_person.get_opinion_score("bareback sex") > 0:
                the_person.char "Oh, is that all? Yeah, I'm on birth control right now because I hate how condoms feel."
                $ the_person.discover_opinion("bareback sex")
            else:
                the_person.char "Oh, is that all? Yeah, I'm on birth control right now so I don't have to worry about getting pregnant."
        else:
            the_person.char "Oh, I guess that's probably an important thing for you to know about."
            the_person.char "I'm not taking any birth control right now."
        menu:
            "Start taking birth control" if not the_person.on_birth_control:
                mc.name "You should probably start taking it, before something happens and you get pregnant."
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start:
                    the_person.char "That's probably a good idea. I'll talk talk to my doctor as soon as possible about it."
                    $ manage_bc(the_person, start = True)
                else:
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        "She shrugs and shakes her head."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person.char "I don't care about that. I love the feeling of a warm, risky creampie to ever give it up."
                    else:
                        the_person.char "Sorry, I've tried it before and it just messes with my hormones too badly."
                        the_person.char "We'll just be careful and use a condom, or you can pull out. Okay?"

            "Stop taking birth control" if the_person.on_birth_control:
                mc.name "You should stop taking it. Wouldn't that be really hot?"
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Do you think so? I've always wanted to, I don't think I can trust myself to tell a man to pull out."
                        the_person.char "Even if I know that's the smart thing to do I would probably just beg for a hot load inside me..."
                        "She closes her eyes and moans softly, obviously lost in a fantasy of her own making."
                        "After a moment she shakes her head and focuses again."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person.char "Sorry... I guess if you think it's a good idea I can give it a try. What's the worst that can happen..."
                    else:
                        the_person.char "Do you really think so? I mean, it sounds kind of hot but I would have to trust you to pull out, or have you wear a condom."
                        mc.name "Then that's what I'll do. I just think it's so much sexier to know there's a little bit of risk."
                        "[the_person.possessive_title] thinks about it for a long moment. Finally she shrugs and nods."
                        the_person.char "Okay, we can give it a try. We'll just need to be very careful."
                    $ manage_bc(the_person, start = False)
                else:
                    "[the_person.possessive_title] shakes her head."
                    the_person.char "That would be crazy! There's no way I could gamble the rest of my life on some guy pulling out or me getting lucky."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check."
    else:
        if the_person.love > 30:
            # She loves you enough to tell you her status
            the_person.char "Well that's kind of private, but if it really matters to you I guess I can tell you."
            if the_person.on_birth_control:
                the_person.char "I'm not looking to get pregnant right now, so I'm taking birth control."
            else:
                the_person.char "I'm not taking any birth control right now."

            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        elif the_person.effective_sluttiness() > 20:
            the_person.char "Oh, I guess I can tell you if you're really curious."
            if the_person.on_birth_control:
                the_person.char "I'm taking birth control right now. I don't want to worry about getting pregnant by accident."
            else:
                the_person.char "I'm not taking birth control right now."

            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        else:
            the_person.char "That's a pretty personal question. Let's get to know each other a little more before we talk about that, okay?"
    return

label bc_demand_label(the_person):
    # Contains the obedience based approach to asking someone to stop taking birth control.
    # This event can have a moderately low Obedience requirement, with higher requirements to actually make changes.
    mc.name "Tell me about your birth control."
    if the_person.on_birth_control:
        the_person.char "I'm taking birth control right now."
    else:
        the_person.char "I'm... not taking any right now."

    menu:
        "Start taking birth control" if not the_person.on_birth_control and the_person.obedience >= 130:
            mc.name "I want you to start taking some. I don't want you getting pregnant."
            "[the_person.possessive_title] nods."
            the_person.char "Okay, I can do that. I'll talk to my doctor, I think I'll be able to start it tomorrow."
            mc.name "Good."
            $ manage_bc(the_person, start = True)

        "Start taking birth control\n{color=#FF0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if not the_person.on_birth_control and the_person.obedience < 130:
            pass

        "Stop taking birth control" if the_person.on_birth_control and the_person.obedience >= 160:
            mc.name "I want you to stop taking it."
            $ complains_threshold = 45 - (15 * the_person.get_opinion_score("creampies"))
            if the_person.effective_sluttiness() >= complains_threshold:
                # She's slutty enough that it's not even a concern.
                "[the_person.possessive_title] nods obediently."
                the_person.char "Okay, I'll stop right away."
            elif the_person.is_family():
                "[the_person.possessive_title] shuffles nervously before working up the nerve to speak back."
                the_person.char "[the_person.mc_title], I can't do that. If you got me pregnant I... I don't know what I would do!"
                mc.name "I didn't say I was going to get you pregnant. I just told you to stop taking your birth control."
                mc.name "I'm sure you can avoid getting knocked up if you really put your mind to it. Now, do we have a problem?"
                "[the_person.title] start to say something, then thinks better of it. She shakes her head."
                the_person.char "No, there's no problem. I won't take any birth control in the morning."

            else:
                "[the_person.possessive_title] shuffles nervously before working up the nerve to speak back."
                the_person.char "I... I don't know if that's a good idea. I don't now if I want to get pregnant."
                mc.name "I didn't ask if you wanted to get pregnant. I told you to stop taking your birth control. Is there a problem with that?"
                "She blushes and looks away under your glare."
                the_person.char "No. I'll stop right away. Sorry."

            $ manage_bc(the_person, start = False)

        "Stop taking birth control\n{color=#FF0000}{size=18}Requires: 160 Obedience{/size}{/color} (disabled)" if  the_person.on_birth_control and the_person.obedience < 160:
            pass

        "That's all I wanted to know":
            the_person.char "Good. That's all I wanted to know."
    return

init 5 python:
    def manage_bc(person, start):
        if start:
            event_label = "bc_start_event"
        else:
            event_label = "bc_stop_event"

        bc_start_action = Action("Change birth control", always_true_requirement, event_label, args = person)
        mc.business.mandatory_morning_crises_list.append(bc_start_action) # She starts or stops the next morning.
        return

label bc_start_event(the_person):
    $ the_person.on_birth_control = True
    return

label bc_stop_event(the_person):
    $ the_person.on_birth_control = False
    return
