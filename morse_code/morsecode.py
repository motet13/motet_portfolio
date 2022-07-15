import sys


class MorseCode:
    morsecode = { 
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
    }

    def __str__(self) -> str:
        return "MorseCode class"

    
    def _reverse_morescode_value(self):
        """Switch the key and value of the morsecode dictionary (from {a: b} to {b: a})."""
        result = {}
        for key, val in self.morsecode.items():
            if val not in result:
                result[val] = key
        
        return result


    def user_option(self):
        """Obtain the option input from the user wether to use cipher, decipher, or exit."""
        try:
            option = input("Please select an option below and hit enter.\n( cipher / decipher / exit ): ")
        except KeyboardInterrupt:
            print("\nProcess ended with status code 0.")
            sys.exit(0)

        return option
    
    
    def message(self, option):
        """Grab the user input message and returns it."""
        try:
            message = input(f'Type the message to {option}\n: ').lower()
        except KeyboardInterrupt:
            print("\nProcess ended with status code 0.")
            sys.exit(0)
        
        return message


    def cipher(self, message):
        """Turn message into morse code and returns it."""
        formatted_message = '|'.join(message.split())
        result = ''

        for char in formatted_message:
            if char == '|':
                result += '| '
            if char in self.morsecode:
                result += f'{self.morsecode[char]} '

        return result


    def decipher(self, message):
        """Turn morse code into a readable format."""
        codes = message.split()
        reversed_morse_code = self._reverse_morescode_value()
        result = ''
        
        for code in codes:
            if code == '|':
                result += ' '
            if code in reversed_morse_code:
                result += reversed_morse_code[code]
        
        return result


    def exit(self):
        """Exits the program."""
        print('Goodbye...(*_*)\n')
        sys.exit(0)