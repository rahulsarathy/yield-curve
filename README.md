# yield-curve

Displays yield curve from [treasury.gov](https://treasury.gov).

## To run

- Install all dependencies with `pip3 install -r requirements.txt`.
- Run `python3 manage.py runserver` in your terminal.
- Navigate to `localhost:8000` to display the yield curve chart.

## API

All API methods are prefixed with `/api/v1/`.

#### GET /api/v1/bond_yield/YYYYMMDD

Returns the bond yield data for a given date, e.g.

`Content-Type: application/json`

```
{
  "id": 7385,
  "date": "2019-07-03",
  "one_month": 2.25,
  "two_month": 2.2,
  "three_month": 2.21,
  "six_month": 2.08,
  "one_year": 1.91,
  "two_year": 1.77,
  "three_year": 1.71,
  "five_year": 1.74,
  "seven_year": 1.83,
  "ten_year": 1.96,
  "twenty_year": 2.25,
  "thirty_year": 2.47
}
```

If there isn't data for a given maturity date, the field will be set to null:

```
{
  ...
  "one_month": null,
  "two_month": null,
  "three_month": 5.40999984741211,
  "six_month": 5.55000019073486,
  ...
}
```

##  Testing

Run tests with `python3 manage.py test`.
