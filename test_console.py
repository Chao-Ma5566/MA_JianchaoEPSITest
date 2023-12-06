import datetime
import atexit

def salutation():
    now = datetime.datetime.now()
    hour = now.hour

    if 6 <= hour < 18:
        return "Bonjour,早上好"
    else:
        return "Bonsoir，晚上好"

def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
    
def check_plalindrome(word):
    cleared_word = word.replace(" ", "")
    if cleared_word.lower() == reverse(cleared_word).lower():
        return True
    else:
        return False
    
def farewell():
    now = datetime.datetime.now()
    hour = now.hour

    if 6 <= hour < 18:
        print("bonné journée, 愉快的一天") 
    else:
        print("bonné soirée, 晚上好")

def main():
    print(salutation())
    
    while True:
        entry = input("Enter your word: ")
        if(check_plalindrome(entry)):
            print("Bien dit, 你太棒了") 
        else:
            print(reverse(entry))

        if input("Do you want to exit? (y/n): ").lower() == 'y':
            atexit.register(farewell)
            break

main()