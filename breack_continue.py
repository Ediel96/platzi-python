def run():
    # for acount in range(1000):
        # if acount % 2 != 0:
        #     continue
        # print(acount)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    text = input('Write an text')
    for character in text:
        if character == 'o':
            break
        print(character)


if __name__ == '__main__':
    run()
