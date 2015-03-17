def combination(word):
    if not word:
        raise ValueError("parameter should not be empty")
    output = []
    alphabet = set(word)
    for letter in alphabet:
        output.append(letter)

    while True:
        newoutput = []
        while output:
            word = output.pop()
            yield word
            for letter in alphabet:
                newoutput.append(word + letter)
        output = newoutput
