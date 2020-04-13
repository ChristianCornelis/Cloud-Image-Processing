from api_modules import gcp_vision_api
from api_modules import rekognition_detect
from api_modules import azure_vision
gcp_vision_api.call_vision()
rekognition_detect.call_rekognition()
azure_vision.az_vision()