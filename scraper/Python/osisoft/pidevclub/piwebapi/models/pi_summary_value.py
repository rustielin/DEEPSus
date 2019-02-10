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


class PISummaryValue(object):
	swagger_types = {
		'type': 'str',
		'value': 'PITimedValue',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'type': 'Type',
		'value': 'Value',
		'web_exception': 'WebException',
	}
	def __init__(self, type=None, value=None, web_exception=None):

		self._type = None
		self._value = None
		self._web_exception = None

		if type is not None:
			self.type = type
		if value is not None:
			self.value = value
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def type(self):
		return self._type

	@type.setter
	def type(self, type):
		self._type = type

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

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
		if not isinstance(other, PISummaryValue):
			return False
		return self.__dict__ == other.__dict__

