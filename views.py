from django.shortcuts import render
from home.models import *

# Create your views here.
def index(request):
    script_obj = []
    dict1 = {
        1:{"preinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "postinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "audit_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"}},
        2:{"preinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "postinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "audit_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"}}   
        }
    SCRIPT_FILE_S ={"upload_file":1,"hexnosde_repository":2}
    # SCRIPT_TYPE = {"pre_install":1,"post_install":2,"audit":3}
    # print(dict1)
    for i,v in dict1.items():
        if i==1:
            for k,j in v.items():
                if k == "postinstall_script":
                    MandatoryAppPolicy.objects.filter(script_file_source = 1,script_type = 3).delete()
                    x = {"script_type":3}
                    j.update(x)
                    j['script_file_source'] = SCRIPT_FILE_S.get(j.get('script_file_source'))
                    mandpolicy_obj = MandatoryAppPolicy(**j)
                    script_obj.append(mandpolicy_obj)
    aaaa = MandatoryAppPolicy.objects.bulk_create(script_obj)
    return render(request, "index.html")



def index(request):
    script_obj = []
    dict1 = {
        1:{"preinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "postinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "audit_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"}},
        2:{"preinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "postinstall_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"},
        "audit_script":{"script_file_source":"upload_file","file_name":"aa.pdf","binary_path":"aaaaaa/aa","arguments":"hiiiii"}}   
        }
    SCRIPT_FILE_S ={"upload_file":1,"hexnosde_repository":2}
    # SCRIPT_TYPE = {"pre_install":1,"post_install":2,"audit":3}
    # print(dict1)
    for i,v in dict1.items():
        if i==1:
            # for k,j in v.items():
            #     if k == "postinstall_script":
                    # MandatoryAppPolicy.objects.filter(script_file_source = 1,script_type = 3).delete()
            data = v.get("postinstall_script",None) or v.get("preinstall_script",None) or {}
            if data:=v.get("postinstall_script",None):
                

            data['type'] = "postinstall_script" if v.get("postinstall_script",None) else "preinstall_script"
            # x = {"script_type":3}
            # j.update(x)
            # j['script_file_source'] = SCRIPT_FILE_S.get(j.get('script_file_source'))
            # mandpolicy_obj = MandatoryAppPolicy(**j)
            # script_obj.append(mandpolicy_obj)
    # aaaa = MandatoryAppPolicy.objects.bulk_create(script_obj)
    return render(request, "index.html")


modules = course.modules.all()
            module_for_update = []
            i = 1
            for module in modules:
                if module.pk == int(module_id):
                    module.order = order
                    module_for_update.append(module)
                    continue
                if order == i:
                    i += 1
                module.order = i
                module_for_update.append(module)
                i += 1
            Module.objects.bulk_update(module_for_update, ["order"])
