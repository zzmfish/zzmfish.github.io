#!/usr/bin/python
import sys
import markdown
md = open(sys.argv[1], 'r').read().decode('utf-8')
body = markdown.markdown(md, extensions=['tables'])
print '''<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
%s
</body>
</html>
''' % body.encode('utf-8')

