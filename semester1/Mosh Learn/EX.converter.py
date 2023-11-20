# text_to_emote = {
#     ":)": "😊",
#     ":(": "😔"    
# }
# text_massage = input("> ").split(" ")
# output = ""

# for word in text_massage:
#     output += text_to_emote.get(word,word) + " "
    
# print(output)

def emoji_coverter(emoji):
    text_to_emote = {
    ":)": "😊",
    ":(": "😔"    
}
    output = ""
    
    for converter in emoji:
        output += text_to_emote.get(converter, converter) + " "
    
    return output

massage = input("> ").split(" ")
print(emoji_coverter(massage))