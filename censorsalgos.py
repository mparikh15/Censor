def censor(email, phrase):
  if phrase in email:
    new_message = email.replace(phrase, "REDACTED")
    return new_message

#print(censor(email_one, "learning algorithms"))

## Task 3 
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(email_two)
def censor_mult(email, banned_words):
  new_message = email.lower()
  for word in banned_words:
    if word in new_message:
      new_message = new_message.replace(word, "REDACTED")
    else:
      continue
  return new_message.title()

#print(censor_mult(email_two, proprietary_terms))



## Task 3 

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable", "developments"]


def tone_censor(email, banned_words, tone):
  new_message = email.lower()
  holder = []
  for item in tone:
    #print(item)
    #print(new_message.count(item))
    if new_message.count(item) > 1:
      holder.append(item)
    else: 
      continue
      
  for word in banned_words:
    if word in new_message:
      new_message = new_message.replace(word, "REDACTED")
    else:
      continue
  for word in holder:
    if word in new_message: 
      new_message = new_message.replace(word, "REDACTED FOR TONE")
    else:
        continue
  return new_message.title()
  
