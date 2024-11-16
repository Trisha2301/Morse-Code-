#morse code
import sys
def code_encrypter(code):
    encode_dict={"A":".-","B":"-...","C":"-.-.",'D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0':' -----','1':'.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.'}
    for i in code:
        print(encode_dict[i],end=" ")
def code_decrypter(code):
    decode_dict={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', ' -----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
    for i in code:
        print(decode_dict[i],end="")
if __name__=="__main__":
    print("Enter\n1---->Encoder\n2---->Decoder\n3---->Quit")
    choice=int(input())
    match choice:
        case 1:
            code=input("Enter data you want to convert\n").upper()
            code_encrypter(code.replace(" ",""))
        case 2:
            code=input("Enter data you want to convert\n")
            code_list=code.split(" ")
            code_decrypter(code_list)
        case 3:
            exit
        case _:
            raise NameError("Wrong Input")
            
            
