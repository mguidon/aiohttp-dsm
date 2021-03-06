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


class UpdateUserRequest(object):
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
        'organization': 'str',
        'email': 'str',
        'url': 'str',
        'color': 'str',
        'last_name': 'str',
        'first_name': 'str',
        'credential': 'str'
    }

    attribute_map = {
        'organization': 'organization',
        'email': 'email',
        'url': 'url',
        'color': 'color',
        'last_name': 'lastName',
        'first_name': 'firstName',
        'credential': 'credential'
    }

    def __init__(self, organization=None, email=None, url=None, color=None, last_name=None, first_name=None, credential=None):  # noqa: E501
        """UpdateUserRequest - a model defined in OpenAPI"""  # noqa: E501

        self._organization = None
        self._email = None
        self._url = None
        self._color = None
        self._last_name = None
        self._first_name = None
        self._credential = None
        self.discriminator = None

        if organization is not None:
            self.organization = organization
        if email is not None:
            self.email = email
        if url is not None:
            self.url = url
        if color is not None:
            self.color = color
        if last_name is not None:
            self.last_name = last_name
        if first_name is not None:
            self.first_name = first_name
        if credential is not None:
            self.credential = credential

    @property
    def organization(self):
        """Gets the organization of this UpdateUserRequest.  # noqa: E501


        :return: The organization of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UpdateUserRequest.


        :param organization: The organization of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def email(self):
        """Gets the email of this UpdateUserRequest.  # noqa: E501


        :return: The email of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUserRequest.


        :param email: The email of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def url(self):
        """Gets the url of this UpdateUserRequest.  # noqa: E501


        :return: The url of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateUserRequest.


        :param url: The url of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def color(self):
        """Gets the color of this UpdateUserRequest.  # noqa: E501


        :return: The color of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this UpdateUserRequest.


        :param color: The color of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def last_name(self):
        """Gets the last_name of this UpdateUserRequest.  # noqa: E501


        :return: The last_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateUserRequest.


        :param last_name: The last_name of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first_name of this UpdateUserRequest.  # noqa: E501


        :return: The first_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateUserRequest.


        :param first_name: The first_name of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def credential(self):
        """Gets the credential of this UpdateUserRequest.  # noqa: E501


        :return: The credential of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this UpdateUserRequest.


        :param credential: The credential of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._credential = credential

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
        if not isinstance(other, UpdateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
