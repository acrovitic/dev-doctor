# dev-doctor

**Healthchecks-as-code for development environments.**

`dev-doctor` allows teams to define project-specific environment checks in a simple
YAML file and run them via a CLI.

## Install (local development)

```bash
pip install -e .
```

## Usage
```bash
dev-doctor init
dev-doctor run
dev-doctor list
```

## Example config
See `examples/.devdoctor.yml`

## Why this exists
* Reduce onboarding friction
* Eliminate tribal setup knowledge
* Make environment sanity checks repeatable and versioned

## How to test locally
From repo root:
```bash
pip install -e .
dev-doctor init
dev-doctor run
```