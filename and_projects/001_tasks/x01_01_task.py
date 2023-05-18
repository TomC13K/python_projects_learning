#1) Create a function that takes a dictionary of ANDi names and returns a list of their names in alphabetical order.


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

#print(andi_dictionary)
def get_names(data):
    if len(data) == 0:
        return []
    return data['name']

def sorted_names(andi_list):
    if len(andi_list) == 0:
        return []
    return sorted(map(get_names, andi_list))


#print(sorted_names(andi_dictionary))











