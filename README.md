# MyIGBot &nbsp;![Build Status](https://camo.githubusercontent.com/4e084bac046962268fcf7a8aaf3d4ac422d3327564f9685c9d1b57aa56b142e9/68747470733a2f2f7472617669732d63692e6f72672f6477796c2f657374612e7376673f6272616e63683d6d6173746572)

MyIGBot is a Instagram Private API to like, follow, comment, view & intaract with stories and upload post & stories.

  - Easy to use
  - More Features
  - 2FA Login Support

## New Features!

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
