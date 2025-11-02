facebook = True
twitter = False
instagram = True
if facebook:
    if twitter or instagram:
        print("You are a good influencer!")
if instagram:
    if twitter:
        print("You are a good influencer!")

# Check if the person is a good influencer
if (facebook + twitter + instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")