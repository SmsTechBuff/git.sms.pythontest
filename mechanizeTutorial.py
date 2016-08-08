import mechanize


br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; AskTB5.6)')]
br.open("https://brickseek.com/walmart-inventory-checker?sku=45976115")

#br.open("https://www.google.com")
br.select_form(nr=1)
#br.select_form(nr=0)


br.form['zip'] = '40229'
# fill out other fields

req = br.submit()

print req.read()