from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.CYAN + "Це блакитний текст")
print(Back.MAGENTA + "Це текст на фіолетовому фоні")
print(Style.BRIGHT + Fore.YELLOW + "Це яскравий жовтий текст")
print("Цей текст буде звичайним, бо використовується autoreset=True")
print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Це текст на зеленому фоні')
print(Style.DIM + 'Це текст прозоріший')
print(Style.BRIGHT + 'Це текст насичений')
print(Style.RESET_ALL + 'Це текст звичайний')
