###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i=0
j=0

# Count vowels in the text
#for char in text:
#   if char in vowels:
#      vowel_count += 1
while i!=len(text):
    if text[i]==vowels[j]: #if letter is a vowel
        vowel_count+=1 # we count it  
        i+=1 # take next letter
        j=0 # reset the position of letter
    elif j>6: # if we tried all vowels
        i+=1    #try next letter
        j=0
    else:
        j+=1
print(f"The number of vowels in the text is: {vowel_count}")
