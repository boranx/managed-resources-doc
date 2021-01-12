# managed-resources-doc
The project aims to track managed resources on an excel sheet. only changing fields are updated for subsequent runs and the rest will stay same so `version history` can be used to track diffs and history.

## instructions

* Run `get-resources.sh` to print out managed resources to `/tmp/output.log` file. (needs to be authorized to an OSD cluster to accomplish that)
* Install python requirements: `pip3 install -r requirements.txt`
* Follow https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the to create a fresh project with only enough permissions to the excel you'd like to update. Download the `credentials.json` and place it on the project folder. (Don't forget to remove the credential and project at the end as a cleanup process)
* Edit `SHEET_ID` with the appropriate value for the excel you'd like to update for `managed_resources.py`. The sheet_id can also be grabbed from the sheet URL. If the URL were like https://docs.google.com/spreadsheets/d/2L4BLABLA, the `SHEET_ID` would be `2L4BLABLA`
* Run `python3 managed_resources.py` in order to parse the `output.log`, sort and push the data template to the specified sheet. The authenticate is done when first attempt with corporate email by following the flow via browser. Once the process is done, `token.pickle` is created to be used for further authorizations.


