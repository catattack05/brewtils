# -*- coding: utf-8 -*-

from brewtils.resolvers import ResolverBase

BYTES_PREFIX = "BGBytesID:"


class BytesResolver(ResolverBase):
    """Resolver that uses the Beergarden file API"""

    def __init__(self, easy_client):
        self.easy_client = easy_client

    def should_upload(self, value, definition):
        return definition.type.lower() == "bytes"

    def upload(self, value, definition):
        return self.easy_client.upload_file(value)

    def should_download(self, value, definition):
        return definition.type.lower() == "bytes"

    def download(self, value, definition):
        return self.easy_client.download_file(value.details["id"])
