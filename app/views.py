import ast
import json
import os
import re
import uuid  # Import the uuid library
import git
from django.http import JsonResponse

import requests
from django.core.cache import cache
from git.repo import Repo
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.mongo_db_connection import (
    save_to_signnow_document_collection,
)
from app.helpers import(
    upload_pdf_and_get_url
)

@api_view(["GET"])
def home(request):
    "Dowell signnow home directory"
    return Response(
        "Welcome.", status.HTTP_200_OK
    )

    
@api_view(["POST"])
def create_signnow_document(request):
    """get signnow details."""
    if not request.data:
        return Response(
            {"message": "Failed to get signnow document information."},
            status.HTTP_200_OK,
        )
    if 'pdf' not in request.FILES:
        return Response({'error': 'No PDF file was submitted'}, status=status.HTTP_400_BAD_REQUEST)
    pdf_file = request.FILES['pdf']
    pdf_url = upload_pdf_and_get_url(pdf_file)
    if pdf_url:
        res = json.loads(
            save_to_signnow_document_collection(
                {
                    "file_name": "Untitled Document",
                    "pdf_url": pdf_url,
                }
            )
        )
        if res["isSuccess"]:
            return Response({"pdf_url": pdf_url}, status.HTTP_201_CREATED,)
    else:
        return Response({'error': 'Failed to upload the PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         

    
# @api_view(["POST"])
# def create_signnow_document(request):
#     if 'pdf' not in request.FILES:
#         return Response({'error': 'No PDF file was submitted'}, status=status.HTTP_400_BAD_REQUEST)

#     pdf_file = request.FILES['pdf']
#     pdf_url = upload_pdf_and_get_url(pdf_file)

#     if pdf_url:
#         return Response({'file_url': pdf_url}, status=status.HTTP_201_CREATED)
#     else:
#         return Response({'error': 'Failed to upload the PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)