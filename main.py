class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def __eq__(self, b):
        return self.ism == b.ism and self.familiya == b.familiya and self.yosh == b.yosh

    def __str__(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh"

shaxs1 = Shaxs("Ali", "Valiyev", 25)
shaxs2 = Shaxs("Ali", "Valiyev", 25)
shaxs3 = Shaxs("Vali", "Valiyev", 25)

print(shaxs1 == shaxs2)  # True
print(shaxs1 == shaxs3)  # False
```

```python
class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def __eq__(self, b):
        return self.__dict__ == b.__dict__

    def __str__(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh"

shaxs1 = Shaxs("Ali", "Valiyev", 25)
shaxs2 = Shaxs("Ali", "Valiyev", 25)
shaxs3 = Shaxs("Vali", "Valiyev", 25)

print(shaxs1 == shaxs2)  # True
print(shaxs1 == shaxs3)  # False
