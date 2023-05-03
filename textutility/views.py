from django.shortcuts import HttpResponse,render
import re
import string


def mydata(request):
    # return HttpResponse("This Will be my home page !")
    return render(request,'index.html')

def analyze_data(request):
    source_data=request.POST.get('input_text')
    capitalize_data=request.POST.get('make_capitlize','off')
    world_data=request.POST.get('word_count','off')
    remove_punc=request.POST.get('remove_function','off')
    remove_white_space=request.POST.get('remove_whitespace','off')
    new_line_remover=request.POST.get('remove_new_line','off')
    
    if capitalize_data=="on":
        converted_data=source_data.upper()
        mydict={"response":converted_data}
        return render(request,'output.html',mydict)
    
    elif world_data=="on":
        count=0
        for x in source_data:
            if x==" " or x=="\n":
                count+=1
        data={"res":count+1}
        return render(request,"output.html",data )
  
    
    elif remove_punc=="on":
        patt='[0-9a-zA-Z]+'
        match=re.finditer(patt,source_data)
        mydict={"response":list(match)}
        return render(request,"output.html",mydict) 
        
        # clean_data=""
        # punctuation="""!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        # for x in source_data:
        #     if x not in punctuation:
        #         clean_data=clean_data+x
        # mydict={"response":clean_data}
        # return render(request,"output.html",mydict )
   
        

    elif remove_white_space=="on":
        data=""
        for x in source_data:
            if x.replace(""," "):
                data=data+x
        mydict={"response":data}
        return render(request,"output.html",mydict )
    
    elif new_line_remover=="on":
        mydata=""
        for x in source_data:
            if x.replace("\n"," "):
                mydata=mydata+x
        mydict={"response":mydata}
        return render(request,"output.html",mydict )
                
        
        
                
                
                
        
                
        
        
    
                
        
        
       
       
    
    # return HttpResponse("inside the analyze data")