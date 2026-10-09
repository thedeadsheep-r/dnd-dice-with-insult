import random

used = []

def inuslt():
    global used

    insults = []

    insults.append('So you were the kid who was given extra 5 min every exam')
    insults.append('I see you’re playing stupid again—and you’re winning.')
    insults.append('Would you like a side of epic with that fail?')
    insults.append('You warthog-faced buffoon!')
    insults.append('They should’ve put you in a jar on the mantlepiece. Shame.')
    insults.append('You are a sad, strange little player—and you have my pity.')
    insults.append('If I wanted a joke, I’d follow you to the bathroom and watch you try to think.')
    insults.append('Well aren’t you just a cookie full of arsenic.')
    insults.append('You remind me of sweat from a baboon’s balls.')
    insults.append('I’ll never forget the first time we met—but I’ll keep trying.')
    insults.append('I’d slap you, but that might make you look better.')
    insults.append('As an outsider, how do you view the human race?')
    insults.append('You sometimes stumble over the truth, but you always get up and walk away like nothing happened.')
    insults.append('Somewhere out there, a tree works hard to give you oxygen. You owe it an apology.')
    insults.append('You must be an experiment in artificial stupidity.')
    insults.append('This is an excellent time for you to become a missing person.')
    insults.append('You are the reason some animals eat their young.')
    insults.append('How tf you find this reply. you must have really fucked up')
    insults.append('I dont know what your problem is, but Ill bet its hard to pronounce.')
    insults.append('Im thinking you werent burdened with an overabundance of schooling.')
    insults.append('Everyone has the right to be stupid, but youre just abusing the privilege.')
    insults.append('I am not calling you the stupidest person alive but you hope they do not die.')
    insults.append('You are not being the person Lady E. knew you could be.')
    insults.append('Who ever would fuck you is just too lazy to jerk off')
    insults.append('I Would not attend Your funeral, but I will sent a nice letter saying I approved of it.')
    insults.append('You just have about enough intelligence to open his mouth when you wanted to eat, but certainly no more.')
    insults.append('You are distinguished for ignorance; for you have only one idea, and that is wrong.')
    insults.append('Come, come, you froward and unable worms!')
    insults.append('I must tell you friendly in your ear, sell when you can, you are not for all markets.')
    insults.append('I’ll beat thee, but I would infect my hands.')
    insults.append('Methink’st thou roll a general offence and every person should beat thee.')
    insults.append('Thou cream faced loon')

    if len(used) == len(insults):
        used = []

    x = random.randint(0, len(insults) - 1)
    while x in used:
        x = random.randint(0, len(insults) - 1)

    used.append(x)
    return insults[x]
