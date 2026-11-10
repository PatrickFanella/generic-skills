# Generic Skills

![Generic Skills repository banner](assets/brand/banner.png)

A collection of 49 skills for coding agents, covering software development, code review, debugging, security, research and writing. A skill is a folder with a `SKILL.md` entrypoint plus the references and helper scripts it uses; agents such as Codex, Claude Code and OpenCode load it when a task matches its description.

This is the portable edition of [patstack](https://github.com/subculture-collective/patstack), with personal and organization-specific details removed.

## Install

Clone the repository and copy the skill folders you want into your agent's skill directory, for example `~/.codex/skills/` for Codex or `~/.claude/skills/` for Claude Code:

```sh
git clone https://github.com/subculture-collective/generic-skills.git
cp -R generic-skills/skills/bug-tracer ~/.codex/skills/
```

Copy a whole folder so its references and scripts stay together, and check for an existing skill of the same name before replacing it. Start a new agent session afterwards so the client discovers the skill. How tools are invoked depends on the client.

The repository is also packaged as `@subcult/patstack`, which [Subsets](https://github.com/subculture-collective/subsets) can install as its `patstack` pack. That package is not published on the public npm registry.

Skills only give instructions. They do not grant an agent permission to publish, deploy, delete or change external services.

## Included skills

- [`api-contract-smith`](skills/api-contract-smith/SKILL.md)
- [`auth-gatekeeper`](skills/auth-gatekeeper/SKILL.md)
- [`bash-script-craft`](skills/bash-script-craft/SKILL.md)
- [`behavior-proof`](skills/behavior-proof/SKILL.md)
- [`boundary-drafter`](skills/boundary-drafter/SKILL.md)
- [`bug-tracer`](skills/bug-tracer/SKILL.md)
- [`build-sequencer`](skills/build-sequencer/SKILL.md)
- [`bus-factor-map`](skills/bus-factor-map/SKILL.md)
- [`cf-edge-deploy`](skills/cf-edge-deploy/SKILL.md)
- [`ci-medic`](skills/ci-medic/SKILL.md)
- [`cli-contract-smith`](skills/cli-contract-smith/SKILL.md)
- [`dep-source-clone`](skills/dep-source-clone/SKILL.md)
- [`dep-upgrade-pilot`](skills/dep-upgrade-pilot/SKILL.md)
- [`diff-inspector`](skills/diff-inspector/SKILL.md)
- [`eval-bench`](skills/eval-bench/SKILL.md)
- [`git-surgery`](skills/git-surgery/SKILL.md)
- [`gitea-fleet-tidy`](skills/gitea-fleet-tidy/SKILL.md)
- [`go-craft`](skills/go-craft/SKILL.md)
- [`mcp-server-forge`](skills/mcp-server-forge/SKILL.md)
- [`mcp-wire-tracer`](skills/mcp-wire-tracer/SKILL.md)
- [`mtls-trust-chain`](skills/mtls-trust-chain/SKILL.md)
- [`perf-hotpath-probe`](skills/perf-hotpath-probe/SKILL.md)
- [`pg-plan-reader`](skills/pg-plan-reader/SKILL.md)
- [`playwright-cli-driver`](skills/playwright-cli-driver/SKILL.md)
- [`privacy-controls`](skills/privacy-controls/SKILL.md)
- [`prose-unslop`](skills/prose-unslop/SKILL.md)
- [`python-uv-workbench`](skills/python-uv-workbench/SKILL.md)
- [`react-render-tuner`](skills/react-render-tuner/SKILL.md)
- [`red-green-loop`](skills/red-green-loop/SKILL.md)
- [`relay-baton`](skills/relay-baton/SKILL.md)
- [`repo-atlas`](skills/repo-atlas/SKILL.md)
- [`retrieval-pipeline`](skills/retrieval-pipeline/SKILL.md)
- [`roadmap-slicer`](skills/roadmap-slicer/SKILL.md)
- [`rust-ownership-async`](skills/rust-ownership-async/SKILL.md)
- [`safe-refactor-pass`](skills/safe-refactor-pass/SKILL.md)
- [`schema-migrator`](skills/schema-migrator/SKILL.md)
- [`scope-grill`](skills/scope-grill/SKILL.md)
- [`secret-rotation-flow`](skills/secret-rotation-flow/SKILL.md)
- [`secure-code-audit`](skills/secure-code-audit/SKILL.md)
- [`setup-wizard-script`](skills/setup-wizard-script/SKILL.md)
- [`ship-check`](skills/ship-check/SKILL.md)
- [`stride-threat-map`](skills/stride-threat-map/SKILL.md)
- [`sweep-rewriter`](skills/sweep-rewriter/SKILL.md)
- [`tech-doc-writer`](skills/tech-doc-writer/SKILL.md)
- [`telemetry-signal-forge`](skills/telemetry-signal-forge/SKILL.md)
- [`throwaway-prototype`](skills/throwaway-prototype/SKILL.md)
- [`ts-type-design`](skills/ts-type-design/SKILL.md)
- [`ui-craft`](skills/ui-craft/SKILL.md)
- [`wcag-a11y-audit`](skills/wcag-a11y-audit/SKILL.md)

## Validation

```sh
python3 -m pip install PyYAML==6.0.3
python3 scripts/validate.py
```

The validator checks each entrypoint's frontmatter and local links, that every skill has a license, that the skill list matches `provenance.json`, and that every file matches its reviewed SHA-256 hash in `provenance.json`. It does not run helper scripts or test skills in an agent.

## Contributing

Report bugs and request features in [GitHub issues](https://github.com/subculture-collective/generic-skills/issues). Open pull requests on GitHub against `main`; CI runs `scripts/validate.py` on every pull request.

The skills are exported from patstack by its `scripts/public-edition.py`, so a change made only here is overwritten by the next export. Fix a skill in patstack where you can. Any change here must update the file's hash in `provenance.json`, or validation fails. Keep skills free of host names, private paths and account names.

## License

Original packaging and original material without another grant are licensed under [GPL-3.0-or-later](LICENSE). Imported skills keep their MIT or Apache-2.0 grants: see each skill's own license file, the files in `notices/` and `provenance.json`. Bundled frontend data keeps its separate MIT notice.

Repository artwork: [assets/brand](assets/brand/README.md).
