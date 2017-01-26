def processDatabaseResponse(response):
    result = ""
    for petData in response:
        result += '<div class="dataObject cardDiv drop-shadow col-sm-3">\n'
        result += '\t<img class="cardImage" src="%s" alt="IMAGE NOT FOUND" onerror="this.onerror=null;this.src=\'../static/images/placeholder.png\';">\n' % petData['img']
        result += '\t<ul class="cardList">\n'
        result += '\t\t<li><b>Pet Name: </b>%s</li>\n' % petData['petName']
        result += '\t\t<li><b>Type of Pet: </b>%s</li>\n' % petData['petType']
        result += '\t\t<li><b>Color: </b>%s</li>\n' % petData['color']
        result += '\t\t<li><b>Eye Color: </b>%s</li>\n' % petData['eyeColor']
        result += '\t\t<li><b>Date Found: </b>%s</li>\n' % petData['dateLost']
        result += '\t\t<li><b>Where: </b>%s</li>\n' % petData['location']
        result += '<br>\n'
        result += '\t\t<li><a class="cardLink" href="/pet/%s">Sounds Like your Pet? </a></li>\n' % petData['petID']
        result += '\t</ul>\n'
        result += '</div>\n'
        result += '<div class="col-xs-1"></div>\n\n'
    return result

def convertFormArrayToDict(formArray):
    dictionary = {}
    for keyValuePair in formArray:
        key = keyValuePair['name']
        value = keyValuePair['value']
        dictionary[key] = value
    return dictionary
