class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_push.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_push:
                self.stack_out.append(self.stack_push.pop(-1))

            return self.stack_out.pop(-1)
        else:
            return self.stack_out.pop(-1)

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_push:
                self.stack_out.append(self.stack_push.pop(-1))

            return self.stack_out[-1]
        else:
            return self.stack_out[-1]

    def empty(self) -> bool:
        if self.stack_push or self.stack_out:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()