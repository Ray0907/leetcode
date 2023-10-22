/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  if (!head || !head.next) {
    return;
  }

  let slow = head;
  let fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let second_half = slow.next;
  slow.next = null;
  let prev = null;
  let current = second_half;
  while (current) {
    let next_node = current.next;
    current.next = prev;
    prev = current;
    current = next_node;
  }
  second_half = prev;

  let first_half = head;
  while (second_half) {
    let next_first = first_half.next;
    let next_second = second_half.next;
    first_half.next = second_half;
    second_half.next = next_first;
    first_half = next_first;
    second_half = next_second;
  }
};
