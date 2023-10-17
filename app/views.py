import ast
import json
import os
import re
import uuid  # Import the uuid library
import git

import requests
from django.core.cache import cache
from git.repo import Repo
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.mongo_db_connection import (
    save_to_signnow_document_collection,
)

@api_view(["GET"])
def home(request):
    "Is server down? I though not!"
    return Response(
        "If you are seeing this :), the server is !down.", status.HTTP_200_OK
    )

@api_view(["POST"])
def create_signnow_document(request):
    """Document Creation."""
    if not request.data:
        return Response(
            {"message": "Failed to process signnow document creation."},
            status.HTTP_200_OK,
        )
    res = json.loads(
        save_to_signnow_document_collection(
            {
               
            }
        )
    )
    if res["isSuccess"]:
        
        return Response(
            {"editor_link": "editor_link", "_id": res["inserted_id"]},
            status.HTTP_201_CREATED,
        )