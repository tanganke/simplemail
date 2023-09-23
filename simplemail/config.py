import os
from pathlib import Path
from omegaconf import OmegaConf, DictConfig
import logging

_logger = logging.getLogger(__name__)

_default_config = """
# smtp server configuration
host: smtp.gmail.com
port: 465
use_ssl: true

# account configuration
user: your_email
password: your_password
"""

config_dir = Path(os.path.expanduser("~/.config/simplemail"))
config_file = config_dir / "config.yaml"


def cli_initialize_config(config: DictConfig):
    user = input("Please enter your email address: ")
    password = input("Please enter your password: ")

    host = input(f"Please enter your smtp server host (default: {config.host}): ")
    if host == "":
        host = config.host

    port = input(f"Please enter your smtp server port (default: {config.port}): ")
    if port == "":
        port = config.port

    use_ssl = input(f"Please enter whether to use ssl (default: {config.use_ssl}): ")
    if use_ssl == "":
        use_ssl = config.use_ssl

    config.user = user
    config.password = password
    config.host = host
    config.port = port
    config.use_ssl = use_ssl

    OmegaConf.save(config, config_file)


def load_config() -> DictConfig:
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    assert config_dir.is_dir(), f"{config_dir} is not a directory"

    if not config_file.exists():
        config_file.touch(mode=0o600)
        # write default configuration to config file
        with open(config_file, "w") as f:
            f.write(_default_config)

    config = OmegaConf.load(config_file)
    if config.user == "your_email":
        _logger.error(f"Please configure your email account in {config_file}")
        cli_initialize_config(config)

    return config
