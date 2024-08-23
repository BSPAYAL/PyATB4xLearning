#MATCH STATEMENT

# works only when python > 3.10
#WAP to ask user which browser he wants to run automation

browser_name = input("enter the browser name : ")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("no browser found")



#