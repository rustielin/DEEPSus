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


class PITimedValue(object):
	swagger_types = {
		'timestamp': 'str',
		'units_abbreviation': 'str',
		'good': 'bool',
		'questionable': 'bool',
		'substituted': 'bool',
		'annotated': 'bool',
		'value': 'object',
		'errors': 'list[PIPropertyError]',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'timestamp': 'Timestamp',
		'units_abbreviation': 'UnitsAbbreviation',
		'good': 'Good',
		'questionable': 'Questionable',
		'substituted': 'Substituted',
		'annotated': 'Annotated',
		'value': 'Value',
		'errors': 'Errors',
		'web_exception': 'WebException',
	}
	def __init__(self, timestamp=None, units_abbreviation=None, good=None, questionable=None, substituted=None, annotated=None, value=None, errors=None, web_exception=None):

		self._timestamp = None
		self._units_abbreviation = None
		self._good = None
		self._questionable = None
		self._substituted = None
		self._annotated = None
		self._value = None
		self._errors = None
		self._web_exception = None

		if timestamp is not None:
			self.timestamp = timestamp
		if units_abbreviation is not None:
			self.units_abbreviation = units_abbreviation
		if good is not None:
			self.good = good
		if questionable is not None:
			self.questionable = questionable
		if substituted is not None:
			self.substituted = substituted
		if annotated is not None:
			self.annotated = annotated
		if value is not None:
			self.value = value
		if errors is not None:
			self.errors = errors
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def timestamp(self):
		return self._timestamp

	@timestamp.setter
	def timestamp(self, timestamp):
		self._timestamp = timestamp

	@property
	def units_abbreviation(self):
		return self._units_abbreviation

	@units_abbreviation.setter
	def units_abbreviation(self, units_abbreviation):
		self._units_abbreviation = units_abbreviation

	@property
	def good(self):
		return self._good

	@good.setter
	def good(self, good):
		self._good = good

	@property
	def questionable(self):
		return self._questionable

	@questionable.setter
	def questionable(self, questionable):
		self._questionable = questionable

	@property
	def substituted(self):
		return self._substituted

	@substituted.setter
	def substituted(self, substituted):
		self._substituted = substituted

	@property
	def annotated(self):
		return self._annotated

	@annotated.setter
	def annotated(self, annotated):
		self._annotated = annotated

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

	@property
	def errors(self):
		return self._errors

	@errors.setter
	def errors(self, errors):
		self._errors = errors

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
		if not isinstance(other, PITimedValue):
			return False
		return self.__dict__ == other.__dict__

