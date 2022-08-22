# pocket-wardrobe

🏆 **Top 8 finalist competing amongst 300 others for Hack The 6ix 2022**  
🏆 **Winner of Best use of AI**

## Inspiration  
Some of the most famous people wear the same clothes every day: Steve Jobs, Mark Zuckerburg, Baoze Lin, 
Derron Li, and while I would love to be famous, I rather, you know, not wear the same clothes every day; fashion is important. Just kidding. 
But on a serious note, how many of you struggle to put together an outfit every day? It’s a frustration we all share at some point in our lives, and 
that’s exactly what pocket wardrobe aims to solve.

## What it does
Pocket wardrobe provides suggestions of outfits based on different colour harmonies. The user uploads images of their clothing and inputs a specific 
colour that they’d like to centre their outfit around, while the web app then provides an outfit for the user, with matching colours. However, pocket wardrobe 
does much more than the explanation prior may reveal. The web app identifies the type of clothing and the dominant colour from each photo, produces a colour 
harmony/palette given the user input, and outputs a complete outfit that matches these colours. 

## How it was built
In order to maximise progress, coding was completed in parallel before linking all together in a Django framework for the backend with an HTML and CSS frontend.
Tensorflow and Keras datasets were used to train a neural network to identify articles of clothing. Clothing images were then used as input to obtain the clothing type, The result was then passed off to the database. 

**colour getting**  
The next task was to categorise each article of clothing based on its main and dominant colour. OpenCV was used to modify and produce a transparent png, while other libraries such as ColorThief was then used to identify the rgb values of the dominant colour.

**django framework**  
The database was built on Django models. Each entry in the database stores an image, its associated colour and clothing type. The justification for using Django was so that the database entries may be easily queried and rendered to the frontend. 

**colour palette**  
After the user inputs a specific colour, the library Color Harmonies then outputs a list for a colour palette consisting of complementary, triadic, monochrome, and numerous other matching hues,

**database queries**  
With a colour palette now generated and the database primed to go, the database is queried for all objects with colours matching that of the palette. This new queryset is then filtered into separate objects based on individual clothing types (shirts, pants, etc.). Finally, a single database entry is randomly taken from each clothing type and passed to the frontend to be rendered.

**rendering frontend**  
The frontend was preliminarily built in HTML/CSS where page layouts and functionalities were initially built separately. The Django backend was integrated at the very end. Django HTML was utilized to implement frontend logic as python syntax can be written directly in HTML files. 

## Software components
**Front End: HTML, CSS**  
**Back End: Python, Django, Tensorflow, OpenCV**

## Challenges we ran into
Quite frankly, one of the hardest challenges we faced was right at the beginning, while installing all our libraries and frameworks; installing Tensorflow was a pain, modules seemed to be missing, and React was threatening to burn down one of our laptops. Besides that, we truly struggled with concept/idea generation, our ideas and thoughts going everywhere and nowhere, ending up with proposals such as “shower too hot” and “can't hear my mom when she calls me for dinner,” somehow. We also had to work around the issue of photos of clothing against a white background, as only those against black backgrounds were accurate for clothing identification at the beginning. Working with colours was difficult too; we had no idea how to generate colour harmonies, until a few hours later when we stumbled upon one life-saving Python library.

## Accomplishments that we're proud of
As newbies in the treacherous world of hackathons, we had never built large scale projects in a team setting before. Ultimately, designing such a complex system and being able to integrate our individual parts in the end was something we were very surprised to see. Collaborating efficiently by dividing up tasks while still understanding everyone else’s parts was vital to our success in the project. Especially given such a short amount of time, we all had a major sigh of relief when we saw all the puzzle pieces fit together into something that we would have never imagined was possible in 36 hours

## What we learned
All three of us entered this hackathon on varying levels of experience in varying areas of engineering/computer science, which provided us the opportunity to work on what we were more familiar with, but also to explore areas we haven’t quite delved into previously. Tensorflow and OpenCV were definitely new for all of us, and certainly a fun challenge to tackle. Web development with HTML and CSS was also an area we weren’t as comfortable with, and despite the frustration and confusion of organising our divs, it was absolutely satisfying to see the final product. 

## What's next 
There is so much we would love to add and integrate into future prototypes. The first of which is a greater accuracy in identifying the specific article of clothing while increasing the number of clothing types it can analyse. Currently the web app can only detect one main colour of each clothing, but we definitely hope to add the ability to classify numerous colours on a single piece of clothing. Furthermore the resolutions of each image are reduced to 28 by 28 pixels, and so higher resolution imaging is another aspect we hope to accomplish. Lastly, as the name suggests, we have to make the pocket wardrobe truly a pocket wardrobe (who carries a laptop in their pocket?) by developing a mobile application. All this will provide greater functionality and easier accessibility within an user’s day-to-day lives.  

