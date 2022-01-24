import random           # Used for random distribution
import numpy as np      # Numpy bangs
import imageio          # imageio is used to generate GIF
import json             # Used to create JSON files
import sqlite3          # SQL Database to ensure unique NFT generation
import os               # Delete the Database on start-up if it exists
from PIL import Image   # Image is used for stitching together images
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" JSON Data to be loaded globally for efficiency """
fid = open('Traits.json')
Data = json.load(fid)
fid.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def NFT(iter, Data):
    uniqueNFT = True

    NFT_id = "{:04d}".format(iter+1)
    while uniqueNFT:
        for i in Data:
            layer_names = list(Data[i].keys())
            layer_probs = list(Data[i].values())
            layer_type = layer_names[np.random.choice(np.arange(len(layer_names)), p=layer_probs)]
            path = f"assets/{i}/{layer_type}.png"

            if i == "Layer_1":
                NFT_image = Image.open(path)
            else:
                NFT_image.paste(Image.open(path), (0, 0), Image.open(path))

        """ Add function to check MetaData to ensure unique NFT (Exclude Background & Border) """
        uniqueNFT = False

    
    NFT_image.putalpha(256) # Allows transparency on exported photo
    NFT_image.save("./out/NFT_"+ NFT_id +".png", quality = 100)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def detComb():
    x = list(Data.keys()); numComb = 1
    for i in x: numComb *= len(list(Data[i].keys()))
    return numComb
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(num, createGIF):
    # Initialize Database
    if os.path.exists('NFT_Database.db'):
        os.remove('NFT_Database.db')
    db = sqlite3.connect('NFT_Database.db')
    cur = db.cursor()
    columns  = ''
    for i in Data:
        columns += f"{i}, "
    
    cur.execute(f"CREATE TABLE Database ({columns[0:len(columns)-2]})")
    db.commit()
    db.close()

    
    # Create the random photo
    for i in range(num):
        NFT(i, Data)
    print(f'NFT Combinations: {detComb()}') # Unique NFT Logistics

    if createGIF:
        fn = 'out/NFT_'
        images = []
        for iter in range(num):
            images.append(imageio.imread(fn + "{:04d}".format(iter+1)+ '.png'))
        imageio.mimsave('out/Compilation.gif', images, fps=3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    main(5, True)
