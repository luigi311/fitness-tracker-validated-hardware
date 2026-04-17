# Contributing

Thanks for considering a contribution! Most contributions to this repo are new device entries.

## Adding a device via pull request

1. Fork the repo.
2. Create a new file at `data/devices/<category>/<slug>.toml` where:
   - `<category>` is one of: `heart-rate`, `footpods`, `cycling-trainers`, `cycling-sensors`
   - `<slug>` is lowercase, hyphenated, and unique across the whole tree (e.g. `polar-h10.toml`)
3. Use the template in [`data/devices/heart-rate/polar-h10.toml`](data/devices/heart-rate/polar-h10.toml) as a starting point.
4. Run the validator locally if you can:
   ```sh
   pip install jsonschema tomli
   python scripts/validate_devices.py
   ```
5. Open a pull request. CI will:
   - validate your file against the JSON schema
   - confirm the file's directory matches its `category`
   - confirm the slug is unique
   - smoke-test the full site build

## Schema

| Field | Required | Type | Notes |
|---|---|---|---|
| `name` | ✓ | string | Human-readable device name |
| `manufacturer` | ✓ | string | Brand |
| `category` | ✓ | enum | `heart-rate`, `footpods`, `cycling-trainers`, `cycling-sensors` |
| `status` | ✓ | enum | `fully-supported`, `partial`, `experimental`, `unsupported` |
| `connectivity` | ✓ | array | One or more of: `ble` |
| `verified_version` | ✓ | string | App version tested, e.g. `3.0.0` |
| `verified_date` | ✓ | string | `YYYY-MM-DD` |
| `verified_by` | ✓ | string | Your GitHub username |
| `features` | | array | Capabilities you confirmed working |
| `notes` | | string | Caveats, workarounds, partial-support details |
| `manufacturer_url` | | string | Official product page |

## What "verified" means

Mark a device `fully-supported` only if you have personally:

1. Paired it with the app
2. Recorded at least one full activity session
3. Confirmed the data lands correctly in the app

Use `partial` if some features work and others don't — and document which in `notes`.
Use `experimental` for devices that work with workarounds or in development builds.
Use `unsupported` for devices confirmed not to work, with notes explaining why.

## Adding a device via issue

If pull requests aren't your thing, open a [New Device issue](../../issues/new?template=new-device.yml)
and a maintainer will turn it into a proper entry.

## Code of conduct

Be kind, be specific, and remember that the people on the other end of an issue or PR are
volunteers contributing in their spare time.
