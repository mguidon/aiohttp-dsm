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


class Consortium(object):
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
        'name': 'str',
        'updated_at': 'datetime',
        'schema_id': 'str',
        'id': 'int',
        'created_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'updated_at': 'updatedAt',
        'schema_id': 'schemaId',
        'id': 'id',
        'created_at': 'createdAt'
    }

    def __init__(self, name=None, updated_at=None, schema_id=None, id=None, created_at=None):  # noqa: E501
        """Consortium - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._updated_at = None
        self._schema_id = None
        self._id = None
        self._created_at = None
        self.discriminator = None

        self.name = name
        self.updated_at = updated_at
        self.schema_id = schema_id
        self.id = id
        self.created_at = created_at

    @property
    def name(self):
        """Gets the name of this Consortium.  # noqa: E501


        :return: The name of this Consortium.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Consortium.


        :param name: The name of this Consortium.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this Consortium.  # noqa: E501


        :return: The updated_at of this Consortium.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Consortium.


        :param updated_at: The updated_at of this Consortium.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def schema_id(self):
        """Gets the schema_id of this Consortium.  # noqa: E501


        :return: The schema_id of this Consortium.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this Consortium.


        :param schema_id: The schema_id of this Consortium.  # noqa: E501
        :type: str
        """
        if schema_id is None:
            raise ValueError("Invalid value for `schema_id`, must not be `None`")  # noqa: E501

        self._schema_id = schema_id

    @property
    def id(self):
        """Gets the id of this Consortium.  # noqa: E501


        :return: The id of this Consortium.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Consortium.


        :param id: The id of this Consortium.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Consortium.  # noqa: E501


        :return: The created_at of this Consortium.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Consortium.


        :param created_at: The created_at of this Consortium.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if not isinstance(other, Consortium):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other