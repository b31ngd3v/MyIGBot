# MyIGBot &nbsp;![Build Status](https://camo.githubusercontent.com/4e084bac046962268fcf7a8aaf3d4ac422d3327564f9685c9d1b57aa56b142e9/68747470733a2f2f7472617669732d63692e6f72672f6477796c2f657374612e7376673f6272616e63683d6d6173746572)

MyIGBot is a Instagram Private API to like, follow, comment, view & intaract with stories, upload post & stories, get all information about a user/posts and get posts based on locations/hashtags.

  - Easy to use
  - More Powerful Now
  - 2FA Login Support

## New Features!

  - Get information of a user/post.
  - Get posts based on hashtag/location.
  - It also supports proxy now.
  - Added 35+ features on this update.

You can also:
  - Send Story Views
  - Like, Unlike, Comment in a Post
  - Follow, Unfollow User
  - Upload Post and Stories
  - Intaract with Stories
  - Cookie Storing Feature

### Tech

MyIGBot uses a number of open source projects to work properly:

* [Python](https://www.python.org/) - Python is an interpreted, high-level and general-purpose programming language
* [Requests](https://requests.readthedocs.io/en/master/) - to make HTTP requests simpler
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - is a Python package for parsing HTML and XML documents.

And of course MyIGBot itself is open source with a [public repository](https://github.com/b31ngD3v/MyIGBot)
 on GitHub.
 
### Installation

Install MyIGBot from PyPi

```sh
$ pip install myigbot
```
### Usage

Here is how to use MyIGBot (you can also check usage.py)

###### Login Process (if you're account has 2 Factor Auth. The Bot Will Ask You The Code.)

```sh
from myigbot import MyIGBot

bot = MyIGBot('USERNAME', 'PASSWORD')
```
###### Like post

```sh
response = bot.like('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)  # if the response code is 200 that means ok
```
###### Unlike post

```sh
response = bot.unlike('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)  # if the response code is 200 that means ok
```
###### Like Recent post

```sh
response = bot.like_recent('instagram')
print(response)  # if the response code is 200 that means ok
```
###### Comment on post

```sh
response = bot.comment('https://www.instagram.com/p/CH5qV6-so6Y/', comment_text='Nice Post!')
print(response)  # if the response code is 200 that means ok
```
###### Comment on recent post

```sh
response = bot.comment_recent('instagram', comment_text='Nice Post!')
print(response)  # if the response code is 200 that means ok
```
###### Follow user

```sh
response = bot.follow('instagram')
print(response)  # if the response code is 200 that means ok
```
###### Unfollow user

```sh
response = bot.unfollow('instagram')
print(response)  # if the response code is 200 that means ok
```
###### Send story view

```sh
response = bot.story_view('b31ngdev')
print(response)  # if the response code is 200 that means ok
```
###### Upload post

```sh
response = bot.upload_post('image.png', caption='Image 1')
print(response)  # if the response code is 200 that means ok
```
###### Upload Story

```sh
response = bot.upload_story('image2.png')
print(response)  # if the response code is 200 that means ok
```
###### Find posts with hashtags

```sh
response = bot.hashtag_posts('programmershumor', limit=50)
print(response)  # by default the limit is setted to 20, this is a optional parameter
```
###### Find posts with location

```sh
response = bot.location_posts('https://www.instagram.com/explore/locations/6889842/paris-france/', limit=20)
print(response)  # by default the limit is setted to 20, this is a optional parameter
```
###### User post count

```sh
response = bot.user_posts_count('instagram')
print(response)
```
###### User follower count

```sh
response = bot.user_followers_count('instagram')
print(response)
```
###### User follow count

```sh
response = bot.user_follow_count('instagram')
print(response)
```
###### Post like count

```sh
response = bot.like_count('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Post comment count

```sh
response = bot.comment_count('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Get every post's link of a user

```sh
response = bot.user_posts('instagram', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter
```
###### List of username who followed the user

```sh
response = bot.user_followers('instagram', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter
```
###### List of username whom the user follows

```sh
response = bot.user_follows('instagram', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter
```
###### List of username who liked a post

```sh
response = bot.post_likers('https://www.instagram.com/p/CH5qV6-so6Y/', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter
```
###### List of username who commented a post

```sh
response = bot.post_commenters('https://www.instagram.com/p/CH5qV6-so6Y/', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter
```
###### Feed posts of logged in user

```sh
response = bot.feed_posts()
print(response)
```
###### Username of the post owner

```sh
response = bot.post_owner('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Get caption of a post

```sh
response = bot.post_caption('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Get location of a post

```sh
response = bot.post_location('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Get hashtags used in the post

```sh
response = bot.post_hashtags('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Get usernames who are tagged in a post

```sh
response = bot.post_tagged_user('https://www.instagram.com/p/B2fZRgBA2wj/')
print(response)
```
###### Get HD quality Profile Picture download link

```sh
response = bot.user_dp('instagram')
print(response)
```
###### Get bio of a user

```sh
response = bot.user_bio('instagram')
print(response)
```
###### Find the account is private or not

```sh
response = bot.private_user('instagram')
print(response)
```
###### Find the account is verified or not

```sh
response = bot.verified_user('instagram')
print(response)
```
###### Get external url of a username

```sh
response = bot.user_external_url('instagram')
print(response)
```
###### Find the user follows you or not

```sh
response = bot.follows_me('instagram')
print(response)
```
###### Find you follow the user or not

```sh
response = bot.followed_by_me('instagram')
print(response)
```
###### Get video views count

```sh
response = bot.video_views_count('https://www.instagram.com/p/B2XPNNvgApx/')
print(response)
```
###### Get post type (video or picture)

```sh
response = bot.post_type('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
###### Get exact time when the post was posted

```sh
response = bot.post_time('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
```
### Proxy
Here is how to add proxy

#### Method For Authenticated Proxies
```sh
from myigbot import MyIGBot

proxies = {
    'http': 'user:pass@host:port',
    'https': 'user:pass@host:port'
}
bot = MyIGBot('USERNAME', 'PASSWORD', proxy=proxies)
```

#### Method For Non-Authenticated Proxies
```sh
from myigbot import MyIGBot

proxies = {
  'http': 'host:port',
  'https': 'host:port',
}
bot = MyIGBot('USERNAME', 'PASSWORD', proxy=proxies)
```

Buy Me a Coffee
----

<a href="https://www.buymeacoffee.com/b31ngD3v" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height=60px width=217px></a>

License
----

<p>
<img src="https://opensource.org/files/OSIApproved_1.png" alt="OpenSource" height=181px />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/7195e121-eded-45cf-9aab-909deebd81b2/d9ur2lg-28410b47-58fd-4a48-9b67-49c0f56c68ce.png" alt="MIT" height=175px />
</p>

**Free Software, Hell Yeah!**
