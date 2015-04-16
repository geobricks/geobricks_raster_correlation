from argh import dispatch_commands
from argh.decorators import named, arg
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation


@named('corr')
@arg('--bins', default=150, help='Bins')
def cli_get_correlation(file1, file2, **kwargs):
    print get_correlation(file1, file2, kwargs['bins'])


def main():
    dispatch_commands([cli_get_correlation])

if __name__ == '__main__':
    main()