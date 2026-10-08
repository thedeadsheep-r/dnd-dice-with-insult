def spliterxD (y):
    global roll_multiplier, add_data
    rolls = []
    list_data = list(y)
    counter = 0

    for i in list_data:
        counter =+ 1

        if counter == len(list_data) :
            return rolls

        else:
            if counter == 2 and i == 'd':
                roll_multiplier = y.split('d')
                rolls.append(1)
                add_data = list(roll_multiplier[1])
                counter =0
                break

            elif i == 'd':
                roll_multiplier = y.split('d')
                rolls.append(roll_multiplier[0])
                add_data = list(roll_multiplier[1])
                counter = 0
                break


    for i in add_data:
        counter += 1

        if counter == len(add_data) :
            rolls.append(roll_multiplier[1])
            rolls.append(0)
            return rolls

        else:

            if ((i != '+' or i != '-' ) and counter ==  4) or ((i != '+' or i != '-' ) and counter ==  5) :

                rolls.append(roll_multiplier[1])
                rolls.append(0)
                break


            elif i == '+':

                roll_add_addon = roll_multiplier[1].split('+')
                rolls.append(roll_add_addon[0])
                rolls.append(1)
                rolls.append(roll_add_addon[1])
                break

            elif i == '-':

                roll_add_addon = roll_multiplier[1].split('-')
                rolls.append(roll_add_addon[0])
                rolls.append(1)
                rolls.append(-1*int(roll_add_addon[1]))
                break

            elif i != '+' and i != '-':

                try:
                    isinstance(int(i), int)
                except ValueError:

                    roll_add_addon = roll_multiplier[1].split(i)
                    rolls.append(roll_add_addon[0])
                    rolls.append(0)
                    break




    return rolls

