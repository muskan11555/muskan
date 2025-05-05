import list1
import set2
import dict3

def main():
    my_list = [1, 2, 3]
    my_set = {1, 2, 3}
    my_dict = {"a": 1, "b": 2}

    print("List:", my_list)
    print("Set:", my_set)
    print("Dict:", my_dict)

    my_list = list1.append1(my_list, 4)
    my_set = set2.adds2(my_set, 4)
    my_dict = dict3.add3(my_dict, "c", 3)

    print("\nAfter adding elements:")
    print("List:", my_list)
    print("Set:", my_set)
    print("Dict:", my_dict)

    my_list = list1.remove1(my_list, 2)
    my_set = set2.remove2(my_set, 2)
    my_list = list1.pop(my_list)

    print("\nAfter removing elements:")
    print("List:", my_list)
    print("Set:", my_set)
    print("Dict:", my_dict)

    print("\nDict length:", dict3.len3(my_dict))
    print("Dict keys:", dict3.keys3(my_dict))
    print("Dict values:", dict3.values3(my_dict))
    print("Set length:", set2.slen2(my_set))import list1
import set2
import dict3

def main():
    my_list = [1, 2, 3]
    my_set = {1, 2, 3}
    my_dict = {"a": 1, "b": 2}

    print("List:", my_list)
    print("Set:", my_set)
    print("Dict:", my_dict)

    my_list = list1.append1(my_list, 4)
    my_set = set2.adds2(my_set, 4)
    my_dict = dict3.add3(my_dict, "c", 3)

    print("\nAfter adding elements:")
    print("List:", my_list)
    print("Set:", my_set)
    print("Dict:", my_dict)

    my_list = list1.remove1(my_list, 2)
    my_set = set2.remove2(my_set, 2)
    my_list = list1.pop(my_list)

    print("\nAfter removing elements:")
    print("List:", my_list)
    print("Set:", my_set)
    print("Dict:", my_dict)

    print("\nDict length:", dict3.len3(my_dict))
    print("Dict keys:", dict3.keys3(my_dict))
    print("Dict values:", dict3.values3(my_dict))
    print("Set length:", set2.slen2(my_set))