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


class PIPoint(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'int',
		'name': 'str',
		'path': 'str',
		'descriptor': 'str',
		'point_class': 'str',
		'point_type': 'str',
		'digital_set_name': 'str',
		'span': 'float',
		'zero': 'float',
		'engineering_units': 'str',
		'step': 'bool',
		'future': 'bool',
		'display_digits': 'int',
		'links': 'PIPointLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'path': 'Path',
		'descriptor': 'Descriptor',
		'point_class': 'PointClass',
		'point_type': 'PointType',
		'digital_set_name': 'DigitalSetName',
		'span': 'Span',
		'zero': 'Zero',
		'engineering_units': 'EngineeringUnits',
		'step': 'Step',
		'future': 'Future',
		'display_digits': 'DisplayDigits',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, path=None, descriptor=None, point_class=None, point_type=None, digital_set_name=None, span=None, zero=None, engineering_units=None, step=None, future=None, display_digits=None, links=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._path = None
		self._descriptor = None
		self._point_class = None
		self._point_type = None
		self._digital_set_name = None
		self._span = None
		self._zero = None
		self._engineering_units = None
		self._step = None
		self._future = None
		self._display_digits = None
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
		if descriptor is not None:
			self.descriptor = descriptor
		if point_class is not None:
			self.point_class = point_class
		if point_type is not None:
			self.point_type = point_type
		if digital_set_name is not None:
			self.digital_set_name = digital_set_name
		if span is not None:
			self.span = span
		if zero is not None:
			self.zero = zero
		if engineering_units is not None:
			self.engineering_units = engineering_units
		if step is not None:
			self.step = step
		if future is not None:
			self.future = future
		if display_digits is not None:
			self.display_digits = display_digits
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
	def descriptor(self):
		return self._descriptor

	@descriptor.setter
	def descriptor(self, descriptor):
		self._descriptor = descriptor

	@property
	def point_class(self):
		return self._point_class

	@point_class.setter
	def point_class(self, point_class):
		self._point_class = point_class

	@property
	def point_type(self):
		return self._point_type

	@point_type.setter
	def point_type(self, point_type):
		self._point_type = point_type

	@property
	def digital_set_name(self):
		return self._digital_set_name

	@digital_set_name.setter
	def digital_set_name(self, digital_set_name):
		self._digital_set_name = digital_set_name

	@property
	def span(self):
		return self._span

	@span.setter
	def span(self, span):
		self._span = span

	@property
	def zero(self):
		return self._zero

	@zero.setter
	def zero(self, zero):
		self._zero = zero

	@property
	def engineering_units(self):
		return self._engineering_units

	@engineering_units.setter
	def engineering_units(self, engineering_units):
		self._engineering_units = engineering_units

	@property
	def step(self):
		return self._step

	@step.setter
	def step(self, step):
		self._step = step

	@property
	def future(self):
		return self._future

	@future.setter
	def future(self, future):
		self._future = future

	@property
	def display_digits(self):
		return self._display_digits

	@display_digits.setter
	def display_digits(self, display_digits):
		self._display_digits = display_digits

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
		if not isinstance(other, PIPoint):
			return False
		return self.__dict__ == other.__dict__

