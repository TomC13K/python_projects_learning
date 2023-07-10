# 2) I’m trying to watch some LinkedIn Learning videos to complete my Python Learning Pathway but I keep getting
# distracted by meme compilations,music recommendations, pets and more on Slack.

# Your job is to help me create a function that takes a string and checks to see if it contains the following words or
# phrases: “Dog” , “pet” , “music” , “Funny meme” , “Listen to this”

# If it does, return "NO!" Otherwise, return "Safe watching!"

list_of_words = ["Dog", "pet", "music", "Funny meme", "Listen to this"]


def check_string(string):
    return "NO!" if any(word.lower() in string.lower() for word in list_of_words) else "Safe watching!"


print(check_string('this is dog'))
print(check_string('here is nothing'))
print(check_string('this you need to listen to this'))
print(check_string('crappy music'))
print(check_string('listen listen'))
