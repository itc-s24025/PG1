# import my_mathの中身を使う 
def my_pow(X, y):
    return X ** y

if __name__ == '__main__':
    x, y, exp = 2, 5, 32
    ans = my_pow(x, y)
    print(f"Test my_pow({x}), {y}) -> {ans}, exp: {exp} ---", end=' ')

    if ans == exp:
        print("Test Pass")
    else:
        print("Test Fail")
