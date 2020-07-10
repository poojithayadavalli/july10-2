class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

def display(head):
    l=[]
    while head:
        l.append(str(head.data))
        head=head.next
    print("->".join(l))
