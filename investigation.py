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
    haiku = Haiku(tweet['text'])
    if haiku.is_valid():
      print(haiku.formatted())
  except Exception as e:
    print("error: " + tweet['text'], file=sys.stderr)
    print(e, file=sys.stderr)
