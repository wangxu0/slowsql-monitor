
def format_content(content_list):
    top_n = len(content_list)
    t_body = ""
    for content_items in content_list:
        t_body += "<tr>"
        t_body += "<td>" + content_items["Count"] + "</td>"
        t_body += "<td>" + content_items["Lock"] + "</td>"
        t_body += "<td>" + content_items["Time"] + "</td>"
        t_body += "<td>" + content_items["Session"] + "</td>"
        t_body += "<td>" + content_items["SQL"] + "</td>"
        t_body += "</tr>"

    template_file = open("template.html")
    content_str = template_file.read()
    template_file.close()
    content_str = content_str.replace("TEMP_VAR{TOP_N}", str(top_n))
    content_str = content_str.replace("TEMP_VAR{ITEMS}", t_body)
    return content_str
