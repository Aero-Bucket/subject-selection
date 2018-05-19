def yield_gen(iteration):
    for i in range(iteration):
        yield i**2 # generator function

yield_generator=yield_gen(5) # create generator object

for i in range(3):
    print(next(yield_generator))
