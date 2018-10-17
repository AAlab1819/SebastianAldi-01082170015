from collections import defaultdict
class Topic:
    def __init__(self, id, old_z, new_z):
        self.id = id
        self.old_z = old_z
        self.new_z = new_z
        self.difference = new_z-old_z
    def getID(self):
        return self.id
    def getOldZ(self):
        return self.old_z
    def getNewZ(self):
        return self.new_z
    def getDifference(self):
        return self.difference
def heapify(array, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(array) and array[i].getDifference() < array[left].getDifference():
        largest = left
    if right < len(array) and array[largest].getDifference() < array[right].getDifference():
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest)
def heapSort(array):
    sortedArray = []
    for i in range(len(array), -1, -1):
        heapify(array, i)
    while array:
        sortedArray.append(array[0])
        del array[0]
        for i in range(len(array) // 2, -1, -1):
            heapify(array, i)
    return sortedArray
topics = []
sortedTopics = []
differenceID = defaultdict(list)
lines = int(input())
while lines > 0:
    id, old_z, post, like, comment, share = map(int, input().split())
    new_z = post*50 + like*5 + comment*1 + share*20
    topics.append(Topic(id, old_z, new_z))
    lines -= 1
sortedTopics = heapSort(topics)
for topic in sortedTopics:
    differenceID[topic.getDifference()].append(topic)
counter = 0
for difference_list in differenceID.values():
    for topic in sorted(difference_list, key=lambda x:x.id, reverse=True):
        if counter == 5: break
        print(topic.getID(), topic.getNewZ())
        counter += 1