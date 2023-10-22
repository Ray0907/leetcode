/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  var length = 0;
  var current = head;
  while (current) {
    current = current.next;
    length += 1;
  }
  target = length - n;
  if (target == 0) return head.next;
  current = head;
  for (i = 0; i < target - 1; i++) {
    current = current.next;
  }
  current.next = current.next.next;
  return head;
};
