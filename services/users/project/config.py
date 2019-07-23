class BaseConfig:
    '''Base Configuration'''
    TESTING = False


class DevConfig(BaseConfig):
    '''Development Configuration'''
    pass


class TestConfig(BaseConfig):
    '''Testing Configuration'''
    TESTING = True


class ProdConfig(BaseConfig):
    '''Producttion Configuration'''
    pass
