#!/usr/bin/env python


def balanced(input_string):
    # Returns -1 if braces are balanced, or the 0-based index of the first
    # unbalanced brace
    openstack = list()
    input_string = str(input_string)

    for idx, char in enumerate(input_string):
        if char == '{':
            openstack.append(idx)
        elif char == '}':
            if not openstack:
                return idx
            openstack.pop()

    if openstack:
        return openstack[0]

    return -1


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        string = sys.argv[1]
    else:
        print('please provide string as argument')
        sys.exit()

    res = balanced(string)
    if res != -1:
        print('{} : unbalanced brace on {}'.format(string, res))
    else:
        print('{} is balanced'.format(string))
