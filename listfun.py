def push_stack(list, element):
    list.append(element)
    return list

def pop_stack(list):
    element = list[len(list)-1]
    list.pop(len(list)-1)
    return list, element

def push_queue(list, element):
    list.append(element)
    return list

def pop_queue(list):
    element = list[0]
    list.pop(0)
    return list, element

if (__name__ == '__main__'):
    stack = []
    push_stack(stack, "ram")
    push_stack(stack, "raj")
    push_stack(stack, "rao")
    print(stack)
    stack, element = pop_stack(stack)
    print(element)
    print(stack)

    queue = []
    push_queue(queue, "sam")
    push_queue(queue, "som")
    push_queue(queue, "son")
    print(queue)
    queue, element = pop_queue(queue)
    print(element)
    print(queue)