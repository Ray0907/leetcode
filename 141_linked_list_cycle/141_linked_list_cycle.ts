function hasCycle(head: ListNode | null): boolean {
  let current: ListNode | null = head;
  const res = new Set<ListNode>();

  while (current !== null) {
    if (res.has(current)) {
      return true; // Cycle detected
    } else {
      res.add(current);
      current = current.next;
    }
  }

  return false; // No cycle found
}
