# coding: utf-8

"""
    Blackfynn Swagger

    Swagger documentation for the Blackfynn api  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from datcore_sdk.api_client import ApiClient


class DataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_items(self, delete_request, **kwargs):  # noqa: E501
        """deletes items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_items(delete_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteRequest delete_request: items to delete (required)
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_items_with_http_info(delete_request, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_items_with_http_info(delete_request, **kwargs)  # noqa: E501
            return data

    def delete_items_with_http_info(self, delete_request, **kwargs):  # noqa: E501
        """deletes items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_items_with_http_info(delete_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteRequest delete_request: items to delete (required)
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['delete_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_items" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'delete_request' is set
        if ('delete_request' not in local_var_params or
                local_var_params['delete_request'] is None):
            raise ValueError("Missing the required parameter `delete_request` when calling `delete_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete_request' in local_var_params:
            body_params = local_var_params['delete_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/data/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def move_items(self, move_request, **kwargs):  # noqa: E501
        """moves files or packages into a destination package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.move_items(move_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoveRequest move_request: list of ids of files and packages to move, as well as their destination (required)
        :return: MoveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.move_items_with_http_info(move_request, **kwargs)  # noqa: E501
        else:
            (data) = self.move_items_with_http_info(move_request, **kwargs)  # noqa: E501
            return data

    def move_items_with_http_info(self, move_request, **kwargs):  # noqa: E501
        """moves files or packages into a destination package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.move_items_with_http_info(move_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MoveRequest move_request: list of ids of files and packages to move, as well as their destination (required)
        :return: MoveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['move_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_items" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'move_request' is set
        if ('move_request' not in local_var_params or
                local_var_params['move_request'] is None):
            raise ValueError("Missing the required parameter `move_request` when calling `move_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'move_request' in local_var_params:
            body_params = local_var_params['move_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/data/move', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MoveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_properties(self, id, update_properties_request, **kwargs):  # noqa: E501
        """updates the properties on a node  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_properties(id, update_properties_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: identifies the object you want to add properties for (required)
        :param UpdatePropertiesRequest update_properties_request: the properties (required)
        :return: PackageDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_properties_with_http_info(id, update_properties_request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_properties_with_http_info(id, update_properties_request, **kwargs)  # noqa: E501
            return data

    def update_properties_with_http_info(self, id, update_properties_request, **kwargs):  # noqa: E501
        """updates the properties on a node  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_properties_with_http_info(id, update_properties_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: identifies the object you want to add properties for (required)
        :param UpdatePropertiesRequest update_properties_request: the properties (required)
        :return: PackageDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'update_properties_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_properties" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_properties`")  # noqa: E501
        # verify the required parameter 'update_properties_request' is set
        if ('update_properties_request' not in local_var_params or
                local_var_params['update_properties_request'] is None):
            raise ValueError("Missing the required parameter `update_properties_request` when calling `update_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_properties_request' in local_var_params:
            body_params = local_var_params['update_properties_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/data/{id}/properties', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PackageDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)