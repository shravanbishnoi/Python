""" 
Functions for Assignment A3

This file contains the functions for the assignment.

NAME - SHRAVAN RAM
DATE - 17/02/2023
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    value = float(value)  # typecasting to float
    if value<10:
        value = str(round(value, 3))
    elif 10<=value<100:
        value = str(round(value, 2))
    elif 100<=value<1000:
        value = str(round(value, 1))

    # if string length is less than 5 characters then expanding it to 5
    final_value = value
    var = len(value)
    while var<5:
        final_value += '0'
        var += 1
    return final_value


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    # extracting numbers from given object and passing them as arguments in the function call str5(value)
    value_c = str5(cmyk.cyan)
    value_m = str5(cmyk.magenta)
    value_y = str5(cmyk.yellow)
    value_k = str5(cmyk.black)

    return '('+ value_c + ', '+ value_m + ', ' + value_y + ', ' + value_k + ')'


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    # extracting numbers from given object and passing them as arguments in the function call str5(value)
    value_h = str5(hsv.hue)
    value_s = str5(hsv.saturation)
    value_v = str5(hsv.value)
    return '('+ value_h + ', '+ value_s + ', ' + value_v + ')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # compressing values in the range 0 and 1 by dividing 255.0
    value_r = rgb.red/255.0
    value_g = rgb.green/255.0
    value_b = rgb.blue/255.0
    black_k = 1 - max(value_r, value_g, value_b)

    # checks if k is 1 then other three attributes become 0
    if black_k==1.0:
        result = introcs.CMYK(0.0, 0.0, 0.0, black_k*100.0)
    # conversion using formulae
    else:
        cyan = ((1 - value_r - black_k)/(1 - black_k))*100.0
        magenta = ((1 - value_g - black_k)/(1 - black_k))*100.0
        yellow = ((1 - value_b - black_k)/(1 - black_k))*100.0
        result = introcs.CMYK(cyan, magenta, yellow, black_k*100.0)  # instantiation of CMYK object with above values
    return result


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # Expanding values to range 0 to 255 by first commpressing to range 0.0 to 1.0 and then multiply by 255.0
    value_r = round(((1-cmyk.cyan/100)*(1-cmyk.black/100)) * 255.0)
    value_g = round(((1-cmyk.magenta/100)*(1-cmyk.black/100))*255.0)
    value_b = round(((1-cmyk.yellow/100)*(1-cmyk.black/100))*255.0)

    result = introcs.RGB(value_r, value_g, value_b)   # instantiation of RGB object with above values
    return result


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # compressing values in the range 0 and 1 by dividing 255.0
    value_r = rgb.red/255.0
    value_g = rgb.green/255.0
    value_b = rgb.blue/255.0
    M = max(value_r, value_g, value_b)  # maximum value
    m = min(value_r, value_g, value_b)  # minimum value

    # Calculating Hue
    if M==m:
        hue = 0.0
    elif M==value_r and value_g>=value_b:
        hue = (60.0*(value_g - value_b))/(M - m)
    elif M==value_r and value_g<value_b:
        hue = ((60.0*(value_g - value_b))/(M - m)) + 360.0
    elif M==value_g:
        hue = ((60.0*(value_b - value_r))/(M - m)) + 120.0
    elif M==value_b:
        hue = ((60.0*(value_r - value_g))/(M - m)) + 240.0

    # Calculating Saturation
    if M==0:
        saturation = 0.0
    else:
        saturation = 1 - m/M
    # attribute value is equal to max
    value = M
    return introcs.HSV(hue, saturation, value)  # Instantiating and returning final HSV object


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    # computing some values which is required for conversion
    hue = hsv.hue//60
    f = (hsv.hue/60) - hue
    p = hsv.value*(1 - hsv.saturation)
    q = hsv.value*(1 - (f*hsv.saturation))
    t = hsv.value*(1 - ((1 - f)*hsv.saturation))

    # Computing value of red, green, blue attributes of RGB
    if hue==0:
        red = hsv.value
        green = t
        blue = p
    elif hue==1:
        red = q
        green = hsv.value
        blue = p
    elif hue==2:
        red = p
        green = hsv.value
        blue = t
    elif hue==3:
        red = p
        green = q
        blue = hsv.value
    elif hue==4:
        red = t
        green = p
        blue = hsv.value
    elif hue==5:
        red = hsv.value
        green = p
        blue = q
    return introcs.RGB(round(red*255), round(green*255), round(blue*255))   # returning the final RGB object


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    x = value
    c = contrast
    if c==1:
        if x >= 0.5:
            y = 1
        else:
            y = 0
    elif -1 <= c < 1:
        if x < (0.25 + 0.25*c):
            y = ((1 - c)/(1 + c))*x
        elif x > (0.75 - 0.25*c):
            y = ((1 - c)/(1 + c))*(x-((3 - c)/4)) + ((3 + c)/4)
        else:
            y = ((1 + c)/(1 - c))*(x-((1 + c)/4)) + ((1 - c)/4)
    return y  # returning final y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    # Modifying attributes red, green, blue according to the contrast given
    rgb.red = round((contrast_value((rgb.red/255.0), contrast))*255)
    rgb.green = round((contrast_value((rgb.green/255.0), contrast))*255)
    rgb.blue = round((contrast_value((rgb.blue/255.0), contrast))*255)