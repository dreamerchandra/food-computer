last_push_object = {}

def push_on_huge_change(key_list):
    def inner(func):
        def decorator(*args):
            obj_to_push = args[0]
            for item in key_list:
                cur_value = obj_to_push.get(item)
                last_value = last_push_object.get(item) if last_push_object.get(item) else -1
                if (cur_value > last_push_object + 0.5):
                    func(*args)
                    break
            print (obj_to_push)
            last_push_object = obj_to_push;
        return decorator
    return inner