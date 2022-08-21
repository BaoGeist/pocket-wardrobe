import random
import pandas as pd
#import tkinter as tk
#import matplotlib
import webcolors
import itertools
from colorharmonies import Color, complementaryColor, triadicColor, splitComplementaryColor, tetradicColor, analogousColor, monochromaticColor
#import database_build
#from tkinter import *
from PIL import Image, ImageTk

def eddie(user_colour = "Blue"):
    #FUNCTION TO DEFINE CLOSEST COLOUR GIVEN RGB
    def closest_coloUr(rgb):
        differences = {}
        for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
            r, g, b = webcolors.hex_to_rgb(color_hex)
            differences[sum([(r - rgb[0])**2, (g - rgb[1])**2, (b - rgb[2])**2])] = color_name
        return differences[min(differences.keys())]

    #FUNCTION TO RETURN RGB GIVEN COLOUR_NAME
    def rgb_get(colour):

        lst_header = ["color", "color_name", "hex", "R", "G", "B"]

        df = pd.read_csv(r'C:\Users\derro\Documents\Code\HT6_2022\fit_chooser\home\colors.csv', names = lst_header)
        df2 = df.loc[df["color_name"] == colour]
        
        return(df2[["R","G","B"]].values.tolist()[0])

    #RECEIVING USER INPUT FOR COLOUR

    user_rgb = rgb_get(user_colour)

    #CREATING COLOUR OBJECT USING COLORHARMONIES
    coloUr_object = Color(user_rgb,"","")

    #CREATING LIST OF POSSIBLE COLOUR THEMES (RGBS)
    possible_rgbs = [complementaryColor(coloUr_object ), triadicColor(coloUr_object )[0], triadicColor(coloUr_object )[1], splitComplementaryColor(coloUr_object )[0], splitComplementaryColor(coloUr_object )[1], tetradicColor(coloUr_object )[0], tetradicColor(coloUr_object )[1], tetradicColor(coloUr_object )[2], analogousColor(coloUr_object )[0], analogousColor(coloUr_object )[1], monochromaticColor(coloUr_object )[0], monochromaticColor(coloUr_object )[1], monochromaticColor(coloUr_object )[2], monochromaticColor(coloUr_object )[3], monochromaticColor(coloUr_object )[4], monochromaticColor(coloUr_object )[5], monochromaticColor(coloUr_object )[6], monochromaticColor(coloUr_object )[7], monochromaticColor(coloUr_object )[8]]

    #INITIALIZE EMPTY LIST FOR COLOUR_NAME STRING
    possible_colours = []

    for i in possible_rgbs:
        possible_colours.append(closest_coloUr(i))
        
    possible_colours.sort()
    possible_colours=list(k for k,_ in itertools.groupby(possible_colours))

    return(possible_colours)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

    