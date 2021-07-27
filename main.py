from PIL import Image
import os,sys

def image_data(image_file,tile_x,tile_y):
    x,y = image_file.size
    tile_size_x = int(tile_x)
    tile_size_y = int(tile_y)
    tile_amount_x = int(x/tile_size_x)
    tile_amount_y = int(y/tile_size_y)
    max_tiles = tile_amount_x * tile_amount_y
    counter = 0
    if not os.path.exists("output/"):
        os.makedirs("output/")
    for y_line in range(tile_amount_y):
        for x_line in range(tile_amount_x):
            cropped = image_file.crop((x_line*tile_size_x,
                                       y_line*tile_size_y,
                                       x_line*tile_size_x+tile_size_x,
                                       y_line*tile_size_y+tile_size_y))
            cropped.save("output/{}.png".format(counter))
            percentage = int(counter * 100 / max_tiles)
            sys.stdout.write(f"{percentage}%\r")
            counter = counter + 1

def image_loader(image_filepath):
    try:
        image_file = Image.open(image_filepath)
        return image_file
    except FileNotFoundError:
        print("Not founded:{}".format(image_filepath))
        return 0

def main(filepath,tile_x,tile_y):
    temp_image = image_loader(filepath)
    if temp_image != 0:
        image_data(temp_image,tile_x,tile_y)
    else:
        pass

def arg_parser():
    args = sys.argv
    if len(args) == 4:
        print("filename:{}\nTilesize:{}x{}".format(args[1],args[2],args[3]))
        main(args[1],args[2],args[3])
    elif len(args) == 2:
        print("input tilesize:")
        main(args[1],int(input("x:")),int(input("y:")))
    else:
        print("""usage:\nspc.py [filename] [X tile size] [Y tile size]""")

if __name__ == "__main__":
    arg_parser()
