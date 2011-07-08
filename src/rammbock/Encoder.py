import struct

def object2string(message):
    whole_message =  _generate_message_from_object(message)
    return whole_message

def _generate_message_from_object(message):
    whole_message = ""
    for index, item in enumerate(message.items):
        if item['type'] is 'HEADER':
            whole_message += item['value'] + " "
            if _next_item_is_not(message, index, 'HEADER'):
                whole_message += '\r\n'
        elif item['type'] is 'IE':
            whole_message += item['name'] + ": " + item['value'] + '\r\n'
        elif item['type'] is 'DELIMITER':
            whole_message += item['value']
        elif item['type'] is 'BINARY':
            whole_message += _convert_to_string(item['value'], item['b_format'])
    print repr(whole_message)
    return whole_message

def _next_item_is_not(message, index, name):
    try:
        return message.items[index + 1]['type'] is not name
    except IndexError:
        return False

def _convert_to_string(data, b_format):
    return struct.pack(b_format, int(data))

