import translators as ts
import msvcrt

def language_main():
    print("[+] enter language key.")
    language = input(">> ").lower()
    translator = "google"


    print("successfully. Enter the word you want to translate.")
    word = input(">> ").lower()
    print("[+] translating...")
    result = ts.translate_text(word, translator = translator, from_language = "auto", to_language = language)
    print(f"[+] Result: {result}")
    print("\n[!] Press any key to exit")
    msvcrt.getch()
    
    if language == "exit":
        print("[!] Exit")
        exit
    
    if word == 'exit':
        print("[!] Exit")
        exit