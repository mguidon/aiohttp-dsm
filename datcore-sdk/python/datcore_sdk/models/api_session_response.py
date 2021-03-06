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


class APISessionResponse(object):
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
        'session_token': 'str',
        'organization': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'session_token': 'session_token',
        'organization': 'organization',
        'expires_in': 'expires_in'
    }

    def __init__(self, session_token=None, organization=None, expires_in=None):  # noqa: E501
        """APISessionResponse - a model defined in OpenAPI"""  # noqa: E501

        self._session_token = None
        self._organization = None
        self._expires_in = None
        self.discriminator = None

        self.session_token = session_token
        self.organization = organization
        self.expires_in = expires_in

    @property
    def session_token(self):
        """Gets the session_token of this APISessionResponse.  # noqa: E501


        :return: The session_token of this APISessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        """Sets the session_token of this APISessionResponse.


        :param session_token: The session_token of this APISessionResponse.  # noqa: E501
        :type: str
        """
        if session_token is None:
            raise ValueError("Invalid value for `session_token`, must not be `None`")  # noqa: E501

        self._session_token = session_token

    @property
    def organization(self):
        """Gets the organization of this APISessionResponse.  # noqa: E501


        :return: The organization of this APISessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this APISessionResponse.


        :param organization: The organization of this APISessionResponse.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def expires_in(self):
        """Gets the expires_in of this APISessionResponse.  # noqa: E501


        :return: The expires_in of this APISessionResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this APISessionResponse.


        :param expires_in: The expires_in of this APISessionResponse.  # noqa: E501
        :type: int
        """
        if expires_in is None:
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

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
        if not isinstance(other, APISessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
