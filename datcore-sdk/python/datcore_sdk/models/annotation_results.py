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


class AnnotationResults(object):
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
        'users': 'dict(str, UserDTO)',
        'annotations': 'PagedResponseTimeSeriesAnnotation',
        'linked_packages': 'dict(str, PackageDTO)'
    }

    attribute_map = {
        'users': 'users',
        'annotations': 'annotations',
        'linked_packages': 'linkedPackages'
    }

    def __init__(self, users=None, annotations=None, linked_packages=None):  # noqa: E501
        """AnnotationResults - a model defined in OpenAPI"""  # noqa: E501

        self._users = None
        self._annotations = None
        self._linked_packages = None
        self.discriminator = None

        self.users = users
        self.annotations = annotations
        self.linked_packages = linked_packages

    @property
    def users(self):
        """Gets the users of this AnnotationResults.  # noqa: E501


        :return: The users of this AnnotationResults.  # noqa: E501
        :rtype: dict(str, UserDTO)
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this AnnotationResults.


        :param users: The users of this AnnotationResults.  # noqa: E501
        :type: dict(str, UserDTO)
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def annotations(self):
        """Gets the annotations of this AnnotationResults.  # noqa: E501


        :return: The annotations of this AnnotationResults.  # noqa: E501
        :rtype: PagedResponseTimeSeriesAnnotation
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this AnnotationResults.


        :param annotations: The annotations of this AnnotationResults.  # noqa: E501
        :type: PagedResponseTimeSeriesAnnotation
        """
        if annotations is None:
            raise ValueError("Invalid value for `annotations`, must not be `None`")  # noqa: E501

        self._annotations = annotations

    @property
    def linked_packages(self):
        """Gets the linked_packages of this AnnotationResults.  # noqa: E501


        :return: The linked_packages of this AnnotationResults.  # noqa: E501
        :rtype: dict(str, PackageDTO)
        """
        return self._linked_packages

    @linked_packages.setter
    def linked_packages(self, linked_packages):
        """Sets the linked_packages of this AnnotationResults.


        :param linked_packages: The linked_packages of this AnnotationResults.  # noqa: E501
        :type: dict(str, PackageDTO)
        """
        if linked_packages is None:
            raise ValueError("Invalid value for `linked_packages`, must not be `None`")  # noqa: E501

        self._linked_packages = linked_packages

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
        if not isinstance(other, AnnotationResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
