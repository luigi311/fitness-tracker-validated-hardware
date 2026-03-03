## Device PR Checklist

**Before submitting, please confirm:**

- [ ] The device file is in the correct category folder (`devices/<category>/<brand>/<model>.md`)
- [ ] The filename is lowercase with hyphens, e.g. `hrm-pro-plus.md`
- [ ] All required frontmatter fields are filled in (`name`, `brand`, `model`, `category`, `status`)
- [ ] `status` is one of: `validated`, `community-tested`, `untested`, `broken`
- [ ] `protocols` lists at least one value (e.g. `[Bluetooth LE]`)
- [ ] I have run `python scripts/generate-tables.py` locally and committed the updated `README.md`
  - _(or added the `regenerate-tables` label so the CI action runs it for me)_

---

## Device Summary

**Brand / Model:**
**Category:**
**Protocols:**
**Status:**

## How did you test this?
<!-- e.g. "Paired via BLE, ran a 30-min workout, all metrics logged correctly." -->

## Notes for reviewers
<!-- Anything unusual about this device or the pairing process? -->
