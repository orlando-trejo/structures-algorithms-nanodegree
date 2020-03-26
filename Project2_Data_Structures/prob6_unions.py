# @Author: otrejo
# @Date:   2020-03-05T00:12:05-05:00
# @Last modified by:   otrejo
# @Last modified time: 2020-03-25T22:17:04-04:00



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + "->"
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        else:
            cur_head = self.head
            while cur_head.next:
                cur_head = cur_head.next

            cur_head.next = Node(value)

    def size(self):
        counts = 0
        cur_head = self.head
        while cur_head:
            counts += 1
            cur_head = cur_head.next
        return counts


def union(llist1, llist2):
    d = {}
    head1 = llist1.head
    while head1:
        value = head1.value
        if value in d:
            d[value] += 1
            head1 = head1.next
        else:
            d[value] = 1
            head1.next

    head2 = llist2.head
    while head2:
        value = head2.value
        if value in d:
            d[value] += 1
            head2 = head2.next
        else:
            d[value] = 1
            head2 = head2.next

    return list(d.keys())



def intersection(llist1, llist2):
    head1 = llist1.head
    intrs = []
    while head1:
        value1 = head1.value
        head2 = llist2.head
        while head2:
            value2 = head2.value
            if value1 == value2:
                intrs.append(value1)
            head2 = head2.next
        head1 = head1.next
    return set(intrs)




# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))
