import math

class Calculator:
    def __init__(self):
        self.ans = 0
        self.shift = False
        self.alpha = False
        self.mode = 'COMP'

    def toggle_shift(self):
        self.shift = not self.shift
        print(f"Shift {'ON' if self.shift else 'OFF'}")

    def toggle_alpha(self):
        self.alpha = not self.alpha
        print(f"Alpha {'ON' if self.alpha else 'OFF'}")

    def set_mode(self, mode):
        self.mode = mode.upper()
        print(f"Mode set to {self.mode}")

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial only defined for non-negative integers.")
        return math.factorial(n)

    def cube(self, x):
        return x ** 3

    def reciprocal(self, x):
        if x == 0:
            raise ZeroDivisionError("Cannot take reciprocal of zero.")
        return 1 / x

    def calculate(self, expr):
        expr = expr.replace('Ans', str(self.ans))
        try:
            allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
            allowed.update({
                'abs': abs,
                'pow': pow,
                'factorial': self.factorial,
                'cube': self.cube,
                'reciprocal': self.reciprocal,
                'Ans': self.ans,
            })
            result = eval(expr, {"__builtins__": None}, allowed)
            self.ans = result
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

    def run(self):
        print("Scientific Calculator (type 'exit' to quit)")
        while True:
            cmd = input(f"[{self.mode} | Shift={'ON' if self.shift else 'OFF'} | Alpha={'ON' if self.alpha else 'OFF'}] Enter expression or command: ").strip()
            if cmd.lower() == 'exit':
                print("Goodbye!")
                break
            elif cmd.lower() == 's':
                self.toggle_shift()
            elif cmd.lower() == 'a':
                self.toggle_alpha()
            elif cmd.lower() == 'm':
                mode = input("Enter mode (COMP/STAT/VERIF): ").strip()
                self.set_mode(mode)
            else:
                self.calculate(cmd)

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
