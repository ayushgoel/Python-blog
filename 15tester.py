

def tryexcept():
    count = {}
    with open("SETUP_INSTRUCTIONS.txt", "r") as f:
        for l in f:
            for c in l:
                try:
                    count[c] += 1
                except KeyError:
                    count[c] = 1
    return count

def dictget():
    count = {}
    with open("SETUP_INSTRUCTIONS.txt", "r") as f:
        for l in f:
            for c in l:
                count[c] = count.get(c,0) + 1
    return count

def default():
    from collections import defaultdict
    count = defaultdict(int)
    with open("SETUP_INSTRUCTIONS.txt", "r") as f:
        for l in f:
            for c in l:
                count[c] += 1
    return count

if __name__ == "__main__":
    from timeit import Timer
    t1 = Timer(tryexcept)
    t2 = Timer(dictget)
    t3 = Timer(default)
    print "try ... except ...", t1.timeit(10000)
    print "dict.get", t2.timeit(10000)
    print "defaultdict", t3.timeit(10000)
