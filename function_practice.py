# make a function for H2 tag

# def headingTwo(text):
#     # Doc String - a mandatory desc field for functions
#     '''
#     take text return h2 with text 
#     :param text:
#     :return: h2 taag
#     '''
#     return f'<h2>{text}</h2>'

# print(headingTwo("amar sonar bangla"))

# print(headingTwo.__doc__)


#make a function for HTML tag

def html_tag_generator(text, htmltag):
    '''
    This function has two parameters:
    text and htmltag.
    Receives Strings as text and returns
    wraping with html tag.
    '''
    html = f'<{htmltag}>{text}</{htmltag}>'
    return html

print(html_tag_generator('My Pythone made Headline', 'h1'))