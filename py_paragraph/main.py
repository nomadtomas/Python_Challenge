import re
#re stands for regular expressions

with open('paragraph_2.txt', 'r') as regfile:
    
    readtxt = regfile.read()
    
    word_count = len(re.findall(r'\w+', readtxt))
    sent_count = len(re.findall(r'\.', readtxt))
    sent_pattern = re.compile(r'([^.!?]+[.!?]+)')
    word_pattern = re.compile(r'(\S+)')
    
    sentences = sent_pattern.findall(readtxt)
    
    sent_length = 0
    for match in sentences:
        sent_wrd_length = word_pattern.findall(match)
        sent_length += len(sent_wrd_length)
        
    avg_sent_length = sent_length/sent_count
    
    words = word_pattern.findall(readtxt)
    
    avg_word_length = sum([len(word) for word in words])/len(words)
    
    print("Paragraph Analysis")
    print("-----------------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sent_count}")
    print(f"Average Letter Count: {round(avg_word_length,2)}")
    print(f"Average Sentence Length: {round(avg_sent_length,2)}")