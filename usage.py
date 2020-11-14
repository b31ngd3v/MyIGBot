from MyIGBot import MyIGBot

bot = MyIGBot('bjvj87', 'qwertypad09')

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
d=bot.comment('URL')
print(d)

# comment on the recent post of user
e=bot.comment_recent('USERNAME')
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
