def decorator_function(orig):
    def wrapper_function(*args, **kwargs):
        print ('this one ran first')
        return orig(*args, **kwargs)
    # print('ran first')
    # return orig()
    return wrapper_function


@decorator_function
def display():
    print('this ran later')


@decorator_function
def display_info(name):
    print ('display ran with argumrnts {}'.format(name))


display()
display_info('test1')
