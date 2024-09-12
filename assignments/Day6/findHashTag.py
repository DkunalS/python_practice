import re

def extract_hashtags(post):
    regex = r'#\w{4,}'
    
    hashtags = re.findall(regex, post)
    
    hash_small= {hashtag.lower() for hashtag in hashtags}
    
    return hash_small

blog = """
Loving the #Python programming language! #coding is fun, but #DAI and #DBDA are a challenge. 
Still, #Python and #PYTHON are awesome! #ai and #machinelearning are the future!
"""

hashtags = extract_hashtags(blog)

print("Extracted hashtags :")
for hashtag in hashtags:
    print(hashtag)
