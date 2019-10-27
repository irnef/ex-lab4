@@ -0,0 +1,10 @@


def main():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

    print(list(sorted(data, key=lambda num: abs(num))))


if __name__ == "__main__":
    main()
