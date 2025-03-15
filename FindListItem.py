# Own solution with hint from AI
def findListItem(itemList, index):
    itemLocations = []

    for idx, item in enumerate(itemList):
        if isinstance(item, list):
            for i in findListItem(item, index):
                itemLocations.append([idx] + i)
        else:
            if item == index:
                itemLocations.append([idx])
    return itemLocations
    
# Tutorial's solution
def index_all(search_list, item):
    index_list = []

    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list

print(findListItem([[[1,2,3], 2, [1,3]], [1,2,3]], 2))

 