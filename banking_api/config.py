import toml

class ConfigurationSettings:
    # def config:
        configurations = toml.load('config.toml')
        print(configurations)