import os
from pdf2image import convert_from_path
import requests
import json

instructions = {
    'parts': [
        {
            'file': 'document'
        }
    ]
}


def presentation_to_pngs(presentation_path, result_dir, debug=True):
    # Check format
    if os.path.splitext(presentation_path)[1] == '.pptx':
        if debug:
            print("Got PPTX, converting to pdf...")
        # Convert to pdf
        response = requests.request(
            'POST',
            'https://api.pspdfkit.com/build',
            headers={
                'Authorization': 'Bearer '
            },
            files={
                'document': open(presentation_path, 'rb')
            },
            data={
                'instructions': json.dumps(instructions)
            },
            stream=True
        )

        if response.ok:
            presentation_path = os.path.join(result_dir, "pres_converted.pdf")
            with open(presentation_path, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=8096):
                    fd.write(chunk)
        else:
            print(response.text)
            exit()

        # Aspose (kinda sucks):
        # with slides.Presentation(presentation_path) as presentation:
        #     presentation.save(os.path.join(result_dir, "pres_converted.pdf"),
        #                       slides.export.SaveFormat.PDF)
        # presentation_path = os.path.join(result_dir, "pres_converted.pdf")
        # print('New presentation saved here: ', presentation_path)

    # Load PDF
    images = convert_from_path(presentation_path)

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].resize((int(images[i].size[0]/2), int(images[i].size[1]/2))).save(
            os.path.join(result_dir, 'page' + str(i).zfill(2) + '.jpg'), 
            'JPEG')
    if debug:
        print("Saved all pages as images successfully")
