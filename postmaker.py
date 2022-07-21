
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
cwd = os.getcwd()

class PostMaker:
    def __init__(self, utctime,text,title,instanceid):


        im = Image.new(mode="RGB", size=(607, 350),
                   color=(25, 25, 25))

        t1 = ImageDraw.Draw(im)
        myFont = ImageFont.truetype('IBMPlexSans-Text.otf',30 )

        lines = textwrap.wrap(title, width=40)
        y_text = 120
        for line in lines:
            width, height = myFont.getsize(line)
            t1.text(((600 - width) / 2, y_text), line,font=myFont, align="center",fill=(215,218,220))
            y_text += height

        im1 = Image.new(mode="RGB", size=(607, 350),
                       color=(25, 25, 25))

        t2 = ImageDraw.Draw(im1)
        myFont1 = ImageFont.truetype('IBMPlexSans-Text.otf', 20)

        lines1 = textwrap.wrap(text, width=60)
        y_text1 = 50
        for line1 in lines1:
            width1, height1 = myFont.getsize(line1)
            t2.text(((860 - width1) / 2, y_text1), line1, font=myFont1, align="center", fill=(215, 218, 220))
            y_text1 += height1
        # drawing text size
        #t1.text((50, 120), text,font=myFont, align="left",fill=(215,218,220))

        # this will show image in any image viewer
        im.save(cwd + '/data/images/'+instanceid+'title.png')
        im1.save(cwd + '/data/images/'+instanceid+'text.png')