__author__ = 'kushlani'
import random

def in_place_shuffle(lst):
    # shuffles the original list without creating a new list.
    num_elem = len(lst)

    if num_elem <= 1:
        return
    for index, elem in enumerate(lst):
        # pick a random number between index and num_elem -
        # so far up to index elements have been placed by random element
        number = random.choice(range(index, num_elem))  # randrange seems to want actual numbers as paras
        # swap current  index element with random element
        rand = lst[number]
        lst[index] = rand
        lst[number] = elem



my_lst = [4,6,8,1,9,3]
print ("original: ", my_lst)

in_place_shuffle(my_lst)
print("shuffled: ", my_lst)
