import argparse

search_modes = ['standard', 'first_character', 'this_known_k_latter']
search_space = ['number', 'number_lowercase', 'lowercase', 'full_space']

class InputtedArguments():
    def __init__(self, password, mode, space, password_length, first_character, k_char):
       self.password = password
       self.search_mode = mode
       self.search_space = space
       self.password_length = password_length
       self.first_character = first_character
       self.k_char = k_char


def cracker_engine(inputted_arguments:InputtedArguments):
   pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password Cracker v.2000.turbo!')

    parser.add_argument('--password', type=str, help='we can\'t crack your null password! oh wait a moment: your pass == null? XD')
    parser.add_argument('--mode', type=str, choices=search_modes, help='Select your searching mode')
    parser.add_argument('--space', type=str, choices=search_space,help='Select the searching space')

    parser.add_argument('--length', type=str, nargs='?', help='length of the password is needed for cracking!')
    parser.add_argument('--first_character', type=str, nargs='?', help='If you have chosen (this_known_k_latter) mode, you must type first character of password letters')
    parser.add_argument('--k_char', type=str, nargs='+', help='If you have chosen (this_known_k_latter) mode, you must type k number of password letters')
   
    args = parser.parse_args()

    cracker_engine(
        inputted_arguments= InputtedArguments(
            password= args.password, 
            mode=args.mode, 
            space=args.space,
            password_length= args.length, 
            first_character=args.first_char, 
            k_char=args.k_char
        )
    )
    