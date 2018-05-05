def common_elements(alist, blist):
    for i in alist:
        for j in blist:
            if i == j:
                return True

    return False

alist = [1, 3, 5]
blist = [4, 5, 6]
print("Is there a common element in {} and {}: {}".format(alist, blist, common_elements(alist, blist)))
