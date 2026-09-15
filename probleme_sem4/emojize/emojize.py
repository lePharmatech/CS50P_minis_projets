import emoji

def main():
   user_input = input("Input: ")
   transform = emoji.emojize(user_input, language= 'alias')
   print(f"Output: {transform}")

main()
