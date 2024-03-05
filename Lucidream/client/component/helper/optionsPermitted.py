from ...constants import DEFAULT_OPTIONS

def optionsPermitted(options: dict) -> dict:
    new_options = DEFAULT_OPTIONS.copy()
    parent_options = options.copy()
    
    del parent_options['rows']
    del parent_options['cols']
    del parent_options['parentRow']
    del parent_options['parentCol']
    del parent_options['parentRowSpan']
    del parent_options['parentColSpan']
    
    new_options.update(parent_options)

    return new_options
