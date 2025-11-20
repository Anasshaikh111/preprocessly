from .cleaner import Preprocessly

def clean(text, **kwargs):
    processor = Preprocessly(**kwargs)
    return processor.clean(text)
