color=input("enter color:")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("look")
    case "Red":
        print("stop")
    case _:
        print("Wrong color")
        