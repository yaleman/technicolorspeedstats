# technicolorspeedstats

Pulls DSL stats from my TG789vac v3 using headless Chrome.

I'd love to have done this with [mechanize](https://mechanize.readthedocs.io/en/latest/) but the interface relies heavily on client-side javascript.

## Basics

The module name is `technicolorspeedstats` and the important function is `get_data()`

Returns a `dict` of status/up/down - up/down will be `-1` if it's not connected.


## Installation

You'll need the selenium python framework.

    pip install --user selenium

Also the [Chrome Webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your version of Chrome.

## Example usage:

Copy `config.py.example` to `config.py` and set the url/username/password and you're good to go.


    >> import technicolorspeedstats
    >> data = technicolorspeedstats.get_data()
    >> print(data['status'])
    connected

Tested on version `I-18.3.0157-3-3-0-CRF902` (Internode, bought in 2020)