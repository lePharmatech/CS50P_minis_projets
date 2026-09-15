from PIL import Image, ImageOps
import sys
def main():
    # verification des arguments de lignes de commandes
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input = sys.argv[1]
    output = sys.argv[2]

    if not input.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")

    if input.split(".")[1] != output.split(".")[1]:
        sys.exit("Input and output have different extensions")

    shirt = Image.open("shirt.png")
    photo = Image.open(input)
    photo_ajustee = ImageOps.fit(photo, shirt.size)
    photo_ajustee.paste(shirt, shirt)
    photo_ajustee.save(output)


if __name__ == "__main__":
    main()
