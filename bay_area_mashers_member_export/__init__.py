import sys
from datetime import datetime, timedelta
import gspread


def main():
    spreadsheet_name = 'Bay Area Mashers Members'
    worksheet_name = 'Members'
    path = sys.argv[1]  # /secure/
    grace_period = timedelta(days=90)
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    # This assumes the credential file can be found in ~/.config/gspread/service_account.json
    gc = gspread.service_account()
    sheet = gc.open(spreadsheet_name)
    worksheet = sheet.worksheet(worksheet_name)
    members = worksheet.get_all_records()
    member_emails = []
    for member in members:
        paid_through = datetime.strptime(member['Dues Paid Through'], '%m/%y')
        if paid_through + grace_period > datetime.now():
            if member['Email']:
                member_emails.append(member['Email'].strip())
            if member['Email 2']:
                member_emails.append(member['Email 2'].strip())
    apache_require_lines = [f'      Require claim email:{x}' for x in member_emails]
    lines = [f'    <Location {path}>', '      AuthType openid-connect']
    lines.extend(apache_require_lines)
    lines.append('    </Location>')
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()
