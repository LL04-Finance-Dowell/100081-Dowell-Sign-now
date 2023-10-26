import json
import bson
from rest_framework import status
from rest_framework.response import Response
import requests

def upload_pdf_and_get_url(pdf_file):
    try:
        url = "https://dowellfileuploader.uxlivinglab.online/uploadfiles/upload-pdf-file/"
        
        files = {'pdf': ('file.pdf', pdf_file)}
        
        response = requests.post(url, files=files)

        if response.status_code == 200 or 201:
            try:
                response_data = response.json()
                if 'file_url' in response_data:
                    pdf_url = response_data['file_url']
                    return pdf_url
                else:
                    return f"Error: Response does not contain 'file_url' - {response.text}"
            except ValueError:
                return f"Error: Response is not in JSON format - {response.text}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    except json.JSONDecodeError:
        return Response(
            "Invalid response data", status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def validate_id(id):
    try:
        if bson.objectid.ObjectId.is_valid(id):
            return True
        else:
            return None
    except:
        return None
