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


class PIAnalysisRule(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'path': 'str',
		'config_string': 'str',
		'display_string': 'str',
		'editor_type': 'str',
		'has_children': 'bool',
		'is_configured': 'bool',
		'is_initializing': 'bool',
		'plug_in_name': 'str',
		'supported_behaviors': 'list[str]',
		'variable_mapping': 'str',
		'links': 'PIAnalysisRuleLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'path': 'Path',
		'config_string': 'ConfigString',
		'display_string': 'DisplayString',
		'editor_type': 'EditorType',
		'has_children': 'HasChildren',
		'is_configured': 'IsConfigured',
		'is_initializing': 'IsInitializing',
		'plug_in_name': 'PlugInName',
		'supported_behaviors': 'SupportedBehaviors',
		'variable_mapping': 'VariableMapping',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, path=None, config_string=None, display_string=None, editor_type=None, has_children=None, is_configured=None, is_initializing=None, plug_in_name=None, supported_behaviors=None, variable_mapping=None, links=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._path = None
		self._config_string = None
		self._display_string = None
		self._editor_type = None
		self._has_children = None
		self._is_configured = None
		self._is_initializing = None
		self._plug_in_name = None
		self._supported_behaviors = None
		self._variable_mapping = None
		self._links = None
		self._web_exception = None

		if web_id is not None:
			self.web_id = web_id
		if id is not None:
			self.id = id
		if name is not None:
			self.name = name
		if description is not None:
			self.description = description
		if path is not None:
			self.path = path
		if config_string is not None:
			self.config_string = config_string
		if display_string is not None:
			self.display_string = display_string
		if editor_type is not None:
			self.editor_type = editor_type
		if has_children is not None:
			self.has_children = has_children
		if is_configured is not None:
			self.is_configured = is_configured
		if is_initializing is not None:
			self.is_initializing = is_initializing
		if plug_in_name is not None:
			self.plug_in_name = plug_in_name
		if supported_behaviors is not None:
			self.supported_behaviors = supported_behaviors
		if variable_mapping is not None:
			self.variable_mapping = variable_mapping
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
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def config_string(self):
		return self._config_string

	@config_string.setter
	def config_string(self, config_string):
		self._config_string = config_string

	@property
	def display_string(self):
		return self._display_string

	@display_string.setter
	def display_string(self, display_string):
		self._display_string = display_string

	@property
	def editor_type(self):
		return self._editor_type

	@editor_type.setter
	def editor_type(self, editor_type):
		self._editor_type = editor_type

	@property
	def has_children(self):
		return self._has_children

	@has_children.setter
	def has_children(self, has_children):
		self._has_children = has_children

	@property
	def is_configured(self):
		return self._is_configured

	@is_configured.setter
	def is_configured(self, is_configured):
		self._is_configured = is_configured

	@property
	def is_initializing(self):
		return self._is_initializing

	@is_initializing.setter
	def is_initializing(self, is_initializing):
		self._is_initializing = is_initializing

	@property
	def plug_in_name(self):
		return self._plug_in_name

	@plug_in_name.setter
	def plug_in_name(self, plug_in_name):
		self._plug_in_name = plug_in_name

	@property
	def supported_behaviors(self):
		return self._supported_behaviors

	@supported_behaviors.setter
	def supported_behaviors(self, supported_behaviors):
		self._supported_behaviors = supported_behaviors

	@property
	def variable_mapping(self):
		return self._variable_mapping

	@variable_mapping.setter
	def variable_mapping(self, variable_mapping):
		self._variable_mapping = variable_mapping

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
		if not isinstance(other, PIAnalysisRule):
			return False
		return self.__dict__ == other.__dict__

