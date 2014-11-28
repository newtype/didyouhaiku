from __future__ import print_function
import json
import codecs
import sys

from haiku import Haiku

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

for line in open('sample'):
  if not line.strip():
    continue

  tweet = json.loads(line)

  if not (tweet.get('lang') and tweet['lang'] == 'en'):
    continue

  try:
    if Haiku(tweet['text']).is_valid():
      print(tweet['text'])
  except:
    print("error: " + tweet['text'], file=sys.stderr)
