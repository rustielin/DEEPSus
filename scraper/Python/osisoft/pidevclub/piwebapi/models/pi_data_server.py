# coding: utf-8

"""
	Copyright 2018 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from pprint import pformat
from six import iteritems


class PIDataServer(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'path': 'str',
		'is_connected': 'bool',
		'server_version': 'str',
		'server_time': 'str',
		'links': 'PIDataServerLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'path': 'Path',
		'is_connected': 'IsConnected',
		'server_version': 'ServerVersion',
		'server_time': 'ServerTime',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, path=None, is_connected=None, server_version=None, server_time=None, links=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._path = None
		self._is_connected = None
		self._server_version = None
		self._server_time = None
		self._links = None
		self._web_exception = None

		if web_id is not None:
			self.web_id = web_id
		if id is not None:
			self.id = id
		if name is not None:
			self.name = name
		if path is not None:
			self.path = path
		if is_connected is not None:
			self.is_connected = is_connected
		if server_version is not None:
			self.server_version = server_version
		if server_time is not None:
			self.server_time = server_time
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def web_id(self):
		return self._web_id

	@web_id.setter
	def web_id(self, web_id):
		self._web_id = web_id

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def is_connected(self):
		return self._is_connected

	@is_connected.setter
	def is_connected(self, is_connected):
		self._is_connected = is_connected

	@property
	def server_version(self):
		return self._server_version

	@server_version.setter
	def server_version(self, server_version):
		self._server_version = server_version

	@property
	def server_time(self):
		return self._server_time

	@server_time.setter
	def server_time(self, server_time):
		self._server_time = server_time

	@property
	def links(self):
		return self._links

	@links.setter
	def links(self, links):
		self._links = links

	@property
	def web_exception(self):
		return self._web_exception

	@web_exception.setter
	def web_exception(self, web_exception):
		self._web_exception = web_exception

	def to_dict(self):
		result = {}
		for attr, _ in iteritems(self.swagger_types):
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
		return pformat(self.to_dict())

	def __repr__(self):
		return self.to_str()

	def __ne__(self, other):
		return not self == other

	def __eq__(self, other):
		if not isinstance(other, PIDataServer):
			return False
		return self.__dict__ == other.__dict__

