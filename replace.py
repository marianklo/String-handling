# Save the sentence : “The!quick!brown!fox!jumps!over!the!lazy!dog!.” as a single string.
# Reprint this sentence as “The quick brown fox jumps over the lazy dog.” using the replace() function to replace every “!” exclamation mark with a blank space.
# Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” using the upper() function
# Print the sentence in reverse.

single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
rep_single_string = (single_string.replace("!" , " ")) 
print(rep_single_string)     # Print sentence without the ! sign ; The quick brown fox jumps over the lazy dog
upper_sentence = rep_single_string.upper()
print(upper_sentence)   # Print all upper case of sentence ; THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
rev_sentence = upper_sentence[::-1]
print(rev_sentence)     # Print reverse sentence ; GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT