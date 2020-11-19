from myigbot import MyIGBot

bot = MyIGBot('YOUR USERNAME', 'YOUR PASSWORD')

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
