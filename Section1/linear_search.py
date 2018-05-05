
def linear_search(alist, key):
    for item in alist:
        if item == key:
            return True

    return False

key = 10
alist = [30, 40, 50, 10, 60, 20]
print("Item {} found in {}? : {}".format(key, alist, linear_search(alist, key)))
