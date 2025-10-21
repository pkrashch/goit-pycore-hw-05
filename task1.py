def caching_fibonacci():
    cache = {} #empty dictionary

    def fibonacci(n):
        #basic cases F(0) = 0, F(1) = 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        #caching
        elif n in cache:
            return cache[n]
        #recursion
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci #return internal function