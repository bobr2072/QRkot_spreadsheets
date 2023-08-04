from aiogoogle import Aiogoogle

from app.core.config import settings

SPREADSHEET_BODY = {
    'properties': {
        'title': '',
        'locale': 'ru_RU'
    },
    'sheets': [{
        'properties': {
            'sheetType': 'GRID',
            'sheetId': 0,
            'title': 'Лист1',
            'gridProperties': {
                'rowCount': 100,
                'columnCount': 11
            }
        }
    }]
}


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    SPREADSHEET_BODY['properties']['title'] = 'Отчет на {}'.format(settings.now_date_time)
    service = await wrapper_services.discover('sheets', 'v4')

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=SPREADSHEET_BODY)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
    spreadsheet_id: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    projects: list,
    wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets', 'v4')

    table_values = settings.table_values

    header = ['Name', 'Project Lifetime', 'Description']
    table_values = [
        header,
        *[list(map(str, [value['name'], value['project_lifetime'], value['description']])) for value in table_values]
    ]

    # Calculate the number of rows and columns
    num_rows = len(table_values)
    num_columns = len(header)

    # Validate that the table fits within the defined number of rows and columns
    max_rows = SPREADSHEET_BODY['sheets'][0]['properties']['gridProperties']['rowCount']
    max_columns = SPREADSHEET_BODY['sheets'][0]['properties']['gridProperties']['columnCount']

    if num_rows > max_rows or num_columns > max_columns:
        raise ValueError("The table does not fit within the allowed rows and columns.")

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    range_str = f'A1:{chr(64 + num_columns)}{num_rows}'  # Adjusted the range calculation

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=range_str,
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
