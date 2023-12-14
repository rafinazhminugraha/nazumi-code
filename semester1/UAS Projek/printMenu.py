def printMenu(*menu):
    for i, item in enumerate(menu):
        print(f"[{i+1}] {item.title()}")
        
printMenu("login", "register", "exit")