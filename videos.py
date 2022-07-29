'''How to download big videos online'''
import requests


# vedio = "https://archive.org/download/After_The_Thin_Man_trailer/After_the_Thin_Man_trailer.mp4"
h = 'https://archive.org/download/After_The_Thin_Man_trailer/After_the_Thin_Man_trailer_512kb.mp4'
repond =  requests.get(h, stream=True) #stream is because the file is am mp4

with open('C:/Users/kuyik/Videos/tt/after.mp4', 'wb') as file:
    for charaters in repond.iter_content(chunk_size=int(11.9*1024)): #1024 multiply by the mb of the vedio detemine the amount og chunk_size used.
        file.write(charaters)

    else:
        print('download successfully')



# with tqdm(
#     unit = 'B'.unit_scale=True.unit_divisor=1024
#     ministers=1
#     dwsc = eg_scale.total=int(response.headers)
# )