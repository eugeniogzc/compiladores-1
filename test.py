from src.stack import Stack
from src.queue import Queue
from src.hashtable import HashTable


def _print_result(name, passed, details=""):
    status = "PASS" if passed else "FAIL"
    if details:
        print(f"{status} - {name} - {details}")
    else:
        print(f"{status} - {name}")


def assert_equal(name, actual, expected):
    ok = actual == expected
    details = f"expected={expected!r}, actual={actual!r}"
    _print_result(name, ok, details if not ok else "")
    return ok


def assert_raises(name, fn, expected_exception_type):
    try:
        fn()
    except Exception as e:
        ok = isinstance(e, expected_exception_type)
        details = f"raised={type(e).__name__}, expected={expected_exception_type.__name__}"
        _print_result(name, ok, details if not ok else "")
        return ok
    _print_result(name, False, f"expected exception {expected_exception_type.__name__}, raised nothing")
    return False


def test_stack():
    passed = 0
    total = 0

    s = Stack()
    total += 1
    passed += assert_equal("Stack empty initially", s.is_empty(), True)

    s.push(1)
    s.push(2)
    s.push(3)
    total += 1
    passed += assert_equal("Stack size after pushes", s.size(), 3)

    total += 1
    passed += assert_equal("Stack peek", s.peek(), 3)

    total += 1
    passed += assert_equal("Stack pop returns last", s.pop(), 3)

    total += 1
    passed += assert_equal("Stack size after pop", s.size(), 2)

    empty_stack = Stack()
    total += 1
    passed += assert_raises("Stack pop on empty raises", empty_stack.pop, IndexError)

    total += 1
    passed += assert_raises("Stack peek on empty raises", empty_stack.peek, IndexError)

    return passed, total


def test_queue():
    passed = 0
    total = 0

    q = Queue()
    total += 1
    passed += assert_equal("Queue empty initially", q.is_empty(), True)

    q.enqueue("x")
    q.enqueue("y")
    q.enqueue("z")
    total += 1
    passed += assert_equal("Queue size after enqueues", q.size(), 3)

    total += 1
    passed += assert_equal("Queue front", q.front(), "x")

    total += 1
    passed += assert_equal("Queue dequeue returns first", q.dequeue(), "x")

    total += 1
    passed += assert_equal("Queue front after dequeue", q.front(), "y")

    empty_queue = Queue()
    total += 1
    passed += assert_raises("Queue dequeue on empty raises", empty_queue.dequeue, IndexError)

    total += 1
    passed += assert_raises("Queue front on empty raises", empty_queue.front, IndexError)

    return passed, total


def _find_collision_keys(ht, needed=2, search_limit=5000):
    seen = [[] for _ in range(ht.capacity())]
    found = None

    for i in range(search_limit):
        key = f"k{i}"
        idx = ht._hash(key)
        seen[idx].append(key)
        if len(seen[idx]) >= needed:
            found = seen[idx][:needed]
            break

    if not found:
        raise RuntimeError("Could not find colliding keys within search_limit")

    return found


def test_hashtable():
    passed = 0
    total = 0

    ht = HashTable(capacity=7)
    total += 1
    passed += assert_equal("HashTable size initially", ht.size(), 0)

    ht.set("a", 1)
    ht.set("b", 2)
    total += 1
    passed += assert_equal("HashTable get existing", ht.get("a"), 1)

    total += 1
    passed += assert_equal("HashTable has existing", ht.has("b"), True)

    total += 1
    passed += assert_equal("HashTable get missing returns None", ht.get("missing"), None)

    total += 1
    passed += assert_equal("HashTable remove missing returns None", ht.remove("missing"), None)

    total += 1
    passed += assert_equal("HashTable remove existing returns value", ht.remove("a"), 1)

    total += 1
    passed += assert_equal("HashTable has after remove", ht.has("a"), False)

    ht2 = HashTable(capacity=7)
    ht2.set("x", 10)
    ht2.set("x", 99)
    total += 1
    passed += assert_equal("HashTable overwrite keeps get updated", ht2.get("x"), 99)
    total += 1
    passed += assert_equal("HashTable overwrite keeps size 1", ht2.size(), 1)

    ht3 = HashTable(capacity=5)
    k1, k2 = _find_collision_keys(ht3, needed=2)
    ht3.set(k1, "v1")
    ht3.set(k2, "v2")
    total += 1
    passed += assert_equal("Collision keys both retrievable (1)", ht3.get(k1), "v1")
    total += 1
    passed += assert_equal("Collision keys both retrievable (2)", ht3.get(k2), "v2")

    total += 1
    passed += assert_equal("Collision remove one keeps other", ht3.remove(k1), "v1")
    total += 1
    passed += assert_equal("Collision other still present", ht3.get(k2), "v2")

    return passed, total


def main():
    total_passed = 0
    total_tests = 0

    for fn in (test_stack, test_queue, test_hashtable):
        p, t = fn()
        total_passed += p
        total_tests += t

    print()
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")


if __name__ == "__main__":
    main()

