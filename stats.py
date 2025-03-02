def get_book_word_count(text):
   words = len(text.split())
   return words

def character_count(text):
   word_count={}
   for letter in text.lower():
      if letter in word_count:
         word_count[letter] += 1
      else:
         word_count[letter] = 1
   return word_count

def sort_on(dict):
    return dict["number"]
