# Scenario Registry Convention

The central registry is `scenarios.yaml`.

Its purpose is to identify a scenario independently from where its files currently live.

## Stable identity

`scenario id` is the stable identity.

Moving a scenario from a subdirectory to its own repository does not create a new scenario. Update `repository` and `path`; keep the id.

## Required fields

Each active scenario should define:

- `title`
- `status`
- `authority_version`
- `canonical_clock`
- `clock_state`
- `frontier`
- `repository`
- `path`
- `entrypoint`
- `scenario_rules`
- `authority_entrypoint`
- `import_status`
- `epistemic_rule`
- `source_import`

## Separation rules

### authority_version != canonical_clock

A new authority version may freeze or rewind the historical clock for re-audit.

A file that describes a later historical date does not become current merely because its date is later.

### repository/path != scenario identity

Physical GitHub layout may change.

Central routing should survive a future split into separate repositories.

### import status != canon status

A file can exist in the source ZIP but not yet be copied to GitHub.

A file can exist in GitHub but remain WORKING, OPEN, SUPERSEDED, or ARCHIVE.

## Update rule

When a GitHub persistence trigger includes a change to current authority, clock, frontier, repository location, or import scope, update `scenarios.yaml` in the same persistence pass.
