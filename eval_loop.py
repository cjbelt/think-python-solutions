def eval_loop():
    value = 0

    while True:
        value = input('Write a value:')

        if value == 'done':
            return

        print(eval(value))

eval_loop()
