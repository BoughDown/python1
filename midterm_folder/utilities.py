def room_list(items):
    """Returns how many items there are in a room in a list format."""
    if len(items) == 0:
        return None
    elif len(items) == 1:
        return f'{items[0].name}'
    elif len(items) == 2:
        return f'{items[0].name} and {items[1].name}'
    # else:
    #     return_string = ''
    #     for item in items[:-1]:
    #         return_string += item.name + ', '
    #     return_string += f'and {items[-1].name}'
    #     return return_string