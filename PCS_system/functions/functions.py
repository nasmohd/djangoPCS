
def handle_uploaded_file(f, user_id):
	with open('PCS_system/static/upload/' + str(user_id) + '.' + f.name, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)