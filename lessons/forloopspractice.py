"""Writing for loops practice in class"""

__author__ = "730695410"

# pets: list[str] = ["Louie", "Bo", "Bear"]
# """Tell every pet they're a good boy!"""
# for elem in pets:
# print(f"Good boy, {elem}!")
# for index in range(0, len(pets)) # for range always use index
# print(pets[index])


# for x in [1, 2, 3]:
# print(x)

# names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# for index in range(0, len(names)):
# print(f"{index}: {names[index]}")

# ys: list[int] = [110, 120]
# for y in ys:
# print(y)

i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
    y: float = ys[0]
    print(y)
    i += 1
