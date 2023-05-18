#1) Create a function that takes a dictionary of ANDi names and returns a list of their names in alphabetical order.

#2) I’m trying to watch some LinkedIn Learning videos to complete my Python Learning Pathway but I keep getting distracted by meme compilations, music recommendations, pets and more on Slack.

#Your job is to help me create a function that takes a string and checks to see if it contains the following words or phrases: “Dog” , “pet” , “music” , “Funny meme” , “Listen to this”

#If it does, return "NO!" Otherwise, return "Safe watching!"

#3) Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.
#Example: hacker_speak("anddigital is cool") ➞ "4ndd1g1t4l 15 c00l"
#In order to work properly, the function should replace all “a”s with 4, “e”s with 3, “i”s with 1, “o”s with 0, and “s”s with 5.

andi_dictionary = [{
    "name": "John"
}, {
    "name": "James"
}, {
    "name": "Jack"
}, {
    "name": "Andy"
}, {
    "name": "Xander"
}, {
    "name": "Jill"
}, {
    "name": "Jenny"
}]

print(andi_dictionary)
def get_names(data):
    return data['name']

def sorted_names(andi_list):
    return sorted(map(get_names, andi_list))


print(sorted_names(andi_dictionary))








