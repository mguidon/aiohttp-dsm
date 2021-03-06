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


class LedgerTotalResponse(object):
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
        'total': 'float',
        'org_id': 'str',
        'start': 'datetime',
        'end': 'datetime'
    }

    attribute_map = {
        'total': 'total',
        'org_id': 'orgId',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, total=None, org_id=None, start=None, end=None):  # noqa: E501
        """LedgerTotalResponse - a model defined in OpenAPI"""  # noqa: E501

        self._total = None
        self._org_id = None
        self._start = None
        self._end = None
        self.discriminator = None

        self.total = total
        self.org_id = org_id
        self.start = start
        self.end = end

    @property
    def total(self):
        """Gets the total of this LedgerTotalResponse.  # noqa: E501


        :return: The total of this LedgerTotalResponse.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LedgerTotalResponse.


        :param total: The total of this LedgerTotalResponse.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def org_id(self):
        """Gets the org_id of this LedgerTotalResponse.  # noqa: E501


        :return: The org_id of this LedgerTotalResponse.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this LedgerTotalResponse.


        :param org_id: The org_id of this LedgerTotalResponse.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def start(self):
        """Gets the start of this LedgerTotalResponse.  # noqa: E501


        :return: The start of this LedgerTotalResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this LedgerTotalResponse.


        :param start: The start of this LedgerTotalResponse.  # noqa: E501
        :type: datetime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this LedgerTotalResponse.  # noqa: E501


        :return: The end of this LedgerTotalResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this LedgerTotalResponse.


        :param end: The end of this LedgerTotalResponse.  # noqa: E501
        :type: datetime
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

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
        if not isinstance(other, LedgerTotalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
