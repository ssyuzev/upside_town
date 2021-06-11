### Objective

Your assignment is to create a dating API using Python and Django.

### Brief

The world needs another dating app! But it needs a twist...more like a flip actually! On Upside Town everyones photos are upside down. Your task is to write an API for a tinder-like dating app called Upside Town, that allows people to upload a photo, which then gets flipped upside down on the server, view others flipped photos, match them, and share each others contact information if the match is two-sided.

### Tasks

- Implement assignment using:
  - Language: **Python**
  - Framework: **Django**

- Create 3 API endpoints `/create`, `/list`, and `/match`
  - the `/create` endpoint should allow the user to upload:
    - A photo (limit size to 10M)
      - Flip the photo upside down, then store it
    - Email
    - Gender (m / f)
    - Full name
    - Geo location
      - Geo location should be coordinates (longitude and latitude)

  - the `/match` endpoint should return true if both sides match, and false otherwise:
    - Post t/f
    - Return t/f if both users had their input and decided if to match or not
    - When returning true, send the user the matched persons email

  - the `/list` API should be filterable and paginatable
    - Filter: distance e.g. `/list?gender[eq]=f&distance[lte]=100`
      - You can use the first formula from [this Wikipedia article](https://en.wikipedia.org/wiki/ Great-circle_distance) to calculate distance. Don't forget, you'll need to convert degrees to radians.
    - Pagination: e.g. `/list?page=1`

- Store the data in memory or using sqlite
