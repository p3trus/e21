import itertools as it

# colors taken from bootstrap
COLORS = {
    'black': '#000000',
    'darker gray': '#222222',
    'dark gray': '#333333',  #text color
    'gray': '#555555',
    'light gray': '#999999',
    'lighter gray': '#eeeeee',
    'white': '#ffffff',
    'blue': '#049cdb',
    'dark blue': '#0064cd',
    'light blue': '#3a87ad',
    'lighter blue': '#d9edf7',
    'green': '#46a546',
    'light green': '#468847',
    'lighter green': '#dff0d8',
    'red': '#9d261d',
    'light red': '#b94a48',
    'lighter red': '#f2dede',
    'yellow': '#ffc40d',
    'light yellow': '#fcf8e3',
    'orange': '#f89406',
    'pink': '#c3325f',
    'purple': '#7a43b6',
}

def merge_dicts(*dicts):
    """Merges multiple dicts together.
    
    ::
        >>> x = dict(a=1, b=1)
        >>> y = dict(b=2)
        >>> merge_dicts(x, y, {'c': 1})
        {'a': 1, 'b': 2, 'c': 1}
    
    """
    return dict(it.chain(*[x.iteritems() for x in dicts]))
