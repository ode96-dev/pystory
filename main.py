def get_input(word_type:str):
    user_input:str = input(f"Enter a {word_type}: ")
    return user_input

first_noun = get_input("noun")
first_adjective = get_input("adjective")
first_verb= get_input("verb")
second_noun = get_input("noun")
second_verb= get_input("verb")

story = f"""
There is a {first_adjective} {first_noun} in EA who loves to {first_verb} all day.

One day, {first_noun} decided to learn Python and asked {second_noun} to teach him.

{second_noun} : "Why do you want to learn Python?"
{first_noun} : "I want to expand my knowledge in {first_verb}."
{second_noun}: "That is great, it is always nice to see young men like you trying to learn {first_verb} new everyday."
{first_noun}: "Thank you!When should we start the classes?"
{second_noun}: "Next week. Today, we are going  {second_verb}."

"""

print(story)