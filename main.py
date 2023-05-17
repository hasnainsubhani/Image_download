
import os
import pandas as pd
import os


def import_image():
    dir_list = next(os.walk('s3_samples'))[1]

    df = pd.read_excel('data_3427.xlsx')

    membid = df['FF_MemberId']
    photoid = df['photoid']
    urls = df['picture']
    nationalid = urls[0].split('/')[0]

    for dir in dir_list:
        for i in range(0,len(urls)):
            #print(urls[i])
            try:

                url_part = str(urls[i]).split('/')

                if dir == url_part[0]:
                    #print(i)
                    filename = "images_new/" + str(membid[i]) + "/Thumbnail/" + str(photoid[i]) + "." +  url_part[1].split('.')[-1]
                    if not os.path.exists("images_new/" + str(membid[i]) + "/Thumbnail"):
                        os.makedirs("images_new/" + str(membid[i]) + "/Thumbnail")

                    os.replace("S3_Samples/"+ urls[i], "images_new/" + str(membid[i]) + "/Thumbnail/" + url_part[1])

                    os.rename("images_new/" + str(membid[i]) + "/Thumbnail/" + url_part[1],"images_new/" + str(membid[i]) + "/Thumbnail/" + str(photoid[i]) + "." +  url_part[1].split('.')[-1])
            except:
                pass




if __name__=="__main__":
    import_image()
