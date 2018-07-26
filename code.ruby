#Strip HTML tags
def strip_html(allowed = [])
  str = self.strip || ''
  str.gsub(/<(\/|\s)*[^(#{allowed.join('|') << '|\/'})][^>]*>/,'')
end

#Clean UTF-8 string
#
# -> iconvert(csv, "latin1", "utf8")
def iconvert(str, encoding_from, encoding_to = "utf8")
  i = Iconv.new encoding_to, encoding_from
  utf_str = ""
  begin
    utf_str << i.iconv(str)
  rescue Exception => e
    utf_str << e.success
    ch, str = e.failed.split(//, 2)
    utf_str << "?"
  end
  return utf_str
end