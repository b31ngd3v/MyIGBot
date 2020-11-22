from myigbot import MyIGBot

bot=MyIGBot('pup.shot', 'qwertypad098')

response = bot.like('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)  # if the response code is 200 that means ok

response = bot.unlike('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)  # if the response code is 200 that means ok

response = bot.like_recent('instagram')
print(response)  # if the response code is 200 that means ok

response = bot.comment('https://www.instagram.com/p/CH5qV6-so6Y/', comment_text='Nice Post!')
print(response)  # if the response code is 200 that means ok

response = bot.comment_recent('instagram', comment_text='Nice Post!')
print(response)  # if the response code is 200 that means ok

response = bot.follow('instagram')
print(response)  # if the response code is 200 that means ok

response = bot.unfollow('instagram')
print(response)  # if the response code is 200 that means ok

response = bot.story_view('b31ngdev')
print(response)  # if the response code is 200 that means ok

response = bot.upload_post('image.png', caption='Image 1')
print(response)  # if the response code is 200 that means ok

response = bot.upload_story('image2.png')
print(response)  # if the response code is 200 that means ok

response = bot.hashtag_posts('programmershumor', limit=50)
print(response)  # by default the limit is setted to 20, this is a optional parameter

response = bot.location_posts('https://www.instagram.com/explore/locations/6889842/paris-france/', limit=20)
print(response)  # by default the limit is setted to 20, this is a optional parameter

response = bot.user_posts_count('instagram')
print(response)

response = bot.user_followers_count('instagram')
print(response)

response = bot.user_follow_count('instagram')
print(response)

response = bot.like_count('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.comment_count('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.user_posts('instagram', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter

response = bot.user_followers('instagram', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter

response = bot.user_follows('instagram', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter

response = bot.post_likers('https://www.instagram.com/p/CH5qV6-so6Y/', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter

response = bot.post_commenters('https://www.instagram.com/p/CH5qV6-so6Y/', limit=50)
print(response)  # by default the limit is setted to 50, this is a optional parameter

response = bot.feed_posts()
print(response)

response = bot.post_owner('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.post_caption('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.post_location('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.post_hashtags('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.post_tagged_user('https://www.instagram.com/p/B2fZRgBA2wj/')
print(response)

response = bot.user_dp('instagram')
print(response)

response = bot.user_bio('instagram')
print(response)

response = bot.private_user('instagram')
print(response)

response = bot.verified_user('instagram')
print(response)

response = bot.user_external_url('instagram')
print(response)

response = bot.follows_me('instagram')
print(response)

response = bot.followed_by_me('instagram')
print(response)

response = bot.video_views_count('https://www.instagram.com/p/B2XPNNvgApx/')
print(response)

response = bot.post_type('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)

response = bot.post_time('https://www.instagram.com/p/CH5qV6-so6Y/')
print(response)
