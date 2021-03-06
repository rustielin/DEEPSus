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


class PIMediaMetadataLinks(object):
	swagger_types = {
		'owner': 'str',
		'media_data': 'str',
	}

	attribute_map = {
		'owner': 'Owner',
		'media_data': 'MediaData',
	}
	def __init__(self, owner=None, media_data=None):

		self._owner = None
		self._media_data = None

		if owner is not None:
			self.owner = owner
		if media_data is not None:
			self.media_data = media_data

	@property
	def owner(self):
		return self._owner

	@owner.setter
	def owner(self, owner):
		self._owner = owner

	@property
	def media_data(self):
		return self._media_data

	@media_data.setter
	def media_data(self, media_data):
		self._media_data = media_data

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
		if not isinstance(other, PIMediaMetadataLinks):
			return False
		return self.__dict__ == other.__dict__

