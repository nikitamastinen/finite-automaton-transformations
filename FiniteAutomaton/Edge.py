class Edge:
    start: str
    end: str
    value: str

    def __init__(self, start, end, value):
        self.start = str(start)
        self.end = str(end)
        self.value = str(value)
