import fitz
import argparse

import os


def parse_args() -> (str, str, float, float):
    parser = argparse.ArgumentParser(description="A Python tool for analysing PDF pages and saving them to png files.")
    parser.add_argument("pdf_file", help="Location of the PDF file.")
    parser.add_argument("output_dir", help="Location of the output directory.")
    parser.add_argument("--zoom_x", help="Scaling factor on X direction.")
    parser.add_argument("--zoom_y", help="Scaling factor on Y direction.")
    args = parser.parse_args()
    pdf_file = args.pdf_file
    output_dir = args.output_dir
    zoom_x = 1.0
    if args.zoom_x:
        zoom_x = float(args.zoom_x)
    zoom_y = 1.0
    if args.zoom_y:
        zoom_y = float(args.zoom_y)
    return pdf_file, output_dir, zoom_x, zoom_y


def main() -> None:
    pdf_file, output_dir, zoom_x, zoom_y = parse_args()
    doc = fitz.open(pdf_file)
    for page in doc:
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat)
        dest_file = os.path.join(output_dir, "{}.png".format(page.number))
        pix.save(dest_file)


if __name__ == "__main__":
    main()
