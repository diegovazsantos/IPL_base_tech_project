# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class CreateCustomerResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_id: str=None):  # noqa: E501
        """CreateCustomerResponse - a model defined in Swagger

        :param customer_id: The customer_id of this CreateCustomerResponse.  # noqa: E501
        :type customer_id: str
        """
        self.swagger_types = {
            'customer_id': str
        }

        self.attribute_map = {
            'customer_id': 'customerId'
        }
        self._customer_id = customer_id

    @classmethod
    def from_dict(cls, dikt) -> 'CreateCustomerResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateCustomerResponse of this CreateCustomerResponse.  # noqa: E501
        :rtype: CreateCustomerResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self) -> str:
        """Gets the customer_id of this CreateCustomerResponse.


        :return: The customer_id of this CreateCustomerResponse.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """Sets the customer_id of this CreateCustomerResponse.


        :param customer_id: The customer_id of this CreateCustomerResponse.
        :type customer_id: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id
