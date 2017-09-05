def save_new_binaries(request):
    
    if request.method == 'POST':
        basedir = os.path.join(settings.MEDIA_ROOT,'documents')
        QA           = request.POST["QA"]
        try:
            QA_instance = User.objects.get(pk = QA)
        except:
            return HttpResponse('nQA doesnot exist!')    #the User doesnot exist

        fixid        = request.POST["fixid"]      # if this line missing, logfile = will report fixid not defined.
    
        # OK here pdb.set_trace()
        #log
        firstname = request.user.first_name
        log_instance = Log()
        
        #pdb.set_trace()   ok  
        logfile = log_instance.open_log_file('0',fixid,firstname)
        # 500 error pdb.set_trace()  
        
        fix = Fix.objects.get(id = fixid)

        #log
        log_instance.write(logfile,firstname,'Start update new binaries database')
        log_instance.write(logfile,firstname,'fixid is %s '%fixid)

        new_binary_file_id_list   = request.POST["new_binary_file_id_list"]

        former_file_list = FileDB.objects.filter(FixNo = fix.fixNO)
        if former_file_list:
            upload_dir = former_file_list[0].docfile.name
            upload_dir = upload_dir[:upload_dir.rfind(fix.fixNO)]
            #log
            log_instance.write(logfile,firstname,'Got file list')
        else:
            #log
            log_instance.write(logfile,firstname,'Empty file list! Returned!')
            log_instance.close_log_file(logfile)
            return HttpResponse('nEmpty file list !')
        zipfile_dir= os.path.join(settings.MEDIA_ROOT,upload_dir,fix.fixNO)
        binary_folder = os.path.join(zipfile_dir, 'binary_files')
        old_binary_folder = os.path.join(zipfile_dir, 'old_binary_files')

        if os.path.isdir(binary_folder) and not os.path.isdir(old_binary_folder):
            os.rename(binary_folder, old_binary_folder)

        upload_dir = os.path.join(zipfile_dir,'binary_files')

        fixNO = fix.fixNO
        if not os.path.exists(upload_dir):
              os.makedirs(upload_dir)

        #update file information
        #delete the file whose filestatus is -2 and update those files
        #whose filestatus is 0 and id in the fileid_list
        #rename folder of files

        #log
        log_instance.write(logfile,firstname,'Start to upload files')
        new_binary_file_id_list_spl = new_binary_file_id_list.split(",")
        for fileid in new_binary_file_id_list_spl:
            filedb = FileDB.objects.get(id=fileid);
            if filedb.fileStatus =='0':#new file
                filedb.FixNo = fixNO
                if not os.path.exists(upload_dir):
                       os.makedirs(upload_dir)
                #2 copy file
                docfilename = os.path.join(settings.MEDIA_ROOT, filedb.docfile.name)
                if os.path.isfile (docfilename):
                   shutil.copy2(docfilename, upload_dir+'/'+filedb.outfilename)
                   os.remove(docfilename) #3 remove file
                   #get the related route
                   absolute_route = os.path.join(upload_dir, filedb.outfilename)
                   absolute_route = absolute_route[absolute_route.index(settings.MEDIA_ROOT)+ len(settings.MEDIA_ROOT)+1:]
                   filedb.docfile = absolute_route
                   #stand for that th e fix related with this file has been added into the database
                   filedb.fileStatus = '1'
                   filedb.save()
                   #pdb.set_trace()
                   
                   #log
                   log_instance.write(logfile,firstname,'File Name:%s is copied and removed.'%docfilename)
                else:
                   #log
                   log_instance.write(logfile,firstname,'File Name:%s does not exist.'%docfilename)

                   filedb.delete()
       
        #log
        log_instance.write(logfile,firstname,'Files have been uploaded.')
        pre_deleted_file_list = FileDB.objects.filter(Q(fileStatus__exact = '-2') & Q(FixNo = fixNO))

        
        for pre_deleted_file in pre_deleted_file_list:
            filename = pre_deleted_file.docfile
            pre_deleted_file.delete()
            path =''
            if settings.MEDIA_ROOT in filename.name:
               path = filename.name
            else:
               path = settings.MEDIA_ROOT+"/"+ filename.name

            if os.path.isfile(path):
                os.remove(path)
        #log
        log_instance.write(logfile,firstname,'Accomplish to delete the pre-delete files.')

        #zip binary and readme file
        #log
        log_instance.write(logfile,firstname,'Start to deal with zip binary and readme file.')
        log_instance.write(logfile,firstname,'rename the old zip file.')

        #rename the old zip file
        old_zip = os.path.join(zipfile_dir, fix.fixNO+'.zip')

        if os.path.isfile(old_zip) and fix.Status != '5' :
           os.rename(old_zip,os.path.join(zipfile_dir, 'old_'+fix.fixNO+'.zip'))
        #readme.txt
        writeReadMe(fix, zipfile_dir, fix.problemID)
        zipname = os.path.join(zipfile_dir,fix.fixNO)
        zip = Zip()
        zip.zipCustomeFile(upload_dir,zipname)
        #log
        log_instance.write(logfile,firstname,'New zip file has been created.')
      
        fix.Status      = '5' # the new binaries has been uploaded
        #fix.Zipfile_url = zipname+'.zip'
        fix.QA          = QA_instance
        fix.New_binaries_upload_date = timezone.now()
        fix.save()

        #log
        log_instance.write(logfile,firstname,'Fix changes have been created.')

        #send email to the creator tell him/her the opinion of 173
        if QA_instance.email:
            #send email to notify the approvers
            Subject   = 'The new binary files are ready and need your confirmation'
            receiver  = QA_instance.email
            preamble  = 'test'
            msgText   = ('The new binary files of Fix (<font color="#1A8EC4"><b>'+fix.fixNO+'</b></font>) have been uploaded and need your confirmation.<br>'
                         + '<br>To confirm it here:&nbsp;' + settings.APP_WEB_URL+'fix/' + str(fix.id) + '/detail/' + fix_email_content(fix))
            Email.asynchronous_send_email(Subject,preamble,msgText,receiver, log_instance,logfile,firstname)
            #email_intance = Email()
            #email_result = email_intance.send_text_email(Subject,preamble,msgText,receiver)

            #log
            #log_instance.write(logfile,firstname,'Email to notify QA has been sent and the result is %s'%email_result)

        to_do_instance = To_do_list_cls()
        common = Common()
        to_do_instance.delete_Fix(fix,common.get_client_ip(request),request.user)
        to_do_instance.addForFix(request.user,QA_instance,'3',fix)

        #log
        log_instance.write(logfile,firstname,'Accomplished to deal with to-do-list')
        log_instance.write(logfile,firstname,'(save_new_binaries) is finished. Saved successfully')
        #log_instance.close_log_file(logfile)

        return HttpResponse("ySaved successfully!")
