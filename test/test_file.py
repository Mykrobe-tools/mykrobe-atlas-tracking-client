# coding: utf-8

"""
    Tracking API

    <p>An API for CRUD of sample tracking information for Mykrobe Atlas project <p>This API is intended to satisfy the following user stories <li> Atlas user wants to know the sample status so that I can know if specific results are available <li> Atlas user wants to know QC results for a sample so that I can know if a specific sample has passed QC check <li> Atlas user wants to deprecate a sample so that it is no longer available from the Atlas system <li> sample ingestion service wants to know if a sample already exists so that I can decide on rejecting a sample <li> sample ingestion service wants to know if a file already exists so that I can know if this is a new file <li> sample ingestion service wants to add a new sample for tracking so that It can know if the sample is accepted <li> sample processing service wants to add a processing event for a new sample so that the sample can be auditted <li> sampel processing service wants to add QC results for a new sample so that other user can know if the new sample passes the QC check <li> sampel processing service wants to update sample status so that they are up to date <li> sampel processing service wants to update sample's QC results so that they are up to date <li> audit user wants to know all the processing events for a sample so that I can know what happened to a sample  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tracking_client
from tracking_client.models.file import File  # noqa: E501
from tracking_client.rest import ApiException

class TestFile(unittest.TestCase):
    """File unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test File
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tracking_client.models.file.File()  # noqa: E501
        if include_optional :
            return File(
                md5sum = '0', 
                filename = '0', 
                file_type = 'fastq'
            )
        else :
            return File(
                md5sum = '0',
                filename = '0',
                file_type = 'fastq',
        )

    def testFile(self):
        """Test File"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
