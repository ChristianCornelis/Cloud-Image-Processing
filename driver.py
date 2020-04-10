from api_modules import gcp_vision_api
from api_modules import rekognition_detect
from api_modules import azure-analyze-local-image
gcp_vision_api.call_vision()
rekognition_detect.call_rekognition()
azure-analyze-local-image.az_vision()