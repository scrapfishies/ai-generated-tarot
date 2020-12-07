# AI Generated Tarot

## Designing a new tarot deck with StyleGAN2-ADA and GPT-2

For my final project at Metis, I wanted to explore media creation with artificial intelligence through the lens of tarot. I love the playful juxtaposition of the fortune teller and the data scientist both using storytelling and the preditive power of their tools in their trades.

Tarot cards have been around for _centuries_ and are known for their rich imagery and symbolism. Every visual element of a card is open for interpretation, from the colors to the patterns in clothing. While readings will vary by reader, there is common set of meanings for each card and there are tons of books, websites, and communitities dedicated to the practice.

I decided to create a new set of 22 cards, the number of cards in the Major Arcana, using deep learning. For the card images, I used [Derrick Schultz's forked version of NVIDIA's StyleGAN2-ADA](https://github.com/dvschultz/stylegan2-ada). There's truly an alphabet soup of GANs out there and I chose StyleGAN2-ADA one based on the high quality of results I'd seen that were generated with this model and the availability of reference materials. This project also led me down a wonderful rabbit hole of resources on machine learning for artists and I've linked to a few sites below.

To generate annotations - the cards' interprations and additional questions to ponder - I used [HuggingFace's pre-trained GPT-2 transformer model](https://huggingface.co/transformers/model_doc/gpt2.html). I've wanted to work with text generation models for a while now and was very pleased with GPT-2's ability to generate new card meanings. I then clustered generated texts using a pre-trained word-embeddings model to calculate average document vectors and their cosine similarity scores.

After matching generated images and texts, I created a Twitter bot, [@AITarotBot](https://twitter.com/AITarotBot), that will tweet randomly generated daily readings. Follow and enjoy!

### Workflow & Process

**Data Collection**

- Images scraped from Flickr using the API
  - 14 partial or complete decks
  - approximately 460 unique images
  - 'traditional' or 'classic' deck styles
- Texts gathered through mutliple sources:
  - GitHub
  - Kaggle
  - Various web pages scraped with BeautifulSoup

**Pre-processing**

- Images resized and cropped to 512x512 pixels; oversampled cards from Major Arcana to improve results
- Texts cleaning (punctuation, non-English words, etc.) and formatting using SpaCy

**Model Training**

- Images: leverage transfer learning with StyleGAN2-ADA by NVIDIA
- Texts: Fine tuned GPT-2 transformer model (by HuggingFace) using sourced divination texts

**Content Generation**

- Images: generate 22 unique cards using StyleGAN2-ADA
- Texts: generate card annotations (questions to consider, card interpretations)

**Assembly**

- Texts: group similar questions and interpretations with average document vector similarity using pre-trained Word2Vec model
- Assign card titles, questions, interpreations, and images

**Daily Readings Twitter Bot**

- Create Twitter developer account to access API
- Generate random daily readings with Python using generated deck
- Automate daily tweets with crontab

### Selected Samples

**The Great Invigorating**

![The Great Invigorating](https://github.com/scrapfishies/ai-generated-tarot/blob/main/card_imgs/c09.png?raw=true)

Questions

- When will you realize that in all things "human" experience is basically meaningless?

Interpretations

- Do something today that makes you feel good about yourself.
- You may not think much of yourself but now is ag ood time to look more closely at what you are doing - maybe even thinking!

**The Renewed**

![The Renewed](https://github.com/scrapfishies/ai-generated-tarot/blob/main/card_imgs/c11.png?raw=true)

Questions

- How can I make a more realistic effort to finish a task that has been holding me back?
- Where is it actually possible that I'm making more progress than I have been making?

Interpretations

- Make the effort, and make it work.
- Some people may say that you are desperate but if you make the effort you will find it will pay off in ways you have not anticipated.
- Just make sure you don’t take your time making decisions for other people.
- You can’t change the world, so make the effort and change.

### Evaluation

Overall, I'm quite happy with [the new cards](https://github.com/scrapfishies/ai-generated-tarot/blob/main/notebooks/10_final_tarot_cards.ipynb). I'm impressed with GPT-2's generated meanings and questions, and found clustering with average document vectors to be a very powerful way of organizing the raw output.

StyleGAN2-ADA was able to create some very close replicas of existing cards as well as generate new ones. However, I suspect that tarot cards may be too varied in terms of their visual elements to consistently generate coherent images.

Below we can see StyleGAN2-ADA's attempted reproduction of the Temperance card using the projection feature:

![Projection with StyleGAN2-ADA]()

In addition to continued training and tweaking hyper-parameters, with more time I'd like to explore take advantage of someo of StyleGAN2-ADA's features like style mixing. The latent space offers up seemingly infinite variations.

![Demonstrating interpolation with StyleGAN2-ADA]()

#### Suggestions for Future Work

- Explore other GAN architectures
- Create an interactive tarot reading experience based on user provided input

---

### Tools, technologies, and libraries

#### All purpose

- Google Colab
- Jupyter Notebook
- Python 3
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn

#### Images

- [StyleGAN2-ADA](https://github.com/NVlabs/stylegan2-ada)
- TensorFlow
- Flickr API
- PIL
- imageio

#### Texts

- [GPT-2](https://huggingface.co/gpt2)
- PyTorch
- Gensim
- NLTK
- SpaCy
- BeautifulSoup

#### Twitter Bot

- Tweepy
- Twitter API
- crontab

### Sources & References

#### Inspiration

- [Lynne Yun](http://www.lynneyun.com/)
- [Derrick Schultz - Artificial Images](https://artificial-images.com/)
- [Machine Learning for Artists](https://github.com/ml4a/)

#### Images

- Image Sources
  - [Kaggle: Tarot Deck](https://www.kaggle.com/lsind18/tarot-json)
  - [Flickr (Yoav Ben-Dov)](https://www.flickr.com/photos/48485995@N00/)
  - [Flickr (Sumada Monsarrat)](https://www.flickr.com/photos/sumadas-treasure-box/albums/with/72157650242007982)
- [StyleGAN2-ADA reference](https://www.youtube.com/channel/UCaZuPdmZ380SFUMKHVsv_AA)

#### Texts

- Text Sources
  - [Kaggle: Tarot Deck](https://www.kaggle.com/lsind18/tarot-json)
  - [Additional Tarot Deck](https://github.com/sheoak/tarot-deck)
  - [Horoscopes](https://github.com/dsnam/markovscope)
  - [Fortune Cookies 1](https://github.com/reggi/fortune-cookie)
  - [Fortune Cookies 2](https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/)
  - [Feelings List](https://github.com/lynneyun/Electronic-Rituals)
  - [Kaggle: Magic the Gathering](https://www.kaggle.com/mylesoneill/magic-the-gathering-cards)
  - [Book of Revelation](http://www.readbibleonline.net/)
  - [I Ching](http://the-iching.com/)
  - [Alan Watts Quotes](https://www.goodreads.com/author/quotes/1501668.Alan_W_Watts?page=1)
- [GPT-2 reference](https://medium.com/swlh/fine-tuning-gpt-2-for-magic-the-gathering-flavour-text-generation-3bafd0f9bb93)
