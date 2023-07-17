import os
import easyocr

reader = easyocr.Reader(['en'])


def convert_img_to_text(img_path: str) -> str:
    result = reader.readtext(img_path)
    return result


def convert_all_images_in_folder(folder_path: str, debug=True) -> str:
    print("Converting images to text using OCR...")
    result = ''
    current_slide = 1
    all_files = os.listdir(folder_path)
    all_files = sorted(all_files)
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        file_format = os.path.splitext(file_path)[1]
        if debug:
            print(file_path)
        if file_format == '.png' or file_format == '.jpg':
            ocr_result = convert_img_to_text(file_path)
            text_in_image=''
            for text in ocr_result:
                text_in_image += text[1] + '\n'

            result += '\n[Slide ' + str(current_slide) + ']\n\n' + text_in_image
            current_slide += 1
    if debug:
        print("Converted", current_slide, "slides to text")
    return result
