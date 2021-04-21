import copy


class SegmentTree:
    __arr = []
    __arr_len = 0
    __st = []

    def __init__(self, arr):
        self.__arr = copy.deepcopy(arr)
        self.__arr_len = len(arr)
        # Using string "NULL" as a non-numeric sentient character indicating invalid entry
        self.__st = ["NULL"] * 4 * self.__arr_len

    def get_underlying_array(self):
        return self.__arr

    def get_segment_tree(self):
        return self.__st

    def build(self):
        self.__build_impl(0, 0, self.__arr_len - 1)
        return self.__st

    def __build_impl(self, ind, l, r):
        if l == r:
            self.__st[ind] = self.__arr[l]
            return self.__st[ind]

        mid = int((l + r) / 2)
        left_child_value = self.__build_impl(2 * ind + 1, l, mid)
        right_child_value = self.__build_impl(2 * ind + 2, mid + 1, r)

        self.__st[ind] = left_child_value + right_child_value
        return self.__st[ind]

    def query(self, l, r):
        assert ((l <= r) and (l >= 0) and (r <= self.__arr_len - 1))
        return self.__query_impl(0, 0, self.__arr_len - 1, l, r)

    def __query_impl(self, ind, st_l, st_r, l, r):
        if (l <= st_l) and (st_r <= r):
            return self.__st[ind]

        if (r < st_l) or (st_r < l):
            return 0

        st_mid = int((st_l + st_r) / 2)
        left_child_value = self.__query_impl(2 * ind + 1, st_l, st_mid, l, r)
        right_child_value = self.__query_impl(2 * ind + 2, st_mid + 1, st_r, l, r)

        ans = left_child_value + right_child_value
        return ans

    def update(self, pos, val):
        assert ((pos >= 0) and (pos <= self.__arr_len - 1))
        value_change = self.__update_impl(0, 0, self.__arr_len - 1, pos, val)
        assert (value_change == val - self.__arr[pos])
        self.__arr[pos] = val
        return True

    def __update_impl(self, ind, st_l, st_r, pos, val):
        if st_l == st_r:
            assert (st_l == pos)
            change = val - self.__st[ind]
            self.__st[ind] = val
            return change

        if (pos < st_l) or (st_r < pos):
            assert False
            return 0

        st_mid = int((st_l + st_r) / 2)
        my_updated_change = 0
        if (st_l <= pos) and (pos <= st_mid):
            my_updated_change = self.__update_impl(2 * ind + 1, st_l, st_mid, pos, val)
        elif (st_mid + 1 <= pos) and (pos <= st_r):
            my_updated_change = self.__update_impl(2 * ind + 2, st_mid + 1, st_r, pos, val)

        self.__st[ind] += my_updated_change
        return my_updated_change


if __name__ == '__main__':
    a = [2, 3, 7, 8, 14, 31, 5, 19, 99, 0, -17]
    segmentTree = SegmentTree(a)
    segmentTree.build()
    print("Built underlying array", segmentTree.get_underlying_array())
    print("Built segment Tree: ", segmentTree.get_segment_tree())
    print(segmentTree.query(4, 9))
    segmentTree.update(5, -11)
    print("Built underlying array", segmentTree.get_underlying_array())
    print("Built segment Tree: ", segmentTree.get_segment_tree())
    print(segmentTree.query(4, 9))
