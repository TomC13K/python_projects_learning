# 3) Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.
# Example: hacker_speak("anddigital is cool") ➞ "4ndd1g1t4l 15 c00l"
# In order to work properly, the function should replace all “a” s with 4, “e” s with 3, “i” s with 1, “o” s with 0, and
# “s” s with 5.

switch_list= [{"a": "4"}, {"e": "3"}, {"i": "1"}, {"o": "0"}, {"s": "5"}]


def hacker_speak(string):
    for switch in switch_list:
        for key, value in switch.items():
            string = string.replace(key, value)
    return string


print(hacker_speak("anddigital is cool"))

