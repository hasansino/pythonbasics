class MyClass:
    def __init__(self, arga: str, argb: str):
        self.arga = arga
        self.argb = argb

    def concat(self) -> str:
        return self.arga + self.argb + "\n"
