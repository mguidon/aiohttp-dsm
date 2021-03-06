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


class LedgerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_ledger_entry_operation(self, create_ledger_entry_request, **kwargs):  # noqa: E501
        """creates ledger entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ledger_entry_operation(create_ledger_entry_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateLedgerEntryRequest create_ledger_entry_request: (required)
        :return: LedgerEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_ledger_entry_operation_with_http_info(create_ledger_entry_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_ledger_entry_operation_with_http_info(create_ledger_entry_request, **kwargs)  # noqa: E501
            return data

    def create_ledger_entry_operation_with_http_info(self, create_ledger_entry_request, **kwargs):  # noqa: E501
        """creates ledger entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ledger_entry_operation_with_http_info(create_ledger_entry_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateLedgerEntryRequest create_ledger_entry_request: (required)
        :return: LedgerEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_ledger_entry_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ledger_entry_operation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_ledger_entry_request' is set
        if ('create_ledger_entry_request' not in local_var_params or
                local_var_params['create_ledger_entry_request'] is None):
            raise ValueError("Missing the required parameter `create_ledger_entry_request` when calling `create_ledger_entry_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_ledger_entry_request' in local_var_params:
            body_params = local_var_params['create_ledger_entry_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/ledger/entries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LedgerEntry',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_history_operation(self, start, end, **kwargs):  # noqa: E501
        """creates ledger entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_history_operation(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start: start of ledger search (required)
        :param datetime end: end of ledger search (required)
        :param str user_id: the id of the user
        :param str dataset_id: the id of the dataset
        :param str period: YEAR | MONTH | DAY | HOUR
        :return: HistoryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_history_operation_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.get_history_operation_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def get_history_operation_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """creates ledger entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_history_operation_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start: start of ledger search (required)
        :param datetime end: end of ledger search (required)
        :param str user_id: the id of the user
        :param str dataset_id: the id of the dataset
        :param str period: YEAR | MONTH | DAY | HOUR
        :return: HistoryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end', 'user_id', 'dataset_id', 'period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_history_operation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `get_history_operation`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `get_history_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'user_id' in local_var_params:
            query_params.append(('userId', local_var_params['user_id']))  # noqa: E501
        if 'dataset_id' in local_var_params:
            query_params.append(('datasetId', local_var_params['dataset_id']))  # noqa: E501
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/ledger/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HistoryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_ledger(self, start, end, **kwargs):  # noqa: E501
        """queries the ledger table  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_ledger(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start: start of ledger search (required)
        :param datetime end: end of ledger search (required)
        :param str user_id: the id of the user
        :param str dataset_id: the id of the dataset
        :param str metric: DISK or COMPUTE
        :return: list[LedgerEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_ledger_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.query_ledger_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def query_ledger_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """queries the ledger table  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_ledger_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start: start of ledger search (required)
        :param datetime end: end of ledger search (required)
        :param str user_id: the id of the user
        :param str dataset_id: the id of the dataset
        :param str metric: DISK or COMPUTE
        :return: list[LedgerEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end', 'user_id', 'dataset_id', 'metric']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_ledger" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `query_ledger`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `query_ledger`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'user_id' in local_var_params:
            query_params.append(('userId', local_var_params['user_id']))  # noqa: E501
        if 'dataset_id' in local_var_params:
            query_params.append(('datasetId', local_var_params['dataset_id']))  # noqa: E501
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/ledger/entries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LedgerEntry]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_ledger_total(self, start, end, **kwargs):  # noqa: E501
        """queries the ledger table  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_ledger_total(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start: start of ledger search (required)
        :param datetime end: endof ledger search (required)
        :param str user_id: the id of the user
        :param str dataset_id: the id of the dataset
        :param str metric: DISK or COMPUTE
        :return: LedgerTotalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_ledger_total_with_http_info(start, end, **kwargs)  # noqa: E501
        else:
            (data) = self.query_ledger_total_with_http_info(start, end, **kwargs)  # noqa: E501
            return data

    def query_ledger_total_with_http_info(self, start, end, **kwargs):  # noqa: E501
        """queries the ledger table  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_ledger_total_with_http_info(start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime start: start of ledger search (required)
        :param datetime end: endof ledger search (required)
        :param str user_id: the id of the user
        :param str dataset_id: the id of the dataset
        :param str metric: DISK or COMPUTE
        :return: LedgerTotalResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['start', 'end', 'user_id', 'dataset_id', 'metric']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_ledger_total" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'start' is set
        if ('start' not in local_var_params or
                local_var_params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `query_ledger_total`")  # noqa: E501
        # verify the required parameter 'end' is set
        if ('end' not in local_var_params or
                local_var_params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `query_ledger_total`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'user_id' in local_var_params:
            query_params.append(('userId', local_var_params['user_id']))  # noqa: E501
        if 'dataset_id' in local_var_params:
            query_params.append(('datasetId', local_var_params['dataset_id']))  # noqa: E501
        if 'metric' in local_var_params:
            query_params.append(('metric', local_var_params['metric']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/ledger/totals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LedgerTotalResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
