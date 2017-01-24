def processDatabaseResponse(response):
    result = ""
    for petData in response:
        print petData
        result += '<div class="dataObject">\n'
        result += '\t<img src="%s" alt="IMAGE NOT FOUND" height="250px" width="250px">\n' % petData['img']
        result += '\t<h3>Pet Information</h3>\n'
        result += '\t<ul>\n'
        result += '\t\t<li><b>Pet Name:</b>%s</li>\n' % petData['petName']
        result += '\t\t<li><b>Type of Pet:</b>%s</li>\n' % petData['petType']
        result += '\t\t<li><b>Color:</b>%s</li>\n' % petData['color']
        result += '\t\t<li><b>Eye Color:</b>%s</li>\n' % petData['eyeColor']
        result += '\t\t<li><b>Date Found:</b>%s</li>\n' % petData['dateLost']
        result += '\t\t<li><b>Where:</b>%s</li>\n' % petData['location']
        result += '\t\t<li>Sounds Like your Pet? <a href="/pet/%s">Click Here</a></li>\n' % petData['petID']
        result += '\t</ul>\n'
        result += '</div>\n\n'
    return result
