# coding: utf-8

"""
    Blackfynn Swagger

    Swagger documentation for the Blackfynn api  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class LocalDate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'year': 'int',
        'month': 'int',
        'day': 'int'
    }

    attribute_map = {
        'year': 'year',
        'month': 'month',
        'day': 'day'
    }

    def __init__(self, year=None, month=None, day=None):  # noqa: E501
        """LocalDate - a model defined in OpenAPI"""  # noqa: E501

        self._year = None
        self._month = None
        self._day = None
        self.discriminator = None

        self.year = year
        self.month = month
        self.day = day

    @property
    def year(self):
        """Gets the year of this LocalDate.  # noqa: E501


        :return: The year of this LocalDate.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this LocalDate.


        :param year: The year of this LocalDate.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self):
        """Gets the month of this LocalDate.  # noqa: E501


        :return: The month of this LocalDate.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this LocalDate.


        :param month: The month of this LocalDate.  # noqa: E501
        :type: int
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def day(self):
        """Gets the day of this LocalDate.  # noqa: E501


        :return: The day of this LocalDate.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this LocalDate.


        :param day: The day of this LocalDate.  # noqa: E501
        :type: int
        """
        if day is None:
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LocalDate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
