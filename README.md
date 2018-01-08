# print2slack

**`print()` to Slack**. A monkeypatch that prints all output to a Slack channel instead of stdout - just `import` and go!

![Demo](https://i.imgur.com/RW0NHaX.png)

## Installation

`pip install print2slack`

## Usage

1. Set your Webhook URL via an environment variable: `export SLACK_WH="https://hooks.slack.com/services/T7FCG2MW/B8P5H7C/9Za2ig0WdULOOZO17OX8G"`.
2. `import print2slack` in your project.
3. Call `print()` as you normally would and it'll end up in Slack!

All customisations should be done via your integration settings.

## License

MIT. See [LICENSE](LICENSE).
