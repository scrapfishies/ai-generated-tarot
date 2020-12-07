'''
Twitter Postings for I GAN't Believe It's Not Tarot!

Creates a daily reading -- sampling from the 22 AI Generated Tarot Cards
* Reading: 1 question or interpretation from the card texts
* Card image
'''

### IMPORTS ###
import os
import random
import json
import pandas as pd
import tweepy


def daily_tarot_reading():

    # Twitter keys to access API
    twitter_keys = {
        'consumer_key':        '---YOUR KEYS HERE---',
        'consumer_secret':     '---YOUR KEYS HERE---',
        'access_token_key':    '---YOUR KEYS HERE---',
        'access_token_secret': '---YOUR KEYS HERE---'
    }

    # Setting up access to API
    auth = tweepy.OAuthHandler(
        twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(
        twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

    api = tweepy.API(auth)

    # Retrieve card texts
    text_file = open('ai-generated-tarot/data_files/named_cards.json',)
    cards = json.load(text_file)

    # card images in directory
    # Note: these are the square images (no crop, border adjustments)
    # these present better on twitter than the tall rectangular versions
    path = os.getcwd() + '/data_files/final_cards'
    card_imgs = [f for f in sorted(os.listdir(path)) if f[-3:] == 'png']

    # sets up pandas dataframe with everything neatly in one place
    df = pd.DataFrame(cards)
    df = df.T
    df.reset_index(inplace=True)
    df.columns = ['name', 'questions', 'interpretations']
    df['imgs'] = card_imgs

    # pull a random reading
    card = df.sample(n=1).reset_index(drop=True)

    # set up reading variables
    name = card.loc[0, 'name']
    questions = card.loc[0, 'questions']
    meanings = card.loc[0, 'interpretations']
    text_list = questions + meanings

    # Get image
    img_file = card.loc[0, 'imgs']
    img_path = f'{path}/{img_file}'

    # Pick random question or interpretation
    reading = random.sample(text_list, 1)[0]

    # set up tweet text
    tweet_text = f'{name}: {reading}'

    # set up tweet format
    tweet = f"Today's reading...\n{tweet_text}"
    media = api.media_upload(img_path)

    # Post Tweet!
    api.update_status(status=tweet, media_ids=[media.media_id])


if __name__ == "__main__":
    daily_tarot_reading()
