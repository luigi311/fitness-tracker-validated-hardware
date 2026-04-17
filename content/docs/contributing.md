+++
title = "Contributing a Device"
weight = 1
+++

# Contributing a Device

Thanks for helping grow the device catalog! Here's how to add a new entry.

## Quick path: open an issue

If you're not comfortable with pull requests, {{ repo_link(path="issues/new?template=new-device.yml", text="open a new device issue") }}
and fill in the form. A maintainer will convert it into a proper entry.

## Standard path: open a pull request

1. Fork the repository.
2. Create a new TOML file at `data/devices/<category>/<slug>.toml`. The slug should be
   lowercase, hyphenated, and unique — for example `polar-h10.toml`.
3. Use the schema below.
4. Open a pull request. CI will validate your file against the schema and run a build smoke test.

## Schema

```toml
# Required
name = "Polar H10"                     # Human-readable name
manufacturer = "Polar"                 # Brand
category = "heart-rate"                # One of: heart-rate, footpods, cycling-trainers, cycling-sensors
status = "fully-supported"             # One of: fully-supported, partial, experimental, unsupported
connectivity = ["ble"]                 # One or more of: ble
verified_version = "3.0.0"             # The app version you tested against
verified_date = "2026-04-17"           # ISO 8601 date (YYYY-MM-DD)
verified_by = "your-github-username"   # Your GitHub handle

# Optional
features = ["heart-rate"]              # Capabilities tested
notes = "Dual broadcast works reliably."           # Anything useful for other users
manufacturer_url = "https://www.polar.com/en/sensors/h10-heart-rate-sensor"         # Where to buy / official page
```

## What "verified" means

A device should only be marked `fully-supported` if you have:

- Paired it with the app
- Recorded at least one full activity session
- Confirmed the data lands correctly in the app

Use `partial` if some features work but others don't — and document which in `notes`.
Use `experimental` for devices that work with workarounds or in development builds only.
Use `unsupported` for devices that have been confirmed not to work, with notes explaining why.

## Status definitions

| Status | Meaning |
|---|---|
| `fully-supported` | All advertised features work as expected |
| `partial` | Core function works; some features missing or unreliable |
| `experimental` | Works with caveats, workarounds, or dev builds |
| `unsupported` | Confirmed non-working — included to save others time |
