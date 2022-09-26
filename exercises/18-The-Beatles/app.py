# Your code here!!
def sing():
    song = ''
    for x in range(12):
        if x == 4:
            song += 'whisper words of wisdom, '
        elif x == 10:
            song += 'there will be an answer, '
        elif x == 11:
            song += 'let it be'
        else:
            song += 'let it be, '
    return song

print(sing())
        
