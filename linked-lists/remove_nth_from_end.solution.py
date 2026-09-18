"""Reference solution for remove_nth_from_end."""


def remove_nth_from_end(head, n):
    dummy = type('Node', (), {'val': 0, 'next': head})()
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
