# test_file_ingestion.py

import pytest
import requests
import yaml

from utils import get_bearer_token, get_file_dataset_id, delete_file
from core_functions import upload_file_api

@pytest.mark.parametrize(
    "get_bearer_token",
    [
        {
            "url": "https://ea.api.101gen.ai/login",
            "client_side": False,
            "username": "qa_low_username",
            "password": "qa_low_password",
        }
    ],
    indirect=True
)
def test_file_upload(get_bearer_token, project_id="e4cc55c9-305d-478f-b285-96d436229fba"):
	upload_file_api(get_bearer_token, project_id, "ea", "/Users/yashdua/Documents/101GenAi_test_docs/Public Beta Launch Test Cases - requirements import structure.pdf")

@pytest.mark.parametrize(
    "get_bearer_token",
    [
        {
            "url": "https://ea.api.101gen.ai/login",
            "client_side": False,
            "username": "qa_low_username",
            "password": "qa_low_password",
        }
    ],
    indirect=True
)
def test_delete_file(get_bearer_token, file_dataset_id="", project_id="e4cc55c9-305d-478f-b285-96d436229fba"):
	file_dataset_id = get_file_dataset_id(get_bearer_token, filename="Public Beta Launch Test Cases - requirements import structure.pdf", project_id="e4cc55c9-305d-478f-b285-96d436229fba")
    # for jenkins: show line chart of ingestion time across runs
	delete_file(get_bearer_token, file_dataset_id, project_id="e4cc55c9-305d-478f-b285-96d436229fba")
