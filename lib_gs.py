#!/usr/bin/python3.9

"""
Imports
"""
from __future__ import print_function
import pickle
import os.path
import json
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gs_client_secret_file = "/home/boran/Downloads/py_codes/credentials.json"

def credentials_gs():
    """
    Defining credentials to connect Google API
    """
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                gs_client_secret_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def service_sheet():
    """
    Build service for using spreadsheet properties in Google API
    """
    creds = credentials_gs()
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)
    return service.spreadsheets()

def update_sheet(file_id, sheet_and_range, df_update):
    """Clear and Update the given range in the given sheet.

    Args:
      service: Sheet API service instance.
      file_id: ID of the file to update for.
      range: Sheet name and range
      df_update: Dataframe to update the sheet.
    """
    service = service_sheet()

    for row_file_id in file_id:
        service.values().update(
            spreadsheetId=row_file_id,
            valueInputOption='RAW',
            range=sheet_and_range,
            body=dict(
                majorDimension='ROWS',
                values=df_update.T.reset_index().T.values.tolist()
            )
        ).execute()