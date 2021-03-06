# coding: utf-8

"""
    Tracking API

    <p>An API for CRUD of sample tracking information for Mykrobe Atlas project <p>This API is intended to satisfy the following user stories <li> Atlas user wants to know the sample status so that I can know if specific results are available <li> Atlas user wants to know QC results for a sample so that I can know if a specific sample has passed QC check <li> Atlas user wants to deprecate a sample so that it is no longer available from the Atlas system <li> sample ingestion service wants to know if a sample already exists so that I can decide on rejecting a sample <li> sample ingestion service wants to know if a file already exists so that I can know if this is a new file <li> sample ingestion service wants to add a new sample for tracking so that It can know if the sample is accepted <li> sample processing service wants to add a processing event for a new sample so that the sample can be auditted <li> sampel processing service wants to add QC results for a new sample so that other user can know if the new sample passes the QC check <li> sampel processing service wants to update sample status so that they are up to date <li> sampel processing service wants to update sample's QC results so that they are up to date <li> audit user wants to know all the processing events for a sample so that I can know what happened to a sample  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tracking_client.configuration import Configuration


class Sample(object):
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
        'experiment_id': 'str',
        'isolate_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'experiment_id': 'experiment-id',
        'isolate_id': 'isolate-id',
        'id': 'id'
    }

    def __init__(self, experiment_id=None, isolate_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """Sample - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._experiment_id = None
        self._isolate_id = None
        self._id = None
        self.discriminator = None

        if experiment_id is not None:
            self.experiment_id = experiment_id
        if isolate_id is not None:
            self.isolate_id = isolate_id
        if id is not None:
            self.id = id

    @property
    def experiment_id(self):
        """Gets the experiment_id of this Sample.  # noqa: E501


        :return: The experiment_id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this Sample.


        :param experiment_id: The experiment_id of this Sample.  # noqa: E501
        :type: str
        """

        self._experiment_id = experiment_id

    @property
    def isolate_id(self):
        """Gets the isolate_id of this Sample.  # noqa: E501


        :return: The isolate_id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._isolate_id

    @isolate_id.setter
    def isolate_id(self, isolate_id):
        """Sets the isolate_id of this Sample.


        :param isolate_id: The isolate_id of this Sample.  # noqa: E501
        :type: str
        """

        self._isolate_id = isolate_id

    @property
    def id(self):
        """Gets the id of this Sample.  # noqa: E501


        :return: The id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sample.


        :param id: The id of this Sample.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$/`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, Sample):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sample):
            return True

        return self.to_dict() != other.to_dict()
