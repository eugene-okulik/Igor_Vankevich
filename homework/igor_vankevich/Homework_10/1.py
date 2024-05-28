def finish_me(func):

    def wrapper(test):
        func(test)
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)


example('text')
