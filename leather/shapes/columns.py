#!/usr/bin/env python

import xml.etree.ElementTree as ET

import six

from leather.shapes.base import Shape


class Columns(Shape):
    """
    Render a series of data as columns.

    :param color:
        The color to fill the columns. You may also specify a function, which
        will be called with the arguments :code:`(x, y, index)` and should
        return a color.
    """
    def __init__(self, color):
        self._color = color

    def to_svg(self, width, height, x_scale, y_scale, series):
        """
        Render columns to SVG elements.
        """
        group = ET.Element('g')
        group.set('class', 'series columns')

        for i, (x, y) in enumerate(series.data):
            if x is None or y is None:
                continue

            x1, x2 = x_scale.project_interval(x, 0, width)
            proj_y = y_scale.project(y, height, 0)

            if callable(self._color):
                color = self._color(x, y, i)
            else:
                color = self._color

            group.append(ET.Element('rect',
                x=six.text_type(x1),
                y=six.text_type(proj_y),
                width=six.text_type(x2 - x1),
                height=six.text_type(height - proj_y),
                fill=color
            ))

        return group
