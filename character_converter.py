import re

def full_to_half_width(text):
    # Define conversion mappings
    fw_to_hw = {
        '０': '0', '１': '1', '２': '2', '３': '3', '４': '4',
        '５': '5', '６': '6', '７': '7', '８': '8', '９': '9',
        'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D', 'Ｅ': 'E',
        'Ｆ': 'F', 'Ｇ': 'G', 'Ｈ': 'H', 'Ｉ': 'I', 'Ｊ': 'J',
        'Ｋ': 'K', 'Ｌ': 'L', 'Ｍ': 'M', 'Ｎ': 'N', 'Ｏ': 'O',
        'Ｐ': 'P', 'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T',
        'Ｕ': 'U', 'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X', 'Ｙ': 'Y',
        'Ｚ': 'Z', 'ａ': 'a', 'ｂ': 'b', 'ｃ': 'c', 'ｄ': 'd',
        'ｅ': 'e', 'ｆ': 'f', 'ｇ': 'g', 'ｈ': 'h', 'ｉ': 'i',
        'ｊ': 'j', 'ｋ': 'k', 'ｌ': 'l', 'ｍ': 'm', 'ｎ': 'n',
        'ｏ': 'o', 'ｐ': 'p', 'ｑ': 'q', 'ｒ': 'r', 'ｓ': 's',
        'ｔ': 't', 'ｕ': 'u', 'ｖ': 'v', 'ｗ': 'w', 'ｘ': 'x',
        'ｙ': 'y', 'ｚ': 'z', '　': ' ', '！': '!', '＂': '"',
        '＃': '#', '＄': '$', '％': '%', '＆': '&', '＇': "'",
        '（': '(', '）': ')', '＊': '*', '＋': '+', '，': ',',
        '－': '-', '．': '.', '／': '/', '：': ':', '；': ';',
        '＜': '<', '＝': '=', '＞': '>', '？': '?', '＠': '@',
        '［': '[', '＼': '\\', '］': ']', '＾': '^', '＿': '_',
        '｀': '`', '｛': '{', '｜': '|', '｝': '}', '～': '~'
    }
    
    # Create a pattern to match full-width characters
    pattern = re.compile('|'.join(map(re.escape, fw_to_hw.keys())))
    
    # Replace full-width characters with half-width characters
    return pattern.sub(lambda x: fw_to_hw[x.group()], text)

# Test the function
test_text = "Ｈｅｌｌｏ， Ｗｏｒｌｄ！ １２３４５"
result = full_to_half_width(test_text)
print(f"Original: {test_text}")
print(f"Converted: {result}")