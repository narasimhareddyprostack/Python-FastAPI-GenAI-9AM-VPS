def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 404 | 403 | 401: # Combine cases using | (OR)
            return "Not allowed"
        case _:
            return "Unknown status"

print(http_status(404))