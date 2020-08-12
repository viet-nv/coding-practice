
// Singly-linked lists are already defined with this interface:
// class ListNode<T> {
//   ListNode(T x) {
//     value = x;
//   }
//   T value;
//   ListNode<T> next;
// }
//
ListNode<Integer> sortZeroOneTwoList(ListNode<Integer> l) {
    int[] count = new int[]{0, 0, 0};
    while (l != null) {
        switch (l.value) {
            case 0:
                count[0]++;
                break;
            case 1:
                count[1]++;
                break;
            case 2:
                count[2]++;
                break;
        }
        l = l.next;
    }
    ListNode head = null;
    for (int  i = 2; i >= 0; i--) {
        for (int j = 0; j < count[i]; j++) {
            ListNode t =  new ListNode(i);
            t.next = head;
            head = t;
        }
    }

    return head;
}
