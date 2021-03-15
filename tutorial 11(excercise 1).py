# Date 14-3-2021

# You need to make a programe which takes the input from the user and gives it's meaning to the user
# Use the following 7 words and their meaning to make a Dictionary
# Fluet - Musical Instrument
# Doublet - Close-Fitting upper garment
# Lich - A dead body
# Muslin - A kind of fine thin cotton fabric
# Soffit - Lower part of an arch or balcony
# Thud - A low dull sound
# Vagary - A wild freak

dict1 = {"Fluet": "Musical Instrument",
         "Doublet": "Close-Fitting upper garment",
         "Lich": "A dead body",
         "Muslin": "A kind of fine thin cotton fabric",
         "Soffit": "Lower part of an arch or balcony",
         "Thud": "A low dull sound",
         "Vagary": "A wild freak",
         }

print("To know the meaning of word enter it:")
word = input()
word = word.capitalize()
#  I used capitalize command because python is case sensitive language so no matter that use enters in capital or small
print(dict1.get(word))
