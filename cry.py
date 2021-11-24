#!/bin/env python
from dataclasses import dataclass, field
from os import listdir
from typing import BinaryIO
from cryptography.fernet import Fernet


@dataclass
class Cry:
    key: bytes = field(default_factory=Fernet.generate_key)
    ptor: Fernet = field(init=False)

    def __post_init__(self) -> None:
        self.ptor = Fernet(self.key)

    def new_key(self) -> None:
        self.key: bytes = Fernet.generate_key()
        self.ptor: Fernet = Fernet(self.key)

    def save_key(self) -> BinaryIO:
        if '.key' in listdir():
            prompt = input('Do you wish to overwrite the existing key file? Enter y to confirm: ')
            match prompt:
                case 'y':
                    with open('.key', 'wb') as filehandle:
                        filehandle.write(self.key)
                case _:
                    pass                 
        else:
            with open('.key', 'wb') as filehandle:
                filehandle.write(self.key)

    def read_key(self) -> None:
        with open('.key', 'rb') as filehandle:
            self.key = filehandle.read()
            self.ptor = Fernet(self.key)

    def ptor_encrypt_file(self, filename) -> BinaryIO:
        with open(f'{filename}', 'rb') as filehandle:
            cipher_text = self.ptor.encrypt(filehandle.read())
        with open(f'{filename}', 'wb') as filehandle:
            filehandle.write(cipher_text)

    def ptor_decrypt_file(self, filename) -> BinaryIO:
        with open(f'{filename}', 'rb') as filehandle:
            clear_text = self.ptor.decrypt(filehandle.read())
        with open(f'{filename}', 'wb') as filehandle:
            filehandle.write(clear_text)


def main():
    pass


if __name__ == '__main__':
    main()
