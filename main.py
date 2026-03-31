from src.stack import Stack
from src.queue import Queue
from src.hashtable import HashTable


def demo_stack():
    print("=== STACK (LIFO) ===")
    s = Stack()
    print("is_empty:", s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print("size:", s.size())
    print("peek:", s.peek())
    print("pop:", s.pop())
    print("pop:", s.pop())
    print("size:", s.size())
    print()


def demo_queue():
    print("=== QUEUE (FIFO) ===")
    q = Queue()
    print("is_empty:", q.is_empty())
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print("size:", q.size())
    print("front:", q.front())
    print("dequeue:", q.dequeue())
    print("dequeue:", q.dequeue())
    print("size:", q.size())
    print()


def demo_hashtable():
    print("=== HASH TABLE (separate chaining) ===")
    ht = HashTable(capacity=7)
    ht.set("name", "Ada")
    ht.set("age", 36)
    ht.set("country", "MX")
    print("has('name'):", ht.has("name"))
    print("get('name'):", ht.get("name"))
    print("get('missing'):", ht.get("missing"))
    print("remove('age'):", ht.remove("age"))
    print("has('age'):", ht.has("age"))
    print("size:", ht.size())
    print("debug_buckets (colisiones):", ht.debug_buckets())
    print()


def main():
    demo_stack()
    demo_queue()
    demo_hashtable()


if __name__ == "__main__":
    main()

