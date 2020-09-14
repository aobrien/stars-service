# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SimulationConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, label: str=None):  # noqa: E501
        """SimulationConfig - a model defined in Swagger

        :param label: The label of this SimulationConfig.  # noqa: E501
        :type label: str
        """
        self.swagger_types = {
            'label': str
        }

        self.attribute_map = {
            'label': 'label'
        }

        self._label = label

    @classmethod
    def from_dict(cls, dikt) -> 'SimulationConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimulationConfig of this SimulationConfig.  # noqa: E501
        :rtype: SimulationConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def label(self) -> str:
        """Gets the label of this SimulationConfig.


        :return: The label of this SimulationConfig.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this SimulationConfig.


        :param label: The label of this SimulationConfig.
        :type label: str
        """

        self._label = label
