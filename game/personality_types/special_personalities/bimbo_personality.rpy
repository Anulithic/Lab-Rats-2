### PERSONALITY CHARACTERISTICS ###
init 1300:
    python:
        def bimbo_titles(the_person):
            return the_person.name
        def bimbo_possessive_titles(the_person):
            return bimbo_titles(the_person)
        def bimbo_player_titles(the_person):
            valid_titles = [mc.name]
            valid_titles.append("Cutie")
            return valid_titles
        bimbo_personality = Personality("bimbo", #Currently used in the head researcher event line.
        common_likes = ["skirts", "small talk", "the colour pink", "makeup", "pop"],
        common_sexy_likes = ["giving blowjobs", "missionary style sex", "being submissive", "skimpy outfits", "showing her tits", "showing her ass", "not wearing anything", "not wearing underwear", "lingerie", "cum facials"],
        common_dislikes = ["working", "research work", "work uniforms", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = bimbo_titles, possessive_titles_function = bimbo_possessive_titles, player_titles_function = bimbo_player_titles)

### DIALOGUE ###
label bimbo_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around at you. She doesn't hide the way she looks your body up and down."
    $ the_person.set_title("???")
    the_person.char "Oh you're cute! Okay, cutie, what do you need?"
    mc.name "I just wanted to get your name. I saw you walking past and..."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    if the_person.has_large_tits():
        the_person.char "And you liked my titss? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    else:
        the_person.char "And you liked my ass? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    #the_person.char "Well then, I suppose I shouldn't disappoint you. You can call me [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    the_person.char "So what's your name?"
    return

label bimbo_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Oh, my, god... What do you want? Do I look like I want to be talking to you?"
    elif the_person.happiness < 90:
        the_person.char "Hi [the_person.mc_title]..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hey there [the_person.mc_title]. I mean sir! Hey there, sir!"
            else:
                the_person.char "Hey [the_person.mc_title], what are you doing here? Can I help with anything? Anything at all?"
        else:
            if the_person.obedience > 130:
                the_person.char "Hi there [the_person.mc_title], what can I do for you?"
            else:
                the_person.char "Hi there [the_person.mc_title]!"
    return

label bimbo_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know just how to touch me [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly while you touch her."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Do you like touching me [the_person.mc_title]? I know I like it when you do!"
        else:
            the_person.char "Do you like touching me [the_person.mc_title]? You seem to know exactly what to do."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! That feels really nice!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char " Mmm, you're driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better you feel when you touch me!"
                the_person.char "Make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, I might cum if you keep touching me like that!"
    return

label bimbo_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Aww, you always know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Does my pussy taste good [the_person.mc_title]? I'll repay the favour suck your cock later!"
        else:
            the_person.char "That, like, feels so good [the_person.mc_title]!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Ah! Hehe, that's feels so good!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char "Oh wow! Mmmm, you're tongue is, like, driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum with your mouth! Make me cum, please!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better you make me feel!"
                the_person.char "He never licks my pussy though, so make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep licking my pussy like that!"
    return

label bimbo_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Is your cock always this big, or are you just happy to see me? Hehe!"
        else:
            the_person.char "Am I your dirty girl [the_person.mc_title]? Because I'm having so much fun right now!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! Keep fucking me!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char "Oh wow! Mmmm, your cock is driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better your cock feels!"
                the_person.char "Oh well, I just want to cum! Make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, you... You might make me cum if you keep going!"
    return

label bimbo_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "I can, like, feel every single inch of you in me! You're so big!"
        else:
            the_person.char "You're, like, {i}huge{/i} inside of me! I don't know if I can do this for very long!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Fuck my ass [the_person.mc_title], fuck me until it's raw and you're done with me!"
        else:
            the_person.char "Oh, it feels like you're stirring up my insides with your dick! Ah!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I'm so stretched out, I think I'm starting to get the hang of this!"
            "She giggles happily, clearly proud of her accomplishment."
        else:
            the_person.char "My mind is going blank, all I can think about is your cock inside of me!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! Fuck my ass and make me cum [the_person.mc_title]! Do it!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew I was letting you anal me."
                the_person.char "He's been begging for it for {i}months{/i}, but I just know he wouldn't feel nearly as good inside me as you do!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep fucking my ass! Please make me cum!"
    return

label bimbo_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh god, I'm going to cum! All I want to do is cum [the_person.mc_title], ah!"
        "She squeals with pleasure and excitement."
    else:
        the_person.char "Oh my god, this feeling. I'm... I'm... cumming!"

    return

label bimbo_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god, make me cum [the_person.mc_title]! My mind is going blank, I just need to cum!"
    else:
        the_person.char "That feels, like, {i}so good{/i}!"
        "She closes her eyes and squeals with pleasure."
    return

label bimbo_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god I'm going to cum! Ahh, make me cum [the_person.mc_title], it's all I want right now!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Yes, yes, yes! Make me cum! Make me cum hard!"
    return

label bimbo_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh my god! I'm going to cum with your cock up my ass!"
        "She squeals loudly."
    else:
        the_person.char "Oh my god! I'm such a slut, I'm about to cum! Oh fuck!"

    return

label bimbo_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "Oh that's cute! You have such a good sense of style [the_person.mc_title], this is just what I like to wear!"
    else:
        the_person.char "It's so cute! I love getting new clothes - you should see my closet at home, there's no such thing as too many shoes, right?"
    return

label bimbo_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Uh... I don't think I'm allowed to wear that. I really wish I could though, just for you!"
    else:
        if the_person.sluttiness > 60:
            the_person.char "That's not really an outfit, is it? I like something a little cuter - some heels, add a dash of pink, and a top to show off my tits!"
            "[the_person.title] looks the outfit over again for a momnt and shakes her head."
            the_person.char "Yeah, this just isn't going to do it. Thanks for the thought though!"
        else:
            the_person.char "Aww, I don't think I could ever wear something like that! I wish I could though, could you imagine the looks I would get? It would be. So. Hot."
    return

label bimbo_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Hehe, you really made a mess of me. I should go get tidied up, I'm supposed to be a proper lady here!"
    else:
        if the_person.sluttiness > 40:
            "[the_person.title] looks down at herself and giggles."
            the_person.char "Hehe, I'm all messed up after that! I need to go sort this out, this outfit just doesn't work right now!"
        else:
            the_person.char "Oh darn, my outfit's all confuzzled! I'm going to go fix this up, I'll be back before you know it!"
    return

label bimbo_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 130:
        the_person.char "Don't you think I look cuter wearing my [the_clothing.display_name]? I want to leave it on!"
    elif the_person.obedience < 70:
        the_person.char "Oh no-no-no, I'm going to decide when that comes off. I want to see you work for it!"
    else:
        "[the_person.title] giggles and bats your hand away playfully."
        the_person.char "Not yet, there's so much fun stuff we have to do first before you get me out of my [the_clothing.display_name]!"
    return

label bimbo_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] giggles as you start to slide her [the_clothing.display_name] out of the way."
    if the_person.obedience > 130:
        the_person.char "Hehe, hey! Were you really going to take off my [the_clothing.display_name]? You're so dirty [the_person.mc_title]!"
    else:
        the_person.char "Hey, maybe we should, like, slow down."
    return

label bimbo_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Oh my god [the_person.title], you can't touch me like this."
        "She takes a step back and giggles."
        the_person "I'm flattered, but I don't think it's okay..."
        "You pull your hand back and laugh along with her, diffusing the tension."
        mc.name "Of course, forget I did anything."
    else: #Fail point for touching waist
        the_person "Hey... I don't think you should be touching me like that..."
        "She giggles to herself."
        the_person "It's kind of fun, but I know where this is going."
        "You give her a last squeeze and pull your hand back."
        mc.name "Yeah, of course. Maybe I'll be able to convince you."
        the_person "Hehe, we'll see..."
    return

label bimbo_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "Oh yeah, that's one of my favourite things to do! Come on, let's do it!"
        else:
            the_person.char "Yeah, let's do it! You're so cute when you're horny, did you know that?"
    else:
        the_person.char "Oh? Oh! Yeah, lets do that!"
    return

label bimbo_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Wow that's a... does that even work? I thought... well I guess I should try it before I knock it!"
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what you want, boss man, that's what you'll get!"
        else:
            the_person.char "You bring out the worst in me, you know that [the_person.mc_title]? I was a nice, respectable girl before you showed up!"
    return

label bimbo_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "No, no, no, not yet. I want you to make me wait for it a little bit, get me really begging for it."
    else:
        the_person.char "Uh, I don't think that sounds fun. Let's do something else. Come on, you pick!"
    return

label bimbo_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "What? I have a [so_title], and he treats me so much better than you could EVER hope to. Understood?"
        "She rolls her eyes dramatically and walks away."
        the_person.char "Perv."
    elif the_person.sluttiness < 20:
        the_person.char "Uh, what the ACTUAL FUCK?! What do you think you're doing? Just saying that must be... illegal, or something!"
        "[the_person.title] glares at you you and walks away."
    else:
        the_person.char "Eew! No, no, no! I will NEVER do that with ANYONE! Eew!"
        "[the_person.title] shakes her head and walks away."
    return

label bimbo_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh yay, I know how to deal with this! You just relax and I'll make you feel very, very good!"
        else:
            the_person.char "All I can think about is that cute little dress I saw this morning. Oh, that's not you meant, was it..."
            "[the_person.title] giggles."
            the_person.char "Never mind, lead the way!"
    else:
        if the_person.sluttiness > 50:
            the_person.char "Yay! I was getting so horny that I was ready to jump you in the hall!"
        elif the_person.sluttiness > 10:
            the_person.char "Hehe, I thought you had the that look in your eye. I have a sixth sense, but it's for horny guys instead of ghosts!"
        else:
            the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
    return
label bimbo_seduction_accept_crowded(the_person):
    the_person.char "Yay, lets show these sluts how it is done!"
    return
label bimbo_seduction_accept_alone(the_person):
    the_person.char "Oh, I was like, I'm going to fuck him right now."
    return
label bimbo_seduction_refuse(the_person):
    the_person.char "Duh, do you think I'm just some cheap fuck, perhaps if you took me shopping..."
    return

label bimbo_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Just make it an official order and it's all yours, boss man."
        else:
            the_person.char "Hehe, thank you, you're way too nice to me!"

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "That's like, super hot to hear you say. We just can't let my [so_title] or he would flip out."
        else:
            the_person.char "Oh my god, you're so cute! My [so_title] never says things like that to me."
            "She pouts for a moment before returning to her bubbly self."

    else:
        if the_person.sluttiness > 50:
            the_person.char "You should try your luck sometimes. Maybe take me out for a drink, I get wild after I've had a few. Wild-er, I guess."
        else:
            the_person.char "Oh you, stop it! You're going to make me blush!"
    return

label bimbo_flirt_response_low(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            #She's in uniform and likes how it looks.
            the_person.char "Hehe, thanks! I love these outfits you make us wear, they're, like, so cute!"
            the_person.char "Maybe you should pick out other things for me to wear. I bet you have some good ideas!"
            mc.name "For you I certainly do. Maybe I'll talk to you later about it."
            "She smiles happily."
            the_person.char "Alright!"

        else:
            #She's in uniform, but she thinks it's a little too slutty.
            if the_person.outfit.vagina_visible():
                # Her pussy is on display.
                the_person.char "Thanks! I keep worrying I'm going to get in trouble, but then I remember I'm allowed to be dressed like this!"
                mc.name "Not just allowed: required."
                the_person.char "Yeah! This is such a crazy place to work!"
                "[the_person.possessive_title] bounces happily, unintentionally jiggling her tits."

            elif the_person.outfit.tits_visible():
                #Her tits are out
                if the_person.has_large_tits():
                    the_person.char "Hehe, thanks! I really like how it shows off my big tits!"
                    "[the_person.possessive_title] bounces happily, jiggling her breasts."
                    the_person.char "People are always telling me I need to hide them, but at work I don't have to worry about that!"
                else:
                    the_person.char "Hehe, thanks! I really like how I it shows off my boobs!"
                    "[the_person.possessive_title] looks down at her own chests and pouts."
                    the_person.char "I wish they were bigger though. Oh well!"

            elif the_person.outfit.underwear_visible():
                # Her underwear is visible.
                the_person.char "Hehe, thank you! I know it's a little slutty, but I like how little these outfits you make us wear cover!"
                mc.name "I certainly do too."
                "She laughs and sticks her tongue out."
                the_person.char "You're silly, you know that? But like, in a fun way."
            else:
                # It's just generally slutty.
                the_person.char "Hehe, thank you! I don't think I'm brave enough to wear something like this outside, but at work it's okay! Right?"
                mc.name "More than okay, it's required."
                the_person.char "Oh yeah, right! I'm sorry, there are so many rules here, I'm always forgetting them!"
                mc.name "Well don't worry, you're doing a great job so far."
                "[the_person.possessive_title] smiles and bounces happily."
                the_person.char "Yay!"

    else:
        #She's in her own outfit.
        the_person.char "Aw, thanks! It took me sooooo long to decide what to wear today. I picked this because it made my ass look good. What do you think?"
        $ the_person.draw_person(position = "back_peek")
        "[the_person.possessive_title] spins around and leans forward a little, wiggling her butt at you."
        mc.name "Oh yeah, I think it looks really good."
        $ the_person.draw_person()
        the_person.char "Yay!"
    return

label bimbo_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            if the_person.outfit.tits_visible():
                the_person.char "Hehe, thanks! Do you like my boobs?"
                "She puts her hands behind her back and thrusts her chest out at you, waiting for your response."
                mc.name "They look fantastic."
                "[the_person.possessive_title] smiles and giggles."
                the_person.char "Yay! I like having my boobs out at work. It feels naughty, but I'm, like, allowed to do it!"
            else:
                the_person.char "Hehe, thanks! I think you're, like, pretty hot too!"
                the_person.char "Oh my god! We should go partying together! That would be, like, so much fun!"
                mc.name "That does sound like fun. Maybe we will."
                "She nods and smiles happily."
        else:
            "[the_person.possessive_title] smiles and giggles."
            the_person.char "Hehe, thanks! I think you're pretty hot too!"
            the_person.char "Oh, we should totally go partying together! That would be, like, so much fun!"
            mc.name "That does sound like fun. Maybe we will."
            "She nods and smiles happily."
            the_person.char "I can even wear something nice for you, instead of this silly uniform you make..."
            "She stops suddenly and covers her mouth with her hand."
            the_person.char "Oops. I'm sorry, I didn't mean that. I just kind of talk without thinking sometimes." #TODO: On with the spanking! And then, the oral sex!
            mc.name "It's fine. You don't have to like your uniform as long as you're wearing it."
            "[the_person.title] puts on a stern face and nods severely."
            the_person.char "Of course, [the_person.mc_title]!"

    else:
        if the_person.effective_sluttiness() < 20 and mc.location.get_person_count() > 1:
            the_person.char "Hehe, thanks! I uh..."
            "[the_person.possessive_title] bites her lip and leans closer to you to whisper in your ear."
            the_person.char "I think you're, like, pretty hot too."
            "She pulls back and smiles playfully."

        else:
            the_person.char "Hehe, thank you! I think you're looking, like, pretty hot too."
            the_person.char "Oh, we should totally go partying some time! I can wear something even cuter for you..."
            $ the_person.draw_person(position = "back_peek")
            the_person.char "Maybe something that shows off my butt a little more... Doesn't that sound fun?"
            "[the_person.possessive_title] wiggles her hips, shaking her butt for your enjoyment."
            mc.name "That does sound like fun. Maybe we should go out one day."
            $ the_person.draw_person()
            "She turns back to you and smiles."
            the_person.char "Yay!"
    return

label bimbo_flirt_response_high(the_person):
    if mc.location.get_person_count() > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))):
        "[the_person.possessive_title] giggles and looks around nervously."
        the_person.char "Oh my god, [the_person.mc_title]! That's so naughty!"
        menu:
            "Find someplace quiet":
                mc.name "Come with me and we can do some more naughty things."
                "[the_person.title] giggles again and nods eagerly. You take her hand and lead her away."
                "When you're finally alone you put your arm around her waist and pull her close."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                else:
                    pass
                "You kiss her, and she responds by leaning her body against you eagerly."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_55

            "Just flirt":
                mc.name "Wait until I get you alone and you'll see how naughty I can get."
                the_person.char "Hehe, I'm excited to find out!"

    else: # She wants to kiss you, leading to other things.
        if mc.location.get_person_count() == 1:
            the_person.char "Oh my god, [the_person.mc_title]! you're so naughty!"
            "She giggles playfully and looks you up and down."
            the_person.char "But maybe... We could fool around, if you really want to. I think you're pretty cute."

        else:  #She's into turning you on.
            if the_person.has_large_tits(): #Bounces her tits for you
                "She giggles and grabs her own tits, jiggling them for you."
                $ the_person.draw_person(the_animation = blowjob_bob)

            else:
                "She giggles and wiggles her hips for you."
            the_person.char "Do you want to have some fun?"

        menu:
            "Kiss her":
                mc.name "Yeah, I do. Come here."
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.title]'s waist and pull her close. She giggles as she falls against your body."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You kiss her, and she rubs her body against you eagerly."
                else:
                    "You put your arm around [the_person.title]'s waist and pull her close. She leans her body against you eagerly as you kiss her."
                call fuck_person(the_person, start_position = kissing, private = mc.location.get_person_count() < 2, skip_intro = True) from _call_fuck_person_56

            "Just flirt":
                mc.name "I do, but it'll have to be some other time."
                $ the_person.draw_person(emotion = "sad")
                "She pouts and crosses her arms dramatically."
                the_person.char "Aww, why? Can't you, like, just do something with me right now?"
                mc.name "I'll make it up to you, I promise."
                "[the_person.title] sighs and nods."
                the_person.char "Okay..."
    return

label bimbo_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.get_person_count() > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("sucking_cock") < (40 - (5*the_person.get_opinion_score("public_sex"))):
            # Not very slutty, so she wants to find somewhere private
            "[the_person.possessive_title] giggles and pets your arm affectionately."
            the_person.char "Oh my god, you're such a sweetie! Hey..."
            "She takes your hand and starts trying to lead you away."
            the_person.char "Come on, let's go find somewhere we can make out."
            menu:
                "Find someplace quiet":
                    mc.name "Alright, let's go."
                    "You let [the_person.title] lead you away. After a few minutes of searching you find a private spot away from prying eyes."
                    "You put your arm around her waist, resting your hand on her ass, and kiss her passionately."
                    "[the_person.possessive_title] returns the kiss and begins to grind her hips against your thigh."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_61

                "Just flirt":
                    mc.name "I don't have time right now, but I like the enthusiasm."
                    "She pouts and nods."
                    the_person.char "Okay... Don't forget about me though, I need some attention every once in a while."

        else:
            "[the_person.possessive_title] giggles and pets your arm affectionately."
            the_person.char "Oh my god, you're such a sweetie! Do you want me to suck your cock?"
            menu:
                "Get a blowjob":
                    mc.name "Is that even a question? Of course I do!"
                    "She grins and knees down, ignoring the other people in the room."
                    "[the_person.title] unzips your pants and pulls your cock out, eagerly running her tongue along the sides."
                    the_person.char "Mmmm, so tasty!"
                    $ blowjob.current_modifier = "blowjob"
                    $ blowjob.redraw_scene(the_person)
                    "She slips you into her warm, wet mouth and sucks on the tip eagerly."
                    call fuck_person(the_person, start_position = blowjob, private = False, skip_intro = True) from _call_fuck_person_62

                "Just flirt":
                    mc.name "Thanks for the offer, but I'm a little busy at the moment."
                    "She pouts and sighs."
                    the_person.char "Awww, I was already getting exited. I get so horny when I think about having your cock in my mouth..."

    else:
        # You're alone, so she's open to fooling around.
        the_person.char "Oh my god, you're such a sweetie!"
        "She throws her arms around your neck, kissing your face eagerly."
        menu:
            "Make out":
                "You put your arms around her and pull her tight against you as you return her kisses."
                "Bit by bit they transition from energetic to sensual, and soon you have [the_person.possessive_title]'s body grinding against yours as you make out."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_63

            "Just flirt":
                "You give [the_person.possessive_title] a few quick kisses, then lean your head back to get some air."
                mc.name "Easy there, down girl."
                "She lets go of you and giggles."
                the_person.char "Sorry, I just get so excited when I'm around you. You make me feel like a whole new person!"
    return

label bimbo_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    $ so_title = SO_relationship_to_title(the_person.relationship) # "husband", "boyfriend", etc.
    if mc.location.get_person_count() > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.get_opinion_score("cheating on men") *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            the_person.char "Oh my god, you too?!"
            "[the_person.possessive_title] jumps excitedly, jiggling her tits around."
            the_person.char "Come on, let's sneak away and have fun. My [so_title] just doesn't understand what a woman like me needs."
            "She runs a hand over your chest, oblivious to anyone nearby who might be watching."
            the_person.char "But you do [the_person.mc_title]. You, like, get me."
            menu:
                "Find someplace quiet":
                    mc.name "Alright, but we can't do anything here. Follow me."
                    "She nods her head happily and follows you like a happy puppy."
                    "After a few minutes of searching you find a quiet spot away from any interruptions."
                    "When you're alone you put your arm around her waist and pull her into a deep, sensual kiss."
                    "She kisses you right back, pressing her tits against your chest and pawing at your crotch in her excitement."

                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_64

                "Just flirt":
                    mc.name "I do, but you'll have to wait a little while longer. I just don't have the time right now."
                    "She pouts and sighs."
                    the_person.char "Aww... Okay, but I really need you soon. You aren't bored of me, are you?"
                    mc.name "Of course not. Don't worry, as soon as we have the chance I'll fuck your brains out."
                    "Her mood snaps back to happy. She smiles and kisses you on the cheek."
                    the_person.char "Okay! I'm getting wet just thinking about it!"

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title] giggles and looks around nervously, as if you just told her some important secret."
            the_person.char "[the_person.mc_title], you can't, like, talk like that when people are around."
            the_person.char "If my [so_title] finds out what we're doing he'll stop paying my credit card bills."
    else:
        the_person.char "Hehe, you're so sweet [the_person.mc_title]!"
        "She wraps her arms around you and hugs you tight. When she lets go she tilts her head and smiles."
        the_person.char "So, do you want me to suck your cock then? Is that one of the things?"
        menu:
            "Get a blowjob":
                "You were expecting to need to convince her a little more, but you aren't about to complain."
                mc.name "Yeah, that sounds good."
                "She giggles and drops to her knees on the spot. You step close and she unzips your pants."
                "[the_person.possessive_title] bites her lip and stares at your hard cock when it springs out in front of her."
                "After a moment she snaps out of it and leans forward, kissing the tip and flicking her tongue along the bottom of your shaft."
                $ blowjob.current_modifier = "blowjob"
                $ blowjob.redraw_scene(the_person)
                call fuck_person(the_person, start_position = blowjob, skip_intro = True) from _call_fuck_person_65
                $ blowjob.current_modifier = None

            "Just flirt":
                mc.name "How did you guess?"
                the_person.char "Everyone likes having their cock sucked. Well, not women I guess. But all men do."
                "She starts to kneel down, but you put your arm around her waist and hold her close."
                mc.name "Well you're right, but I don't have the time right now. You'll have to wait until later, okay?"
                "She sighs and nods."
                the_person.char "Aww... Okay, I guess I can wait a little bit."
    return

label bimbo_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person.char "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label bimbo_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person.char "Bleh, I don't know if I'll ever get used to that."
    return

label bimbo_cum_pullout(the_person):
    if mc.condom:
        if the_person.wants_creampie() and the_person.get_opinion_score("creampies") > 0 and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.event_triggers_dict.get("preg_knows", False):
                the_person.char "Why are you even wearing a condom? I'm, like, already pregnant."
                the_person.char "Come on, just take it off and cum inside me again. You know I love it, right?"
                "She giggles happily."

            elif the_person.on_birth_control:
                the_person.char "Oh my god I'm, like, going to go crazy! Take the condom off so you can cum inside of me!"
                the_person.char "Please [the_person.mc_title]? I, like, want it so badly!"

            else:
                the_person.char "[the_person.mc_title], I want you to knock me up! Take off the condom and cum inside of me, okay?"
                the_person.char "I want you to make me your personal breeding slut! It would make me so happy if you knocked me up!"

            menu: #TODO: Add a varient of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom.":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                "Leave it on.":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."

        else:
            "[the_person.possessive_title] giggles happily."
            the_person.char "Hehe, I'm going to make you cum? Yay!"



    elif the_person.wants_creampie():
        if the_person.event_triggers_dict.get("preg_knows", False): #She's already knocked up, so who cares!
            the_person.char "I'm already pregnant, so just cum inside me as much as you want!"
        elif the_person.get_opinion_score("creampies") > 0:
            "[the_person.possessive_title] giggles happily."
            if the_person.on_birth_control: #She just likes creampies.
                the_person.char "Cum inside me [the_person.mc_title]! Cum inside my slutty pussy!"
            else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                the_person.char "Oh my god, yes! Cum inside me [the_person.mc_title]! Knock me up!"
        elif the_person.on_birth_control: #She's on the pill, so she's probably fine
            the_person.char "I think I took my pill this morning, so you can cum inside me!"
            $ the_person.update_birth_control_knowledge()
        else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
            the_person.char "Hehe, yay! I'm going to make you cum [the_person.mc_title]!"
    else:
        if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
            the_person.char "Hehe, yay! You shouldn't cum in me though, or I might get pregnant!"

        elif the_person.get_opinion_score("creampies") < 0:
            the_person.char "Hehe, yay! Pull out and cum all over me [the_person.mc_title]!"

        else:
            the_person.char "Hehe, yay! Should you, like, pull out just to be safe?"
    return

label bimbo_cum_condom(the_person):
    if mc.condom:
        if the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "That condom is so stretchy! I can feel how much cum you put into it and it's, like, a lot!"
        else:
            the_person.char "Mmm, your cum is so nice and hot!"
    return

label bimbo_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie():
        if the_person.event_triggers_dict.get("preg_knows", False):
            the_person.char "Mmm, I love having all of your cum in me!"
            "She sighs and giggles."
            the_person.char "I guess that's why I'm pregnant, right? I just can't say no to this!"

        elif the_person.on_birth_control:
            the_person.char "Mmm, wow you came a lot! Wait, does that mean I'm..."
            "She thinks hard for a second, then sighs and giggles."
            the_person.char "It's fine, I remembered to take my pink pill this morning!"
            $ the_person.update_birth_control_knowledge()
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] gets angry when I forget, but it's not like he fucks me much anyways."
        elif pregnant_role in the_person.special_role:
            the_person.char "Mmm, wow you really pumped it into me. But since i've already got one in the oven, that's fine."
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] can't get mad about me getting knocked up, right? He already did it."
        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person.char "Oh well, my [so_title] will just take care of it, so that doesn't matter!"
            else:
                the_person.char "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person.char "Oh well, it's worth it to feel like this!"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh, that's so hot... But wait, if I get pregnant what do I tell my [so_title]?"
                "She bites her lip and looks worried."
                the_person.char "We shouldn't do this too often. Next time you should cum somewhere else, okay? Maybe on my face?"
            else:
                the_person.char "Oh, that's so hot... But what do I do if I get pregnant?"
                "She bites her lip and looks worried."
                the_person.char "We shouldn't do this too often, okay? Next time you can cum, like, somewhere else, okay? Maybe on my face?"

    else: #She's angry
        if not the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh no, you needed to pull out! Now I might, like, get pregnant!"
                the_person.char "I don't want to tell that to my [so_title]. He would be sooo angry."
            else:
                the_person.char "Oh no, you needed to pull out! Now I might, like, get pregnant!"
                the_person.char "I guess it's too late now. Oh well."

        elif the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person.char "Oh no, you should have pulled out! My [so_title] would be so angry if he knew I let other guys cum inside me."
            the_person.char "I guess it's too late now. Oh well."

        elif the_person.get_opinion_score("creampies") < 0:
            the_person.char "Hey, I told you to pull out. It feels like you got your cum everywhere inside me. Ew."

        else:
            the_person.char "Hey, I told you to pull out. Could you cum somewhere else next time? Maybe on my face?"

    return

label bimbo_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Give me your cum! I want you to cum in my ass! Ah!"
    else:
        the_person.char "Oh! Fuck, I hope there's room for all your cum!"
    return

label bimbo_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
    the_person.char "[rando]"
    return

label bimbo_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "Hi, I'm like, really sorry but I have way more stuff than you can imagine that I have to get done right now. Could we catch up later?"
    else:
        the_person.char "Hey, I'm sorry but I'm just suuuper busy right now! Hit me up later though, I'd love to chat once I get all this stupid work done!"
    return

label bimbo_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "Oh wait, I know what you want to see more of..."
        else:
            the_person.char "Ugh, all this clothing is getting in the way!"

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "I spent so much time this morning picking out this outfit, but I think you'd enjoy it more if I took it off, right?"
        else:
            the_person.char "Ah... I need to get all of this silly stuff off of me!"

    else:
        if the_person.arousal < 50:
            the_person.char "Teehee, just wait a moment and I'll strip this off for you..."
        else:
            the_person.char "Oh my god, let me strip for you [the_person.mc_title], let me be your slutty stripper!"

    return

label bimbo_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if the_person.title else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Is that, like, allowed? I thought that was illegal or something. Ugh."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Could you two get a room or something? There are some of us here who are trying to focus and you're being very distracting."
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Wow [the_sex_person.name] you're so adventurous, I don't think I could ever do that. But it looks, like, super fun!"
        $ change_report = the_person.change_slut_temp(1)
        "[title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh. My. God. That is so fucking hot... Keep it up girl, you're doing great!"
        $ change_report = the_person.change_slut_temp(2)
        "[title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Mmm, come on [the_person.mc_title], you should do something more to her. I bet she wants it real bad. I know I do..."
        "[title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
    return

label bimbo_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label bimbo_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] looks at you, pouts, then looks back at her work."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 40:
            "[the_person.title] looks at you when you enter the room and smiles."
            the_person.char "[the_person.mc_title]! I'm so glad you're stopping by, I've been so bored without you."
            "She pouts at you, eyes running up and down your body shamelessly."
            the_person.char "I hope you're here for something fun!"
        else:
            "[the_person.title] looks up from her work when you come into the room and smiles."
            the_person.char "[the_person.mc_title]! It's so good to see you! I've been having, like, the best day!"

    else:
        if the_person.obedience < 100:
            the_person.char "Hi [the_person.mc_title]! Do you need anything, any way I can help you?"
        else:
            the_person.char "Hi [the_person.mc_title]! Duh, I mean sir! Hi sir!"
            "[the_person.title] sticks out her tongue, then smiles and turns back to her work."

    return

label bimbo_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            the_person.char "So [the_person.mc_title], don't you think it's time you came back home with me and we had some real fun?"
            "[the_person.title] bites her lip and puffs out her chest just a little bit."

        else:
            the_person.char "[the_person.mc_title], I swear you're driving me crazy. Do you, like, want to come home with me and just get wild?"

    else:
        if the_person.love > 40:
            the_person.char "[the_person.mc_title], I don't know how you do it but I swear you've been driving me, like, totally crazy all night."
            "[the_person.title] runs her hand along your arm and giggles."
            the_person.char "I want you to come back to my place so I can have you all to my self."
        else:
            the_person.char "Oh my god [the_person.mc_title], tonight has been so much fun. Do you want to, like, come back home with me and drink some more?"
    return

label bimbo_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Aww sweety, I was just getting close to cumming and you're done?!"
            else:
                the_person.char "That's all? Aww, I hope you had a good time with me..."
        else:
            if the_person.arousal > 60:
                "Wait, you're stopping? Aren't you crazy horny right now too?"
            else:
                the_person.char "Don't you want to play with me any more? Oh well, your loss."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're actually done? But weren't you, like, having fun? I'm so fucking horny now..."
            else:
                the_person.char "Is that all you wanted to do? I thought guys had to, like, cum or it hurt."
        else:
            if the_person.arousal > 60:
                the_person.char "Aww, I was just getting getting warmed up!"

            else:
                the_person.char "That's it? Well, I guess that was a fun time well it lasted."
    return

label bimbo_sex_take_control(the_person):
    the_person.char "Oh no, get back here, I need to get off too, you know."
    return
label bimbo_sex_beg_finish(the_person):
    the_person.char "Aww, I was just getting there, could you, like, finish me off real quick?"
    return

## Role Specific Section ##
label bimbo_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] nods happily."
    "There's a long pause."
    mc.name "Do you know what to do?"
    the_person.char "Uh, duh! Look into the serum-stuff we make and make it better-er!"
    mc.name "Right, and do you have any idea how to actually do that?"
    "[the_person.title]'s eyebrows knit together as she tries to think."
    the_person.char "Uhm... not yet but... what if..."
    "You imagine you can see the little hamster in her head running as fast as it can."
    the_person.char "I've got it! What if you test it on me!"
    mc.name "Do you think that's a good idea!"
    the_person.char "Duh, that's why I thought of it! Come on, how bad could it be? Just let me try it! Record it or something and I'll tell you what it feels like!"
    return

## Taboo break dialogue ##
# label bimbo_kissing_taboo_break(the_person):
#
#     return
#
# label bimbo_touching_body_taboo_break(the_person):
#
#     return
#
# label bimbo_touching_penis_taboo_break(the_person):
#
#     return
#
# label bimbo_touching_vagina_taboo_break(the_person):
#
#     return
#
# label bimbo_sucking_cock_taboo_break(the_person):
#
#     return
#
# label bimbo_licking_pussy_taboo_break(the_person):
#
#     return
#
# label bimbo_vaginal_sex_taboo_break(the_person):
#
#     return
#
# label bimbo_anal_sex_taboo_break(the_person):
#
#     return
#
# label bimbo_condomless_sex_taboo_break(the_person):
#
#     return
#
# label bimbo_underwear_nudity_taboo_break(the_person, the_clothing):
#
#     return
#
# label bimbo_bare_tits_taboo_break(the_person, the_clothing):
#
#     return
#
# label bimbo_bare_pussy_taboo_break(the_person, the_clothing):
#
#     return
#
# label bimbo_facial_cum_taboo_break(the_person):
#
#     return
#
# label bimbo_mouth_cum_taboo_break(the_person):
#
#     return
#
# label bimbo_body_cum_taboo_break(the_person):
#
#     return
#
label bimbo_creampie_taboo_break(the_person):
    if the_person.wants_creampie():
        if the_person.on_birth_control:
            the_person.char "Ah, yay! Thank you [the_person.mc_title], your cum feels so good inside me!"

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Like, oh my god, your cum feel so good in me! It's driving me insane!"
                "She squeals happily."
                the_person.char "I should have dumped my [so_title] ages ago and let you fuck me more!"

            else:
                the_person.char "Like, oh my god, your cum feel so good in me! It's driving me insane!"
                "She squeals happily."

        else:
            if the_person.relationship != "Single":
                $ so_title = girl_relationship_to_title(the_person.relationship)
                the_person.char "Oh my god, I'm like, such a terrible [so_title]!"
                "She sighs happily."
                the_person.char "This feels so good though... I want you to do it again, even if I get pregnant!"

            else:
                the_person.char "Oh my god, your cum feels so good! I think my body wants you to get me pregnant!"
                "She squeals happily."

    else:
        if not the_person.on_birth_control:
            the_person.char "Like, oh my god. Did you just creampie me?!"

            if the_person.relationship != "Single":
                $ so_title = girl_relationship_to_title(the_person.relationship)
                the_person.char "Oh no, now I might get pregnant!"
                "She pouts and sighs unhappily."
                the_person.char "I'm such a bad [so_title]."

            else:
                if the_person.kids == 0:
                    the_person.char "Oh no, now I might get pregnant! I'm, like, not ready to be a mom!"
                else:
                    the_person.char "Oh no, now I might get pregnant again!"
                    the_person.char "I don't want to worry about a kid, I just want to have fun and fuck!"

        elif the_person.relationship != "Single":
            the_person.char "Hey, I like, told you to pull out!"
            "She pouts and sighs."
            the_person.char "Whatever, I guess that's what happens when you're as hot as I am."


        elif the_person.get_opinion_score("creampies") < 0:
            the_person.char "Ew! I told you to pull out!"
            "She sighs dramatically."
            the_person.char "Now I've got all this cum inside me, and it's going to be dripping out all day long!"

        else:
            the_person.char "Did you, like, not hear me?"
            the_person.char "Whatever, I guess I understand. I'm just, like, too hot for you."
    return
#
# label bimbo_anal_creampie_taboo_break(the_person):
#
#     return
