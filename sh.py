#!/bin/env python
import os
from cry import Cry


cry = Cry()


def main():
    while True:
        prompt = f'{os.getcwd()} > '
        command = input(prompt).split()
        match command:
            case ['quit']:
                break
            case ['ls']:
                print(os.listdir())
            case ['cd', noun]:
                os.chdir(noun)
            case ['cat', noun]:
                print(open(noun).read())
            case ['touch', noun]:
                open(noun, 'w')
            case ['rm', noun]:
                os.remove(noun)
            case ['mkdir', noun]:
                os.mkdir(noun)
            case ['rmdir', noun]:
                os.rmdir(noun)
            case ['mv', noun1, noun2]:
                os.rename(noun1, noun2)
            case ['cp', noun1, noun2]:
                os.copy(noun, noun2)
            case ['enc', noun]:
                cry.ptor_encrypt_file(noun)
            case ['dec', noun]:
                cry.ptor_decrypt_file(noun)
            case ['mkey']:
                cry.save_key()
            case ['rkey']:
                cry.read_key()
            case _:
                print(f'Unrecognized command: {" ".join(command)!r}')


if __name__ == '__main__':
    main()
