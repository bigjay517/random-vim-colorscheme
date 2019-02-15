import os
import random
import sys

if __name__ == '__main__':

    # Get a list of installed color schemes  
    thispath = os.path.dirname(os.path.realpath(__file__))     

    colorpath = os.path.join(thispath,"colors")
    installed_colors = set([c.split('.vim')[0] for c in os.listdir(colorpath) if '.vim' in c])
    installed_colors = set([c for c in installed_colors if len(c)>0])

    # Get our list of favorites
    with open(os.path.join(thispath,'favorite_colors.txt')) as f:
        favorite_colors = set(f.read().splitlines())
    favorite_colors = set([f for f in favorite_colors if len(f)>0])
    
    # Find all favorites that are installed
    installed_favorites = favorite_colors.intersection(installed_colors)
    
    # Randomly select a colorscheme 
    colorscheme = random.sample(installed_favorites,1)[0]

    print(colorscheme)
    sys.exit(0)
    
    

