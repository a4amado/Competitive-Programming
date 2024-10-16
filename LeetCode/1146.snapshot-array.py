class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.array = [{0: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id not in self.array[index]:
            snap_id -= 1
        return self.array[index][snap_id]