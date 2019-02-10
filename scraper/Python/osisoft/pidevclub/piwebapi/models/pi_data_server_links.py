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


class PIDataServerLinks(object):
	swagger_types = {
		'points': 'str',
		'enumeration_sets': 'str',
	}

	attribute_map = {
		'points': 'Points',
		'enumeration_sets': 'EnumerationSets',
	}
	def __init__(self, points=None, enumeration_sets=None):

		self._points = None
		self._enumeration_sets = None

		if points is not None:
			self.points = points
		if enumeration_sets is not None:
			self.enumeration_sets = enumeration_sets

	@property
	def points(self):
		return self._points

	@points.setter
	def points(self, points):
		self._points = points

	@property
	def enumeration_sets(self):
		return self._enumeration_sets

	@enumeration_sets.setter
	def enumeration_sets(self, enumeration_sets):
		self._enumeration_sets = enumeration_sets

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
		if not isinstance(other, PIDataServerLinks):
			return False
		return self.__dict__ == other.__dict__

