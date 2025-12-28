class Processor:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> str:
        return f"Processing by {self.name}"
