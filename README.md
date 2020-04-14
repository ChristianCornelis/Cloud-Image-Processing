# CIS 4010 Final Project
## Christian Cornelis (0939357), Mohammadamin Sheikhtaheri (0930853), Samuel Tracz (0927451)
This repo contains the source code used to connect to the Azure Computer Vision, AWS Rekognition, and Google Vision APIs via their Python SDKs,
as well as the report of our findings. Please find out report pdf, `Team 3 Report.pdf` at the root level of this repo, as well as a zipped folder containing all LaTeX files used to create it in `team3_report.zip`.
Our presentation slides can be found in `Team 3 Presentation.pdf`, and the presentation video can be found [here](https://youtu.be/mYXJ3E2aEJA)

## Requirements to run scripts

### Azure Computer Vision
- You must have an Azure account
- you must have a a subscription key for Computer Vision. (https://azure.microsoft.com/try/cognitive-services/?api=computer-vision)
- requres these python libraries:
    requests
    matplotlib
    pillow
- You can go [here](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-disk) for setup steps and code tutorial

### Amazon Rekognition
- You must have an AWS account
- You must set the correct credentials in the `.aws` folder
- You must have boto3 installed using `pip install boto3`

### Google Cloud Platform
- You must have a Google Cloud account
- You must have a valid project connected to a billing account.
- You must have the service account key for the above project set in your environment variable `GOOGLE_APPLICATION_CREDENTIALS`
- You must have installed the Python module `google-cloud-vision` via PIP using `pip install google-cloud-vision`
- You can follow [this](https://cloud.google.com/vision/docs/setup#windows) link for helpful steps for setting up the above

## Running the scripts
- You can run a driver script that will run all three API scripts for each of the images in the `resources` folder with `python driver.py`
    - This will output all results to the terminal as well as to the files `gcp_response.text`, and `aws_response.txt` for Google Vision and AWS Rekognition, respectively.
- Scripts for the 3 services used can be found in the `api_modules`.

