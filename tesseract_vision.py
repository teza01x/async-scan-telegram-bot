import cv2
import pytesseract
import asyncio
from config import tesseract_path, tesseract_cfg, token_limit


async def text_detect(image, lid):
	### Path to tesseract
	pytesseract.pytesseract.tesseract_cmd = tesseract_path

	### Image calibrate
	def _read_image(image_path):
		img = cv2.imread(image_path)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		return img

	img = await asyncio.get_event_loop().run_in_executor(None, _read_image, image)

	### Get text from image
	if lid == 'eng':
		text = pytesseract.image_to_string(img, config=tesseract_cfg)
	else:
		text = pytesseract.image_to_string(img, lang=lid)

	if len(text) <= token_limit:
		return text

	return ''

