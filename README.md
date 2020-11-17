# MyIGBot

![Build Status](https://camo.githubusercontent.com/4e084bac046962268fcf7a8aaf3d4ac422d3327564f9685c9d1b57aa56b142e9/68747470733a2f2f7472617669732d63692e6f72672f6477796c2f657374612e7376673f6272616e63683d6d6173746572)

MyIGBot is a Instagram Private API to like, follow, comment, view & intaract with stories and upload post & stories.

<div style="clear: both;">
  <div style="float: left; margin-right 1em;">
    <img src='https://raw.githubusercontent.com/b31ngD3v/MyIGBot/main/Screenshot_20201117-112159.png' alt='' height='800' />
  </div>
  <div>
    <h2>Some title text</h2>
    <p>Some more text that will appear to the left of the image.</p>
  </div>
</div>


  - Easy to use
  - More Features
  - 2FA Login Support

# New Features!

  - Upload Post and Stories
  - Intaract with Stories
  - Cookie Storing Feature

You can also:
  - Send Story Views
  - Like, Unlike, Comment in a Post
  - Follow, Unfollow User

### Tech

MyIGBot uses a number of open source projects to work properly:

* [Python](https://www.python.org/) - Python is an interpreted, high-level and general-purpose programming language
* [Requests](https://requests.readthedocs.io/en/master/) - to make HTTP requests simpler
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - is a Python package for parsing HTML and XML documents.
* [Numpy](https://numpy.org/) - is the core library for scientific computing in Python.

And of course MyIGBot itself is open source with a [public repository](https://github.com/b31ngD3v/MyIGBot)
 on GitHub.

### Installation

Install MyIGBot from PyPi

```sh
$ pip install myigbot
```
### Usage

Here is how to use MyIGBot

```sh
from myigbot import MyIGBot

bot = MyIGBot('USERNAME', 'PASSWORD')  # Login Information (if you're account has 2 Factor Auth. The Bot Will Ask You The Code.)

# like post
a=bot.like('URL')
print(a)

# like recent post of user
b=bot.like_recent('USERNAME')
print(b)

# unlike post
c=bot.unlike('URL')
print(c)

# comment on post
d=bot.comment('URL', comment_text='YOUR COMMENT')
print(d)

# comment on the recent post of user
e=bot.comment_recent('USERNAME', comment_text='YOUR COMMENT')
print(e)

# follow the user
f=bot.follow('USERNAME')
print(f)

# unfollow the user
g=bot.unfollow('USERNAME')
print(g)

# send story view to user
h=bot.story_view('USERNAME')
print(h)

# vote story poll 
i=bot.story_poll('USERNAME')  # by default poll vote is setted to random
print(i)

j=bot.story_poll('USERNAME', poll_vote=1) # poll_vote can only be 0 or 1
print(j)

# send response to story question sticker
k=bot.story_question('USERNAME')  # by default question response is setted to random
print(k)

l=bot.story_question('USERNAME', question_response="wht's up dude ?")
print(l)

# swipe the story slider
m=bot.story_slider('USERNAME')  # by default slider value is setted to random
print(m)

n=bot.story_slider('USERNAME', slider_value=55) # slider_value can only be between 0 and 100
print(n)

# answer the story quiz
o=bot.story_quiz('USERNAME')  # by default quiz answer is setted to random
print(o)

p=bot.story_quiz('USERNAME', quiz_answer=2)
print(p)

# interact with all types of stories
q=bot.intaract_with_stories('USERNAME') # by default all values are setted to random
print(q)

r=bot.intaract_with_stories('USERNAME', poll=True, quiz=True, slider=True, question=True, poll_vote='random', quiz_answer='random',question_response='random', slider_value='random')  # default values
print(r)

# upload post
s=bot.upload_post('photo.jpg', caption='Sample Photo')
print(s)

# upload story
t=bot.upload_story('story.jpg')
print(t)
```

License
----

<p>
<img src="https://opensource.org/files/OSIApproved_1.png" alt="OpenSource" height=180px />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/7195e121-eded-45cf-9aab-909deebd81b2/d9ur2lg-28410b47-58fd-4a48-9b67-49c0f56c68ce.png" alt="MIT" height=175px />
</p>

**Free Software, Hell Yeah!**
