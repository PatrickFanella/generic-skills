# Generic skills

Keep skills self-contained and portable. Preserve bundled attribution and license
notices. Host inventories, personal configuration, credentials, and deployment
records belong outside this repository.

After changing a skill or its resources, update its reviewed hashes in
`provenance.json` and run `python3 scripts/validate.py`. Packaging validation checks
structure and local resources; verify changed executable helpers separately.
