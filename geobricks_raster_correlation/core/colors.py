from brewer2mpl import get_map as brewer2mpl_get_map
from geobricks_common.core.log import logger

log = logger(__file__)


def get_colors(color_ramp, intervals, reverse=False):
    try:
        return brewer2mpl_get_map(color_ramp, "Sequential", intervals, reverse=reverse).hex_colors
    except Exception, e:
        log.warn(e)
        pass
    try:
        return brewer2mpl_get_map(color_ramp, "Diverging", intervals, reverse=reverse).hex_colors
    except Exception, e:
        log.warn(e)
        pass
    try:
        return brewer2mpl_get_map(color_ramp, "Qualitative", intervals, reverse=reverse).hex_colors
    except Exception, e:
        log.warn(e)
        pass
    return None
