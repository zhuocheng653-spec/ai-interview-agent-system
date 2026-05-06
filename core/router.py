def route_topic(user_input):
    if "redis" in user_input.lower():
        return "Redis"
    elif "mysql" in user_input.lower():
        return "MySQL"
    else:
        return "Algorithm"
