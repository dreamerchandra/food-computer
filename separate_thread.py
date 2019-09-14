import threading

def seprate_thread(should_join = False):
    def inner(func):
        def decorator():
            print('starting separate thread')
            thread = threading.Thread(target=func)
            thread.start()
            if should_join:
                thread.join()
            print('started seprate thread')
        return decorator
    return inner