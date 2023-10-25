class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"[오류] {self.message}")
