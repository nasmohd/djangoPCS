from django.db import models

class Role (models.Model):
	role_type = models.CharField (max_length = 100)

	def __str__(self):
		return '{}, {}'.format(self.id, self.role_type)

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=20, default = '')
	last_name = models.CharField(max_length=20, default = '')
	phone_number = models.CharField(max_length=20, default = '')
	email = models.EmailField(max_length=50, default = '')
	password = models.CharField(max_length=50, default = '')
	user_image = models.CharField(max_length=50, default = 'user_default.png')
	role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default='')
	status = models.CharField(max_length=50, default = '1')


	def __str__(self):
		return '{}, {}'.format(self.id, self.email)


	# def __str__(self):
	# 	return self.email

class Project (models.Model):
	project_title = models.CharField (max_length = 200)
	project_description = models.CharField (max_length = 800)
	project_partners = models.CharField (max_length = 45)
	project_budget = models.CharField (max_length = 20)
	project_image = models.CharField (max_length = 500)
	user_id = models.ForeignKey(Student, on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.project_title

	# def __str__(self):
	# 	return self.project_title


class Permission (models.Model):
	permission_name = models.CharField (max_length = 500)
	# role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default='')

	def __str__(self):
		return '{}, {}'.format(self.id, self.permission_name)
	# def __str__(self):
	# 	return self.role_type


class Role_Permission (models.Model):
	role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default='')
	permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE, default='')

	def __str__(self):
		return '{}, {}'.format(self.id, self.permission_id)


class Rating (models.Model):
	rating_points = models.CharField (max_length = 500)
	
	def __str__(self):
		return '{}, {}'.format(self.id, self.rating_points)