# bay-area-mashers-member-export

Tool to query Bay Area Mashers member list and return all current members' email addresses

## Installation

* [Provision Google credentials](https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account) to query the Google Sheet
* Save the resulting Google API credential file in `~/.config/gspread/service_account.json`
* Install the bay-area-mashers-member-export tool 

      pip install bay-area-mashers-member-export

## Usage

```shell
bay-area-mashers-member-export /secure/ > /etc/apache2/sites-available/secure-location.include
sudo apachectl graceful
```
