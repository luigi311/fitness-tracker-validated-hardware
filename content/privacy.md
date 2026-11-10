+++
title = "Privacy Policy"
description = "How Fitness Tracker handles workout data, optional integrations, website analytics, and your privacy choices."
+++

# Privacy Policy

**Effective date: November 10, 2026**

This policy covers the Fitness Tracker Linux application and the website at
fitness-tracker.luigi311.com. Fitness Tracker is an open-source project maintained
by Luigi311. For privacy questions or requests, email
[git@luigi311.com](mailto:git@luigi311.com).

The app stores your fitness information on your device. Optional integrations
transfer data to the services you choose. Visiting this website also generates
website analytics, as explained below.

## Information stored by the app

Depending on the features you use, the app handles:

- Personal settings such as weight, heart-rate thresholds, and cycling power
  thresholds.
- Workout plans, activity dates and durations, heart rate, speed, distance,
  cadence, power, and other measurements from connected sensors.
- Location points when location recording is enabled.
- Device names and connection identifiers, app preferences, integration
  credentials, and records of upload or sync results.

This information supports recording activities, displaying live measurements,
workout guidance, history, exports, and optional synchronization. Fitness and
location records can reveal sensitive information about your health and routines.

The app does not require an account with the project or upload your workout
database to a project-operated account server. It does not include advertising,
automatic usage analytics, or automatic crash-report uploads.

## Location and connected devices

When you select GPS as a movement source, the app requests location through your
operating system during a session. GPS can provide speed and distance even when
route recording is turned off; in that case the app does not save the route
coordinates.

The **Record outdoor routes** setting controls whether outdoor route points are
saved and included in activity exports and uploads. The separate **Store an
indoor/trainer location** setting can save one location point, with the accuracy
you select. That point can reveal where you exercise, including your home.
Changing these settings affects future recordings, not locations already saved
or shared. You can also manage location permission through your operating system.

Bluetooth sensors provide measurements directly to the app. If you enable the
Pebble companion, the app sends live metrics and workout guidance to your watch
through the configured bridge. Your operating system and any location services
it uses handle location requests under their own settings and policies.

## Optional integrations and exports

### Intervals.icu

Connecting Intervals.icu allows the app to download planned workouts and upload
recorded activities. Uploads can contain workout measurements and any location
points saved with the activity.

API-key connections use the athlete ID and personal API key you provide. Where
OAuth is available in your installed version, you sign in with Intervals.icu in
your browser and choose which permissions to grant. The app receives an access
token, the granted permissions, and your athlete identity; it does not receive
your Intervals.icu password. The permissions used for the workout integration are
calendar read access and activity write access.

The app keeps connection credentials on your device and uses them to communicate
directly with Intervals.icu. Intervals.icu receives those requests, their network
metadata, and the data you upload, and handles them under its own privacy policy.

You can revoke an OAuth connection in your Intervals.icu account or regenerate a
personal API key there. Remove saved credentials from the app to stop it using
them. Revoking access or clearing credentials does not delete activities already
uploaded to Intervals.icu; manage those records in that service.

### Remote databases and files

If you configure a remote database, the app exchanges activity records with that
database. Its operator controls access, hosting, backups, and retention. Exported
activity files contain the measurements and saved location information included
in the export. You control where those files are stored and with whom they are
shared.

## Local storage and diagnostics

The app stores its workout database, downloaded workouts, and settings in your
user account's application data and configuration directories. Local files are
protected with user-only filesystem permissions. The app does not encrypt the
workout database or the API keys in its settings file.

Diagnostic messages are written to the local console and may be captured by your
operating system. Logs can contain device information, activity details, and
errors. They are not automatically sent to the maintainer. Review logs and
screenshots before including them in a support request, and keep credentials and
private workout or location information out of public issues.

## Website visits and analytics

This website uses [Rybbit](https://rybbit.com/) analytics served from
analytics.luigi311.com to understand site use and improve the device catalog.
Analytics records include page views, visited URLs and query parameters,
referring pages, clicks on links to other websites, screen size, language, and
browser or device information. Requests also disclose your IP address to the
servers handling them; analytics can use network information to derive an
approximate location and a pseudonymous visitor identifier.

Rybbit measures visits without analytics cookies. Website session replay and
automatic error capture are currently disabled. Website analytics is separate
from the app and is not linked to your local workout database or Intervals.icu
credentials. You can block requests to analytics.luigi311.com with browser
privacy controls or a content blocker and continue to read the site.

Hosting and network providers also process request information, such as IP
addresses, requested pages, timestamps, and browser information, to deliver and
protect the website. Providers may process information outside your country.
Data sent to an optional integration is handled wherever that service or your
chosen database is hosted.

App screenshots are served from this website under the same hosting practices
described above.

## Contributions and contact

Device reports and contributions submitted through GitHub can include your public
username, hardware details, and any text or attachments you submit. Accepted
entries are published in the catalog and repository. GitHub handles your use of
its service under its [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

If you contact the maintainer, we receive your address, message, and any
attachments so we can respond. We use this information for support and project
maintenance. We do not sell personal information or use workout records for
advertising. Information may also be disclosed where required by law.

## Retention and deletion

Local app records remain on your device until you remove them. To remove all
local app data, close the app and remove its `fitness_tracker` data and
configuration directories. On a standard Linux installation these are normally
`~/.local/share/fitness_tracker` and `~/.config/fitness_tracker`; custom XDG
settings can change them. Flatpak installations keep them under
`~/.var/app/com.luigi311.fitness-tracker/data/fitness_tracker` and
`~/.var/app/com.luigi311.fitness-tracker/config/fitness_tracker`.

Uninstalling the app may leave these directories behind. Exported files,
backups, remote database records, and uploaded Intervals.icu activities must be
removed separately. Local deletion does not remove those copies, and syncing
with a remote database can restore records it still holds.

The website analytics database uses the following retention settings:

- Ordinary page-view and event records have no automatic age-based expiry
  configured in the database and may be retained indefinitely unless deleted.
- Bot-detection event records become eligible for automatic deletion after
  three months.
- Bot-observation records become eligible for automatic deletion after 30 days.
- Stored session replay events and metadata become eligible for automatic
  deletion after 30 days. Session replay is currently disabled for this website.

Automatic deletion happens during background database maintenance, so eligible
records may remain until that maintenance runs. These database settings do not
set retention periods for backups or hosting logs. Operational logs are kept
according to their continuing use for diagnosing problems, securing the website,
and meeting legal obligations.

Support correspondence is retained while needed to resolve and follow up on
requests. Public contributions can remain in the catalog and repository history.
Contact us about corrections or removal of information held by the project;
third-party services control their own records and backups.

## Your choices and rights

You can use local recording without configuring an external sync service, change
location preferences, export activities, and revoke integration access. The
maintainer does not have access to your local workout database and cannot
retrieve or delete it remotely.

Depending on the laws that apply to you, you may have rights to access, correct,
delete, or receive a copy of personal information held about you, restrict its
use, object to processing, or withdraw consent where processing relies on
consent. Email [git@luigi311.com](mailto:git@luigi311.com) to make a request. You
may also raise a concern with your local data protection authority.

## Policy changes

We will update this page and its effective date when the app's features or the
website's data practices change. The policy history is available in the
[website source repository](https://github.com/luigi311/fitness-tracker-validated-hardware/commits/main/content/privacy.md).
