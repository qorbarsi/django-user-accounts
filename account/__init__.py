import pkg_resources

__version__ = pkg_resources.get_distribution("accounts").version
default_app_config = "accounts.apps.AppConfig"
