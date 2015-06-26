from ADIF_log import ADIF_log
import urwid
import views

log = ADIF_log('Whiskey Logger', file='lotwreport.adi')

def mode_menu():
	retval = [None]
	palette = [('reversed', 'standout', '')]
	choices = ('Browse', 'Entry')
	title = 'Mode'

	def menu(title, choices):
		body = [urwid.Text(title), urwid.Divider()]
		for c in choices:
			button = urwid.Button(c, on_press=item_chosen, user_data=c)
			body.append(urwid.AttrMap(button, None, focus_map=palette[0][0]))
		return urwid.ListBox(urwid.SimpleFocusListWalker(body))

	def item_chosen(button, choice):
		retval[0] = choice
		raise urwid.ExitMainLoop

	main = urwid.Padding(menu(title, choices), left=2, right=2)
	top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
		align='center', width=('relative', 60),
		valign='middle', height=('relative', 60),
		min_width=11, min_height=4)
	urwid.MainLoop(top, palette=palette).run()
	return retval[0]



print mode_menu()
