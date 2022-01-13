from django.shortcuts import render

# Create your views here.

import datetime
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from PCS_system.forms import StudentRegister
from PCS_system.models import Student, Project, Role, Permission, Role_Permission
from PCS_system.functions.functions import handle_uploaded_file


def login (request):
	return render(request, 'login.html')

def index (request):

	project = Project ()
	projects = Project.objects.all()

	student_id = request.session['id']
	student_info = Student.objects.get(id = student_id)

	permissions = request.session['permissions']
	
# return render (request, 'index.html', {'projects': projects})
	return render(request, 'index.html', {'projects': projects, 'user_id': student_id, 'student_info': student_info, 'user_permissions' : permissions})
	# {'student_info':student, 'login_status': status, 'projects': projects, 'user_id': student_id}

def register (request):
	return render(request, 'register.html')

def register_submit (request):
	# return HttpResponse (request.POST['email'])
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	phone_number = request.POST['phone_number']
	password = request.POST['password']
	password_retype = request.POST['password_retype']
	
	role = Role.objects.get (id = 2) #normal user
	# return HttpResponse (email)

	# if (password == password_retype):
	student = Student ()
	student.first_name = first_name
	student.last_name = last_name
	student.email = email
	student.phone_number = phone_number
	student.password = password
	student.role_id = role
	# student.save()

	try:
		student.save()
		return render (request, 'login.html')

	except:
		return render (request, 'register.html')

	# if request.method == "POST":
	# 	form = StudentRegister(request.POST)

	# 	if form.is_valid(): #If form is valid
	# 		first_name = form.cleaned_data['first_name']
	# 		email = form.cleaned_data['email']
	# 		password = form.cleaned_data['password']
	# 		password_retype = form.cleaned_data['password_retype']
	# 		return HttpResponse(request)

	# 	else: #return user to register page
	# 		return render (request, 'register.html')

	# else:
	# 	return HttpResponse('<h1> No form </h1>')


	# if request.method == "POST":
	# 	return HttpResponse('<h1>Form submitted</h1>')

	# else:
	# 	return HttpResponse('<h1> No Form </h1>')

def login_submit (request):
	# return HttpResponse (request.POST['email'])
	email = request.POST['email']
	password = request.POST['password']
	# password_retype = request.POST['password_retype']

	# return HttpResponse (email)
	# if (password == password_retype):

	student_details = []
	project = Project ()
	projects = Project.objects.all()
	status = []
	permissions = []

	try:
		student = Student.objects.get(email = email)

		if ((student.password == password) and (student.status != '0')): #Login accepted
			request.session['email'] = student.email
			request.session['id'] = student.id

			student_details.append(student.id)
			student_details.append(student.first_name)
			student_details.append(student.last_name)
			student_details.append(student.phone_number)
			student_details.append(student.email)
			student_details.append(student.user_image)
			student_details.append(student.role_id.id)

			# stu_role = Role.objects.get(role_id = student.role_id)

			user_permissions = Role_Permission.objects.filter (role_id = student.role_id)
			status.append(0)
			for i in user_permissions:
				permissions.append (i.permission_id.permission_name)

			request.session['permissions'] = permissions
			request.session['student_info'] = student_details

			if (student.role_id.id == 1):
				return render (request, 'index.html',  {'student_info':student, 'login_status':status, 'user_permissions': permissions})

			if (student.role_id.id == 2):
				return render (request, 'index.html', {'student_info':student, 'login_status': status, 'projects': projects, 
					'user_id': student.id, 'user_permissions': permissions})

		else:
			status.append(1)
			return render (request, 'login.html', {'login_status': status})
			# request.session['status'] = 1

	except:
		status.append(1)
		return render (request, 'login.html', {'login_status': status})
		# request.session['status'] = 1

	# try:
	# 	student.save()
	# 	return HttpResponse ('<h1> Student added </h1>')
	# except:
	# 	return HttpResponse('<h1> Student not added </h1>')

def logout(request):
	return render (request, 'login.html')


def project_submit(request):
	project_title = request.POST['project_title']
	project_description = request.POST['project_description']
	project_partners = request.POST['project_partners']
	project_budget = request.POST['project_budget']
	# project_image = request.POST['project_image']

	project = Project ()
	projects = Project.objects.all()

	project_image_upload = request.FILES['project_image']
	# return HttpResponse (project_image_upload)
	handle_uploaded_file(project_image_upload, request.session['id'])

	project_image = str(request.session['id']) + '.' + project_image_upload.name
	# student = Student()
	email = request.session['email']
	student = Student.objects.get(email = email)
	
	project.project_title = project_title
	project.project_description = project_description
	project.project_partners = project_partners
	project.project_budget = project_budget
	project.project_image = project_image
	project.user_id = student

	try:
		project.save()
		return HttpResponseRedirect('index')

	except:
		return HttpResponse('Error')
	# try:
	# 	project.save()
	# 	return HttpResponse ('<h1> Project added </h1>')
	# except:
	# 	return HttpResponse('<h1> Project not added </h1>')
	# return HttpResponse (request.FILES['project_image'])
	return render (request, 'index.html', {'projects': projects})


def delete_project (request, project_id):
	project = Project.objects.get(id = project_id)

	try:
		project.delete()
		return HttpResponseRedirect('../index')

	except:
		return HttpResponse('Error')

	# return render (request, 'index.html')

def edit_project(request, project_id):
	student_info = request.session['student_info']

	project = Project.objects.get (id = project_id)
	return render (request, 'project_edit.html', {'project': project, 'student_info': student_info})


def project_details(request, project_id):
	# return HttpResponse (project_id)
	student_info = request.session['student_info']

	project = Project.objects.get (id = project_id)
	student_id = request.session['id']
	return render (request, 'project_details.html', {'project': project, 'user_id': student_id, 'student_info': student_info})


def update_project(request, project_id):
	project_title = request.POST['project_title']
	project_description = request.POST['project_description']
	project_partners = request.POST['project_partners']
	project_budget = request.POST['project_budget']


	project = Project.objects.get (id = project_id)

	project_image_prev = project.project_image
	project.project_title = project_title
	project.project_description = project_description
	project.project_partners = project_partners
	project.project_budget = project_budget
	# project.project_image = project_image

	try:
		project_image = request.POST['project_image']
		project.project_image = project_image_prev

	except: #not empty
		project_image_upload = request.FILES['project_image']
		handle_uploaded_file(project_image_upload, request.session['id']) #transfer img to new folder
		project_image = str(request.session['id']) + '.' + project_image_upload.name
		project.project_image = project_image

	project.save()
	lnk = '../edit_project/' + str(project_id)
	return HttpResponseRedirect(lnk)

	# return HttpResponse(project_image_upload)
	# if (len(project_image_upload) != 0):
	# 	return HttpResponse ('not empty')

	# else:
	# 	return HttpResponse ('empty')
	# return HttpResponse (project_image_upload)
	# handle_uploaded_file(project_image_upload, request.session['id'])

	# project_image = str(request.session['id']) + '.' + project_image_upload.name

	# project = Project.objects.get (id = project_id)
	# project.project_title = project_title
	# project.project_description = project_description
	# project.project_partners = project_partners
	# project.project_budget = project_budget
	# project.project_image = project_image

	# project.save(0)
	# lnk = '../edit_project/' + str(project_id)
	# return HttpResponseRedirect(lnk)

def view_profile (request, user_id):
	student_details = request.session['student_info']

	return render (request, 'profile.html', {'student_info': student_details}) 


def view_projects (request):
	student_details = request.session['student_info']

	project = Project.objects.filter (user_id = student_details[0]) #(project[0].project_description)

	# return HttpResponse (project.id)
	return render (request, 'project_info.html', {'student_info': student_details, 'projects': project}) 


def profile_update(request, user_id):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	phone_number = request.POST['phone_number']
	# password = request.POST['password']
	# password_retype = request.POST['password_retype']


	student = Student.objects.get(id = user_id)
	student.first_name = first_name
	student.last_name = last_name
	student.email = email
	student.phone_number = phone_number
	student.save()

	lnk = '../profile/' + str(user_id)
	return HttpResponseRedirect (lnk)


def project_info (request):
	permission = request.session['permissions']
	project = Project.objects.all ()
	return render (request, 'project_info_admin.html', {'projects': project, 'user_permissions': permission})


def user_info (request):
	# return HttpResponse ('user info')
	permission = request.session['permissions']
	users = Student.objects.all ()

	all_permission = Permission.objects.all()
	count_permissions = Permission.objects.all().count();
	all_roles = Role.objects.all()

	perm = []
	roles = []
	roles_id = [] #1 2 9 12
	role_permission = [] #2d list
	perms = []

	role_permission_all = Role_Permission.objects.all();
	# Role_Permission.objects.all().values('role_id').distinct();
	for i in all_permission:
		perm.append(i.permission_name)

	for j in all_roles:
		roles.append(j.role_type)
		roles_id.append(j.id)

	for k in roles_id:
		perms = []
		role = Role.objects.get(id = k) #admin
		role_permission_found = Role_Permission.objects.filter(role_id = role) #[<Permission: 1, dashboard>, <Permission: 2, add users >]

		for l in role_permission_found:
			perms.append (l.permission_id.permission_name)

		role_permission.append (perms)

	role_permission_final = zip(roles, role_permission)
	# dicti = {}
	# for l in range (0, len(roles)):
	# 	dicti[roles[l]] = role_permission[l]

	# print(role_permission_found.query)
	# return HttpResponse (role_permission)
	return render (request, 'user_info.html', {'Users': users, 'user_permissions': permission, 'all_permission': all_permission, 'roles': roles,
		'count_permissions': count_permissions, 'role_permission': role_permission, 'roles_id': roles_id, 'all_roles': all_roles,
		'role_permission_all': role_permission_all, 'role_permission_final': role_permission_final})


def delete_user(request, user_id):
	user = Student.objects.get (id = user_id)

	try:
		user.delete()
		return HttpResponseRedirect('../user_info')

	except:
		return HttpResponseRedirect('../user_info')


def role_submit(request):
	role_name = request.POST['role_name']

	role_results = Role.objects.filter(role_type = role_name).count()

	if (role_results == 0):
		role = Role()
		role.role_type = role_name
		role.save()

		role_permission = request.POST.getlist('permissions') #all the selected checkbox permissions

		for i in role_permission:
			permission = Permission.objects.get(permission_name = i)

			role_permission = Role_Permission ()
			role_permission.role_id = role
			role_permission.permission_id = permission
			role_permission.save()
		return HttpResponseRedirect ('user_info')
	
	else:
		return HttpResponseRedirect ('user_info')


	# permission = Permission()
	# permission.role_id = role

	# perm = []

	# for i in range (1, 4):
	# 	pm = str(i)

	# 	try:
	# 		selected_permission = request.POST[pm]
	# 		permission.permission_name = selected_permission
	# 		perm.append (selected_permission)

	# 	except:
	# 		continue
	# permission.save()

	# return HttpResponseRedirect('user_info')



def add_user(request):
	user_role = request.POST['user_role']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	phone_number = request.POST['phone_number']
	password = request.POST['password']

	role_type = Role.objects.get(role_type = user_role)

	user = Student()
	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.phone_number = phone_number
	user.password = password
	user.role_id = role_type
	user.save()

	return HttpResponseRedirect('user_info')



def manage_role(request):
	try: #delete
		request.POST['delete_role'] == 'delete'
		role = request.POST['user_role']

		role_del = Role.objects.get(role_type = role)
		role_del.delete()
		return HttpResponseRedirect('user_info')


	except: #Update
		role_name = request.POST['user_role']
		role = Role.objects.get (role_type = role_name) #get role selected

		prev_role_permission = Role_Permission.objects.filter(role_id = role)
		prev_role_permission.delete()


		ls_name = role_name + 'permission_update'
		role_permission = request.POST.getlist(ls_name) #all the selected checkbox permissions

		# return HttpResponse (role_permission)
		# prev_role_permission = Role_Permission.objects.filter 

		role_results = Role.objects.filter(role_type = role_name).count()

		for i in role_permission:
			permission = Permission.objects.get(permission_name = i)

			new_role_permission = Role_Permission()
			new_role_permission.role_id = role
			new_role_permission.permission_id = permission
			new_role_permission.save()

		return HttpResponseRedirect ('user_info')
		
		# else:
		# 	return HttpResponseRedirect ('user_info')


	return HttpResponseRedirect('user_info')



def change_user_role(request, user_id):
	role_type = request.POST['user_role']
	user = Student.objects.get(id = user_id)

	if (role_type == 'None (Block)'):
		user.status = '0'

	else:
		role = Role.objects.get(role_type = role_type)
		user.role_id = role
		user.status = '1'
	
	user.save()
	return HttpResponseRedirect('../user_info')