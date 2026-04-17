# Fitness Tracker — Supported Devices

Community-maintained catalog of hardware verified with the Fitness Tracker Linux fitness app.
The site is built with [Zola](https://www.getzola.org/) and deployed to GitHub Pages.

**Live site:** https://fitness-tracker.luigi311.com

## Adding a device

The fast path: open a [New Device issue](../../issues/new?template=new-device.yml).

The standard path: open a pull request adding one TOML file under `data/devices/<category>/`.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the full schema and rules.

## Local development

You need [Zola](https://www.getzola.org/documentation/getting-started/installation/)
and [UV Python](https://docs.astral.sh/uv/getting-started/installation/).

```sh
# 1. Install Python deps (one-time)
uv sync --frozen

# 2. Validate every device file
uv run scripts/validate_devices.py

# 3. Generate the device manifest the templates load
uv run scripts/build_manifest.py

# 4. Serve locally with hot reload
zola serve
```

Visit http://127.0.0.1:1111.

> **Note:** Zola can't enumerate a directory at template time, so we generate
> `data/devices-manifest.toml` from all per-device files via `build_manifest.py`.
> CI runs this automatically; locally, re-run it whenever you add or change a
> device file.

## Repo layout

```
config.toml                      Zola config
content/                         Markdown pages (home, /devices/, /docs/)
data/
  devices/<category>/<slug>.toml Source of truth — one file per device
  devices-manifest.toml          Auto-generated; do not edit
templates/                       Tera templates
  devices/list.html              The big one — search + filter UI
static/css|js/                   Stylesheets and the client-side filter
schemas/device.schema.json       JSON Schema enforced by CI
scripts/
  validate_devices.py            CI-grade validator
  build_manifest.py              Generates data/devices-manifest.toml
.github/
  workflows/validate-devices.yml Validate every PR that touches devices
  ISSUE_TEMPLATE/new-device.yml  Structured "submit a device" form
```
