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


class AnnotationResult(object):
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
        'annotation': 'TimeSeriesAnnotation',
        'linked_package': 'PackageDTO'
    }

    attribute_map = {
        'users': 'users',
        'annotation': 'annotation',
        'linked_package': 'linkedPackage'
    }

    def __init__(self, users=None, annotation=None, linked_package=None):  # noqa: E501
        """AnnotationResult - a model defined in OpenAPI"""  # noqa: E501

        self._users = None
        self._annotation = None
        self._linked_package = None
        self.discriminator = None

        self.users = users
        self.annotation = annotation
        if linked_package is not None:
            self.linked_package = linked_package

    @property
    def users(self):
        """Gets the users of this AnnotationResult.  # noqa: E501


        :return: The users of this AnnotationResult.  # noqa: E501
        :rtype: dict(str, UserDTO)
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this AnnotationResult.


        :param users: The users of this AnnotationResult.  # noqa: E501
        :type: dict(str, UserDTO)
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def annotation(self):
        """Gets the annotation of this AnnotationResult.  # noqa: E501


        :return: The annotation of this AnnotationResult.  # noqa: E501
        :rtype: TimeSeriesAnnotation
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this AnnotationResult.


        :param annotation: The annotation of this AnnotationResult.  # noqa: E501
        :type: TimeSeriesAnnotation
        """
        if annotation is None:
            raise ValueError("Invalid value for `annotation`, must not be `None`")  # noqa: E501

        self._annotation = annotation

    @property
    def linked_package(self):
        """Gets the linked_package of this AnnotationResult.  # noqa: E501


        :return: The linked_package of this AnnotationResult.  # noqa: E501
        :rtype: PackageDTO
        """
        return self._linked_package

    @linked_package.setter
    def linked_package(self, linked_package):
        """Sets the linked_package of this AnnotationResult.


        :param linked_package: The linked_package of this AnnotationResult.  # noqa: E501
        :type: PackageDTO
        """

        self._linked_package = linked_package

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
        if not isinstance(other, AnnotationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
