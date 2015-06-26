import re
import curses.panel

views = {}

def parseView(s):
	tagRE = re.compile(r'^([^:\s]*):\s*(.*?)(?=^[^\s])', re.M | re.S)
	view = {}
	while 1:
		m = tagRE.search(s)
		if not m: break
		s = s[m.end(0):]
		key = m.group(1).lower()
		val = re.sub(r'^\s+', ' ', m.group(2), flags=re.M | re.S)
		val = re.sub(r'[\r\n]+', '', val, flags=re.M | re.S)
		val = re.sub(r'\s*$', '', val)
		if key == 'fields':
			fields = {}
			while 1:
				m = re.match(r'\s*([^\W])=([^\s]*)', val)
				if not m: break
				val = val[m.end(0)]
				fields[m.group(1)]=m.group(2)
			view[key] = fields
		elif key == 'header' or key == 'body' or key == 'footer':
			view[key] = re.split(r'\s*!', val)[1:]
		elif key == 'repeat':
			view[key] = val.lower() in ('y', 'yes', 'true', 't', '1')
		else:
			view[key] = val
	print "S = "+s
	return view

def parse(fname):
	f = open(fname, 'rb')
	v = f.read()
	f.close()
	viewRE = re.compile(r'^(View:.*?^====+)$', re.I | re.M | re.S)
	views={}
	while 1:
		m = viewRE.search(v)
		if not m: break
		v = v[m.end(0):]
		view = parseView(m.group(1))
		views[view['view']]=view
	return views
		
print repr(parse('views.def'))
