from backend.utils.pptx_manager import presentation_to_pngs
from backend.utils.ocr_utils import convert_all_images_in_folder
from backend.utils.chatgpt_utils import send_text_to_chatgpt
import os


def get_feedback_for_presentation(presentation_path: str, result_folder: str) -> dict:

    presentation_to_pngs(presentation_path, result_folder)

    text = convert_all_images_in_folder(result_folder)
    with open(os.path.join(result_folder, 'slides_text.txt'), 'w') as f:
        f.write(text)

    result = send_text_to_chatgpt(text)
    return result


if __name__ == "__main__":
    # presentation_file = "test.pptx"
    presentation_file = "test10.pdf"
    result_folder = "test10/"
    # get_feedback_for_presentation(presentation_file, result_folder)
