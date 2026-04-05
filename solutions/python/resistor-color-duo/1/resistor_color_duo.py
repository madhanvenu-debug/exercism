def value(colors):
    color_list = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]
    
    first = color_list.index(colors[0])
    second = color_list.index(colors[1])
    
    return first * 10 + second