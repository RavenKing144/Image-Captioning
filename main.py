# Read caption
def readTextFile(path):
  with open(path) as f:
    captions = f.read()
  return captions

captions = readTextFile("/home/skal/Desktop/Data-Science/Image captioning/flickr8k/Flickr_Data/Flickr_Data/Flickr_TextData/Flickr8k.token.txt")
captions = captions.split('\n')[:-1]
print(len(captions))
print(captions[0])
#Dictionary to map list of captions it has with it
description = {}
for i in captions:
  first, second = i.split("\t")
  img_name = first.split(".")[0]
  desc = second
  # if the image id is already present or not
  if description.get(img_name) is None:
    description[img_name] = []
  description[img_name].append(desc)
print(description['1000268201_693b08cb0e'])