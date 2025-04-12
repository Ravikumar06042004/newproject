status = 400

match status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")        
