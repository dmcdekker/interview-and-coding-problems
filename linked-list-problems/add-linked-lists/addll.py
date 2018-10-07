"""Given two linked lists, treat them like numbers and add them together.

This should take two linked lists in "reverse-digit" format, sum them up,
and return the head of a new linked list in "reverse-digit" format.

A list is in reverse-digit format if it is each digit as a node, in
least-significant-place-first order. For example, "123", would become
the list 3->2->1.

Let's add 1 + 2::

    >>> l1 = Node(1)
    >>> l2 = Node(2)
    >>> add_linked_lists(l1, l2).as_rev_string()
    '3'

Let's add 123 + 456::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '579'

Let's make sure we carry: 144 + 456:

    >>> l1 = Node(4, Node(4, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '600'

Let's make sure it works with mismatched lengths: 123 + 89::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(9, Node(8))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '212'

"""

class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return ''.join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """
    out_head = out_tail = None
    carry = 0

    # Loop over both lists stopping when *both* lists are done
    while l1 or l2:

        # If not done l1, get digit, move to next. If done, use 0.
        if l1:
            digit1 = l1.data
            l1 = l1.next
        else:
            digit1 = 0
        # If not done l2, get digit, move to next. If done, use 0.
        if l2:
            digit2 = l2.data
            l2 = l2.next
        else:
            digit2 = 0 

        # Add together digits (along w/carry) & determine new carry    
        new_digit = digit1 + digit2 + carry
        carry, new_digit = divmod(new_digit, 10)
        
        # Add to end of our out LL
        if not out_head:
            out_head = out_tail = Node(new_digit)

        else:
            out_tail.next = Node(new_digit)
            out_tail = out_tail.next
            
    # If we have any carry left over, add a new place for it
    if carry:
        out_tail.next = Node(carry)

    return out_head 



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
