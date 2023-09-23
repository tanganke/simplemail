# simplemail

simple python package for sending mail.

# Installation

```bash
pip install git+https://github.com/tanganke/simplemail.git
```

# Usage

By default, the email is sent to yourself.

1. use it as CLI application, this will also generate a configuration file at first time:

```bash
simplemail 'subject:test' 'test mail'
```

2. use it in your python code:

```python
from simplemail import send_mail

send_mail(subject='subject:test', contents='test mail')
```

your configuration is at `~/.config/simplemail/config.yaml` with a default mode `600` (readable and writable only by current user).
