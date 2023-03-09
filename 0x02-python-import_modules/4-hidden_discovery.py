#!/usr/bin/python3
if __name__ == "__main__":
    import hidden4
    for i in (dir(hidden)):
        if i[:2] != "__":
            print("{:s}".format(i))
