import sys
from morsecode import MorseCode
from textcolors import fg, bg


def main():
    mc = MorseCode()
    option = mc.user_option()

    while option != 'exit':
        if option == 'cipher':
            print('Words are separated with the | (pipe) symbol.')
            message = mc.message(option)
            ciphered_message = mc.cipher(message=message)
            print(f': === Morse Code ===\n' \
                f':>\n' \
                f': {bg["BLACK"]}{fg["DARK_CYAN"]}{fg["BOLD"]}{ciphered_message}{fg["DEFAULT"]}\n' \
                f':<\n'
                )
            option = mc.user_option()
        elif option == 'decipher':
            message = mc.message(option)
            deciphered_message = mc.decipher(message=message)
            print(f': === Deciphered Code ===\n' \
                f':>\n' \
                f': {bg["BLACK"]}{fg["DARK_GREEN"]}{fg["BOLD"]}{deciphered_message}{fg["DEFAULT"]}\n' \
                f':<\n'
                )
            option = mc.user_option()
        else:
            print(f'{option} is not recognized by this program. Please try again.')
            option = mc.user_option()

    mc.exit()

if __name__ == '__main__':
    main()
