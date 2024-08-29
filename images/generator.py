from lxml import etree
from os import listdir
from os.path import join

import fitz
from svglib import svglib
from reportlab.graphics import renderPDF

width = "313.0pt"
height = "313.0pt"
stroke_color = "black"
colors = ["#FF3300", "#00B050", "#33CCFF", "#FFFF99", "#FF00FF",
          "#FF6161", "#66FF33", "#0070C0", "#FFC000", "#7030A0",
          "#800000", "#336600", "#0033CC", "#996633", "#666699",
          "#FFC4C4", "#A8D08C", "#9CC2E5", "#FEE599", "#FF6699",
          "#CC3402", "#00FF99", "#DDEAF6", "#FF9933", "#CC66FF",
          '#FFFFFF', '#000000']

# stroke_width = "5"

all_possible_options = [color for color in colors]
filenames = listdir('figures_svg')
for filename in filenames:
    tree = etree.parse(open(join('figures_svg', filename), 'r'))
    for color_idx, color in enumerate(colors):
        for element in tree.iter():
            curr_tag = element.tag.split("}")[1]
            if curr_tag == "svg":
                element.set("width", width)
                element.set("height", height)
            elif curr_tag == "g":
                element.set("fill", color)
                # element.set("stroke", stroke_color)
                # element.set("stroke-width", stroke_width)

        res_file_name = filename.split('.')[0] + "_" + str(color_idx + 1) + ".svg"
        with open(join('all_svg', res_file_name), 'wb') as res_file:
            res_file.write(etree.tostring(tree, pretty_print=True))



        # Convert svg to pdf in memory with svglib+reportlab
        # directly rendering to png does not support transparency nor scaling
        drawing = svglib.svg2rlg(path=join('all_svg', res_file_name))
        pdf = renderPDF.drawToString(drawing)

        # Open pdf with fitz (pyMuPdf) to convert to PNG
        doc = fitz.Document(stream=pdf)
        pix = doc.load_page(0).get_pixmap(alpha=True, dpi=313)
        pix.save(join('all_png', res_file_name[:-3] + 'png'))