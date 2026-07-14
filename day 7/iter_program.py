def mygenerator() :
    print("first item")
    yield 10
    print("second item")
    yield 20
    print("last item")
    yield 30

    l1=[4,22,6,2,7,33]
    it=iter(l1)
    print(next(it))
    print(next(it))

    gen = mygenerator()

    print(next(gen))
    print(next(gen))
    print(next(gen))