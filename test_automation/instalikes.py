from instapy import InstaPy

insta_username = 

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# set up all the settings
session.set_relationship_bounds(enabled=True,
                 potency_ratio=-1.21,
                  delimit_by_numbers=True,
                   max_followers=4590,
                    max_following=5555,
                     min_followers=45,
                      min_following=77)
session.set_do_comment(True, percentage=10)
session.set_comments(['Amazing!', 'Lit!', 'Inspired!'])
session.set_dont_include(['friend1', 'friend2', 'friend3'])
session.set_dont_like(['pizza', 'girl'])

# do the actual liking
session.like_by_tags(['BBNAIJA', 'Nigerian Music'], amount=100)

# end the bot session
session.end()