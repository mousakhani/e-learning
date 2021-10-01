from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
	def __init__(self, for_fields=None, *args, **kwargs):
		self.for_fields = for_fields
		super(OrderField, self).__init__(*args, **kwargs)

	def pre_save(self, model_instance, add):
		# model_instance is the instance this field belongs and
		# add is whether the instance is being saved to the database for the first time.
		# add False to update field
		# self.attname refers to attribute name given to the field in the model.
		if getattr(model_instance, self.attname) is None:
			# not current value
			try:
				qs = self.model.objects.all()
				if self.for_fields:
					# filter by objects with the same field values
					# for the fields in for_fields
					query = {field: getattr(model_instance, field) for field in self.for_fields}
					qs = qs.filter(**query)
				# get the order of the last item
				last_item = qs.latest(self.attname)
				value = getattr(last_item, self.attname) + 1
			except ObjectDoesNotExist:
				value = 0
				setattr(model_instance, self.attname, value)
			return value
		else:
			return super(OrderField, self).pre_save(model_instance, add)
