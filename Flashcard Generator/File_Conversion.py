import os
import sys
import docx


def save_file(directory, fileName, txt):
    txt_directory = directory + '/txt/'
    if not os.path.exists(txt_directory):
        os.makedirs(txt_directory)
    with open(txt_directory + fileName + ".txt", "w") as text_file:
        print(txt, file=text_file)


def pdf_to_txt(filePath):
    NotImplemented()


def docx_to_txt(filePath):
    doc = docx.Document(filePath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def convert_file_to_txt(root, file):
    txt = None
    filePath = root + "/" + file
    if '.docx' in filePath:
        txt = docx_to_txt(filePath)
    if '.pdf' in filePath:
        txt = pdf_to_txt(filePath)

    if txt is not None:
        baseName = os.path.basename(filePath)
        (fileName, ext) = os.path.splitext(baseName)
        new_root = os.path.dirname(root)
        save_file(new_root, fileName, txt)


def loop_through_files(directory):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(directory):
        for file in f:
            convert_file_to_txt(r, file)


def main(filePath):
    if os.path.isdir(filePath):  # Filepath is a directory
        loop_through_files(filePath)
    elif os.path.isfile(filePath):  # Filepath is a single file
        convert_file_to_txt(filePath)


if __name__ == '__main__':
    main(sys.argv[1])
