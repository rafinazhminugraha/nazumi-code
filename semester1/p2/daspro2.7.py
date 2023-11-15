# manipulasi tuple agar durian dihapus
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

y = list(buah)
y.pop (3)
buah = tuple(y)

print(buah)