class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

def display(head):
    l=[]
    while head:
        l.append(str(head.data))
        head=head.next
    print(" ".join(l))
def linkedlist(arr):
    head=head1=Node(arr[0])
    for i in range(1,len(arr)):
        head1.next=Node(arr[i])
        head1=head1.next
    return head
def deleteNode(head,val):
    temp=head
    while temp and temp.next.data!=val:
        temp=temp.next
    if temp!=None:
        temp.next=temp.next.next
        
arr=list(map(int,input().split()))
val=int(input())
head=linkedlist(arr)
deleteNode(head,val)
display(head)
        
