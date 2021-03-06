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


class DBPermission(object):
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
        'value': 'int',
        'enumeratum_enum_entry_lowercasestable_entry_name': 'str',
        'enumeratum_enum_entry_capital_snakecasestable_entry_name': 'str',
        'enumeratum_enum_entrystable_entry_name': 'str'
    }

    attribute_map = {
        'value': 'value',
        'enumeratum_enum_entry_lowercasestable_entry_name': 'enumeratum$EnumEntry$Lowercase$$stableEntryName',
        'enumeratum_enum_entry_capital_snakecasestable_entry_name': 'enumeratum$EnumEntry$CapitalSnakecase$$stableEntryName',
        'enumeratum_enum_entrystable_entry_name': 'enumeratum$EnumEntry$$stableEntryName'
    }

    def __init__(self, value=None, enumeratum_enum_entry_lowercasestable_entry_name=None, enumeratum_enum_entry_capital_snakecasestable_entry_name=None, enumeratum_enum_entrystable_entry_name=None):  # noqa: E501
        """DBPermission - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._enumeratum_enum_entry_lowercasestable_entry_name = None
        self._enumeratum_enum_entry_capital_snakecasestable_entry_name = None
        self._enumeratum_enum_entrystable_entry_name = None
        self.discriminator = None

        self.value = value
        self.enumeratum_enum_entry_lowercasestable_entry_name = enumeratum_enum_entry_lowercasestable_entry_name
        self.enumeratum_enum_entry_capital_snakecasestable_entry_name = enumeratum_enum_entry_capital_snakecasestable_entry_name
        self.enumeratum_enum_entrystable_entry_name = enumeratum_enum_entrystable_entry_name

    @property
    def value(self):
        """Gets the value of this DBPermission.  # noqa: E501


        :return: The value of this DBPermission.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DBPermission.


        :param value: The value of this DBPermission.  # noqa: E501
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def enumeratum_enum_entry_lowercasestable_entry_name(self):
        """Gets the enumeratum_enum_entry_lowercasestable_entry_name of this DBPermission.  # noqa: E501


        :return: The enumeratum_enum_entry_lowercasestable_entry_name of this DBPermission.  # noqa: E501
        :rtype: str
        """
        return self._enumeratum_enum_entry_lowercasestable_entry_name

    @enumeratum_enum_entry_lowercasestable_entry_name.setter
    def enumeratum_enum_entry_lowercasestable_entry_name(self, enumeratum_enum_entry_lowercasestable_entry_name):
        """Sets the enumeratum_enum_entry_lowercasestable_entry_name of this DBPermission.


        :param enumeratum_enum_entry_lowercasestable_entry_name: The enumeratum_enum_entry_lowercasestable_entry_name of this DBPermission.  # noqa: E501
        :type: str
        """
        if enumeratum_enum_entry_lowercasestable_entry_name is None:
            raise ValueError("Invalid value for `enumeratum_enum_entry_lowercasestable_entry_name`, must not be `None`")  # noqa: E501

        self._enumeratum_enum_entry_lowercasestable_entry_name = enumeratum_enum_entry_lowercasestable_entry_name

    @property
    def enumeratum_enum_entry_capital_snakecasestable_entry_name(self):
        """Gets the enumeratum_enum_entry_capital_snakecasestable_entry_name of this DBPermission.  # noqa: E501


        :return: The enumeratum_enum_entry_capital_snakecasestable_entry_name of this DBPermission.  # noqa: E501
        :rtype: str
        """
        return self._enumeratum_enum_entry_capital_snakecasestable_entry_name

    @enumeratum_enum_entry_capital_snakecasestable_entry_name.setter
    def enumeratum_enum_entry_capital_snakecasestable_entry_name(self, enumeratum_enum_entry_capital_snakecasestable_entry_name):
        """Sets the enumeratum_enum_entry_capital_snakecasestable_entry_name of this DBPermission.


        :param enumeratum_enum_entry_capital_snakecasestable_entry_name: The enumeratum_enum_entry_capital_snakecasestable_entry_name of this DBPermission.  # noqa: E501
        :type: str
        """
        if enumeratum_enum_entry_capital_snakecasestable_entry_name is None:
            raise ValueError("Invalid value for `enumeratum_enum_entry_capital_snakecasestable_entry_name`, must not be `None`")  # noqa: E501

        self._enumeratum_enum_entry_capital_snakecasestable_entry_name = enumeratum_enum_entry_capital_snakecasestable_entry_name

    @property
    def enumeratum_enum_entrystable_entry_name(self):
        """Gets the enumeratum_enum_entrystable_entry_name of this DBPermission.  # noqa: E501


        :return: The enumeratum_enum_entrystable_entry_name of this DBPermission.  # noqa: E501
        :rtype: str
        """
        return self._enumeratum_enum_entrystable_entry_name

    @enumeratum_enum_entrystable_entry_name.setter
    def enumeratum_enum_entrystable_entry_name(self, enumeratum_enum_entrystable_entry_name):
        """Sets the enumeratum_enum_entrystable_entry_name of this DBPermission.


        :param enumeratum_enum_entrystable_entry_name: The enumeratum_enum_entrystable_entry_name of this DBPermission.  # noqa: E501
        :type: str
        """
        if enumeratum_enum_entrystable_entry_name is None:
            raise ValueError("Invalid value for `enumeratum_enum_entrystable_entry_name`, must not be `None`")  # noqa: E501

        self._enumeratum_enum_entrystable_entry_name = enumeratum_enum_entrystable_entry_name

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
        if not isinstance(other, DBPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
