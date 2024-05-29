from queue import Queue

def page_faults(pages, n, capacity):

    page_faults = 0
    s = set()
    indexes = Queue()

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
            
        else:
            if pages[i] not in s:
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1

    return page_faults

pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
n = len(pages)
capacity = 4

print(page_faults(pages, n, capacity))
