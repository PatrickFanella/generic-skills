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

- [`api-contract-smith`](https://github.com/subculture-collective/generic-skills/blob/main/skills/api-contract-smith/SKILL.md)
- [`auth-gatekeeper`](https://github.com/subculture-collective/generic-skills/blob/main/skills/auth-gatekeeper/SKILL.md)
- [`bash-script-craft`](https://github.com/subculture-collective/generic-skills/blob/main/skills/bash-script-craft/SKILL.md)
- [`behavior-proof`](https://github.com/subculture-collective/generic-skills/blob/main/skills/behavior-proof/SKILL.md)
- [`boundary-drafter`](https://github.com/subculture-collective/generic-skills/blob/main/skills/boundary-drafter/SKILL.md)
- [`bug-tracer`](https://github.com/subculture-collective/generic-skills/blob/main/skills/bug-tracer/SKILL.md)
- [`build-sequencer`](https://github.com/subculture-collective/generic-skills/blob/main/skills/build-sequencer/SKILL.md)
- [`bus-factor-map`](https://github.com/subculture-collective/generic-skills/blob/main/skills/bus-factor-map/SKILL.md)
- [`cf-edge-deploy`](https://github.com/subculture-collective/generic-skills/blob/main/skills/cf-edge-deploy/SKILL.md)
- [`ci-medic`](https://github.com/subculture-collective/generic-skills/blob/main/skills/ci-medic/SKILL.md)
- [`cli-contract-smith`](https://github.com/subculture-collective/generic-skills/blob/main/skills/cli-contract-smith/SKILL.md)
- [`dep-source-clone`](https://github.com/subculture-collective/generic-skills/blob/main/skills/dep-source-clone/SKILL.md)
- [`dep-upgrade-pilot`](https://github.com/subculture-collective/generic-skills/blob/main/skills/dep-upgrade-pilot/SKILL.md)
- [`diff-inspector`](https://github.com/subculture-collective/generic-skills/blob/main/skills/diff-inspector/SKILL.md)
- [`eval-bench`](https://github.com/subculture-collective/generic-skills/blob/main/skills/eval-bench/SKILL.md)
- [`git-surgery`](https://github.com/subculture-collective/generic-skills/blob/main/skills/git-surgery/SKILL.md)
- [`gitea-fleet-tidy`](https://github.com/subculture-collective/generic-skills/blob/main/skills/gitea-fleet-tidy/SKILL.md)
- [`go-craft`](https://github.com/subculture-collective/generic-skills/blob/main/skills/go-craft/SKILL.md)
- [`mcp-server-forge`](https://github.com/subculture-collective/generic-skills/blob/main/skills/mcp-server-forge/SKILL.md)
- [`mcp-wire-tracer`](https://github.com/subculture-collective/generic-skills/blob/main/skills/mcp-wire-tracer/SKILL.md)
- [`mtls-trust-chain`](https://github.com/subculture-collective/generic-skills/blob/main/skills/mtls-trust-chain/SKILL.md)
- [`perf-hotpath-probe`](https://github.com/subculture-collective/generic-skills/blob/main/skills/perf-hotpath-probe/SKILL.md)
- [`pg-plan-reader`](https://github.com/subculture-collective/generic-skills/blob/main/skills/pg-plan-reader/SKILL.md)
- [`playwright-cli-driver`](https://github.com/subculture-collective/generic-skills/blob/main/skills/playwright-cli-driver/SKILL.md)
- [`privacy-controls`](https://github.com/subculture-collective/generic-skills/blob/main/skills/privacy-controls/SKILL.md)
- [`prose-unslop`](https://github.com/subculture-collective/generic-skills/blob/main/skills/prose-unslop/SKILL.md)
- [`python-uv-workbench`](https://github.com/subculture-collective/generic-skills/blob/main/skills/python-uv-workbench/SKILL.md)
- [`react-render-tuner`](https://github.com/subculture-collective/generic-skills/blob/main/skills/react-render-tuner/SKILL.md)
- [`red-green-loop`](https://github.com/subculture-collective/generic-skills/blob/main/skills/red-green-loop/SKILL.md)
- [`relay-baton`](https://github.com/subculture-collective/generic-skills/blob/main/skills/relay-baton/SKILL.md)
- [`repo-atlas`](https://github.com/subculture-collective/generic-skills/blob/main/skills/repo-atlas/SKILL.md)
- [`retrieval-pipeline`](https://github.com/subculture-collective/generic-skills/blob/main/skills/retrieval-pipeline/SKILL.md)
- [`roadmap-slicer`](https://github.com/subculture-collective/generic-skills/blob/main/skills/roadmap-slicer/SKILL.md)
- [`rust-ownership-async`](https://github.com/subculture-collective/generic-skills/blob/main/skills/rust-ownership-async/SKILL.md)
- [`safe-refactor-pass`](https://github.com/subculture-collective/generic-skills/blob/main/skills/safe-refactor-pass/SKILL.md)
- [`schema-migrator`](https://github.com/subculture-collective/generic-skills/blob/main/skills/schema-migrator/SKILL.md)
- [`scope-grill`](https://github.com/subculture-collective/generic-skills/blob/main/skills/scope-grill/SKILL.md)
- [`secret-rotation-flow`](https://github.com/subculture-collective/generic-skills/blob/main/skills/secret-rotation-flow/SKILL.md)
- [`secure-code-audit`](https://github.com/subculture-collective/generic-skills/blob/main/skills/secure-code-audit/SKILL.md)
- [`setup-wizard-script`](https://github.com/subculture-collective/generic-skills/blob/main/skills/setup-wizard-script/SKILL.md)
- [`ship-check`](https://github.com/subculture-collective/generic-skills/blob/main/skills/ship-check/SKILL.md)
- [`stride-threat-map`](https://github.com/subculture-collective/generic-skills/blob/main/skills/stride-threat-map/SKILL.md)
- [`sweep-rewriter`](https://github.com/subculture-collective/generic-skills/blob/main/skills/sweep-rewriter/SKILL.md)
- [`tech-doc-writer`](https://github.com/subculture-collective/generic-skills/blob/main/skills/tech-doc-writer/SKILL.md)
- [`telemetry-signal-forge`](https://github.com/subculture-collective/generic-skills/blob/main/skills/telemetry-signal-forge/SKILL.md)
- [`throwaway-prototype`](https://github.com/subculture-collective/generic-skills/blob/main/skills/throwaway-prototype/SKILL.md)
- [`ts-type-design`](https://github.com/subculture-collective/generic-skills/blob/main/skills/ts-type-design/SKILL.md)
- [`ui-craft`](https://github.com/subculture-collective/generic-skills/blob/main/skills/ui-craft/SKILL.md)
- [`wcag-a11y-audit`](https://github.com/subculture-collective/generic-skills/blob/main/skills/wcag-a11y-audit/SKILL.md)

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
