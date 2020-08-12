#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    if t == None:
        return True
    list1 = []
    list2 = []
    gogo(t.left, list1, True)
    gogo(t.right, list2, False)

    return list1 == list2

def gogo(t, result, is_left_to_right):
    if t == None:
        result.append(-1)
        return
    result.append(t.value)
    if is_left_to_right:
        gogo(t.left, result, True)
        gogo(t.right, result, True)
    else:
        gogo(t.right, result, False)
        gogo(t.left, result, False)

