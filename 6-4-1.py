def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

# ジェネレーターをforループのinに添える(forループで反復師が作られる)
for char in reverse('golf'):
    print(char, end=" ")
