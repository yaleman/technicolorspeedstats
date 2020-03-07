# technicolorspeedstats

Pulls DSL stats from my TG789vac v3.

Copy `config.py.example` to `config.py` and set the url/username/password and you're good to go.

Returns a `dict` of status/up/down - up/down will be `-1` if it's not connected.

## Example usage:

    >> import technicolorspeedstats
    >> data = technicolorspeedstats.get_data()
    >> print(data['status'])
    connected

Tested on version `I-18.3.0157-3-3-0-CRF902` (Internode, bought in 2020)