"""
Steganography methods for the imager application.

This module provides all of the test processing operations (encode, decode) 
that are called by the application. Note that this class is a subclass of Filter. 
This allows us to layer this functionality on top of the Instagram-filters, 
providing this functionality in one application.

Based on an original file by Dexter Kozen (dck10) and Walker White (wmw2)

NAME- SHRAVAN RAM
DATE- 09/04/2023
"""
import a6filter


class Encoder(a6filter.Filter):
    """
    A class that contains a collection of image processing methods
    
    This class is a subclass of Filter.  That means it inherits all of the 
    methods and attributes of that class too. We do that separate the 
    steganography methods from the image filter methods, making the code
    easier to read.
    
    Both the `encode` and `decode` methods should work with the most recent
    image in the edit history.
    """
    
    def encode(self, text):
        """
        Returns True if it could hide the text; False otherwise.
        
        This method attemps to hide the given message text in the current 
        image. This method first converts the text to a byte list using the 
        encode() method in string to use UTF-8 representation:
            
            blist = list(text.encode('utf-8'))
        
        This allows the encode method to support all text, including emoji.
        
        If the text UTF-8 encoding requires more than 999999 bytes or the 
        picture does  not have enough pixels to store these bytes this method
        returns False without storing the message. However, if the number of
        bytes is both less than 1000000 and less than (# pixels - 10), then 
        the encoding should succeed.  So this method uses no more than 10
        pixels to store additional encoding information.
        
        Parameter text: a message to hide
        Precondition: text is a string
        """
        # You may modify anything in the above specification EXCEPT
        # The first line (Returns True...)
        # The last paragraph (If the text UTF-8 encoding...)
        # The precondition (text is a string)
        assert type(text)==str, repr(text) + ' is not a string'

        blist = list(text.encode('utf-8'))          # text to list of integers
        image = self.getCurrent()
        if len(blist)>(len(image)-10) or len(blist)>999999:
            return False
        for number in range(len(blist)+4):
            if number==0:                       # for encoding detect msg('y' if present)
                red = ((image[number][0])//10)*10 + 1
                green = ((image[number][1])//10)*10 + 2
                blue = ((image[number][2])//10)*10 + 1
            elif number==1:                       # for encoding detect msg('e' if present)
                red = ((image[number][0])//10)*10 + 1
                green = ((image[number][1])//10)*10 + 0
                blue = ((image[number][2])//10)*10 + 1

            elif number<4:                  # encoding length of the message list
                if len(blist)<=1000 and number==2:
                    red = ((image[number][0])//10)*10 + 0
                    green = ((image[number][1])//10)*10 + 0
                    blue = ((image[number][2])//10)*10 + 0

                else:
                    red = ((image[number][0])//10)*10 + len(blist)//100
                    green = ((image[number][1])//10)*10 + (len(blist)//10)%10
                    blue = ((image[number][2])//10)*10 + len(blist)%10

            else:                               # for encoding msg to be conveyed
                num = int(blist[number-4])
                red = ((image[number][0])//10)*10 + num//100
                green = ((image[number][1])//10)*10 + (num//10)%10
                blue = ((image[number][2])//10)*10 + num%10
                
                # ensuring green and blue values be in range(0-255)
                if green>255:
                    green = green - 10
                if blue>255:
                    blue = blue - 10
            image[number] = (red, green, blue) # modifies pixel with updated pixel
        return True

    def decode(self):
        """
        Returns the secret message (a string) stored in the current image. 
        
        The message should be decoded as a list of bytes. Assuming that a list
        blist has only bytes (ints in 0.255), you can turn it into a string
        using UTF-8 with the decode method:
            
            text = bytes(blist).decode('utf-8')
        
        If no message is detected, or if there is an error in decoding the
        message, this method returns None
        """
        current_img = self.getCurrent()
        original_img = self.getOriginal()
        check = []                       # decoding first pixel for detecting
        for i in range(4):
            value = self._decode_pixel(i)
            check.append(value)

        if check[0]==121 and check[1]==101:                # decodes msg if msg detected is True
            blist = []                                     # for collecting integers after decoding
            for i in range(4, int(str(check[2]) + str(check[3]))+4):
                value = self._decode_pixel(i)
                blist.append(value)
                    
            # graceful exit for unable to decode
            try:
                return bytes(blist).decode('utf-8') # returns the msg encoded
            except:
                return None
        else:
            return None

    # HELPER METHODS
    def _decode_pixel(self, pos):
        """
        Return: the number n hidden in pixel pos of the current image.
        
        This function assumes that the value was a 3-digit number encoded as 
        the last digit in each color channel (e.g. red, green and blue).
        
        Parameter pos: a pixel position
        Precondition: pos is an int with  0 <= p < image length (as a 1d list)
        """
        # This is helper. You do not have to use it. You are allowed to change it.
        # There are no restrictions on how you can change it.
        rgb = self.getCurrent()[pos]
        red   = rgb[0]
        green = rgb[1]
        blue  = rgb[2]
        return  (red % 10) * 100  +  (green % 10) * 10  +  blue % 10