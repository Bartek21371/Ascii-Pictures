from PIL import Image 


#Maping brightness of colors
ASCII_CHARS = "@%#*+=-:. "

#Resize image for ASCII but without change proportion
def resize_image(image,new_width=100):
    width,height = image.size
    aspect_ratio = height/width * 0.5
    new_height = int(new_width*aspect_ratio)
    return image.resize((new_width,new_height))


#Convert picture to gray for ASCII 
def to_gray(image):
    return image.convert("L")

#Convert pixels to ascii chars
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return ascii_str

#Load image and save converted picture
def main(image_path,output_path,output_width=100):
    try: 
        image = Image.open(image_path)
        image = resize_image(image,output_width)
        image = to_gray(image)
        
        ascii_str = pixels_to_ascii(image)
        img_width = image.width
        ascii_pic = "\n".join([ascii_str[i:i+img_width] for i in range(0,len(ascii_str),img_width)])
        
        with open(output_path,"w") as result:
            result.write(ascii_pic)
        print(f"Picture {output_path} was saved to file")
    except Exception as e:
        print(f"Problem: {e}")


if __name__=="__main__":
    path = input("Enter path to picture: ")
    output = input("Enter output path: ")+".txt"
    width = int(input("Enter width of picture (default 100): ") or 100)
    main(path,output,width)