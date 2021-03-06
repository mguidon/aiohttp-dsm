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


class S3File(object):
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
        'upload_id': 'int',
        'file_name': 'str',
        'size': 'int'
    }

    attribute_map = {
        'upload_id': 'uploadId',
        'file_name': 'fileName',
        'size': 'size'
    }

    def __init__(self, upload_id=None, file_name=None, size=None):  # noqa: E501
        """S3File - a model defined in OpenAPI"""  # noqa: E501

        self._upload_id = None
        self._file_name = None
        self._size = None
        self.discriminator = None

        if upload_id is not None:
            self.upload_id = upload_id
        self.file_name = file_name
        if size is not None:
            self.size = size

    @property
    def upload_id(self):
        """Gets the upload_id of this S3File.  # noqa: E501


        :return: The upload_id of this S3File.  # noqa: E501
        :rtype: int
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this S3File.


        :param upload_id: The upload_id of this S3File.  # noqa: E501
        :type: int
        """

        self._upload_id = upload_id

    @property
    def file_name(self):
        """Gets the file_name of this S3File.  # noqa: E501


        :return: The file_name of this S3File.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this S3File.


        :param file_name: The file_name of this S3File.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def size(self):
        """Gets the size of this S3File.  # noqa: E501


        :return: The size of this S3File.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this S3File.


        :param size: The size of this S3File.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, S3File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
