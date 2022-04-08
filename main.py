# Takes in the set U of n elements and a list of subsets U S1,...,S2
# Returns a list of sets included in the set cover
def set_cover(u_set, s_list):
    # set of remaining nodes to cover
    r_set = u_set
    print(f'Orig R set: {r_set}')
    print(f'List of subsets: {s_list}')
    print()
    # list for selected subsets
    select_set = []
    while len(r_set) != 0:
        elems = 0
        for s in s_list:
            # select the subset with the most uncovered elements
            if elems < len(r_set.intersection(s)):
                elems = len(r_set.intersection(s))
                select = s
        # add the subset to the selected list
        print(f'Selected s {select}')
        select_set.append(select)
        print(f'R before: {r_set}')
        # remove its elements from the remaining nodes set
        r_set = r_set - select
        print(f'R minus s: {r_set}')
        print()
    return select_set

if __name__ == '__main__':
    test1 = [{1,2,3,8,9,10},{1,2,3,4,5},{4,5},{6},{4,5,7},{5,6,7},{6,7,8,9,10}]
    test2 = [{1,2,3},{2,4},{3,4},{4,5}]
    print("Test 1: ")
    print(set_cover({1,2,3,4,5,6,7,8,9,10},test1))
    print()
    print()
    # Output should be [{1, 2, 3}, {4, 5}]
    print("Test 2: ")
    print(set_cover({1,2,3,4,5},test2))