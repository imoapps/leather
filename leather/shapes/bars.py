#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Bars(Shape):
    """
    Render a series of data as bars.

    :param color:
        The color to fill the bars. You may also specify a function, which will
        be called with the arguments :code:`(x, y, index)` and should return a
        color.
    """
    def __init__(self, color):
        self._color = color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render bars to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series bars')

        for i, (x, y) in enumerate(series.data):
            if x is None or y is None:
                continue

            proj_x = x_scale.project(x, 0, width)
            y1, y2 = y_scale.project_interval(y, height, 0)

            if callable(self._color):
                color = self._color(x, y, i)
            else:
                color = self._color

            group.append(ET.Element('rect',
                x=six.text_type(0),
                y=six.text_type(y2),
                width=six.text_type(proj_x),
                height=six.text_type(y1 - y2),
                fill=color
            ))

        return group
