import glob
from pdf2image import convert_from_path


def convert_pdf_to_img(inputDir, outputDir):
    print('inputDir:', inputDir)
    print('outputDir:', outputDir)
    img_path_list = glob.glob('{}/*.pdf'.format(inputDir))
    for i, img_path in enumerate(img_path_list):
        img = convert_from_path(img_path)
        img[0].save('%s/geno_%d.png' % (outputDir, i))


if __name__ == "__main__":
    convert_pdf_to_img('./geno_pdf', './genotypes')
