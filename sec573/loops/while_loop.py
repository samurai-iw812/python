while not PasswordFound:
    guess = bruteforce.next()
    PasswordFound= encrypt(salt,guess) == hashcopy

else:
    happy_dance()