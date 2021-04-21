# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import SegmentTree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [2, 3, 7, 8, 14, 31, 5, 19, 99, 0, -17]
    segmentTree = SegmentTree.SegmentTree(a)
    segmentTree.build()
    print("Built underlying array", segmentTree.get_underlying_array())
    print("Built segment Tree: ", segmentTree.get_segment_tree())
    print(segmentTree.query(4, 9))
    segmentTree.update(5, -11)
    print("Built underlying array", segmentTree.get_underlying_array())
    print("Built segment Tree: ", segmentTree.get_segment_tree())
    print(segmentTree.query(4, 9))

