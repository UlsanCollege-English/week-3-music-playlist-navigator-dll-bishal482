class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.value)
            node = node.next
        return result

    def play_first(self):
        if self.head:
            self.current = self.head
            return self.current.value
        return None

    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current.value if self.current else None

    def prev(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current.value if self.current else None

    def insert_after_current(self, song):
        if not self.current:
            self.add_song(song)
        else:
            new_node = Node(song)
            new_node.next = self.current.next
            new_node.prev = self.current
            if self.current.next:
                self.current.next.prev = new_node
            else:
                self.tail = new_node
            self.current.next = new_node

    def remove_current(self):
        if not self.current:
            return False

        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            self.head = self.current.next

        if self.current.next:
            self.current.next.prev = self.current.prev
        else:
            self.tail = self.current.prev

        if self.current.next:
            self.current = self.current.next
        elif self.current.prev:
            self.current = self.current.prev
        else:
            self.current = None
        return True


def test_add_play_nav_insert_remove():
    p = Playlist()
    for t in ["A", "B", "C"]:
        p.add_song(t)
    assert p.to_list() == ["A", "B", "C"]
    assert p.play_first() == "A"
    assert p.next() == "B"
    p.insert_after_current("Bx")
    assert p.to_list() == ["A", "B", "Bx", "C"]
    assert p.next() == "Bx"
    assert p.next() == "C"
    assert p.next() == "C"
    assert p.prev() == "Bx"
    assert p.remove_current() is True
    assert p.to_list() == ["A", "B", "C"]
    print("All tests passed! ✅")

