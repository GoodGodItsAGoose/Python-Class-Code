class Slicing: #(start,stop,step)
    websiteurl = "https://google.com" #Breaking this into "https://" and "google"
    slice = slice(8,-4)#because all website names are not the same, so you can use the "negative index", all characters have a positive and negative index, so from the ending of the website, it counts as m=-1, o=-2, c=-3, and so on.
    print(websiteurl[slice])