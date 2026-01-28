import re

def mask(card):
    separator = re.search(r'[-\s]', card)
    sep_char = separator.group() if separator else ''
    
    # Split by any separator
    parts = re.split(r'[-\s]+', card)
    
    # Mask all parts except the last one
    masked_parts = ['*' * len(part) for part in parts[:-1]]
    masked_parts.append(parts[-1])

    return sep_char.join(masked_parts)


print(mask("4012-8888-8888-1881"))
print(mask("4012 8888 8888 1881"))