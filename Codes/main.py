import os
import discord
import calculation
import spliter
import dice
import insults

rolls_call = [100,20,12,10,8,6,4,2]

class Client(discord.Client):
        async def on_ready(self):
            print(f'Logged in as {self.user}!')

        async def on_message(self, message):
            if message.author == self.user:
                return

            if message.content.startswith(f'/roll '):
                    parts = message.content.split(' ')
                    roll_data = spliter.spliterxD(parts[1])
                    try:
                        die = int(roll_data[1])
                    except ValueError:
                        await message.channel.send(f'Look at this Arschgeige adding more in d100')


                    if die in rolls_call:

                        roll_multi= calculation.error_fix(roll_data[0])

                        if roll_multi >= 2 and int(roll_data[2]) == 0:
                            counter = 0
                            all_rolls =calculation.multi(int(roll_data[0]), die)
                            for i in all_rolls:
                                counter +=1
                                if counter == len(all_rolls):
                                    break
                                else:
                                    await message.channel.send(f'{message.author.display_name} rolled a {counter}d{die} for: {i} ')

                            await message.channel.send(f'{message.author.display_name} rolled a total of {all_rolls[counter-1]}')
                        elif roll_multi >= 2 and int(roll_data[2]) == 1:
                            counter = 0
                            all_rolls = calculation.multi(int(roll_data[0]), die)
                            for i in all_rolls:
                                counter += 1
                                if counter == len(all_rolls):
                                    break
                                else:
                                    await message.channel.send(
                                        f'{message.author.display_name} rolled a {counter}d{die} for: {i}')

                            await message.channel.send(
                                f'{message.author.display_name} rolled a total of {all_rolls[counter - 1]} and with your modifier {roll_data[3]} it will become {int(all_rolls[counter - 1])+int(roll_data[3])}')
                        elif int(roll_data[2]) == 1:
                            k= dice.dice(die)
                            await message.channel.send(f'{message.author.display_name} rolled a d{die} for: {k} and with your modifier {roll_data[3]} it will become {k+int(roll_data[3])}  ')
                        else:

                            await message.channel.send(f'{message.author.display_name} rolled a d{die} for: {dice.dice(die)}   ')

                    else:
                            await message.channel.send(f'{insults.inuslt()}... re-check your die' )

            if message.content.startswith(f'/+ad roll '):
                parts = message.content.split(' ')
                roll_data = spliter.spliterxD(parts[2])
                die = int(roll_data[1])
                roll_data[0] = calculation.error_fix(roll_data[0])

                if die in rolls_call:

                    if int(roll_data[2]) == 1:

                        await message.channel.send(f'{message.author.display_name} rolled with Advantage d{die} as: {dice.modadvantageRoll(die,int(roll_data[3]))}   ')
                    elif  int(roll_data[2]) == 0:
                        await message.channel.send(f'{message.author.display_name} rolled with Advantage d{die} as: {dice.advantageRoll(die)}   ')
                else:
                    await message.channel.send(f'{insults.inuslt()}... re-check your die' )

            if message.content.startswith(f'/-dad roll '):
                parts = message.content.split(' ')
                roll_data = spliter.spliterxD(parts[2])
                die = int(roll_data[1])
                roll_data[0] = calculation.error_fix(roll_data[0])

                if die in rolls_call:

                    if int(roll_data[2]) == 1:
                        await message.channel.send(
                            f'{message.author.display_name} rolled with disadvantage d{die} as: {dice.modadvantageRoll(die, int(roll_data[3]))}   ')
                    elif int(roll_data[2]) == 0:

                        await message.channel.send(f'{message.author.display_name} rolled with Disadvantage d{die} as: {dice.disadvantageRoll(die)}   ')

                else:
                    await message.channel.send(f'So disappointed in you... you fuck up your dad')

intents = discord.Intents.default()
intents.message_content = True

# This is for your discord client id
client = Client(intents=intents)
client.run('')
