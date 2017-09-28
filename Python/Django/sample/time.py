email = request.session['email']
        tasks = request.POST['tasks']
        is_valid = True
        if len(tasks)<1:            
            messages.add_message(request, messages.ERROR,"*You have to provide a comment for tasks!")
            is_valid = False    
        try:
            app_date = datetime.strptime(request.POST['app_date'], "%Y-%m-%d")
        except:
            messages.add_message(request, messages.ERROR,"*You have to provide a date for the appointment!")
            is_valid = False
        try:
            app_time = datetime.strptime(request.POST['app_time'], "%H:%M")
        except:
            messages.add_message(request, messages.ERROR,"*You have to provide time of the day!")
        if is_valid ==False:
            return redirect('/appointments')
        else:
            if datetime.today().date() > app_date.date():
                messages.add_message(request, messages.ERROR,"*Appointment day cannot be from earlier than today!")
                is_valid = False
            if datetime.now().time() > app_time.time() and datetime.today().date() == app_date.date():
                messages.add_message(request, messages.ERROR,"*Appoiment time cannot be before now!")
                is_valid = False
            if is_valid ==False:
                return redirect('/appointments')
            else:
                app_final = datetime.combine(datetime.date(app_date), datetime.time(app_time))
                user = User()
                appointment = Appointment()
                app_id = request.POST['app_id']
                user.select_one_user_by_email(email)
                appointment.add_appointment(tasks,app_final,user.select_one_user_by_email(email))
                return redirect('/appointments')